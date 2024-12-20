#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import os
import shutil
from urllib.parse import urljoin
import json

class AssignmentScraper:
    def __init__(self, base_url, output_dir):
        self.base_url = base_url
        self.output_dir = output_dir
        self.assignments = []

    def download_file(self, url, local_path):
        """Download a file and save it locally"""
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            with open(local_path, 'wb') as f:
                shutil.copyfileobj(response.raw, f)
            return True
        except Exception as e:
            print(f'Error downloading {url}: {e}')
            return False

    def process_assignment(self, assignment_url, number):
        """Process a single assignment and its resources"""
        try:
            # Create assignment directory
            assignment_dir = os.path.join(self.output_dir, f'assignment_{number:02d}')
            os.makedirs(assignment_dir, exist_ok=True)

            # Download main HTML
            response = requests.get(assignment_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Process images
            images_dir = os.path.join(assignment_dir, 'images')
            os.makedirs(images_dir, exist_ok=True)

            for img in soup.find_all('img'):
                if img.get('src'):
                    img_url = urljoin(assignment_url, img['src'])
                    img_filename = os.path.basename(img_url)
                    local_path = os.path.join(images_dir, img_filename)
                    
                    if self.download_file(img_url, local_path):
                        # Update image src to local path
                        img['src'] = f'images/{img_filename}'

            # Save processed HTML
            with open(os.path.join(assignment_dir, 'assignment.html'), 'w', encoding='utf-8') as f:
                f.write(str(soup))

            # Extract and save metadata
            metadata = {
                'title': soup.title.string if soup.title else f'Assignment {number}',
                'number': number,
                'url': assignment_url,
                'images': [img['src'] for img in soup.find_all('img')]
            }

            with open(os.path.join(assignment_dir, 'metadata.json'), 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2)

            self.assignments.append(metadata)
            print(f'Successfully processed Assignment {number}')
            return True

        except Exception as e:
            print(f'Error processing assignment {number}: {e}')
            return False

    def scrape_all_assignments(self):
        """Scrape all assignments from the index page"""
        try:
            response = requests.get(self.base_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all assignment links
            for link in soup.find_all('a'):
                href = link.get('href', '')
                if 'assignment' in href.lower():
                    # Extract assignment number
                    number = int(''.join(filter(str.isdigit, href.split('Assignment')[0])))
                    assignment_url = urljoin(self.base_url, href)
                    self.process_assignment(assignment_url, number)

            # Save assignments index
            with open(os.path.join(self.output_dir, 'assignments.json'), 'w', encoding='utf-8') as f:
                json.dump({
                    'assignments': sorted(self.assignments, key=lambda x: x['number'])
                }, f, indent=2)

        except Exception as e:
            print(f'Error scraping assignments: {e}')

def main():
    base_url = 'https://lucasblanco.com/ed/ART1300/as/'
    output_dir = 'content/ART1300'
    
    scraper = AssignmentScraper(base_url, output_dir)
    scraper.scrape_all_assignments()

if __name__ == '__main__':
    main()