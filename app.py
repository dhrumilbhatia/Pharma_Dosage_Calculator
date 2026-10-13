# app.py
import streamlit as st

import main

st.set_page_config(page_title="Pharma Dosage Calculator", page_icon="🏥")
st.title("🏥 Dosage Calculator")
st.write(
    "A learning-focused clinical dosage calculator that accepts patient "
    "measurements, calculates BMI, and estimates a weight-based daily dose "
    "for the selected medicine using a configured safety limit."
)

with st.expander("About this app"):
    st.markdown(
        """
        This app collects a patient's name, age, weight in kilograms, height
        in centimeters, and selected medicine. It calculates BMI as an
        informational health indicator, then calculates a simplified
        weight-based medication dose and applies the medicine's configured
        maximum daily limit.

        **Important:** This is an educational demonstration, not a medical
        prescribing tool. Medication decisions must be checked by a qualified
        healthcare professional using the patient's diagnosis, allergies,
        medical history, kidney/liver function, formulation, and current
        clinical guidance.
        """
    )

with st.expander("How the app works"):
    st.markdown(
        """
        ### Section 1: Enter patient details
        Provide the patient's name, age, weight in kilograms, and height in
        centimeters.

        ### Section 2: Select a medicine
        Choose one of the medicines available in the application's drug
        database.

        ### Section 3: Calculate BMI
        The app converts height from centimeters to meters and calculates:

        `BMI = weight (kg) / height (m)²`

        It then displays the BMI value and category.

        ### Section 4: Calculate the dose
        The app applies the selected medicine's configured rule:

        `weight (kg) × medicine dose (mg/kg)`

        If that result exceeds the configured maximum daily amount, the app
        caps the result and displays a safety warning.

        ### Section 5: Generate the report
        Press **Calculate Safe Dosage & Print Rx** to display the patient
        details, BMI, selected medicine, recommended daily dose, and any
        safety warning.
        """
    )

col1, col2 = st.columns(2)

with col1:
    st.subheader("Patient Details")
    p_name = st.text_input("Patient Name", "Dhrumil")
    p_age = st.number_input("Age (Years)", min_value=1, max_value=120, value=30)
    p_weight_kg = st.number_input("Weight (kg)", min_value=2.0, max_value=300.0, value=75.0)
    p_height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=185.0)

with col2:
    st.subheader("Medication Details")
    available_drugs = main.get_drug_list()
    selected_drug = st.selectbox("Select Medication", available_drugs)

with st.expander(f"Medication information: {selected_drug}"):
    drug_details = main.drug_database.get_drug_details(selected_drug)
    dosage_rules = main.drug_database.get_safe_dosage(selected_drug)

    if drug_details is not None and dosage_rules is not None:
        st.markdown(f"**Medicine class:** {drug_details['class']}")
        st.markdown(f"**Common uses:** {drug_details['common_uses']}")
        st.markdown(f"**Conditions where it may be prescribed:** {drug_details['conditions']}")
        st.markdown(f"**Important limitation:** {drug_details['not_for']}")
        st.markdown(
            f"**Configured demonstration rule:** {dosage_rules['mg_per_kg']} mg/kg, "
            f"capped at {dosage_rules['max_daily_mg']} mg per day."
        )
        st.info(
            "This information describes common uses, not a recommendation for this "
            "patient. A healthcare professional must confirm the diagnosis, medicine, "
            "dose, interactions, contraindications, and duration."
        )

bmi = p_weight_kg / ((p_height_cm / 100) ** 2)
bmi_category = main.utils.bmi_category(bmi)
st.subheader("BMI Health Indicator")
st.metric("BMI", f"{bmi:.1f}", bmi_category)
st.progress(min(max(bmi / 40, 0.0), 1.0), text="BMI scale: 0 to 40+")
st.caption(
    "Underweight: below 18.5 | Healthy range: 18.5–24.9 | "
    "Overweight: 25–29.9 | Obese: 30–34.9 | Extremely obese: 35 or above"
)
st.warning(
    "BMI is an informational screening measure. It is not used to determine "
    "medication dosage; the dosage remains weight-based and capped by the drug limit."
)

if st.button("Calculate Safe Dosage & Print Rx", type="primary"):
    prescription_text = main.process_prescription(
        name=p_name,
        age=p_age,
        weight_kg=p_weight_kg,
        height_cm=p_height_cm,
        selected_drug=selected_drug,
    )
    st.success("Calculation Successful!")
    st.info(prescription_text)
