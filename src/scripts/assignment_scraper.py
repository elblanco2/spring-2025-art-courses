import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin, urlparse
from pathlib import Path
import shutil

class AssignmentScraper:
    def __init__(self, base_url, course_code):
        self.base_url = base_url
        self.course_code = course_code
        self.output_dir = Path(f'content/{course_code}')
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def download_file(self, url, output_path):
        """Download a file from URL to specified path"""
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            with open(output_path, 'wb') as f:
                shutil.copyfileobj(response.raw, f)
            return True
        except Exception as e:
            print(f'Error downloading {url}: {e}')
            return False

    def process_images(self, html_content, base_url, assignment_dir):
        """Extract and download images from HTML content"""
        soup = BeautifulSoup(html_content, 'html.parser')
        images = soup.find_all('img')
        
        for img in images:
            if img.get('src'):
                img_url = urljoin(base_url, img['src'])
                img_filename = os.path.basename(urlparse(img_url).path)
                img_path = assignment_dir / 'images' / img_filename
                
                img_path.parent.mkdir(exist_ok=True)
                if self.download_file(img_url, img_path):
                    # Update image src in HTML to relative path
                    img['src'] = f'images/{img_filename}'

        return str(soup)

    def scrape_assignment(self, assignment_url, assignment_number):
        """Scrape a single assignment and its resources"""
        try:
            # Create assignment directory
            assignment_dir = self.output_dir / f'assignment_{assignment_number}'
            assignment_dir.mkdir(exist_ok=True)

            # Download main HTML
            response = requests.get(assignment_url)
            response.raise_for_status()
            html_content = response.text

            # Process images and update HTML
            updated_html = self.process_images(html_content, assignment_url, assignment_dir)

            # Save updated HTML
            with open(assignment_dir / 'assignment.html', 'w', encoding='utf-8') as f:
                f.write(updated_html)

            # Download associated files (docx, pptx, etc.)
            base_name = os.path.splitext(os.path.basename(assignment_url))[0]
            for ext in ['.docx', '.pptx']:
                file_url = assignment_url.replace('.html', ext)
                if requests.head(file_url).status_code == 200:
                    self.download_file(file_url, assignment_dir / f'{base_name}{ext}')

            return True

        except Exception as e:
            print(f'Error processing assignment {assignment_number}: {e}')
            return False

    def extract_assignment_info(self, html_content):
        """Extract key information from assignment HTML"""
        soup = BeautifulSoup(html_content, 'html.parser')
        info = {
            'title': soup.title.string if soup.title else '',
            'objectives': [],
            'requirements': [],
            'materials': [],
            'due_date': None
        }

        # Extract sections based on common headers or formatting
        # This will need to be customized based on actual HTML structure
        return info

    def create_assignment_metadata(self, assignment_number, info):
        """Create metadata file for assignment"""
        metadata_path = self.output_dir / f'assignment_{assignment_number}' / 'metadata.json'
        with open(metadata_path, 'w') as f:
            json.dump(info, f, indent=2)

def main():
    # Example usage
    base_url = 'https://lucasblanco.com/ed/ART1300/as/'
    scraper = AssignmentScraper(base_url, 'ART1300')
    
    # Test with Assignment 3
    assignment_url = f'{base_url}3ViewfinderDrawingAssignment.html'
    success = scraper.scrape_assignment(assignment_url, 3)
    
    if success:
        print(f'Successfully scraped assignment 3')

if __name__ == '__main__':
    main()