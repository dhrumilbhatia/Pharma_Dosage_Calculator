# utils.py
def calculate_bmi(weight_kg, height_cm):
    """Calculates BMI from a person's weight in kilograms and height in centimetres."""
    height_m = height_cm / 100
    return round(weight_kg / (height_m * height_m), 1)


def bmi_category(bmi):
    """Returns the standard adult BMI category for a BMI value."""
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Healthy range"
    if bmi < 30:
        return "Overweight"
    return "Obesity"