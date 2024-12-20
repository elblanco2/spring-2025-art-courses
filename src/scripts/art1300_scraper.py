import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path

class ART1300Scraper:
    def __init__(self):
        self.base_url = 'https://lucasblanco.com/ed/ART1300/as/'
        self.assignments = []

    def fetch_assignments(self):
        try:
            response = requests.get(self.base_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all assignment links
            links = soup.find_all('a', href=True)
            assignment_links = [link for link in links if 'assignment' in link['href'].lower()]
            
            for link in assignment_links:
                assignment_url = self.base_url + link['href']
                self.fetch_assignment_content(assignment_url)
                
        except Exception as e:
            print(f'Error fetching assignments: {e}')

    def fetch_assignment_content(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract assignment content
            content = {
                'url': url,
                'title': soup.title.string if soup.title else '',
                'content': soup.get_text(),
                'objectives': self.extract_objectives(soup),
                'requirements': self.extract_requirements(soup)
            }
            
            self.assignments.append(content)
            
        except Exception as e:
            print(f'Error fetching assignment content from {url}: {e}')

    def extract_objectives(self, soup):
        # Look for objectives section
        objectives = []
        obj_section = soup.find(text=lambda t: t and 'objective' in t.lower())
        if obj_section:
            # Extract nearby text that might contain objectives
            pass
        return objectives

    def extract_requirements(self, soup):
        # Look for requirements section
        requirements = []
        req_section = soup.find(text=lambda t: t and 'requirement' in t.lower())
        if req_section:
            # Extract nearby text that might contain requirements
            pass
        return requirements

    def analyze_content(self):
        # Analyze assignments for potential module groupings
        analysis = {
            'total_assignments': len(self.assignments),
            'themes': self.identify_themes(),
            'skill_progression': self.analyze_skill_progression()
        }
        return analysis

    def identify_themes(self):
        # Identify common themes across assignments
        themes = set()
        for assignment in self.assignments:
            # Extract keywords and themes from content
            pass
        return list(themes)

    def analyze_skill_progression(self):
        # Analyze how skills build upon each other
        progression = {
            'foundational_skills': [],
            'intermediate_skills': [],
            'advanced_skills': []
        }
        return progression

    def save_results(self, filename='art1300_analysis.json'):
        output = {
            'assignments': self.assignments,
            'analysis': self.analyze_content()
        }
        
        with open(filename, 'w') as f:
            json.dump(output, f, indent=2)

# Usage
if __name__ == '__main__':
    scraper = ART1300Scraper()
    scraper.fetch_assignments()
    scraper.save_results()
