# patient.py
def create_profile(name, age, weight_kg, height_cm, bmi):
    """Creates and returns a patient profile dictionary."""
    return {
        "name": name, 
        "age": age, 
        "weight_kg": weight_kg,
        "height_cm": height_cm,
        "bmi": bmi
    }