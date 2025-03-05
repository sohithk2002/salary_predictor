import joblib
from django.shortcuts import render

# Load the trained model and LabelEncoder
model = joblib.load('prediction/models/salary_predictor_model.pkl')
label_encoder = joblib.load('prediction/models/label_encoder.pkl')

# Function to predict salary
def predict_salary(user_role):
    try:
        # Encode the user input role
        role_encoded = label_encoder.transform([user_role])[0]
    except ValueError:
        return "Role not found. Please enter a valid role."

    # Make a prediction using the trained model
    predicted_salary = model.predict([[role_encoded]])[0]
    return f"Predicted Salary for '{user_role}': ${predicted_salary:,.2f}"

def home(request):
    return render(request, 'prediction/home.html')

def job_market_insight(request):
    return render(request, 'prediction/job_market_insight.html')

def skill_gap(request):
    predicted_salary = None
    if request.method == 'POST':
        user_role = request.POST.get('role')
        if user_role:
            predicted_salary = predict_salary(user_role)

    return render(request, 'prediction/skill_gap.html', {'predicted_salary': predicted_salary})