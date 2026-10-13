# dosage.py
def calculate_dose(patient_weight_kg, mg_per_kg, max_limit):
    """Calculates the safe dose, ensuring it doesn't exceed the daily limit."""
    recommended = patient_weight_kg * mg_per_kg
    
    if recommended > max_limit:
        return {"dose": max_limit, "warning": "Max daily limit reached!"}
    
    return {"dose": round(recommended, 2), "warning": None}