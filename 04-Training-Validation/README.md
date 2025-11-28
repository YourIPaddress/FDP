# 📘 Model Training Notebook — Overview

This Jupyter Notebook (**Model_training.ipynb**) demonstrates how **data quality**, **noise**, and **evaluation techniques** impact the performance of a Regression Model.  
The notebook visually and statistically explains why **robust evaluation**, **Cross-Validation**, and **Learning Curves** are essential for diagnosing **overfitting** and understanding model behavior.

---

## 📌 Key Concepts Demonstrated

### 1. **Regression Modeling**
- Uses `DecisionTreeRegressor` to predict continuous numerical outcomes.
- Helps illustrate how tree depth and noise affect model behavior.

### 2. **Train-Test Split**
- Demonstrates how data is separated into training and testing sets for **unbiased evaluation**.
- ⚠️ *Note:* `stratify` is **not used** for continuous regression targets.

### 3. **K-Fold Cross-Validation**
- Applies K-Fold CV to compute a stable model performance estimate.
- Evaluation metric: **Root Mean Squared Error (RMSE)**.
- Shows how CV reduces the randomness of a single train-test split.

### 4. **Impact of Noise**
- Two datasets used:
  - **low_noise_data.csv**
  - **high_noise_data.csv**
- You will compare the **average RMSE** for each dataset.
- Demonstrates how **data noise sets a ceiling on achievable accuracy**, regardless of model complexity.

### 5. **Overfitting Diagnosis**
- Generates a **Learning Curve** that highlights:
  - **Low Training Error**
  - **High Validation Error**
- Classic sign of a **High-Variance / Overfit Model**.

---

## 🚀 How to Run the Notebook

### **Prerequisites — Install the following libraries:**

```bash
pip install pandas numpy scikit-learn matplotlib
