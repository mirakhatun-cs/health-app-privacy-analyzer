# 🛡️ Health App Privacy Explainer

**An evidence-aware Android health-app privacy analysis tool combining rule-based security analysis with Meta AI-powered explanations.**

**Meta Global AI Developer Hackathon 2026**

Track: Indie Developer

Theme: Build for Your World

**Developer:** Mira Khatun
**Institution:** Kent State University

## Overview

Android health applications can process highly sensitive personal information, including medical records, reproductive health information, and mental health data.

Security analysis tools such as MobSF identify technical indicators, but their results can be difficult for nontechnical users to understand.

**Health App Privacy Explainer** aims to make these findings more accessible by combining deterministic Python analysis with AI-generated explanations using Meta's Muse Spark model.

The application identifies selected Android permission and third-party SDK indicators, organizes them into understandable categories, and is designed to explain what the evidence does and does not establish.

## The Problem

A security report may identify permissions such as `CAMERA`, `RECORD_AUDIO`, or `ACCESS_FINE_LOCATION`, along with third-party analytics or advertising SDK indicators.

However, these findings alone do not prove that an application collects or shares sensitive information.

Users need a way to understand:

- What the identified permissions allow.
- Why certain SDK indicators deserve attention.
- Which findings are directly supported by static evidence.
- What behavior remains unverified.
- What additional investigation may be appropriate.

## Our Solution

The application follows this pipeline:

**MobSF-style JSON → Python Analyzer → Meta Muse Spark → Streamlit Dashboard**

The rule-based Python analyzer classifies technical findings.

Meta Muse Spark is integrated to generate understandable explanations with explicit uncertainty and recommended verification steps.

The dashboard presents the findings and supports downloading structured analysis results.

## Features

### 1. JSON Report Upload

- Upload a supported JSON report.
- Extract application metadata, permissions, and SDK indicators.
- Display permission and tracker counts.
- Handle invalid JSON.

**Current limitation:** JSON ingestion has been tested with synthetic MobSF-style data. Compatibility with actual MobSF exports still requires validation.

### 2. Permission Analysis

- Classifies selected Android permissions.
- Identifies predefined privacy-sensitive categories.
- Flags unrecognized permissions for further review.
- Generates permission counts.

### 3. Third-Party SDK Analysis

Recognizes selected SDK indicators, including:

- AppsFlyer
- Firebase Analytics
- Google Crashlytics
- AdMob
- Localytics

The system categorizes recognized entries and flags unknown components.

### 4. Meta AI Explanations

The project includes an integration with **Meta Muse Spark 1.3 through Meta Model API**.

The AI component is designed to provide:

- Plain-English explanations of security findings.
- Confirmed technical indicators.
- Unconfirmed privacy possibilities.
- Recommended verification steps.

The model is instructed not to invent findings or present static indicators as confirmed malicious behavior.

**Integration status:** The Python integration module imports successfully, and the Streamlit interface invokes it. Live inference has not yet been verified because the API returned a billing-verification error. Successful AI-generated output remains a pending test.

### 5. Interactive Streamlit Dashboard

The dashboard includes:

- JSON upload.
- Application details.
- Permission and SDK summary metrics.
- Permission classification table.
- Third-party SDK indicator table.
- Privacy interpretation section.
- Meta AI explanation button.
- Downloadable structured analysis in JSON format.

### 6. Evidence-Aware Interpretation

The project distinguishes three categories:

**Confirmed Technical Indicator:** A finding directly identified in the supplied report.

**Unconfirmed Possibility:** A potential implication that cannot be established from static findings alone.

**Recommended Verification:** A suggested additional investigation, such as manual code inspection or network traffic analysis.

These categories prevent unsupported claims about data collection or transmission.

## Technical Architecture

| Component | Technology |
|---|---|
| Programming language | Python |
| Static analysis source | MobSF |
| Classification engine | Rule-based Python |
| AI model | Meta Muse Spark 1.3 |
| AI interface | Meta Model API |
| Dashboard | Streamlit |
| Version control | GitHub |
| Development environment | GitHub Codespaces |

## Project Structure

| File | Description |
|---|---|
| `health_app_analyzer.py` | Original combined text-file analyzer |
| `privacy_analyzer.py` | Original permission analysis |
| `tracker_analyzer.py` | Original SDK analysis |
| `mobsf_parser.py` | JSON report parsing |
| `analysis_engine.py` | Structured permission and SDK classification |
| `meta_explainer.py` | Meta Muse Spark integration |
| `app.py` | Streamlit dashboard |
| `sample_mobsf.json` | Synthetic JSON test report |
| `sample_permissions.txt` | Original sample permissions |
| `sample_trackers.txt` | Original sample SDK entries |
| `test_meta.py` | Meta API connection test |
| `README.md` | Project documentation |

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mirakhatun-cs/health-app-privacy-analyzer.git
cd health-app-privacy-analyzer
```

### 2. Install Dependencies

Python 3 is required.

```bash
python -m pip install streamlit openai
```

### 3. Configure Meta Model API

Create an API key through the Meta developer platform:

https://dev.meta.ai/

Set the environment variable `MODEL_API_KEY` using a secure method, such as GitHub Codespaces secrets.

Never commit your API key to the repository.

Meta AI features require an active, authorized API account. API usage may incur charges depending on available credits and billing settings.

### 4. Run the Application

```bash
python -m streamlit run app.py
```

Open the URL displayed by Streamlit.

### 5. Upload a Report

Upload `sample_mobsf.json` to test the currently supported JSON format.

The sample report is synthetic and is intended for demonstration and software testing.

### 6. Generate an AI Explanation

Click **Generate Meta AI Explanation** after uploading a report.

This feature requires successful Meta Model API authorization and billing verification.

If the model is unavailable, the dashboard displays an error instead of inventing a response.

## Original Research Prototype

The original research implementation uses manually prepared text files.

To run it:

```bash
python health_app_analyzer.py
```

Enter:

```text
sample_permissions.txt
sample_trackers.txt
```

This original analyzer remains available alongside the newer dashboard application.

## Current Testing Status

| Test | Status |
|---|---|
| Original text-file analyzer | Passed |
| Synthetic JSON parser test | Passed |
| Structured analysis engine | Passed |
| Streamlit server startup | Passed |
| Dashboard JSON upload and classification | Passed |
| Meta integration module import | Passed |
| Meta API live inference | Blocked by billing verification |
| Actual MobSF JSON compatibility | Not yet validated |
| Full end-to-end AI demonstration | Pending |

The current synthetic dashboard test identifies four permission entries, three classified as privacy-sensitive, and three recognized SDK indicators.

## Responsible Security Analysis

This tool does not claim that any analyzed application is malicious or violates a privacy policy.

Key limitations:

- Permission declarations do not prove that permissions are exercised.
- SDK indicators do not prove that sensitive data is transmitted.
- SDK identification is based on the supplied report and predefined classification rules.
- Static analysis alone cannot verify runtime data flows.
- The tool does not automatically scan APK files.
- The current version does not perform network monitoring or privacy-policy compliance verification.
- AI explanations require further testing and should not replace independent security validation.

Additional manual investigation and dynamic analysis may be needed.

## Hackathon Development and Research Attribution

This project builds upon my earlier undergraduate cybersecurity research at Kent State University, conducted under the mentorship of Dr. Raiful Hasan in the SPIRIT Lab.

The original research prototype includes permission classification, third-party SDK recognition, and a combined Python console analyzer.

The Meta Global AI Developer Hackathon extension adds:

- Structured JSON parsing.
- A reusable analysis engine.
- A Streamlit dashboard.
- Meta Muse Spark API integration code.
- Evidence-aware AI explanation instructions.
- Structured JSON export.

The pre-existing research components and the hackathon additions are distinguished for transparency.

## Future Development

- Validate parsing with actual MobSF JSON exports.
- Expand supported MobSF findings and security indicators.
- Improve SDK and permission recognition.
- Test and evaluate AI explanation accuracy.
- Add support for CWE-related findings.
- Automate APK analysis through MobSF.
- Add dynamic network analysis.
- Develop a more advanced privacy investigation workflow.

## Author

**Mira Khatun**
Undergraduate Cybersecurity Researcher
Kent State University

Research Mentor: Dr. Raiful Hasan
SPIRIT Lab

[GitHub Profile](https://github.com/mirakhatun-cs)

## Project Status

**Hackathon MVP — Active Development**

The rule-based analysis and dashboard are functional with synthetic test data. Live Meta AI inference and actual MobSF report validation remain pending.