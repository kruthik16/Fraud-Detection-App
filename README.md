# 💳 Fraud Detection Project (Using ML and Deployed with Streamlit)

This project implements a machine learning-based fraud detection system for financial transactions. It includes a Jupyter Notebook for exploratory data analysis (EDA) and model training, a Streamlit web application for interactive fraud predictions, and a dataset sourced from Kaggle.

📌 **Dataset**: [Kaggle - Fraud Detection Dataset](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset/data)  
🚀 **Deployed App**: [Streamlit App](https://fraud-detection-app-taqhypmjn8savxewsib3yw.streamlit.app/)

---

## 📚 Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)

---

## 📌 Project Overview

The Fraud Detection Project aims to identify fraudulent financial transactions using machine learning.  
The project includes:

- 🧪 **Jupyter Notebook**: `notebooks/Analysis_Model.ipynb` for EDA, preprocessing, and training.
- 🌐 **Streamlit App**: `src/app.py` for real-time fraud predictions with a simple UI.

### 🔍 Key Features
- Analyzes transaction patterns across multiple features.
- Utilizes Logistic Regression with class balancing for high fraud recall.
- Offers an interactive web app for end-users to input data and detect fraud.

---

## 📊 Dataset

The dataset (`data/AIML Dataset.csv`) contains **6.3 million** financial transactions with the following columns:

| Column             | Description                                  |
|--------------------|----------------------------------------------|
| `step`             | Time step of the transaction                 |
| `type`             | Type of transaction (e.g., PAYMENT, CASH_OUT)|
| `amount`           | Transaction amount                           |
| `oldbalanceOrg`    | Balance of origin account before transaction |
| `newbalanceOrig`   | Balance of origin account after transaction  |
| `oldbalanceDest`   | Balance of destination account before        |
| `newbalanceDest`   | Balance of destination account after         |
| `isFraud`          | Label (1 = Fraudulent, 0 = Normal)           |

📎 **Note**: If the dataset exceeds GitHub's 100MB limit, download it manually from Kaggle or [insert external link] and place it inside the `data/` folder.

---

## 🗂 Repository Structure

