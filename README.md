# Spring 2025 Art Courses - Canvas LMS Migration

Project to organize and migrate art course content to Canvas LMS modules for Spring 2025.

## Courses

1. ART 1201C-5 Basic Design (Wed 9:40AM - 10:30AM)
2. ART 1202C-71 Two Dimensional Design (Wed 9:40AM - 10:30AM)
3. ART 1205C-44 Color & Composition 1 (Wed 9:40AM - 10:30AM)
4. ART 1300C-30 Drawing (Wed 12:20PM - 1:10PM)
5. ART 2301C-7 Drawing 2 (Wed 12:20PM - 1:10PM)
6. ART 2500C-30 Painting 1 (Wed 12:20PM - 1:10PM)
7. ART 2501C-40 Painting 2 (Wed 12:20PM - 1:10PM)
8. ART 2600C-88 Computer Art (Wed 9:40AM - 10:30AM)
9. ARH1000 Introduction to Art (Wed TBD)

## Project Structure

```
/src
  /scripts           # Python scripts for content scraping and migration
  /templates         # HTML/React templates for content display
  /modules           # Course module organization
    /ART1201C
    /ART1202C
    /ART1205C
    /ART1300C
    /ART2301C
    /ART2500C
    /ART2501C
    /ART2600C
    /ARH1000
  /components        # Reusable React components
/docs               # Project documentation
/tests              # Test files
```

## Development Stack

- React with Tailwind CSS for responsive templates
- Python for content scraping and Canvas LMS integration
- Canvas LMS API for content deployment

## Module Structure

Each course is organized into 5 modules:
1. Foundations & Core Concepts
2. Technical Skills Development
3. Creative Exploration
4. Advanced Applications
5. Final Projects & Portfolio

## Getting Started

1. Clone the repository
2. Install dependencies
3. Configure Canvas LMS API credentials
4. Run content migration scripts

## License

MIT License