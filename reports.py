# reports.py
def generate_prescription(patient, drug, dose_info):
    """Generates a formatted text report for the prescription."""
    report = f"### 📝 Official Prescription\n"
    report += f"**Patient Name:** {patient['name']} (Age: {patient['age']})\n"
    report += f"**Patient Weight:** {patient['weight_kg']} kg\n"
    report += f"**Patient Height:** {patient['height_cm']} cm\n"
    report += f"**BMI:** {patient['bmi']}\n"
    report += f"---\n"
    report += f"**Medication:** {drug}\n"
    report += f"**Recommended Daily Dose:** {dose_info['dose']} mg\n"
    
    if dose_info['warning']:
        report += f"\n⚠️ **SAFETY WARNING:** {dose_info['warning']}\n"
        
    return report