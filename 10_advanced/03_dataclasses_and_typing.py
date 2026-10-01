"""
Phase 1 - Advanced: Dataclasses and Type Annotations
"""

from dataclasses import dataclass, field

@dataclass
class ProjectTask:
    task_id: int
    title: str
    points: int = 1
    tags: list[str] = field(default_factory=list)
    is_completed: bool = False

t1 = ProjectTask(1, "Configure CI/CD Pipeline", points=5, tags=["devops", "git"])
t2 = ProjectTask(2, "Implement OOP Models", points=3, tags=["python"])

print(t1)
print(f"Task 1 Points: {t1.points}")
