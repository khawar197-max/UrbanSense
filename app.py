```python
import streamlit as st
import pandas as pd
import json
from datetime import datetime
from groq import Groq

# ============================================================
# UrbanSense
# AI-Powered Municipal Complaint Intelligence Platform
# ============================================================

st.set_page_config(
    page_title="UrbanSense",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# Custom Styling
# ============================================================

st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .subtitle {
        font-size: 18px;
        color: #666;
        margin-bottom: 25px;
    }

    .priority-critical {
        color: #b71c1c;
        font-weight: bold;
    }

    .priority-high {
        color: #e65100;
        font-weight: bold;
    }

    .priority-medium {
        color: #f57f17;
        font-weight: bold;
    }

    .priority-low {
        color: #2e7d32;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# Header
# ============================================================

st.markdown(
    '<div class="main-title">🏙️ UrbanSense</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-Powered Municipal Complaint Intelligence Platform'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Transform citizen complaints into structured municipal intelligence "
    "for faster prioritization, departmental coordination, and "
    "data-driven public service delivery."
)

st.divider()

# ============================================================
# Sidebar
# ============================================================

st.sidebar.title("🏙️ UrbanSense")

st.sidebar.write(
    "Municipal AI Decision Support"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "📝 Submit Complaint",
        "📊 Dashboard",
        "📋 Complaint History",
        "🤖 AI Municipal Report"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "UrbanSense is a prototype developed for "
    "AI innovation and municipal service delivery."
)

# ============================================================
# Groq API
# ============================================================

try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )
except Exception:
    st.error(
        "Groq API key is not configured. "
        "Please add GROQ_API_KEY to Streamlit Secrets."
    )
    st.stop()

# ============================================================
# Categories
# ============================================================

CATEGORIES = [
    "Sanitation",
    "Sewerage/Drainage",
    "Roads",
    "Streetlights",
    "Water Supply",
    "Encroachment",
    "Parks",
    "Property/Tax",
    "Other"
]

PRIORITIES = [
    "Critical",
    "High",
    "Medium",
    "Low"
]

DEPARTMENTS = [
    "Sanitation Department",
    "Engineering Department",
    "Sewerage/Drainage Department",
    "Streetlight Department",
    "Water Supply Department",
    "Encroachment Department",
    "Parks Department",
    "Property/Tax Department",
    "General Municipal Services"
]

# ============================================================
# AI Complaint Analyzer
# ============================================================

def analyze_complaint(complaint, user_location):

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": """
You are UrbanSense, an AI municipal service intelligence assistant.

Analyze citizen complaints and return ONLY valid JSON.

Allowed categories:
Sanitation, Sewerage/Drainage, Roads, Streetlights,
Water Supply, Encroachment, Parks, Property/Tax, Other.

Allowed priorities:
Critical, High, Medium, Low.

Identify the most appropriate municipal department.

Do not invent a location.

If the citizen provides a location separately, use that location.

Keep the problem summary concise.

Keep the recommended action practical and suitable
for municipal staff.

Return exactly these fields:
category
priority
department
location
problem_summary
recommended_action
"""
            },
            {
                "role": "user",
                "content": f"""
Citizen complaint:

{complaint}

User-provided location:

{user_location}

Return exactly:

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
# Session State - Complaint Database
# ============================================================

if "complaints" not in st.session_state:

    demo_data = [
        {
            "complaint_id": "US-1001",
            "date": "2026-09-10",
            "complaint": "Garbage has accumulated near the school for three days.",
            "category": "Sanitation",
            "priority": "High",
            "department": "Sanitation Department",
            "location": "Military Road",
            "problem_summary": "Garbage accumulation near a school.",
            "recommended_action": "Arrange immediate waste collection and inspect the area.",
            "status": "Pending"
        },
        {
            "complaint_id": "US-1002",
            "date": "2026-09-10",
            "complaint": "Sewage water is overflowing onto the road near the market.",
            "category": "Sewerage/Drainage",
            "priority": "Critical",
            "department": "Sewerage/Drainage Department",
            "location": "Market Area",
            "problem_summary": "Sewage overflow affecting road users.",
            "recommended_action": "Inspect the drainage line and remove the blockage immediately.",
            "status": "In Progress"
        },
        {
            "complaint_id": "US-1003",
            "date": "2026-09-09",
            "complaint": "Several streetlights are not working at night.",
            "category": "Streetlights",
            "priority": "Medium",
            "department": "Streetlight Department",
            "location": "Airport Road",
            "problem_summary": "Multiple streetlights are non-functional.",
            "recommended_action": "Inspect and repair or replace defective streetlight units.",
            "status": "Pending"
        },
        {
            "complaint_id": "US-1004",
            "date": "2026-09-09",
            "complaint": "A large pothole is causing problems for vehicles.",
            "category": "Roads",
            "priority": "High",
            "department": "Engineering Department",
            "location": "Sindhi Society",
            "problem_summary": "Large road pothole creating a traffic hazard.",
            "recommended_action": "Inspect the road and carry out urgent pothole repair.",
            "status": "Resolved"
        },
        {
            "complaint_id": "US-1005",
```
