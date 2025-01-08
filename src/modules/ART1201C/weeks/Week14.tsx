import React, { useState } from 'react';
import { ChevronDown, ChevronUp, BookOpen, Calendar, CheckCircle, Info } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const Week14Page = () => {
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
    weekNumber: 14,
    title: "Final Project Development",
    description: "Focused work time on final projects with individual consultations and peer review sessions.",
    learningObjectives: [],
    assignments: [],
    resources: [],
    competencies: [],
    nextSteps: ""
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

      {/* Assignments */}
      <Card>
        <CardHeader 
          className="cursor-pointer"
          onClick={() => toggleSection('assignments')}
        >
          <div className="flex justify-between items-center">
            <div className="flex items-center">
              <Calendar className="w-5 h-5 mr-2 text-blue-500" />
              <CardTitle>Assignments</CardTitle>
            </div>
            {expandedSections.assignments ? 
              <ChevronUp className="w-5 h-5" /> : 
              <ChevronDown className="w-5 h-5" />
            }
          </div>
        </CardHeader>
        {expandedSections.assignments && (
          <CardContent>
            <div className="space-y-4">
              {weekData.assignments.map((assignment, index) => (
                <div key={index} className="border-b pb-4 last:border-b-0 last:pb-0">
                  <h3 className="font-semibold mb-2">{assignment.title}</h3>
                  <p className="text-gray-600 mb-2">{assignment.description}</p>
                  <div className="flex items-center text-sm text-gray-500">
                    <Calendar className="w-4 h-4 mr-1" />
                    <span>Due: {assignment.dueDate}</span>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        )}
      </Card>

      {/* Resources */}
      <Card>
        <CardHeader 
          className="cursor-pointer"
          onClick={() => toggleSection('resources')}
        >
          <div className="flex justify-between items-center">
            <div className="flex items-center">
              <BookOpen className="w-5 h-5 mr-2 text-purple-500" />
              <CardTitle>Resources</CardTitle>
            </div>
            {expandedSections.resources ? 
              <ChevronUp className="w-5 h-5" /> : 
              <ChevronDown className="w-5 h-5" />
            }
          </div>
        </CardHeader>
        {expandedSections.resources && (
          <CardContent>
            <div className="space-y-4">
              {weekData.resources.map((resource, index) => (
                <div key={index} className="flex items-start space-x-4">
                  <div className="flex-grow">
                    <h3 className="font-semibold">{resource.title}</h3>
                    <p className="text-sm text-gray-600">{resource.description}</p>
                    {resource.link && (
                      <a 
                        href={resource.link}
                        className="text-blue-500 hover:text-blue-600 text-sm mt-1 inline-block"
                      >
                        View Resource →
                      </a>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        )}
      </Card>
    </div>
  );
};

export default Week14Page;