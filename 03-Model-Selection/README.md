
---

# 📘 **MODEL BUILDING WORKBOOKS**

These workbooks introduce **Model Building** using three important machine learning algorithms:

1. **Linear Regression** (Predicting numbers)
2. **Classification** (Predicting categories like Yes/No)
3. **Clustering** (Grouping similar items without labels — optional)

They are designed for **MBA students** and **non-coding beginners**, using simple code and **fill-in-the-blank exercises**.

Each workbook uses a different **real-world business dataset** and includes **visual plots** to build intuition.

---

# 🎯 **Purpose of These Workbooks**

These notebooks help students understand:

* How models are built after preprocessing
* What “training” and “testing” mean
* How to interpret model results
* How to read metrics like **MSE**, **Accuracy**, **R²**, **Confusion Matrix**
* How business decisions can be made from ML outputs
* How visual plots explain model behaviour

Each workbook has **fill-in-the-blanks (_____)** for active participation.

---

---

# 📘 **1. LINEAR REGRESSION WORKBOOK**

### 📂 **Dataset Used**

```
sales_data.csv
```

Contains business data such as:

* Revenue
* Units Sold
* Marketing Spend
* Region
* Monthly Sales (target variable)

---

## 🔍 **What is Linear Regression?**

Linear Regression predicts **continuous numerical values**, such as:

* Monthly sales
* Profit
* Inventory demand
* Advertising ROI

The idea:

> “Find the best straight-line relationship between input factors and output.”

Students learn:

* Choosing input features
* Scaling numeric values
* Training/testing the model
* Using **Mean Squared Error (MSE)**
* Using **R² Score**
* Understanding **prediction vs actual plots**
* Understanding **residuals plots**

---

## 🧠 **Your Tasks (2 Blanks)**

| Blank               | Meaning                               | What to Fill         |
| ------------------- | ------------------------------------- | -------------------- |
| `FEATURES = _____`  | Columns used to predict Monthly Sales | List of column names |
| `test_size = _____` | Train/test split proportion           | Recommended: `0.2`   |

Example FEATURES:

```python
FEATURES = ["Revenue", "Units_Sold", "Marketing_Spend", "Region_North", "Region_South"]
```

---

## 📊 **Visual Plots Included**

### **1. Actual vs Predicted Plot**

Shows how close predictions are to the real sales values.

### **2. Residual Plot**

Shows errors.
Helps identify if the model is consistent or biased.

These plots give **excellent intuition** for beginners.

---

---

# 📘 **2. CLASSIFICATION WORKBOOK (LOGISTIC REGRESSION)**

### 📂 **Dataset Used**

```
customer_churn.csv
```

Contains telecom-style data:

* Customer demographics
* Contract type
* Charges
* Tenure
* Whether the customer churned (Yes/No)

---

## 🔍 **What is Classification?**

Classification predicts **categories**, not numbers.

Examples:

* Will a customer churn? (Yes/No)
* Is a loan risky?
* Will a product return occur?
* Is a transaction fraudulent?

Students learn:

* Converting Yes/No into 1/0
* One-hot encoding categorical features
* Scaling numeric data
* Using **Accuracy**
* Understanding **Precision, Recall, F1-score**
* Reading a **Confusion Matrix**
* Understanding business impact of false positives/negatives

---

## 🧠 **Your Tasks (2 Blanks)**

| Blank               | Meaning                       | What to Fill                                  |
| ------------------- | ----------------------------- | --------------------------------------------- |
| `FEATURES = _____`  | Columns used to predict churn | List of column names except Churn & ChurnFlag |
| `test_size = _____` | Train/test proportion         | Recommended: `0.2`                            |

Example:

```python
FEATURES = ["Gender", "Tenure", "Monthly_Charges", "Total_Charges", "Contract"]
```

---

## 📊 **Visual Plot Included**

### **Confusion Matrix Heatmap**

Shows:

* **True Predictions** (correct)
* **False Predictions** (mistakes)

This helps MBA students understand:

* How many customers were wrongly predicted to churn
* How many churners the model correctly captured
* Why accuracy alone is not enough

---

# 🎉 **Outputs**

Once completed, each notebook prints:


🎊Linear Regression module complete.
🎊Classification module complete.

