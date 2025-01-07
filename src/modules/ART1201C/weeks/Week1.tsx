import React, { useState } from 'react';
import { ChevronDown, ChevronUp, BookOpen, Calendar, CheckCircle, Info } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const Week1Page = () => {
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
    weekNumber: 1,
    title: "Introduction to Basic Design Elements",
    description: "This week introduces fundamental design elements and begins our exploration of visual transformation through the Barcode Assignment.",
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
    </div>
  );
};

export default Week1Page;