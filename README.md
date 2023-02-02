# Heart Disease Classification
Practicing classification with heart disease data. I compare logistic regression, SVM, decision tree, random forest, and naive bayesian models then determine the most reasonable model to predict heart disease in patients.

# clean_data.py
This script converts the CSV into a dataframe. There are methods to manipulate the dataframe, including throwing entries with missing values, replacing missing values with the column's mode, reducing the Sick classification to one value, and scaling features.

# classification_comparison.ipynb
This notebook compares the performances of several classification models. Each model has tuned hyperparameters, if applicable. Uses KFold sampling with 5 splits. For now, the target was reduced to values 0 (Healthy) and 1 (Sick) rather than the expanded Sick classification.

The results show that logistic regression, SVM, random forest, and GaussianNB performed about the same at an R^2 value of 0.83. I will use Logistic Regression for the rest of this dataset's analysis.

# feature_comparison.ipynb
This notebook inspects the importance of each feature in the model. I wanted to see if I could simplify the dataset by reducing dimensionality and possibly yield a better result. I continued using the reduced Sick values where the target was only binomial. 

I first used a Extra Trees classifier to get feature importances and sorted them. Then, I performed logistic regressions while increasing how many features are included in the model so that each iteration includes the ith most important features. 

The best score was about 0.85 when only 4, 8, or 9 features are included. This is only slightly better than including all features, so I'll just deem all features as important. Unfortunately, dimensionality reduction was not achieved.

# Dataset Notes
This dataset was obtained form UC Irvine's machine learning repository.

Citation:
Janosi,Andras, Steinbrunn,William, Pfisterer,Matthias, Detrano,Robert & M.D.,M.D.. (1988). Heart Disease. UCI Machine Learning Repository.

| Attribute | Role    | Description                                                             | Units |
|-----------|---------|-------------------------------------------------------------------------|-------|
| age       | Feature |                                                                         | years |
| sex       | Feature | 1.0 = male; 0.0 = female                                                |       |
| cp        | Feature | chest pain type; 1.0 = angina; 2.0 = abnang; 3.0 = notang; 4.0 = asympt |       |
| trestbps  | Feature | resting blood pressure                                                  | mmHg  |
| chol      | Feature | cholesterol                                                             | mg/dL |
| fbs       | Feature | fasting blood sugar < 120 mg/dL; 1.0 = True; 0.0 = False                |       |
| restecg   | Feature | resting ecg; 0.0 = norm; 1.0 = abn; 2.0 = hyper                         |       |
| thalach   | Feature | maximum heart rate                                                      |       |
| exang     | Feature | exercised induced angina; 1.0 = True; 0.0 = False                       |       |
| oldpeak   | Feature | ST depresion induced by exercise                                        |       |
| slope     | Feature | 1.0 = up; 2.0 = flat; 3.0 = down                                        |       |
| ca        | Feature | Number of major vessels                                                 |       |
| thal      | Feature | 3.0 = norm; 6.0 = fixed; 7.0 = reversed                                 |       |
| num       | Target  | 0 = healthy; 1 = sick 1; 2 = sick 2; 3 = sick 3; 4 = sick 4             |       |