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
# Sidebar Navigation
# ============================================================

st.sidebar.title("🏙️ UrbanSense")

st.sidebar.write("Municipal AI Decision Support")

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
# Constants
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
# Initialize Complaint Data
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
            "date": "2026-09-08",
            "complaint": "Water supply has been interrupted since yesterday.",
            "category": "Water Supply",
            "priority": "High",
            "department": "Water Supply Department",
            "location": "Basheerabad",
            "problem_summary": "Residents are experiencing interruption in water supply.",
            "recommended_action": "Check the supply network and restore water service.",
            "status": "In Progress"
        },
        {
            "complaint_id": "US-1006",
            "date": "2026-09-08",
            "complaint": "A shop has extended its structure onto the public footpath.",
            "category": "Encroachment",
            "priority": "Medium",
            "department": "Encroachment Department",
            "location": "Main Market",
            "problem_summary": "Commercial encroachment is obstructing the public footpath.",
            "recommended_action": "Conduct a site inspection and take action according to municipal regulations.",
            "status": "Pending"
        },
        {
            "complaint_id": "US-1007",
            "date": "2026-09-07",
            "complaint": "The public park needs cleaning and maintenance.",
            "category": "Parks",
            "priority": "Low",
            "department": "Parks Department",
            "location": "Gulshan-e-Iqbal",
            "problem_summary": "Public park requires routine maintenance.",
            "recommended_action": "Schedule cleaning and routine park maintenance.",
            "status": "Resolved"
        },
        {
            "complaint_id": "US-1008",
            "date": "2026-09-07",
            "complaint": "Drain is blocked and rainwater is collecting on the street.",
            "category": "Sewerage/Drainage",
            "priority": "High",
            "department": "Sewerage/Drainage Department",
            "location": "Hamdard Colony",
            "problem_summary": "Blocked drain causing water accumulation.",
            "recommended_action": "Clear the blocked drain and inspect downstream drainage capacity.",
            "status": "In Progress"
        }
    ]

    st.session_state.complaints = demo_data


# ============================================================
# Helper Functions
# ============================================================

def get_dataframe():
    return pd.DataFrame(st.session_state.complaints)


def generate_complaint_id():

    number = 1001 + len(st.session_state.complaints)

    return f"US-{number}"


# ============================================================
# PAGE 1 - SUBMIT COMPLAINT
# ============================================================

if page == "📝 Submit Complaint":

    st.header("📝 Submit a Municipal Complaint")

    st.write(
        "Describe the municipal problem in natural language. "
        "UrbanSense will analyze it using AI."
    )

    complaint = st.text_area(
        "Citizen Complaint",
        placeholder=(
            "Example: There is a large amount of garbage "
            "near a school and it has not been removed for "
            "three days."
        ),
        height=160
    )

    location = st.text_input(
        "Location",
        placeholder="Example: Military Road"
    )

    if st.button(
        "🔍 Analyze Complaint",
        type="primary",
        use_container_width=True
    ):

        if not complaint.strip():

            st.warning(
                "Please enter a complaint first."
            )

        else:

            with st.spinner(
                "UrbanSense AI is analyzing the complaint..."
            ):

                result = analyze_complaint(
                    complaint,
                    location
                )

            if result:

                st.success(
                    "Complaint analyzed successfully!"
                )

                st.divider()

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "📂 Category",
                        result.get(
                            "category",
                            "N/A"
                        )
                    )

                with col2:
                    st.metric(
                        "🚨 Priority",
                        result.get(
                            "priority",
                            "N/A"
                        )
                    )

                with col3:
                    st.metric(
                        "🏢 Department",
                        result.get(
                            "department",
                            "N/A"
                        )
                    )

                st.divider()

                col1, col2 = st.columns(2)

                with col1:

                    st.subheader("📍 Location")

                    ai_location = result.get(
                        "location",
                        ""
                    )

                    if (
                        not ai_location
                        or ai_location.lower()
                        in ["not specified", "unknown"]
                    ):

                        ai_location = (
                            location
                            if location.strip()
                            else "Not specified"
                        )

                    st.write(ai_location)

                with col2:

                    st.subheader("📋 Problem Summary")

                    st.write(
                        result.get(
                            "problem_summary",
                            "No summary available."
                        )
                    )

                st.subheader("🛠️ Recommended Action")

                st.info(
                    result.get(
                        "recommended_action",
                        "No recommendation available."
                    )
                )

                # Save complaint
                complaint_id = generate_complaint_id()

                record = {
                    "complaint_id": complaint_id,
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "complaint": complaint,
                    "category": result.get(
                        "category",
                        "Other"
                    ),
                    "priority": result.get(
                        "priority",
                        "Medium"
                    ),
                    "department": result.get(
                        "department",
                        "General Municipal Services"
                    ),
                    "location": (
                        location
                        if location.strip()
                        else result.get(
                            "location",
                            "Not specified"
                        )
                    ),
                    "problem_summary": result.get(
                        "problem_summary",
                        ""
                    ),
                    "recommended_action": result.get(
                        "recommended_action",
                        ""
                    ),
                    "status": "Pending"
                }

                st.session_state.complaints.append(
                    record
                )

                st.success(
                    f"Complaint saved successfully. "
                    f"Complaint ID: {complaint_id}"
                )

            else:

                st.error(
                    "UrbanSense could not process the complaint. "
                    "Please try again."
                )


# ============================================================
# PAGE 2 - DASHBOARD
# ============================================================

elif page == "📊 Dashboard":

    st.header("📊 Municipal Intelligence Dashboard")

    df = get_dataframe()

    total = len(df)

    critical = len(
        df[df["priority"] == "Critical"]
    )

    high = len(
        df[df["priority"] == "High"]
    )

    pending = len(
        df[df["status"] == "Pending"]
    )

    resolved = len(
        df[df["status"] == "Resolved"]
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Total Complaints",
        total
    )

    col2.metric(
        "Critical",
        critical
    )

    col3.metric(
        "High",
        high
    )

    col4.metric(
        "Pending",
        pending
    )

    col5.metric(
        "Resolved",
        resolved
    )

    st.divider()

    # Category chart

    left, right = st.columns(2)

    with left:

        st.subheader("📂 Complaints by Category")

        category_counts = (
            df["category"]
            .value_counts()
        )

        st.bar_chart(
            category_counts
        )

    with right:

        st.subheader("🚨 Priority Distribution")

        priority_counts = (
            df["priority"]
            .value_counts()
        )

        st.bar_chart(
            priority_counts
        )

    st.divider()

    # Department and location charts

    left, right = st.columns(2)

    with left:

        st.subheader("🏢 Department Workload")

        department_counts = (
            df["department"]
            .value_counts()
        )

        st.bar_chart(
            department_counts
        )

    with right:

        st.subheader("📍 Complaint Hotspots")

        location_counts = (
            df["location"]
            .value_counts()
            .head(10)
        )

        st.bar_chart(
            location_counts
        )

    st.divider()

    # Priority alerts

    st.subheader("🚨 Priority Alerts")

    urgent = df[
        df["priority"].isin(
            ["Critical", "High"]
        )
    ]

    if len(urgent) > 0:

        display_columns = [
            "complaint_id",
            "category",
            "priority",
            "department",
            "location",
            "status"
        ]

        st.dataframe(
            urgent[display_columns],
            use_container_width=True,
            hide_index=True
        )

    else:

        st.success(
            "No critical or high-priority complaints."
        )


# ============================================================
# PAGE 3 - COMPLAINT HISTORY
# ============================================================

elif page == "📋 Complaint History":

    st.header("📋 Complaint History")

    df = get_dataframe()

    col1, col2, col3 = st.columns(3)

    with col1:

        selected_category = st.selectbox(
            "Category",
            ["All"] + sorted(
                df["category"]
                .dropna()
                .unique()
                .tolist()
            )
        )

    with col2:

        selected_priority = st.selectbox(
            "Priority",
            ["All"] + PRIORITIES
        )

    with col3:

        selected_status = st.selectbox(
            "Status",
            [
                "All",
                "Pending",
                "In Progress",
                "Resolved"
            ]
        )

    filtered = df.copy()

    if selected_category != "All":

        filtered = filtered[
            filtered["category"]
            == selected_category
        ]

    if selected_priority != "All":

        filtered = filtered[
            filtered["priority"]
            == selected_priority
        ]

    if selected_status != "All":

        filtered = filtered[
            filtered["status"]
            == selected_status
        ]

    st.write(
        f"Showing **{len(filtered)}** complaints"
    )

    display_columns = [
        "complaint_id",
        "date",
        "complaint",
        "category",
        "priority",
        "department",
        "location",
        "status"
    ]

    st.dataframe(
        filtered[display_columns],
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PAGE 4 - AI MUNICIPAL REPORT
# ============================================================

elif page == "🤖 AI Municipal Report":

    st.header("🤖 AI Municipal Situation Report")

    st.write(
        "Generate a concise management report from "
        "the current complaint database."
    )

    df = get_dataframe()

    if st.button(
        "📄 Generate AI Report",
        type="primary",
        use_container_width=True
    ):

        category_summary = (
            df["category"]
            .value_counts()
            .to_dict()
        )

        priority_summary = (
            df["priority"]
            .value_counts()
            .to_dict()
        )

        department_summary = (
            df["department"]
            .value_counts()
            .to_dict()
        )

        location_summary = (
            df["location"]
            .value_counts()
            .head(10)
            .to_dict()
        )

        status_summary = (
            df["status"]
            .value_counts()
            .to_dict()
        )

        prompt = f"""
You are a municipal management intelligence assistant.

Prepare a concise professional municipal situation report
based only on the following complaint statistics.

Total complaints:
{len(df)}

Category distribution:
{category_summary}

Priority distribution:
{priority_summary}

Department workload:
{department_summary}

Top complaint locations:
{location_summary}

Status distribution:
{status_summary}

The report must contain:

1. Executive Summary
2. Key Issues
3. Priority Concerns
4. Areas Requiring Attention
5. Recommended Management Actions

Do not invent statistics.
Keep the report practical and concise.
"""

        with st.spinner(
            "Generating municipal intelligence report..."
        ):

            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2
            )

            report = (
                response
                .choices[0]
                .message
                .content
            )

        st.success(
            "Municipal report generated successfully."
        )

        st.markdown(report)

        st.download_button(
            label="⬇️ Download Report",
            data=report,
            file_name="UrbanSense_Municipal_Report.txt",
            mime="text/plain"
        )


# ============================================================
# Footer
# ============================================================

st.divider()

st.caption(
    "UrbanSense | AI-powered municipal service intelligence | "
    "Hackathon Prototype"
)
