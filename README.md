# Analyzing Waze User Churn

## Overview 

The User Churn Analysis project aimed to tackle the issue of declining user retention within the Waze navigation app. With the overarching goal of reducing monthly user churn, the project utilized a combination of data analytics and machine learning techniques to delve into user behavior patterns and identify key drivers of churn.

The primary objective of the project was to develop effective strategies for mitigating user churn on the Waze app. By understanding the underlying factors contributing to churn and leveraging data-driven insights, the project aimed to enhance user retention rates and foster long-term engagement with the app.
The project was divided into 4 components :
1. Exploratory data analysis ,which included data cleaning , data transfomation , formatting and Data visualization.
2. Hypothesis testing (T-test)
3. Logistic Regression Modelling
4. ML modelling using ensemble learning (Random Forest Classifier and XGBoost classifier)

 The User Churn Analysis project unveiled valuable insights into user churn within the Waze app. Leveraging advanced data analytics, data visualization and ensemble machine learning, the project identified key drivers of churn and developed effective mitigation strategies. these insights can be used to enhance user retention and drive the app's overall growth. 

## Business Understanding :
User churn analysis helps businesses identify reasons for customer attrition, allowing them to optimize retention strategies. It aids in understanding user behavior patterns, enhancing product/service offerings, improving customer satisfaction, and ultimately boosting profitability through increased customer loyalty and reduced churn rates.

## Data Understanding :
* The more times users used the app, the less likely they were to churn. While 40% of the users who didn't use the app at all last month churned, nobody who used the app 30 days churned.
* The churn rate is highest for people who didn't use Waze much during the last month.
* The proportion of churned users to retained users is consistent between device types.
* Number of driving days had a negative correlation with churn. Users who drove more days of the last month were less likely to churn.
* Nearly all the variables were either very right-skewed or uniformly distributed. 
For the right-skewed distributions, this means that most users had values in the lower end of the range for that variable. 
For the uniform distributions, this means that users were generally equally likely to have values anywhere within the range for that variable.

## Infographics :
![image](https://github.com/v3434/User-Churn-Analysis/assets/70278692/cf97a8f7-fb5e-4426-9858-9845da5f7fc4)
Image 1 : Confusion matrix of the champion model's(XGBhoost Classifier) predictions on the test data.
![image](https://github.com/v3434/User-Churn-Analysis/assets/70278692/b1d8f929-7343-4da2-b69c-15c502fd732b)
Image 2 : As recall increases, precision decreases. a false positive could just mean that a user who will not actually churn gets an email and a banner notification on their phone. It's very low risk.
![image](https://github.com/v3434/User-Churn-Analysis/assets/70278692/c264acff-4e30-4fc9-a9ca-fd635e24e7a0)
Image 3 : Feature Importance
![image](https://github.com/v3434/User-Churn-Analysis/assets/70278692/fc6fae64-becf-49f9-b217-2c35bff3d99f)
Table 1 : Result Table with final Metrics





## Conclusion :
For detailed explanation about the insigts discovered and results obtained from predictive analysis , hypothesis testing , statistical analysis , Data visualization and Exploratory data analytics refer the executive summery report made for each component of the project .

