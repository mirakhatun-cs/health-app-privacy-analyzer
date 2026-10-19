# Health App Privacy Analyzer

**A Python-based research prototype for analyzing privacy and security indicators in Android health applications.**

## Overview

Mobile health applications, including pregnancy trackers, menstrual health apps, and patient portals, may process highly sensitive personal information. Understanding the privacy implications of their permissions and third-party software components is an important part of mobile application security research.

The **Health App Privacy Analyzer** is a Python-based tool developed to help organize and interpret selected privacy-related indicators identified during Android application analysis.

The project focuses on classifying permissions, recognizing known third-party SDKs, and highlighting findings that may require further investigation.

This project is part of my ongoing undergraduate cybersecurity research at **Kent State University**, conducted under the mentorship of **Dr. Raiful Hasan in the SPIRIT Lab**.

## Research Objectives

- Investigate privacy-sensitive permissions in Android health applications.
- Identify and categorize known third-party SDK and tracker indicators.
- Examine potential privacy concerns associated with application functionality.
- Develop a structured approach for interpreting technical security findings.
- Support further research into transparency and privacy protection in mobile health applications.

## Implemented Features

### 1. Android Permission Analysis

- Reads permissions from a text file.
- Categorizes recognized Android permissions by functionality.
- Identifies permissions classified as privacy-sensitive using predefined rules.
- Flags unrecognized permissions for further review.
- Generates permission counts and a summary.

### 2. Third-Party SDK and Tracker Analysis

- Reads SDK or tracker names from a text file.
- Recognizes selected known SDKs, including AppsFlyer, Firebase Analytics, Google Crashlytics, AdMob, and Localytics.
- Categorizes recognized components by their primary functions, such as analytics, advertising, attribution, and crash reporting.
- Flags unrecognized entries for further investigation.
- Generates summary counts.

### 3. Combined Privacy Analysis

The main analyzer combines permission and tracker classifications into a single console report.

It displays:

- Total permissions analyzed
- Number of permissions classified as privacy-sensitive
- Total tracker entries analyzed
- Number of recognized tracker entries
- Individual classifications and items requiring further review

## Technologies Used

- **Python** — Rule-based classification and report generation
- **MobSF** — Used in the broader research workflow for Android security analysis
- **Android Static Analysis** — Examination of application components and potential privacy indicators
- **GitHub** — Version control and project documentation

## Project Structure

| File | Description |
|---|---|
| `privacy_analyzer.py` | Analyzes and categorizes Android permissions |
| `tracker_analyzer.py` | Categorizes third-party SDK and tracker entries |
| `health_app_analyzer.py` | Combines permission and tracker analysis |
| `sample_permissions.txt` | Sample permission input data |
| `sample_trackers.txt` | Sample SDK/tracker input data |
| `README.md` | Project documentation |

## How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/mirakhatun-cs/health-app-privacy-analyzer.git
cd health-app-privacy-analyzer
```

### Step 2: Run the Combined Analyzer

Make sure Python 3 is installed.

```bash
python health_app_analyzer.py
```

If your system uses `python3`, run:

```bash
python3 health_app_analyzer.py
```

### Step 3: Enter the Input Files

When prompted, enter:

**Permission file:**

```text
sample_permissions.txt
```

**Tracker file:**

```text
sample_trackers.txt
```

### Step 4: Review the Results

The analyzer prints categorized permission and tracker findings, followed by a summary.

The supplied sample files contain seven permission entries and six tracker entries, including one unrecognized SDK.

The scripts can also be run individually:

```bash
python privacy_analyzer.py
python tracker_analyzer.py
```

**Note:** The current prototype requires manually prepared text-file inputs. It does not directly scan APK files or automatically import MobSF JSON reports.

## How the Analyzer Works

The current workflow follows a rule-based approach:

1. Collect relevant permission and SDK information during Android application analysis.
2. Prepare text files containing the identified entries.
3. Run the Python analyzer.
4. Compare the entries against predefined classification dictionaries.
5. Display recognized categories, unknown entries, and summary counts.
6. Review the findings alongside the application's functionality and other research evidence.

## Research Limitations

This analyzer is designed to identify **potential privacy indicators, not prove malicious or unauthorized application behavior**.

Important limitations include:

- A requested permission does not prove that an application actively accesses the associated data.
- The presence of an analytics or advertising SDK does not establish that sensitive health information is transmitted.
- SDK classifications are based on predefined names and do not independently verify SDK presence in an APK.
- The tool does not currently perform dynamic analysis or network traffic monitoring.
- The current prototype does not establish whether an application complies with its privacy policy.

Additional manual investigation, runtime testing, and network analysis may be necessary to validate findings.

## Future Development

Planned improvements include:

- Automatic processing of MobSF JSON reports
- Expanded permission and SDK detection rules
- Organization of CWE and security findings
- Comparison of multiple Android health applications
- Structured and exportable privacy reports
- More accessible explanations of technical findings
- Improved validation through additional application testing

## Project Status

🚧 **Active Development — Ongoing Undergraduate Research**

The current version provides a working rule-based prototype for permission and tracker classification.

Development continues as part of a broader investigation into privacy and security risks in mobile health applications.

## Research Affiliation

**Kent State University**  
SPIRIT Lab  
Research Mentor: Dr. Raiful Hasan

## Author

**Mira Khatun**  
Undergraduate Cybersecurity Researcher  
Kent State University

[GitHub Profile](https://github.com/mirakhatun-cs)

