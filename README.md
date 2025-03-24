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

## 🎯 Introduction
This comprehensive solution leverages Generative AI and unsupervised machine learning to automate data profiling for regulatory reporting in banking, transforming manual rule definition into an intelligent, adaptive system that ensures compliance while reducing operational overhead.

## Understanding the Challenge

Regulatory reporting in banking involves compiling vast amounts of data to meet compliance requirements. Data profiling—ensuring reported data aligns with regulatory instructions—traditionally requires manual rule definition based on underlying data and regulatory requirements. 

This hackathon challenge aims to automate this process using Generative AI (LLMs) and unsupervised machine learning to generate data profiling rules and suggest remediation actions based on regulatory reporting instructions.

The process is labor-intensive, error-prone, and difficult to scale across multiple regulations. Manual data profiling creates inconsistencies in rule application and limits the ability to quickly adapt to changing regulatory requirements. 

By automating this process, financial institutions can significantly reduce compliance risks, improve efficiency, and ensure consistent reporting across different regulatory frameworks.

## Key Pain Points in Traditional Regulatory Data Profiling

1) Time-consuming manual rule definition process
2) Inconsistent rule application across different teams
3) Difficulty keeping up with changing regulatory requirements
4) Limited scalability for large datasets and multiple regulations
5) High risk of human error in rule definition and application

## Innovative Solution Concepts

1) AI-Powered Regulatory Rule Extraction

The solution will use Large Language Models to automatically parse regulatory documents and extract precise data profiling rules. By leveraging natural language processing capabilities, the system can understand complex regulatory language and convert it into structured, actionable rules without human intervention.

2) Unsupervised Anomaly Detection for Data Quality

Incorporating unsupervised machine learning algorithms to detect patterns and anomalies in transaction data that might violate regulatory requirements. This approach can identify potential compliance issues that might not be explicitly covered by existing rules, adding an additional layer of protection.

3) Self-Learning Rule Optimization

The system will continuously learn from remediation actions and feedback to improve rule generation over time. This creates a virtuous cycle where the quality of generated rules improves with each iteration, making the solution more effective and reducing the need for manual intervention.

4) Explainable AI for Compliance Transparency

All generated rules and remediation actions will include clear explanations of their regulatory basis, ensuring transparency and auditability. This is critical for regulatory compliance in banking where decisions must be explainable to both internal and external auditors.

## Technical Architecture

The solution architecture leverages AWS services and the specific tools you've requested to create a scalable, secure system for regulatory data profiling automation.

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
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
What inspired you to create this project? Describe the problem you're solving.

## ⚙️ What It Does
Explain the key features and functionalities of your project.

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
- **Your Name** - [GitHub](#) | [LinkedIn](#)
- **Teammate 2** - [GitHub](#) | [LinkedIn](#)
