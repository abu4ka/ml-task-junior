import os
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns 

df = pd.read_csv("./ml-task-junior/data/students_perfomance.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df["risk_level"].value_counts())
print(df.groupby("course_type")["final_score"].mean())



with open("./ml-task-junior/reports/eda_summary.md", "w") as f:
    f.write("# EDA Summary\n\n")
    f.write("## Head\n")
    f.write(df.head().to_markdown())
    f.write("\n\n## Describe\n")
    f.write(df.describe().to_markdown())
    f.write("\n\n## Risk Level Count\n")
    f.write(df["risk_level"].value_counts().to_markdown())
    f.write("\n\n## Score by Course Type\n")
    f.write(df.groupby("course_type")["final_score"].mean().to_markdown())




os.makedirs("./ml-task-junior/reports/plots", exist_ok=True)

#1 Распределение final_score
plt.figure()
df["final_score"].hist(bins=20)
plt.title("Final Score Distribution")
plt.savefig("./ml-task-junior/reports/plots/final_score_distribution.png")
plt.close()

#2 Количество по risk-level 
plt.figure()
df["risk_level"].value_counts().plot(kind="bar")
plt.title("Risk Level")
plt.savefig("./ml-task-junior/reports/plots/risk_level_count.png")
plt.close()

#3 Балл по coursetype 
plt.figure()
df.groupby("course_type")["final_score"].mean().plot(kind='bar')
plt.title("Score by learning format")
plt.savefig("./ml-task-junior/reports/plots/score_by_learning_format.png")
plt.close()


#4 Балл по learning format
plt.figure()
df.groupby("learning_format")["final_score"].mean().plot(kind='bar')
plt.title("Score by learning format")
plt.savefig("./ml-task-junior/reports/plots/score_by_learning_format.png")
plt.close()



#5 study_hours and final_score 
plt.figure()
plt.scatter(df["study_hours_per_week"], df["final_score"], alpha=0.4)
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Final Hours vs Score")
plt.savefig("./ml-task-junior/reports/plots/stydy_hours_final_score.png")
plt.close()


#6 Корреляционная матрица
plt.figure(figsize=(10, 8))
corr = df.select_dtypes(include="number").corr()
plt.imshow(corr, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns, rotation=90)
plt.yticks(range(len(corr)), corr.columns)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("./ml-task-junior/reports/plots/correleation_matrix.png")
plt.close()

print("Analysis complete. Reports saved.")