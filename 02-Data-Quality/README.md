
# 📘 **DATA PREPROCESSING WORKBOOK**

This workbook introduces the most important steps in **Data Preprocessing**, using a simple and guided Python template.  
It is designed for learners from **non-coding backgrounds**, such as MBA students and faculty.

You will only need to **fill in the blanks (_____)** in two places.  
Everything else is already done for you.

---

# 🔍 **1. What is Data Preprocessing?**

Data Preprocessing is the process of **cleaning, transforming, and preparing raw data** before building machine learning models.  
It makes the dataset:

- **Accurate** → remove errors  
- **Complete** → fill missing values  
- **Consistent** → remove duplicates  
- **Machine-Readable** → encode text labels  
- **Comparable** → scale numerical values  

This step takes **70–80%** of the work in any analytics or ML project.

---

# 📂 **2. What Data Are We Using?**

We are using the file:

```

sales_data.csv

````

This file contains business-style data such as:

- Month  
- Region  
- Product Category  
- Revenue  
- Units Sold  
- Marketing Spend  
- Monthly Sales (Target variable)

---

# 🧹 **3. Steps Covered in the Workbook**

---

## ✅ **Step 1: Load the Data**

```python
df = pd.read_csv("sales_data.csv")
````

This reads the dataset into a DataFrame so we can clean it.

---

## ✅ **Step 2: Handling Missing Values**

Real business data often has blanks.

We fill missing values in the **Revenue** column using the **mean**.

```python
df["Revenue"] = df["Revenue"].fillna( _____ )
```

👉 **You must enter:**
`df["Revenue"].mean()`

This replaces missing entries with the average revenue.

---

## ✅ **Step 3: Removing Duplicates**

Duplicate rows are removed to improve quality.

```python
df = df.drop_duplicates()
```

---

## ✅ **Step 4: Encoding Categorical Data**

Machine learning models **cannot read text**, so we convert the `"Region"` column into **numbers** using One-Hot Encoding.

Example:

```
North → 1 0 0 0  
South → 0 1 0 0
```

The code:

```python
encoder = OneHotEncoder()
encoded = encoder.fit_transform(df[["Region"]]).toarray()

df[encoder.get_feature_names_out()] = encoded
df = df.drop(columns=["Region"])
```

This adds new columns:

```
Region_East  
Region_North  
Region_South  
Region_West
```

---

## ✅ **Step 5: Normalizing Numerical Features**

We scale `Revenue` so that all values become comparable.

```python
df["Revenue_scaled"] = scaler.fit_transform(df[["Revenue"]])
```

Scaling is needed because ML models perform better when large values (like revenue) do not overpower small values (like units sold).

---

## ✅ **Step 6: Splitting Data**

We divide the data into:

* **Training Set** — used to teach the model
* **Test Set** — used to check accuracy

You fill the blank:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size= _____
)
```

👉 **Recommended Entry:**
`0.2` (20% Test Data)

---

# 🎯 **4. Your Tasks (Only 2 Blanks!)**

| Task                                  | Location | Expected Answer        |
| ------------------------------------- | -------- | ---------------------- |
| Fill missing Revenue values           | Step 2   | `df["Revenue"].mean()` |
| Choose test size for train-test split | Step 6   | `0.2`                  |

---

# 📊 **5. What Happens After Preprocessing?**

Your data becomes clean and ready for:

* Linear Regression
* Classification
* Forecasting
* Marketing analytics
* Sales prediction
* Customer segmentation

This workbook prepares you for **Model Building**, the next module.

---

# 🎉 **6. Output**

Once everything is completed, you will see:

```
Preprocessing Complete!
```

Your dataset is now clean and machine-ready.

---

If you want, I can now generate:

✔ A **Model Building Workbook (Regression)**
✔ A **Classification Workbook (Yes/No prediction)**
✔ A **Clustering Workbook (Customer Segmentation)**
✔ A **README.md for each module**

Just tell me what you want next!

```

