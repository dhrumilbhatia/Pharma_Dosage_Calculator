# main.py
import patient
import drug_database
import utils
import dosage
import reports

def get_drug_list():
    """Fetches the list of drugs to populate the UI dropdown."""
    return drug_database.get_available_drugs()

def process_prescription(name, age, weight_kg, height_cm, selected_drug):
    """Orchestrates the entire flow from intake to final report."""
    
    # 1. Calculate BMI from the patient's metric measurements.
    bmi = utils.calculate_bmi(weight_kg, height_cm)
    
    # 2. Create patient profile (using patient.py)
    current_patient = patient.create_profile(name, age, weight_kg, height_cm, bmi)
    
    # 3. Get drug safety limits (using drug_database.py)
    drug_specs = drug_database.get_safe_dosage(selected_drug)
    
    # 4. Calculate a weight-based dose safely (using dosage.py).
    # BMI is displayed as a health indicator; it is not used to prescribe medication.
    final_dose_info = dosage.calculate_dose(
        current_patient["weight_kg"], 
        drug_specs["mg_per_kg"], 
        drug_specs["max_daily_mg"]
    )
    
    # 5. Generate and return the report (using reports.py)
    prescription_text = reports.generate_prescription(current_patient, selected_drug, final_dose_info)
    
    return prescription_text