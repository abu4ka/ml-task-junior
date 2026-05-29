import pandas as pd

def add_features(df):
    df["study_efficiency"] = (df["previous_score"] / (df["study_hours_per_week"] + 1)).round(2)
    df["discipline_score"] = df["attendance_rate"] - df["absences"] * 2 - df["late_submissions"] * 3
    df["digital_distraction"] = (df["social_media_hours"] / (df["internet_usage_hours"] + 1)).round(2)
    return df 

df = pd.read_csv("./ml-task-junior/data/students_perfomance.csv")
df = add_features(df)
df.to_csv("./ml-task-junior/data/students_perfomance.csv", index=False)
print('3 features added succesfully')