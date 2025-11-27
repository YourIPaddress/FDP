import nbformat as nbf
import re

# 1. This is your raw code string (I applied the 'sparse_output' fix for you)
raw_code = r"""
# ------------------------
# Classification Workbook (Logistic Regression)
# Dataset: customer_churn.csv
# Students fill the blanks marked with _____
# ------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# 1. Load
df = pd.read_csv("customer_churn.csv")
print("Initial rows:", len(df))

# 2. Quick cleaning
# Convert numeric columns
df["Total_Charges"] = pd.to_numeric(df["Total_Charges"], errors="coerce")
df["Total_Charges"] = df["Total_Charges"].fillna(df["Total_Charges"].median())
# Convert target to 0/1
df["ChurnFlag"] = df["Churn"].map({"Yes":1, "No":0})

# 3. Prepare features - pick columns
# TODO: Fill FEATURES list with appropriate columns from df (exclude Churn and ChurnFlag)
FEATURES = _____   # <- STUDENT FILL
X = df[FEATURES]
y = df["ChurnFlag"]

# 4. Encode categorical features (example: Gender, Contract_Type)
# We will one-hot encode all object dtype columns in X
cat_cols = X.select_dtypes(include=["object"]).columns.tolist()
if cat_cols:
    # FIXED: Updated sparse to sparse_output for compatibility
    enc = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
    enc_arr = enc.fit_transform(X[cat_cols])
    enc_cols = enc.get_feature_names_out(cat_cols)
    X = pd.concat([X.drop(columns=cat_cols), pd.DataFrame(enc_arr, columns=enc_cols, index=X.index)], axis=1)

# 5. Split - fill test_size
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= _____ , random_state=42)

# 6. Scaling numeric columns
num_cols = X_train.select_dtypes(include=[np.number]).columns.tolist()
scaler = StandardScaler()
X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
X_test[num_cols] = scaler.transform(X_test[num_cols])

# 7. Train logistic regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 8. Predict & evaluate
pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)
print("Accuracy:", acc)
print(classification_report(y_test, pred))

# 9. Confusion matrix plot
cm = confusion_matrix(y_test, pred)
plt.figure(figsize=(4,3))
plt.imshow(cm, interpolation='nearest')
plt.title("Confusion Matrix")
plt.colorbar()
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.xticks([0,1], ["No","Yes"])
plt.yticks([0,1], ["No","Yes"])
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i, j], ha="center", va="center", color="white" if cm[i,j]>cm.max()/2 else "black")
plt.tight_layout()
plt.show()

print("Classification module complete.")
"""

# 2. Initialize the notebook object
nb = nbf.v4.new_notebook()
cells = []

# 3. Logic to split the string by Numbered Headers
lines = raw_code.split('\n')
current_chunk = []

# Create the first header for the Imports section
cells.append(nbf.v4.new_markdown_cell("## Setup and Imports"))

for line in lines:
    # Check if line matches "# [Number]." pattern
    if re.match(r'^# \d+\.', line.strip()):
        # Save previous chunk as a code cell (if it's not empty)
        if current_chunk:
            code_content = '\n'.join(current_chunk).strip()
            if code_content:
                cells.append(nbf.v4.new_code_cell(code_content))
            current_chunk = []
        
        # Create a new Markdown cell for this header
        # We replace the '#' comment symbol with '##' to make it a Markdown heading
        header_text = line.replace('#', '##', 1)
        cells.append(nbf.v4.new_markdown_cell(header_text))
    else:
        current_chunk.append(line)

# Add the final chunk of code
if current_chunk:
    code_content = '\n'.join(current_chunk).strip()
    if code_content:
        cells.append(nbf.v4.new_code_cell(code_content))

# 4. Save the file
nb['cells'] = cells
output_filename = 'classification_workbook.ipynb'
nbf.write(nb, output_filename)

print(f"Success! '{output_filename}' has been created.")