# Heart Disease Ensemble Classification
 Practicing bagging and boosting with heart disease data. I compare logistic regression, bagging, and boosting models then determine the most reasonable model to predict heart disease in patients.

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



# Logistic Regression
First, I performed a simple logistic regression knowing that the results wouldn't look great because of the high dimensionality of features. I reduced the target values to either be healthy (0) or sick (1-4 reduced to 1). I used the SciKit-learn logistic model with all 11 features, which failed to converge. Using 80% of the dataset for training, the prediction accuracy was about 82%

# Ensemble Bagging