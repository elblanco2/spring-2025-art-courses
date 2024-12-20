import requests
from bs4 import BeautifulSoup
import json

def scrape_course_content(base_url):
    # Get the main page content
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Initialize content structure
    course_content = {
        'assignments': [],
        'resources': []
    }
    
    # Find all links in the page
    links = soup.find_all('a')
    
    for link in links:
        href = link.get('href')
        text = link.text.strip()
        
        if 'Assignment' in text:
            # Get assignment content
            assignment_url = base_url + href if not href.startswith('http') else href
            assignment_response = requests.get(assignment_url)
            assignment_soup = BeautifulSoup(assignment_response.text, 'html.parser')
            
            assignment_content = {
                'title': text,
                'url': assignment_url,
                'content': assignment_soup.get_text(strip=True),
                'html': assignment_soup.prettify()
            }
            
            course_content['assignments'].append(assignment_content)
        elif any(resource in text.lower() for resource in ['supply', 'help', 'list', 'link']):
            resource_content = {
                'title': text,
                'url': href
            }
            course_content['resources'].append(resource_content)
    
    return course_content

def analyze_content(course_content):
    """Analyze the content to identify themes and potential module groupings"""
    analysis = {
        'num_assignments': len(course_content['assignments']),
        'num_resources': len(course_content['resources']),
        'assignment_themes': [],
        'content_length': []
    }
    
    # Analyze each assignment for themes and length
    for assignment in course_content['assignments']:
        analysis['content_length'].append({
            'title': assignment['title'],
            'length': len(assignment['content'])
        })
        
    return analysis

# Main execution
if __name__ == '__main__':
    base_url = 'https://lucasblanco.com/ed/ART1300/'
    content = scrape_course_content(base_url)
    analysis = analyze_content(content)
    
    # Save the results
    with open('art1300_content.json', 'w') as f:
        json.dump(content, f, indent=2)
    
    with open('art1300_analysis.json', 'w') as f:
        json.dump(analysis, f, indent=2)
