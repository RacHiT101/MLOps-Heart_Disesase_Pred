MLops Pipeline for Bias Detection and Mitigation in Heart Disease Diagnosis Models
Team name: Git Commit 
MLOPS PROBLEM STATEMENT: 
Our goal is to enhance fairness, reliability, and equitable predictions across diverse demographic groups. We’ll emphasize the integration of ensemble techniques to improve model accuracy.

Approach: 
Data Preprocessing and Exploration:
•	Normalize Data: Pre-processed the dataset by handling missing values, outliers, and class imbalances.
•	Stratified Sampling: Ensured diverse representation by stratifying data based on demographic groups.
Bias Detection:
Gender analysis is an important aspect of bias detection and mitigation in machine learning. Helped us understand how our Heart Disease diagnosis models perform across different gender groups and identify any potential disparities or discrimination.
Accuracy of Naive Bayes model for men: 82.35294117647058 
Accuracy of Naive Bayes model for women: 91.30434782608695
These accuracy scores indicate that our Naive Bayes model performs better on women than on men. This could be a sign of gender bias in your model, data, or evaluation metrics. To mitigate this bias, we used:
•	Applied debiasing technique - Reweighting
•	To mitigate bias in our models, we applied AIF3600, a comprehensive open-source library for bias detection and mitigation.
•	AIF3600 was our choice of tool for bias mitigation, as it provides a wide range of metrics, explanations, and algorithms for datasets and models.
 

Ensemble Techniques for Model Optimization:
We have combined four different models, used Voting classifiers, using hard voting strategy, each of which have its own strengths and weaknesses, and aggregated their predictions to obtain a final prediction. Our Ensemble model achieved an accuracy of 0.987, which indicates that your ensemble technique was effective. 
Voting classifiers are a type of ensemble technique that combine the predictions of multiple base models and select the majority vote as the final prediction. They can improve the accuracy and robustness of your machine learning models by leveraging the diversity and strengths of different models.
   

Model Used	Accuracy
Logistic Regression	86.34146341463415
Decision Tree	85.36585365853658
Random Forest	100.0 (Overfitting)
Naïve Bayes	Accuracy of Naive Bayes model for men: 82.35294117647058

Accuracy of Naive Bayes model for women: 91.30434782608695
Extreme Gradient Boost	95.1219512195122
K-Neighbours Classifier	87.8048780487805

Pipeline: 
 

User Interface: 
We have used Streamlit for making the user interface, as it is easy and scalable Python UI Framework. 
 
 

Deployment: 
 

Github Repo: https://github.com/RacHiT101/MLOps-Heart_Disesase_Pred/tree/main

