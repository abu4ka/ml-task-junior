import pandas as pd
import numpy as np

np.random.seed(42)
n = 500


df = pd.DataFrame({
    "age": np.random.randint(17, 30, n),
    "study_hours_per_week": np.random.randint(0, 80, n),
    "attendance_rate": np.random.randint(0, 100, n),
    "previous_score": np.random.randint(0, 100, n),
    "assignments_completed": np.random.randint(0, 30, n),
    "sleep_hours": np.random.randint(0, 14, n),
    "practice_tests_taken": np.random.randint(0, 20, n),
    "late_submissions": np.random.randint(0, 30, n),
    "absences": np.random.randint(0, 50, n),
    "internet_usage_hours": np.random.randint(0, 24, n),
    "social_media_hours": np.random.randint(0, 24, n),
    "gender": np.random.choice(["male", "female"], n),
    "parent_education": np.random.choice(["high_school", "bachelor", "master", "phd"], n),
    "course_type": np.random.choice(["math", "english", "programming", "science"], n),
    "learning_format": np.random.choice(["online", "offline", "hybrid"], n),
    "has_part_time_job": np.random.choice(["yes", "no"], n),
    "internet_access": np.random.choice(["yes", "no"], n),
})



noise = np.random.normal(0, 3, n)

df["final_score"] = (
    df["previous_score"] * 0.35
    + df["attendance_rate"] * 0.25
    + df["study_hours_per_week"] * 1.2
    + df["assignments_completed"] * 1.5
    + df["practice_tests_taken"] * 2
    - df["absences"] * 1.2
    - df["late_submissions"] * 1.5
    - df["social_media_hours"] * 2
    + noise
)

df["final_score"] = df["final_score"].clip(0, 100).round(2)

#Определяем risk_level
def get_risk(score):
    if score >= 75:
        return "low_risk"
    elif score >= 50:
        return "medium_risk"
    else:
        return "high_risk"

df["risk_level"] = df["final_score"].apply(get_risk)

#Сохраняем
df.to_csv("./ml-task-junior/data/students_perfomance.csv", index=False)

print("Dataset generated successfully.")
print(f"Rows: {len(df)}")
print("Saved to data/students_performance.csv")

