import streamlit as st

# Define alcohol properties
alcohol_data = {
    "Ethanol": {"specific_gravity": 0.79, "volume_distribution": 0.53},
    "Methanol": {"specific_gravity": 0.79, "volume_distribution": 0.6},
    "Ethylene Glycol": {"specific_gravity": 1.1, "volume_distribution": 0.83},
    "Isopropanol": {"specific_gravity": 0.785, "volume_distribution": 0.6}
}

st.title("Blood Alcohol Concentration Calculator")

# User inputs
alcohol_type = st.selectbox("Select Alcohol Type", options=list(alcohol_data.keys()))
volume_ingested = st.number_input("Volume Ingested (in mL)", min_value=0.0, step=0.1)
percent_solution = st.number_input("Percent Solution (%)", min_value=0.0, max_value=100.0, step=0.1)
weight = st.number_input("Patient Weight (in kg)", min_value=0.0, step=0.1)

# Calculate blood concentration
if st.button("Calculate Blood Concentration"):
    # Get the selected alcohol's properties
    specific_gravity = alcohol_data[alcohol_type]["specific_gravity"]
    volume_distribution = alcohol_data[alcohol_type]["volume_distribution"]

    # Blood concentration calculation in mg/dL
    blood_concentration_mg_dl = (volume_ingested * percent_solution * specific_gravity) / (volume_distribution * weight)

    # Display result
    st.write(f"Estimated Blood Concentration of {alcohol_type}: {blood_concentration_mg_dl:.2f} mg/dL")
