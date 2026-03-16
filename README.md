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

### 3. Deploy to Google Cloud (CI/CD)
This project features an automated, zero-touch CI/CD pipeline using **GitHub Actions & Google Workload Identity Federation**.
1. Simply push your code to the `main` branch.
2. GitHub Actions will securely authenticate to GCP and trigger `cloudbuild.yaml`.
3. The Agent Engine will automatically deploy to Cloud Run!

### 4. Run the Live Demo
1.  Open the `mock_erp.html` file in your browser to simulate the legacy system.
2.  Connect to your Live WebSocket Endpoint: `wss://synapse-service-3dtobsp3xq-uc.a.run.app/live`
3.  Initiate a voice session ("Start onboarding Merchant XYZ"). The Coordinator Agent will guide you through the FSM phases and use the Navigator Agent to physically click and input data.

## 🧠 Architecture Overview
Please see `docs/DESIGN.md` for a full breakdown of the Brain, Eyes, Memory, and Voice components.

## 💸 $0 Cost Guarantee
This project was strictly designed to run entirely within the GCP and AI Studio free tiers. A `budget_alert.yaml` is provided to kill all Cloud Run invocations if the $0.00 budget is breached.
