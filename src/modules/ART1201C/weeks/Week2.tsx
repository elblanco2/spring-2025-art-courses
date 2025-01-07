import React, { useState } from 'react';
import { ChevronDown, ChevronUp, BookOpen, Calendar, CheckCircle, Info } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const Week2Page = () => {
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
    weekNumber: 2,
    title: "Four Lines Three Times Assignment",
    description: "This week focuses on the expressive qualities of line and composition through repeated exercises.",
    learningObjectives: [
      "Develop control and intentionality in line-making",
      "Understand how repetition affects visual impact",
      "Practice creating visual rhythm through line work"
    ],
    assignments: [
      {
        title: "Four Lines Three Times",
        dueDate: "January 23, 2025",
        points: 10,
        description: "Create three variations of four-line compositions, exploring different arrangements and visual effects."
      }
    ],
    resources: [],
    competencies: [
      "Application of basic design principles through line exploration",
      "Development of technical control and precision"
    ],
    nextSteps: "Prepare for next week's Figure-Ground Assignment by reviewing positive and negative space concepts."
  };

  return (
    <div className="max-w-4xl mx-auto p-6 space-y-6">
      <div className="bg-blue-50 p-6 rounded-lg">
        <h1 className="text-2xl font-bold mb-2">Week {weekData.weekNumber}: {weekData.title}</h1>
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

      {/* Rest of the component structure */}
    </div>
  );
};

export default Week2Page;