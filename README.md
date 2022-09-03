# creditcard-farud-detection-web-app
Sample app detecting fraud transactions of credit card 
![image](https://user-images.githubusercontent.com/60258264/188268476-b9db4579-eeee-4024-a6b6-0fb5171b478c.png)
Installation
link of the data https://www.kaggle.com/code/janiobachmann/credit-fraud-dealing-with-imbalanced-datasets/data

# Description 

The dataset contains transactions made by credit cards in September 2013 by European cardholders.
This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.

It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, … V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-sensitive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.

# Models used 

LogisticRegression
LinearSVC, SVC
KNeighborsClassifie
Randomforest classifier



# steps to run the project 

to use the app follow these steps

create a virtualenv and activate it

$python -m venv venv

$source venv/Scripts/activate.ps1

install all the requirements

$pip install -r requirements.txt


start the app from app.py
$python app.py
you will find a message ending with the url like so

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Just pass any elemnts from the data provided or any other data 
