# drug_database.py
def get_available_drugs():
    """Returns a list of drugs available in the system."""
    return ["Amoxicillin", "Ibuprofen", "Paracetamol", "Azithromycin"]

def get_safe_dosage(drug_name):
    """Returns the dosage rules for a specific drug."""
    # Dictionary storing mg per kg, and absolute max daily limits
    drugs = {
        "Amoxicillin": {"mg_per_kg": 20, "max_daily_mg": 1000},
        "Ibuprofen": {"mg_per_kg": 10, "max_daily_mg": 1200},
        "Paracetamol": {"mg_per_kg": 15, "max_daily_mg": 4000},
        "Azithromycin": {"mg_per_kg": 10, "max_daily_mg": 500}
    }
    return drugs.get(drug_name)


def get_drug_details(drug_name):
    """Returns educational information about a medicine and common uses."""
    details = {
        "Amoxicillin": {
            "class": "Penicillin-type antibiotic",
            "common_uses": "Certain bacterial infections of the ear, nose, throat, skin, and urinary tract.",
            "conditions": "May be prescribed for conditions such as bacterial sinusitis, otitis media, strep throat, or some urinary tract infections when a clinician confirms a susceptible bacterial cause.",
            "not_for": "Viral illnesses such as the common cold or influenza.",
        },
        "Ibuprofen": {
            "class": "Nonsteroidal anti-inflammatory drug (NSAID)",
            "common_uses": "Temporary relief of pain, fever, and inflammation.",
            "conditions": "May be used for headaches, toothache, muscle or joint pain, menstrual cramps, fever, and some inflammatory conditions when appropriate.",
            "not_for": "It is not an antibiotic and does not treat bacterial or viral infections.",
        },
        "Paracetamol": {
            "class": "Analgesic and antipyretic",
            "common_uses": "Relief of mild-to-moderate pain and reduction of fever.",
            "conditions": "May be used for headache, toothache, muscle aches, period pain, and fever when the cause and patient-specific limits are appropriate.",
            "not_for": "It does not treat the underlying cause of an infection and excessive use can seriously harm the liver.",
        },
        "Azithromycin": {
            "class": "Macrolide antibiotic",
            "common_uses": "Treatment of selected bacterial respiratory, skin, and sexually transmitted infections.",
            "conditions": "May be prescribed for certain bacterial pneumonia, bronchitis, throat, skin, or chlamydial infections after clinical assessment.",
            "not_for": "Viral respiratory illnesses, unless a clinician identifies a separate bacterial infection.",
        },
    }
    return details.get(drug_name)