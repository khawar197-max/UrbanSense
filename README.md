# 🏙️ UrbanSense

### AI-Powered Municipal Complaint Intelligence Platform

UrbanSense is an AI-powered municipal services platform designed to help local governments analyze citizen complaints, prioritize municipal issues, identify responsible departments, and generate actionable insights for better public service delivery.

Instead of manually reviewing large numbers of complaints, UrbanSense uses Artificial Intelligence to transform unstructured citizen complaints into structured municipal intelligence.

---

## 🚀 Problem

Municipal organizations receive complaints about issues such as:

* Garbage and sanitation
* Sewerage and drainage
* Damaged roads
* Streetlights
* Water supply
* Encroachments
* Parks and public spaces
* Property and municipal taxes

When complaints are handled manually, it can be difficult to:

* Identify urgent problems quickly
* Assign complaints to the correct department
* Detect recurring problems
* Identify areas with concentrated complaints
* Convert complaint data into useful management information

UrbanSense addresses these challenges using AI-powered complaint analysis.

---

## 💡 Solution

UrbanSense allows a citizen or municipal staff member to enter a complaint in natural language.

The AI analyzes the complaint and automatically identifies:

| AI Output              | Description                         |
| ---------------------- | ----------------------------------- |
| 📂 Category            | Type of municipal problem           |
| 🚨 Priority            | Critical, High, Medium, or Low      |
| 🏢 Department          | Responsible municipal department    |
| 📍 Location            | Location mentioned in the complaint |
| 📋 Summary             | Concise description of the problem  |
| 🛠️ Recommended Action | Suggested municipal response        |

This converts unstructured complaints into structured information that can support municipal decision-making.

---

## ✨ Key Features

### 1. AI Complaint Analysis

Users can submit complaints using ordinary natural language.

Example:

> "There is a large amount of garbage near a school and it has not been removed for three days."

UrbanSense analyzes the complaint and identifies the likely category, priority, department, location, summary, and recommended action.

### 2. Automatic Categorization

UrbanSense currently supports:

* Sanitation
* Sewerage/Drainage
* Roads
* Streetlights
* Water Supply
* Encroachment
* Parks
* Property/Tax
* Other

### 3. Priority Assessment

The AI assigns one of four priority levels:

* 🔴 Critical
* 🟠 High
* 🟡 Medium
* 🟢 Low

This helps municipal teams focus on urgent issues first.

### 4. Department Identification

UrbanSense identifies the municipal department that should normally handle the complaint.

### 5. Location Identification

The system extracts the location mentioned in the complaint. Users can also provide the location separately.

### 6. Recommended Action

The AI provides a practical recommended action that can help municipal staff decide the next step.

---

## 🧠 Technology Stack

* **Python**
* **Streamlit** — Interactive web application
* **Groq API** — AI inference
* **OpenAI GPT-OSS-20B** — AI model
* **JSON** — Structured AI output
* **GitHub** — Source code and version control
* **Streamlit Community Cloud** — Application deployment

---

## 🏗️ System Architecture

```text
Citizen Complaint
       │
       ▼
UrbanSense Web Interface
       │
       ▼
Groq API
       │
       ▼
GPT-OSS-20B
       │
       ▼
AI Complaint Analysis
       │
       ├── Category
       ├── Priority
       ├── Department
       ├── Location
       ├── Problem Summary
       └── Recommended Action
       │
       ▼
Municipal Decision Support
```

---

## 📊 Example Workflow

### Input

```text
There is standing sewage water on the road near the market
and residents are complaining about the smell.
```

### UrbanSense Analysis

```text
Category: Sewerage/Drainage
Priority: High
Department: Municipal Engineering / Sewerage
Location: Near the market
```

### Recommended Action

```text
Inspect the affected drainage line, remove the blockage,
pump out standing wastewater, and restore normal drainage.
```

---

## 🎯 Target Users

UrbanSense can support:

* Municipal Officers
* Local Government Departments
* Municipal Administrators
* Complaint Management Teams
* Sanitation Departments
* Engineering Departments
* Local Councils
* Public Service Delivery Organizations

---

## 🌍 Potential Impact

UrbanSense can help municipalities move from **manual complaint handling** toward **AI-assisted service delivery**.

Potential benefits include:

* Faster complaint classification
* Better prioritization of urgent issues
* Improved departmental assignment
* Reduced manual workload
* Better understanding of recurring municipal problems
* Data-driven municipal management
* Improved public service delivery

---

## 🔮 Future Development

Future versions of UrbanSense can include:

### 📊 Municipal Dashboard

Interactive dashboards showing:

* Complaints by area
* Complaints by category
* Priority distribution
* Department workload
* Complaint status
* Complaint trends

### 🗺️ AI Hotspot Detection

Identify areas where multiple complaints are concentrated and highlight potential municipal hotspots.

### 📸 Image-Based Complaint Analysis

Citizens could upload photographs of:

* Garbage
* Damaged roads
* Open drains
* Broken streetlights
* Encroachments

AI could analyze the image together with the complaint text.

### 🎤 Voice Complaints

Citizens could submit complaints using voice instead of typing.

### 🤖 AI Municipal Reports

UrbanSense could generate automated reports for municipal management, including:

* Daily complaint summaries
* Weekly performance reports
* Priority issue reports
* Area-based problem analysis
* Department workload reports

---

## 🔐 Security

The Groq API key is **not stored in the GitHub repository**.

UrbanSense uses **Streamlit Secrets** to securely store the API key during deployment.

API credentials should never be committed to the source code or publicly shared.

---

## 💻 Local Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/UrbanSense.git
```

Move into the project directory:

```bash
cd UrbanSense
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create Streamlit secrets:

```text
.streamlit/secrets.toml
```

Add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Run the application:

```bash
streamlit run app.py
```

---

## ☁️ Deployment

UrbanSense is designed to be deployed using **Streamlit Community Cloud**.

The application can be connected directly to the GitHub repository and deployed from `app.py`.

---

## 📁 Project Structure

```text
UrbanSense/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🏆 Hackathon Project

**Project:** UrbanSense
**Category:** Artificial Intelligence / Smart Cities / GovTech
**Focus:** Municipal Complaint Intelligence and Public Service Delivery

UrbanSense demonstrates how Generative AI can be applied to real-world municipal challenges and transformed into a practical decision-support tool.

---

## 👥 Team

**UrbanSense Team**

Developed as an AI-powered solution for smarter and more responsive municipal service delivery.

---

## 📜 Disclaimer

UrbanSense is a prototype developed for demonstration and hackathon purposes. AI-generated classifications and recommendations should be reviewed by authorized municipal personnel before operational decisions are made.
