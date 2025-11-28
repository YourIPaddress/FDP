# Step 5 – Model Evaluation

This section explains all evaluation metrics used to assess the performance of the classification model.  


---

# 📌 Understanding TP, TN, FP, FN

These four values form the basis of all classification metrics.

---

### 🟩 **TP — True Positive**
**Definition:**  
Model predicted **Yes** and the actual value was **Yes**.

**Sales example:**  
Model says: “Target will be hit” → Target **was** hit.

**Business meaning:**  
✔ Good prediction  
✔ Helps trust the model’s positive forecasts  

---

### 🟦 **TN — True Negative**
**Definition:**  
Model predicted **No** and the actual value was **No**.

**Sales example:**  
Model says: “Target will NOT be hit” → Target **was not** hit.

**Business meaning:**  
✔ Prevents overproduction  
✔ Saves inventory & marketing costs  

---

### 🟥 **FP — False Positive**
**Definition:**  
Model predicted **Yes** but the actual value was **No**.

**Sales example:**  
Model says: “We will hit the target” → Target **was not** hit.

**Business risk:**  
⚠️ Overconfidence  
⚠️ Overstocking  
⚠️ Wasted budget  
(Also called **Type I Error**)  

---

### 🟨 **FN — False Negative**
**Definition:**  
Model predicted **No** but the actual value was **Yes**.

**Sales example:**  
Model says: “We will NOT hit the target” → Target **was hit**.

**Business risk:**  
⚠️ Missed opportunity  
⚠️ Underproduction  
⚠️ Lost sales  
(Also called **Type II Error**)  

---

# 📌 Summary Table

| Term | Meaning | Sales Example | Business Impact |
|------|---------|---------------|------------------|
| **TP** | Predicted Yes, Actual Yes | Hit predicted & hit occurred | ✔ Good |
| **TN** | Predicted No, Actual No | Not hit predicted & not hit | ✔ Good |
| **FP** | Predicted Yes, Actual No | Predicted hit but missed | ⚠️ Overstock, wasted budget |
| **FN** | Predicted No, Actual Yes | Predicted no but actually hit | ⚠️ Missed revenue |

---

# 📌 1. Accuracy

### **What is Accuracy?**
Accuracy shows the percentage of all predictions the model gets correct.

### **Mathematical Formula**

$$
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
$$

### **Why it matters**
- Gives a quick sense of overall model performance.
- Useful as a basic benchmark.

---

# 📌 2. Precision

### **What is Precision?**
Out of all the cases the model predicted **Yes**, how many were actually **Yes**?

### **Mathematical Formula**

$$
Precision = \frac{TP}{TP + FP}
$$

### **Why it matters**
- Avoids false optimism.
- Prevents unnecessary spending based on wrong “Yes” predictions.

---

# 📌 3. Recall

### **What is Recall?**
Out of all the actual **Yes** cases, how many did the model correctly identify?

### **Mathematical Formula**

$$
Recall = \frac{TP}{TP + FN}
$$

### **Why it matters**
- Ensures the model does not miss important positive outcomes.
- In sales: prevents missing high-performing months.

---

# 📌 4. F1-Score

### **What is F1-Score?**
A balanced measure combining precision and recall.

### **Mathematical Formula**

$$
F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
$$

### **Why it matters**
- Best metric when data is imbalanced.
- Gives a single number to judge model quality.

---

# 📌 5. Confusion Matrix

### **What is it?**
A 2x2 table showing how predictions align with actual outcomes.

### **Structure**

$$
\begin{array}{c|cc}
 & \text{Predicted No} & \text{Predicted Yes} \\\hline
\text{Actual No} & TN & FP \\
\text{Actual Yes} & FN & TP
\end{array}
$$

### **Why it matters**
- Shows exactly *what kinds of mistakes* the model makes.
- Helps businesses understand cost of FP vs FN.

---

# 📌 6. K-Fold Cross-Validation

### **What is Cross-Validation?**
A method to test the model on different splits of the data.

### **Why we use it**
- Ensures model is stable and not overfitting.
- Shows generalization ability.

### **Formula (Mean CV Accuracy)**

$$
CV_{mean} = \frac{1}{k}\sum_{i=1}^{k} Accuracy_i
$$

### **Why it matters**
- Builds confidence the model works on unseen data.
- Essential for production readiness.

---

# 🎉 Final Takeaway

These evaluation metrics collectively show whether the model is accurate, reliable, business-safe, and suitable for **real-world sales forecasting**.

