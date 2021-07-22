
# Overview

I taught myself how to deploy a machine learning model on a web app. 

Started a test server on my local machine by:
- python manage.py runserver
- Go to:  http://127.0.0.1:8000/

# [Software Demo Video](https://youtu.be/JZyoC7ZiUwU)

# Product

**Machine Learning Model**
- Logistic Regression outpreformed the decision tree
- Changing the threshold to .04 increased recall from 99.3% to 100% (saving .7% more lives)
- The tradeoff with lowering the threshold is that precision decreased from 75% to 5% (5% more poeple were unnecessarily admitted)

**Web Pages**
- Home page has a form to fill out
- The results page is a prediction of the parameters that were input

# Development Environment

**Google Colab**
-   Pandas
-   Scikit-learn
-   seaborn
-   numpy


**VScode**
-   Django framework
-   Some HTML
-   Vertual Environment

**Vertual Environment Setup**
  * (first navigate to the folder you want to work in)
  * py -m venv env
  * .\env\Scripts\activate
  * python -m pip install Django
  * py -m django --version


# Useful Websites
- [Data from Kaagle](https://www.kaggle.com/rashikrahmanpritom/heart-attack-analysis-prediction-dataset)

- [Statistical meaning of likelyhood](https://stats.stackexchange.com/questions/2641/what-is-the-difference-between-likelihood-and-probability)

- [Statistical meaning of likelyhood](https://discuss.analyticsvidhya.com/t/what-is-the-difference-between-predict-and-predict-proba/67376)

- [Returning multiple Variables](https://stackoverflow.com/questions/44345538/how-can-i-pass-multiple-variables-to-my-template-in-django)

# Future Work
* Hyperparameter tuning
* Hoast on Heroku
* Clean up the front end and make it look better
