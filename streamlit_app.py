# 🩺 Streamlit Medical Generator V7 - Using External Diagnosis Data
import streamlit as st
from diagnosis_data import pe_by_diagnosis  # 🔗 Load full diagnosis list (500+)

st.set_page_config(page_title="Medical Generator V7", layout="wide")
st.title("🩺 English Admission Note Generator | V7")

# --- Sidebar: Basic Info ---
st.sidebar.header("Basic Info")
age = st.sidebar.number_input("Age", 0, 120, 65)
sex = st.sidebar.selectbox("Sex", ["Male", "Female"])
adl = st.sidebar.selectbox("ADL status", ["ADL independent", "ADL dependent", "Bedridden"])

# --- Diagnosis Section ---
st.subheader("Diagnosis Selection")
diagnosis_options = sorted(pe_by_diagnosis.keys())
primary_dx = st.selectbox("Primary Diagnosis", diagnosis_options)
secondary_dx = st.multiselect("Secondary Diagnoses", diagnosis_options)
combined_dx = list(dict.fromkeys([primary_dx] + secondary_dx))

# --- PE Section: Suggested by Diagnosis ---
st.subheader("Suggested Physical Exams")
pe_selected = []
for dx in combined_dx:
    if dx in pe_by_diagnosis:
        st.markdown(f"**Diagnosis: {dx}**")
        for pe_item in pe_by_diagnosis[dx]:
            col1, col2 = st.columns([1, 2])
            result = col1.selectbox(
                f"{pe_item}",
                ["-", "+", "+ (mild)", "+ (moderate)", "+ (severe)", "Normal"],
                key=f"pe_{dx}_{pe_item}"
            )
            note = col2.text_input(f"Details for {pe_item}", key=f"note_{dx}_{pe_item}")
            pe_selected.append(f"{pe_item}: {result} {note}")

# --- Manual PE Entry ---
st.subheader("Other PE (Manual Entry)")
manual_pe = st.text_area("Additional PE findings")

# --- Chief Complaint ---
st.subheader("Chief Complaint")
complaints = st.text_area("List chief complaints")

# --- Past Medical History ---
st.subheader("Past Medical History")
if "pmh_count" not in st.session_state:
    st.session_state.pmh_count = 1
if st.button("➕ Add PMH"):
    st.session_state.pmh_count += 1
pmh_list = []
for i in range(st.session_state.pmh_count):
    with st.expander(f"PMH Entry #{i+1}"):
        dx = st.text_input(f"Condition {i+1}", key=f"pmh_dx_{i}")
        status = st.text_input(f"Severity / Grade {i+1}", key=f"pmh_status_{i}")
        note = st.text_area(f"Notes {i+1}", key=f"pmh_note_{i}")
        if dx:
            pmh_list.append(f"{dx} ({status}) - {note}")
freeform_pmh = st.text_area("📌 Additional PMH (paragraph)")

# --- ROS ---
st.subheader("Review of Systems (Negative)")
ros_items = ["Fever", "Cough", "Chest pain", "Abdominal pain", "Dysuria"]
ros_negative = []
for ros in ros_items:
    choice = st.radio(f"{ros}", ["-", "+"], horizontal=True, key=f"ros_{ros}")
    if choice == "-":
        ros_negative.append(ros)

# --- Impression & Plan ---
st.subheader("Impression & Plan")
impression = st.text_input("Impression")
plan = st.text_area("Plan")

# --- OPD / ER / Admission Notes ---
st.subheader("Hospital Course")
with st.expander("🩺 Outpatient Department (OPD)"):
    opd_note = st.text_area("OPD Note")
with st.expander("🏥 Emergency Room (ER)"):
    er_note = st.text_area("ER Note")
with st.expander("🏨 Admission"):
    admit_note = st.text_area("Admission Note")

# --- Output Generation ---
if st.button("📄 Generate English Admission Note"):
    all_pe = "; ".join(pe_selected + [manual_pe.strip()])
    pmh_summary = "; ".join(pmh_list)
    output = f"""
This is a {age} y/o {sex.lower()} who is {adl.lower()}.

Chief complaints: {complaints.strip()}

Primary diagnosis: {primary_dx}
Secondary diagnoses: {', '.join(secondary_dx)}

Past medical history: {pmh_summary}
Additional PMH: {freeform_pmh.strip()}

Review of systems negative for: {', '.join(ros_negative)}.
Physical examination showed: {all_pe.strip()}.

OPD course: {opd_note.strip()}
ER course: {er_note.strip()}
Admission course: {admit_note.strip()}

Impression: {impression}
Plan: {plan}
"""
    st.subheader("📝 Final English Admission Note")
    st.code(output.strip(), language="markdown")