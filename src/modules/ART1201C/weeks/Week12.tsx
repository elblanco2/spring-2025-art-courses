import React, { useState } from 'react';
import { ChevronDown, ChevronUp, BookOpen, Calendar, CheckCircle, Info } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const Week12Page = () => {
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
    weekNumber: 12,
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

      {/* Other sections */}
    </div>
  );
};

export default Week12Page;