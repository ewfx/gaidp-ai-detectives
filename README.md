# Regulatory Data Profiling Automation

[![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock-FF9900?logo=amazonaws)](https://aws.amazon.com/bedrock/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python)](https://www.python.org/)
[![Serverless](https://img.shields.io/badge/Architecture-Serverless-FD5750)](https://aws.amazon.com/serverless/)
![License](https://img.shields.io/badge/license-MIT-green)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)

Automated compliance solution that transforms regulatory documents into executable data quality rules for banking institutions.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Key Pain Points in Traditional Regulatory Data Profiling](#key-points-in-traditional-regulatory-data-profiling)
4. [System Architecture](#system-architecture)
5. [Technology Stack](#technology-stack)
6. [Prerequisites](#prerequisites)
7. [Installation Guide](#installation-guide)
8. [Usage Instructions](#usage-instructions)
9. [Directory Structure](#directory-structure)
10. [Contributing](#contributing)
11. [Contact](#contact)

---

## Project Overview
A serverless solution that automates:
- Extraction of regulatory requirements from documents (PDF/Word)
- Generation of data validation rules using AWS Bedrock's Titan models
- Application of rules to transaction datasets
- Generation of remediation suggestions for compliance violations

---

## Key Features
- **AI-Powered Rule Generation**: Convert regulatory text to executable validation rules
- **Multi-Format Support**: Process PDF, DOCX, and CSV files
- **Serverless Architecture**: AWS Lambda-based processing pipeline
- **Compliance Dashboard**: Streamlit web interface for results visualization
- **Audit Trail**: Full documentation of rule generation process

---

## System Architecture

Regulatory Documents → AWS S3 → Text Extraction → LLM Processing → Rule Generation
↓
Transaction Data → Validation Engine → Anomaly Detection → Remediation Suggestions
↓
Streamlit Dashboard ← Results Storage

![Arch](./artifacts/arch/GenAIDP_Hackathon25.gif)

---

## Technology Stack
| Component          | Technology                 |
|--------------------|----------------------------|
| Document Processing| AWS Textract, PyPDF2       |
| AI/ML              | AWS Bedrock (Titan)        |
| Compute            | AWS Lambda                 |
| Storage            | Amazon S3, DynamoDB        |
| UI Framework       | Streamlit                  |
| Validation Engine  | Pandas, PySpark            |

---

## Prerequisites
1. AWS account with Bedrock access
2. Python 3.9+ environment
3. AWS CLI configured with admin privileges
4. Minimum 2GB RAM for local testing

---

## Installation Guide
1. Clone repository:

git clone https://github.com/phanikolla/gaidp-ai-detectives.git

cd gaidp-ai-detectives

2. Create virtual environment:

python -m venv venv

source venv/bin/activate # Windows: venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Configure AWS credentials:

aws configure --profile default

---

## Usage Instructions
### Step 1: Document Upload

from src.ingestion import upload_regulatory_doc

upload_regulatory_doc('path/to/regulation.pdf', bucket='your-s3-bucket')

### Step 2: Rule Generation

python src/rule_generation/generate_rules.py --document regulation.pdf

### Step 3: Data Validation
from src.application import validate_transactions
results = validate_transactions('transactions.csv', rules_version='v1.0')

### Step 4: View Results

streamlit run src/front_end.py

---

## Contributing
1. Fork the repository
2. Create feature branch:

git checkout -b feature/new-validation-method

3. Add tests for new features
4. Submit pull request using the template
5. Ensure all tests pass:

---

## Contact
**Developer/Solutions Architect**: [Phani Kumar]  
**Email**: pkkolla24@gmail.com  
**Issue Tracker**: [GitHub Issues](https://github.com/phanikolla/gaidp-ai-detectives/issues)  

---



# 🚀 Gen AI Data Profiling

## 📌 Table of Contents
- [Introduction](#introduction)
- [Understanding the Challenge](#understanding-the-challenge)
- [Key Pain Points in Traditional Regulatory Data Profiling](#key-points-in-traditional-regulatory-data-profiling)
- [Innovative Solution Concepts](#innovative-solution-concepts)
- [Technical Architecture](#technical-architecture)
- [High-Level Architecture](#high-level-architecture)
- [AWS Services and Components](#aws-services-and-components)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## High-Level Architecture

1) Data Ingestion Layer: Processes regulatory instruction documents and transaction data
2) Rule Generation Layer: Creates data profiling rules based on regulatory instructions
3) Rule Application Layer: Applies rules to transaction data and identifies violations
4) Remediation Layer: Generates detailed remediation actions for violations
5) Presentation Layer: Displays results through a user-friendly interface

## AWS Services and Components

1) **AWS Lambda** : Serverless computing for processing documents and generating rules
2) **API Gateway** : RESTful API interface for communication between components
3) **Amazon S3** : Storage for instruction documents and transaction data
4) **AWS Bedrock** : For accessing the Titan Foundation and Titan Text Embedding models
5) **Streamlit** : For building the user interface
6) **FAISS** : Vector database for efficient similarity search and embeddings storage

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)


## 🛠️ How We Built It
Briefly outline the technologies, frameworks, and tools used in development.

## 🚧 Challenges We Faced
Describe the major technical or non-technical challenges your team encountered.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/your-repo.git
   ```
2. Install dependencies  
   ```sh
   npm install  # or pip install -r requirements.txt (for Python)
   ```
3. Run the project  
   ```sh
   npm start  # or python app.py
   ```

## 🏗️ Tech Stack
- 🔹 Frontend: React / Vue / Angular
- 🔹 Backend: Node.js / FastAPI / Django
- 🔹 Database: PostgreSQL / Firebase
- 🔹 Other: OpenAI API / Twilio / Stripe

## 👥 Team
- **Phani Kumar Kolla** - [GitHub](#) | [LinkedIn](#)
- **Parikshit More** - [GitHub](#) | [LinkedIn](#)
- **Anirudh Yadav** - [GitHub](#) | [LinkedIn](#)
- **Aishwarya** - [GitHub](#) | [LinkedIn](#)
