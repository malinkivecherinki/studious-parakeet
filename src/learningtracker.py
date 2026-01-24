#!/usr/bin/env python3
"""
LearningTracker - Personal learning progress tracker.
"""

from datetime import datetime
from typing import List, Dict

class LearningGoal:
    """Represents a learning goal."""
    def __init__(self, title: str, target_hours: float = 0):
        self.title = title
        self.target_hours = target_hours
        self.completed_hours = 0.0
        self.created_at = datetime.now()
    
    def add_progress(self, hours: float):
        """Add progress hours."""
        self.completed_hours += hours
    
    def get_progress_percent(self) -> float:
        """Get progress percentage."""
        if self.target_hours == 0:
            return 0.0
        return min(100.0, (self.completed_hours / self.target_hours) * 100)

class LearningTracker:
    """Track learning progress."""
    def __init__(self):
        self.goals: List[LearningGoal] = []
    
    def add_goal(self, title: str, target_hours: float = 0) -> LearningGoal:
        """Add a new learning goal."""
        goal = LearningGoal(title, target_hours)
        self.goals.append(goal)
        return goal
    
    def get_progress_summary(self) -> Dict:
        """Get overall progress summary."""
        total_target = sum(g.target_hours for g in self.goals)
        total_completed = sum(g.completed_hours for g in self.goals)
        
        return {
            "total_goals": len(self.goals),
            "total_target_hours": total_target,
            "total_completed_hours": total_completed,
            "overall_progress": (total_completed / total_target * 100) if total_target > 0 else 0
        }

if __name__ == "__main__":
    tracker = LearningTracker()
    print("LearningTracker initialized")
