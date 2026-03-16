# Project Synapse: Autonomous Merchant Onboarding Bridge

Welcome to Project Synapse, built for the **Gemini Live Agent Challenge**. This complete, $0-cost Agent Engine bridges the gap between modern LLM parsing and legacy, non-API systems using Gemini 2.0 Flash's Multimodal Vision and Bidi-Streaming.

![Architecture overview placeholder]

## What it Does
Synapse deconstructs a "Merchant Onboarding" workflow into an **Asynchronous Finite State Machine**:
1.  **Document Data Extraction**: Parses complex documents.
2.  **Risk Analysis**: Cross-references parsed data against compliance rules.
3.  **UI Form Entry**: An autonomous "Navigator" agent uses *vision* to "see" a legacy ERP interface (simulated here) and generate X/Y coordinate clicks to enter the data.

Crucially, throughout the process, the **Gemini Live Bidi-Streaming (WebSockets)** interface allows a human risk analyst to monitor progress and "barge in" proactively via voice.

---

## 🚀 Quick Start (Spin-up Instructions for Judges)

### 1. Clone & Authenticate
```bash
git clone https://github.com/YOUR_REPO/project-synapse.git
cd project-synapse
gcloud auth application-default login
```

### 2. Install Dependencies (Local Testing)
We recommend Python 3.11+.
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Deploy to Google Cloud (0.2 Bonus Points)
This project uses `cloudbuild.yaml` to ensure automated deployment.
```bash
# Set your project ID
export PROJECT_ID="your-gcp-project-id"

# Trigger the deployment
sh deploy.sh
```

### 4. Run the Live Demo
1.  Open the `mock_erp.html` file in your browser. This simulates the legacy system.
2.  Open the Cloud Run `/live` endpoint.
3.  Initiate a voice session ("Start onboarding Merchant XYZ"). The Coordinator Agent will guide you through the FSM phases and use the Navigator Agent to input fields.

## 🧠 Architecture Overview
Please see `docs/DESIGN.md` for a full breakdown of the Brain, Eyes, Memory, and Voice components.

## 💸 $0 Cost Guarantee
This project was strictly designed to run entirely within the GCP and AI Studio free tiers. A `budget_alert.yaml` is provided to kill all Cloud Run invocations if the $0.00 budget is breached.
