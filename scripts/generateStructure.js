const fs = require('fs').promises;
const path = require('path');

const COURSES = [
  'ART1201C',
  'ART1202C',
  'ART1205C',
  'ART1300C',
  'ART2301C',
  'ART2500C',
  'ART2501C',
  'ART2600C'
];

const TOTAL_WEEKS = 15;

async function generateStructure() {
  try {
    // Create base modules directory if it doesn't exist
    await fs.mkdir('src/modules', { recursive: true });

    for (const course of COURSES) {
      console.log(`Generating structure for ${course}...`);
      
      // Create course directory and weeks subdirectory
      const courseDir = `src/modules/${course}/weeks`;
      await fs.mkdir(courseDir, { recursive: true });

      // Generate week files
      for (let week = 1; week <= TOTAL_WEEKS; week++) {
        const weekFile = path.join(courseDir, `Week${week}.tsx`);
        
        // Only create file if it doesn't exist
        try {
          await fs.access(weekFile);
          console.log(`${weekFile} already exists, skipping...`);
        } catch {
          await fs.writeFile(weekFile, getWeekTemplate(week));
          console.log(`Created ${weekFile}`);
        }
      }
    }

    console.log('Structure generation complete!');
  } catch (error) {
    console.error('Error generating structure:', error);
    process.exit(1);
  }
}

function getWeekTemplate(weekNumber) {
  return `import React, { useState } from 'react';
import { ChevronDown, ChevronUp, BookOpen, Calendar, CheckCircle, Info } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const Week${weekNumber}Page = () => {
  const [expandedSections, setExpandedSections] = useState({
    overview: true,
    objectives: false,
    assignments: false,
    resources: false
  });

  const toggleSection = (section) => {
    setExpandedSections((prev) => ({
      ...prev,
      [section]: !prev[section]
    }));
  };

  const weekData = {
    weekNumber: ${weekNumber},
    title: "",
    description: "",
    learningObjectives: [],
    assignments: [],
    resources: [],
    competencies: [],
    nextSteps: ""
  };

  return (
    <div className="max-w-4xl mx-auto p-6 space-y-6">
      {/* Week Header */}
      <div className="bg-blue-50 p-6 rounded-lg">
        <h1 className="text-2xl font-bold mb-2">Week {weekData.weekNumber}</h1>
        <p className="text-gray-600">{weekData.description}</p>
      </div>

      {/* Learning Objectives */}
      <Card>
        <CardHeader 
          className="cursor-pointer"
          onClick={() => toggleSection('objectives')}
        >
          <div className="flex justify-between items-center">
            <div className="flex items-center">
              <CheckCircle className="w-5 h-5 mr-2 text-green-500" />
              <CardTitle>Learning Objectives</CardTitle>
            </div>
            {expandedSections.objectives ? 
              <ChevronUp className="w-5 h-5" /> : 
              <ChevronDown className="w-5 h-5" />
            }
          </div>
        </CardHeader>
        {expandedSections.objectives && (
          <CardContent>
            <ul className="list-disc pl-5 space-y-2">
              {weekData.learningObjectives.map((objective, index) => (
                <li key={index} className="text-gray-700">{objective}</li>
              ))}
            </ul>
          </CardContent>
        )}
      </Card>
    </div>
  );
};

export default Week${weekNumber}Page;`;
}

generateStructure();