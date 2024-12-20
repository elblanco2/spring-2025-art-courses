import requests
import os
from pathlib import Path
import mammoth
import json
from bs4 import BeautifulSoup

class DocxScraper:
    def __init__(self, base_url='https://lucasblanco.com/ed/ART1300/as/'):
        self.base_url = base_url
        self.output_dir = Path('content/ART1300')
        self.assignments = [
            '1ValueHouseDrawingAssignment.docx',
            '2TheBigChallengeDrawingAssignment.docx',
            '3ViewfinderDrawingAssignment.docx',
            '4MondrianLineassignment.docx',
            '5LightandShadowwithCharcoalAssignment.docx',
            '6AlloverDrawing.docx',
            '7Find10newartistsontheArtstorDatabase.docx',
            '8OutofFocusDrawingAssignment.docx',
            '9BasicDrawingPerspective.docx',
            '10BasicDrawingProportion.docx',
            '11FlagDrawings.docx',
            '12FrottageDrawingAssignment.docx',
            '13EllipsesDrawingAssignment.docx',
            '14Straightlinedrawingassignment.docx',
            '15SearchingLineDrawingAssignment.docx',
            '16FiveVersionsofspheres.docx',
            '17FrottageDrawingAssignment.docx',
            '18RecreateaMasterpieceDrawingAssignment.docx',
            '19Inclassstilllifedrawing.docx',
            '20Largestilllifedrawingassignment.docx',
            'exAutomationDrawingAssignment.docx'
        ]
        self.supplementary = [
            ('misc/ART1300HelpfullinksDrawing.docx', 'helpful_links'),
            ('misc/ART1300DrawingSupplylist.docx', 'supply_list')
        ]

    def download_file(self, url, local_path):
        """Download a file and save it locally"""
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            
            with open(local_path, 'wb') as f:
                f.write(response.content)
            return True
        except Exception as e:
            print(f'Error downloading {url}: {e}')
            return False

    def convert_docx_to_html(self, docx_path):
        """Convert DOCX to HTML with mobile-friendly formatting"""
        try:
            with open(docx_path, 'rb') as docx_file:
                result = mammoth.convert_to_html(docx_file)
                html = result.value
                
                # Add mobile-friendly wrapper and styles
                template = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Assignment</title>
                    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
                </head>
                <body class="bg-gray-50">
                    <div class="max-w-2xl mx-auto p-4 bg-white shadow-lg rounded-lg my-4">
                        {html}
                    </div>
                </body>
                </html>
                """
                return template
        except Exception as e:
            print(f'Error converting {docx_path}: {e}')
            return None

    def process_assignment(self, filename, number=None):
        """Process a single assignment DOCX file"""
        try:
            # Create paths
            url = self.base_url + filename
            assignment_dir = self.output_dir / f'assignment_{number:02d}' if number else self.output_dir / 'supplementary'
            docx_path = assignment_dir / filename
            html_path = assignment_dir / f'{os.path.splitext(filename)[0]}.html'

            # Download DOCX
            if self.download_file(url, docx_path):
                # Convert to HTML
                html_content = self.convert_docx_to_html(docx_path)
                if html_content:
                    with open(html_path, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    return True
            return False
        except Exception as e:
            print(f'Error processing {filename}: {e}')
            return False

    def process_all(self):
        """Process all assignments and supplementary materials"""
        # Process main assignments
        for i, filename in enumerate(self.assignments, 1):
            print(f'Processing Assignment {i}: {filename}')
            self.process_assignment(filename, i)

        # Process supplementary materials
        for filename, folder in self.supplementary:
            print(f'Processing supplementary material: {filename}')
            self.process_assignment(filename)

def main():
    scraper = DocxScraper()
    scraper.process_all()

if __name__ == '__main__':
    main()