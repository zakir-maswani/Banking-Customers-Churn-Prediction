# 🏦 Banking Customer Churn Prediction

A machine learning web application that predicts whether a bank customer is likely to churn (exit) based on their profile and account information. Built with a **Decision Tree Classifier** (tuned via GridSearchCV) and deployed as an interactive web app using **Streamlit**.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Demo](#demo)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Features](#features)
- [Methodology](#methodology)
- [Model Performance](#model-performance)
- [Installation](#installation)
- [Usage](#usage)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 Overview

Customer churn is one of the most critical challenges for banks and financial institutions. Losing a customer is significantly more expensive than retaining one. This project builds a binary classification model to identify at-risk customers **before** they leave, enabling proactive retention strategies.

Key highlights:
- Handles **class imbalance** using `class_weight="balanced"` in the classifier
- Uses **GridSearchCV with Stratified K-Fold cross-validation** (optimized for recall) to minimize false negatives — i.e., missing customers who are about to churn
- Deploys the trained model as an interactive **Streamlit** web app for real-time, single-customer predictions

---

## 🎬 Demo

Launch the app locally and use the **sidebar** to input a customer's details. The app instantly predicts whether the customer is:

- 🔴 **At Risk** — likely to churn
- 🟢 **Customer Retained** — likely to stay

---

## 📁 Project Structure

```
Banking-Customers-Churn-Prediction/
│
├── app.py                                      # Streamlit web application
├── Churn_dataset.csv                           # Raw dataset
├── Model.pkl                                   # Serialized trained model
└── data_preprocessing_and_model_training.ipynb # EDA, preprocessing & model training notebook
```

---

## 📊 Dataset

The dataset (`Churn_dataset.csv`) contains **10,000 bank customer records** with the following attributes:

| Column | Description |
|---|---|
| `RowNumber` | Row index (dropped during preprocessing) |
| `CustomerId` | Unique customer identifier (dropped) |
| `Surname` | Customer surname (dropped) |
| `CreditScore` | Customer's credit score (350–850) |
| `Geography` | Country of residence: France, Spain, or Germany |
| `Gender` | Male or Female |
| `Age` | Customer age (18–92) |
| `Tenure` | Number of years as a bank customer (0–10) |
| `Balance` | Account balance |
| `NumOfProducts` | Number of bank products held (1–4) |
| `HasCrCard` | Whether the customer has a credit card (0 or 1) |
| `IsActiveMember` | Whether the customer is an active member (0 or 1) |
| `EstimatedSalary` | Estimated annual salary |
| `Exited` | **Target** — 1 if churned, 0 if retained |

> **Class Imbalance:** ~20% of customers churned vs ~80% retained. This imbalance is addressed during model training.

---

## 🔍 Features Used for Prediction

After dropping irrelevant columns (`RowNumber`, `CustomerId`, `Surname`), the following 10 features are used:

- `CreditScore`
- `Geography` *(encoded: France=1, Spain=2, Germany=3)*
- `Gender` *(encoded: Male=1, Female=0)*
- `Age`
- `Tenure`
- `Balance`
- `NumOfProducts`
- `HasCrCard`
- `IsActiveMember`
- `EstimatedSalary`

---

## ⚙️ Methodology

The full pipeline is documented in `data_preprocessing_and_model_training.ipynb`:

**1. Exploratory Data Analysis (EDA)**
- Class distribution analysis (pie chart & count plot)
- Churn breakdown by Gender and Geography
- Age vs. Credit Score line plot
- Distribution plots for Age and Balance

**2. Data Preprocessing**
- Checked for null values (none found)
- Dropped non-predictive columns: `RowNumber`, `CustomerId`, `Surname`
- Label encoded categorical features: `Geography` and `Gender`

**3. Model Training**
- **Base model:** `DecisionTreeClassifier` with `class_weight="balanced"` and `random_state=42`
- **Hyperparameter tuning:** `GridSearchCV` over:
  - `max_depth`: [3, 5, 7, 9, 10, 11, 13]
  - `min_samples_split`: [5, 7, 8, 10, 13, 15, 17]
- **Cross-validation:** `StratifiedKFold` with 17 splits, shuffled, optimized for **recall**
- **Train/Test split:** 80/20 with stratification

**4. Evaluation**
- Classification report (precision, recall, F1-score)
- Train vs. test accuracy comparison to assess overfitting

---

## 📈 Model Performance

The model is optimized for **recall** to minimize missed churn cases (false negatives). Detailed metrics are available in the notebook's classification report output.

---

## 🚀 Installation

**Prerequisites:** Python 3.8 or higher

**1. Clone the repository**
```bash
git clone https://github.com/zakir-maswani/Banking-Customers-Churn-Prediction.git
cd Banking-Customers-Churn-Prediction
```

**2. Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 💻 Usage

**Run the Streamlit app**
```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`.

Use the **sidebar** to input the following customer details:
- Credit Score, Geography, Gender, Age, Tenure
- Balance, Number of Products, Credit Card status
- Active Member status, Estimated Salary

The app will instantly display the input data and output the churn prediction.

---

**Re-train the model (optional)**

Open and run the notebook end-to-end:
```bash
jupyter notebook data_preprocessing_and_model_training.ipynb
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib & Seaborn | Data visualization |
| Scikit-learn | Model training, tuning & evaluation |
| Streamlit | Web application framework |
| Pickle | Model serialization |
| Jupyter Notebook | EDA & training environment |

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please ensure your code follows existing style conventions and is well-commented.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
