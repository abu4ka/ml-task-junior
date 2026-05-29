def get_recommendation(student, predicted_score, risk_level):
    recommendations = []

    
    if student["attendance_rate"] < 60:
        recommendations.append("Improve attendance")
    
    if student["study_hours_per_week"] < 6:
        recommendations.append("Increase study hours")
    
    if student["assignments_completed"] < 5:
        recommendations.append("Complete more assignments")
    
    if student["sleep_hours"] < 6:
        recommendations.append("Fix sleep schedule")
    
    if student["social_media_hours"] > 4:
        recommendations.append("Reduce social media usage")

    if risk_level == "high_risk" and predicted_score < 50:
        recommendations.append("Consider tutoring")

 
    return ", ".join(recommendations) if recommendations else "Continue current strategy"