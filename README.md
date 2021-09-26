# Used Car Price Prediction <img src="https://user-images.githubusercontent.com/66221394/132251352-52b7f74d-cdc8-4ee7-87e9-18e12a5e31d2.png" width="90" height="50">
## Topics
- [Demo](#Demo)
- [Overview](#Overview)
- [Motivation](#Motivation)
- [Technical Aspect](#Technical-Aspect)
- [Installation](#Installation)
- [Create Flask App](#Create-Flask-App)
- [Deployement on Heroku](#Deployement-on-Heroku)
- [Directory Tree](#Directory-Tree)
- [Bug / Feature Request](#Bug-/-Feature-Request)
- [Technologies Used](#Technologies-Used)
- [Team](#Team)
- [License](#License)
- [Credits](#Credits)

## Demo
Link: https://used-carprice-predictor.herokuapp.com/

[<img src="https://user-images.githubusercontent.com/66221394/132251682-a0adcd3d-9081-48c3-bc8a-9d598b006891.png">](https://predictheartattacks.herokuapp.com/)
[<img src="https://user-images.githubusercontent.com/66221394/132251714-3a1ec02c-62db-48fc-9796-0d91ccb594e6.png">](https://predictheartattacks.herokuapp.com/)


## Overview
This is a price prediction Flask application where a user can input number of features for car and based on those features this application will predict 
the estimated price for your used car. The data is basically obatained after scraping 
[PakWheels <img src = "https://user-images.githubusercontent.com/66221394/132255143-6542d75d-4637-4011-a2d0-c61c717e00fd.jpg" height = "20" width="90">](https://www.pakwheels.com/) 
Website using Sylenium with Python. 
The data contains most of the relevant information that PakWheels provides on car sales including columns like price, make, model, fuel type, 
engine’s capacity, and other categories.
After basic EDA, data preprocessing steps are performed which involves data cleaning along with handling missing values and duplicates, 
handling categorical features, feature engineering to extract features from raw data and feature scaling to limit the range of variables.
Model selection is done after  comparing different regression models like Linear Regression, Decision Tree, 
Gradient Boost and Random Forest Regressors after hyperparameter tuning with RandomizedSearchCV.


## Motivation
The motivation was to build a project from scratch, build a model and transform it into user end application. So got [this](https://www.pakwheels.com/) site to 
srape data and start my project.

## Technical Aspect
This project is divided into two part:
1. Training a machine learning model using Sklearn.

2. Building and hosting a Flask web app on Heroku.
- A user can enter input fields related to car.
- The Input fields are basically the model features.
- After entering the features and pressing 'Get Price' button, the price of the car is shown.

## Installation
The Code is written in Python 3.6. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). 
If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. 
To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/)
the repository:
`pip install -r requirements.txt`

## Create-Flask-App
- First install Flask on your local system. If you haven't already activated your programming environment, first activate it using
`$ source env/bin/activate`

- To install Flask, run the following command:
`$ pip install flask`
After installing create your base application. You can also refer to this amazing guide on [How To Make a Web Application Using Flask in Python 3](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)

## Deployement on Heroku
Before deployement, make sure you've pushed your code to github repository. Create your account on [Heroku](https://dashboard.heroku.com/apps).
Follow [this](https://dev.to/lordofdexterity/deploying-flask-app-on-heroku-using-github-50nh) step by step guide on how to deploy your Flask app on Heroku.

## Directory Tree
Tree structure of our repository is shown below.\
<br/>
├── build\
│   └── static\
├── data\
│   ├── car-scraped-data\
│   │   ├── Finals\
│   │   └── move-pkwheels-stuff\
│   └── cleaned-data\
├── __pycache__\
├── static\
├── templates\
└── Web-Scrape-Notebooks



## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), 
kindly open an issue [here](https://github.com/daniyal214/End-to-End-ML-Projects/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/daniyal214/End-to-End-ML-Projects/issues/new). 
Please include sample queries and their corresponding results.

## Technologies Used
![python](https://camo.githubusercontent.com/3cdf9577401a2c7dceac655bbd37fb2f3ee273a457bf1f2169c602fb80ca56f8/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667)
<img src="https://user-images.githubusercontent.com/66221394/130487933-f4616292-15a6-4d0d-8463-c81fcfe44f64.png" width="180" height="100">
<img src="https://user-images.githubusercontent.com/66221394/130488015-d156d9ba-2b74-4c72-956c-ef5da655c98b.png" width="280" height="100">
<img src="https://user-images.githubusercontent.com/66221394/130488547-ef7a0c7c-ecd9-4c07-8485-d3ab5cce7f3d.png" width="200" height="100">
<img src="https://user-images.githubusercontent.com/66221394/130488284-8f8f1f3d-7015-44dd-865a-566095697572.png" width="250" height="100">

## Team
<img src="https://user-images.githubusercontent.com/66221394/130490754-e043534a-9e0e-44c1-aaf5-fc4453a2b1f9.JPG" width="150" height="210">


## License
Copyright [2021] [Muhammad Daniyal]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

## Credits
Main credits goes to [PakWheels](https://www.pakwheels.com/) Website from where I scraped all the data. The way this website is structured helped me alot
to scrape data more easily otherwise this process would have taken much more time than it did. So kudos to [PakWheels <img src = "https://user-images.githubusercontent.com/66221394/132255143-6542d75d-4637-4011-a2d0-c61c717e00fd.jpg" height = "20" width="90">](https://www.pakwheels.com/)
