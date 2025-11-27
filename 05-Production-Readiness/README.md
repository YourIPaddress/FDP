📘 05 – Production Readiness: Model Evaluation

This module teaches how to evaluate machine learning models in a business context using the Hit_Target column from sales_data.csv.

MBA participants will learn how to measure how well a model performs — not just how to build one.

🎯 What You Will Learn

✔ What Accuracy means in business
✔ Why Precision and Recall matter
✔ What False Positives & False Negatives mean
✔ Why F1 Score is important
✔ How to read a Confusion Matrix
✔ How companies decide campaign effectiveness using ML

📂 Dataset Used: sales_data.csv

We use the same dataset from previous modules to keep the workshop consistent.

Key Columns:

Column	Meaning
Revenue	Total earnings
Units_Sold	Number of units sold
Marketing_Spend	Ad budget
Region	North/South/East/West
Product_Category	Category of product
Month	Month of sale
Hit_Target	Did the product hit its monthly target? (Yes/No)

This dataset supports:

Regression (predict Monthly_Sales)

Classification (predict Hit_Target)

📘 Hands-On Notebook: validation_metrics.ipynb

Participants will:

1️⃣ Load sales_data.csv
2️⃣ Convert Hit_Target → 1/0
3️⃣ Preprocess data (scaling + one-hot encoding)
4️⃣ Train a Logistic Regression model
5️⃣ Evaluate using:

Accuracy

Precision

Recall

F1 Score

6️⃣ Visualize a Confusion Matrix

Everything is beginner-friendly and explained in simple language.

🧠 Business Interpretation

Participants will learn how to answer:

How good is the model at predicting target achievement?

How many TRUE target achievers are identified correctly?

How many FALSE alarms did the model raise?

What does Precision mean for sales decisions?

Should the sales team trust the ML prediction?

This connects ML performance → business action.

🎉 Outcome

After completing this module, participants will understand:

✔ Model accuracy
✔ Confusion matrix insights
✔ KPI-driven classification
✔ Business reliability of ML predictions

This completes the end-to-end ML pipeline for the FDP.
