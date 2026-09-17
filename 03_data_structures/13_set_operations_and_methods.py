"""
Phase 1 - Data Structures: Set Operations (Union, Intersection, Difference)
"""

frontend_skills = {"HTML", "CSS", "JavaScript", "React", "TypeScript"}
backend_skills = {"Python", "JavaScript", "SQL", "FastAPI", "TypeScript", "Docker"}

# Union (All unique skills across both)
full_stack = frontend_skills | backend_skills
print("Union (All Skills):", full_stack)

# Intersection (Common skills)
shared_skills = frontend_skills & backend_skills
print("Intersection (Shared):", shared_skills)

# Difference (Skills only in frontend)
pure_frontend = frontend_skills - backend_skills
print("Frontend Only:", pure_frontend)

# Symmetric Difference (In one or the other, but not both)
exclusive_skills = frontend_skills ^ backend_skills
print("Symmetric Difference:", exclusive_skills)
