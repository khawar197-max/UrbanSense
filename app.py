import streamlit as st
import json
from groq import Groq

# ============================================================
# UrbanSense - AI Municipal Complaint Intelligence
# ============================================================

st.set_page_config(
    page_title="UrbanSense",
    page_icon="🏙️",
    layout="wide"
)

# ============================================================
# Header
# ============================================================

st.title("🏙️ UrbanSense")
st.subheader("AI-Powered Municipal Complaint Intelligence")

st.write(
    "UrbanSense uses AI to analyze citizen complaints, "
    "identify the problem category, assess priority, "
    "identify the responsible department, and recommend action."
)

st.divider()

# ============================================================
# Groq API
# ============================================================

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
    st.error(
        "Groq API key is not configured. "
        "Please add GROQ_API_KEY to Streamlit Secrets."
    )
    st.stop()


# ============================================================
# AI Complaint Analyzer
# ============================================================

def analyze_complaint(complaint):

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": """
You are UrbanSense, an AI municipal service assistant.

Analyze citizen complaints and return ONLY valid JSON.

Use these categories:
Sanitation, Sewerage/Drainage, Roads, Streetlights,
Water Supply, Encroachment, Parks, Property/Tax, Other.

Priority must be:
Critical, High, Medium, or Low.

Do not invent a location if it is not provided.

Keep the problem summary and recommended action
practical and concise.
"""
            },
            {
                "role": "user",
                "content": f"""
Analyze this citizen complaint:

{complaint}

Return exactly this JSON structure:

{{
    "category": "",
    "priority": "",
    "department": "",
    "location": "",
    "problem_summary": "",
    "recommended_action": ""
}}
"""
            }
        ],
        temperature=0.1
    )

    result = response.choices[0].message.content

    try:
        return json.loads(result)
    except json.JSONDecodeError:
        return None


# ============================================================
# Complaint Form
# ============================================================

st.header("📝 Submit a Municipal Complaint")

complaint = st.text_area(
    "Describe the municipal problem",
    placeholder=(
        "Example: There is a large amount of garbage "
        "near a school and it has not been removed for three days."
    ),
    height=150
)

location = st.text_input(
    "Location",
    placeholder="Example: Military Road"
)

# ============================================================
# Analyze Complaint
# ============================================================

if st.button("🔍 Analyze Complaint", type="primary"):

    if not complaint.strip():

        st.warning("Please enter a complaint first.")

    else:

        with st.spinner("UrbanSense is analyzing the complaint..."):

            result = analyze_complaint(complaint)

        if result:

            st.success("Complaint analyzed successfully!")

            st.divider()

            # ------------------------------------------------
            # Main Information
            # ------------------------------------------------

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Category",
                    result.get("category", "N/A")
                )

            with col2:
                st.metric(
                    "Priority",
                    result.get("priority", "N/A")
                )

            with col3:
                st.metric(
                    "Department",
                    result.get("department", "N/A")
                )

            # ------------------------------------------------
            # Location
            # ------------------------------------------------

            st.subheader("📍 Location")

            ai_location = result.get("location", "")

            if (
                not ai_location
                or ai_location.lower() == "not specified"
            ):
                ai_location = (
                    location if location.strip()
                    else "Not specified"
                )

            st.write(ai_location)

            # ------------------------------------------------
            # Problem Summary
            # ------------------------------------------------

            st.subheader("📋 Problem Summary")

            st.write(
                result.get(
                    "problem_summary",
                    "No summary available."
                )
            )

            # ------------------------------------------------
            # Recommended Action
            # ------------------------------------------------

            st.subheader("🛠️ Recommended Action")

            st.info(
                result.get(
                    "recommended_action",
                    "No recommendation available."
                )
            )

        else:

            st.error(
                "UrbanSense could not process the complaint. "
                "Please try again."
            )


# ============================================================
# Footer
# ============================================================

st.divider()

st.caption(
    "UrbanSense | AI-powered municipal service intelligence"
)
