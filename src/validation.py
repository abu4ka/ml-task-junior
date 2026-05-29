def validate_student(student):
    required_fields = ["age", "study_hours_per_week", "attendance_rate", "previous_score",
        "assignments_completed", "sleep_hours", "practice_tests_taken",
        "late_submissions", "absences", "internet_usage_hours", "social_media_hours",
        "gender", "parent_education", "course_type", "learning_format",
        "has_part_time_job", "internet_access"]
    for field in required_fields:
        if field not in student:
            raise ValueError(f"Validation error missing field: {field}")
    
    numeric_rules = {
        "age": (10,80), 
        "study_hours_per_week": (0, 80),
        "attendance_rate": (0, 100),
        "previous_score": (0, 100), 
        "assignments_completed": (0, 30),
        "sleep_hours": (0, 14),
        "practice_tests_taken": (0, 20),
        "late_submissions": (0, 30),
        "absences": (0, 50),
        "internet_usage_hours": (0, 24),
        "social_media_hours": (0, 24),
    }

    for field, (min_val, max_val) in numeric_rules.items():
        value = student[field]
        if not(min_val<=value<=max_val):
            raise ValueError(f"Validation error {field} must be between {min_val} and {max_val}")
        
    category_rules = {
        "gender": ["male", "female"],
        "parent_education": ["high_school", "bachleor", "master", "phd"],
        "course_type": ["math", "english", "programming", "science"],
        "learning_format": ["online", "offline", "hybrid"],
        "has_part_time_job": ["yes", "no"],
        "internet_access": ["yes", "no"],
    }

    for field, allowed in category_rules.items():
        if student[field] not in allowed:
            raise ValueError(f"Validation error: {field} must be one of {allowed}")
    return True 

