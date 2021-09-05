from flask import Flask, request, render_template
import requests
import pandas as pd
import numpy as np 
import pickle
import re

app = Flask(__name__)
pickle_in = open('model-pakwheels-carprice.pkl', 'rb')
model = pickle.load(pickle_in)
q_transform = pickle.load(open('q_transform.pkl','rb'))


@app.route('/', methods =['GET'])
def Home():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def refresh():
    return render_template('index.html')

@app.route('/predict', methods =['GET', 'POST'])
def predict():
    if request.method == 'POST':
        #Model_Year
        model_year = int(request.form['model_year'])
        #Fuel_Type
        fuel_type = int(request.form['fuel_type'])
        #Transmission
        transmission = int(request.form['transmission'])
        #Engine_Capaciy
        engine_capacity = request.form['engine_capacity']
        engine_capacity = int(re.search(r'(\d+)',engine_capacity).group(0))

        #Kms_Driven
        kms_driven = float(request.form['kms_driven'])
        #Color
        color = int(request.form['color'])
        #Assembly
        assembly = int(request.form['assembly'])
        #Body_Type
        body_type = int(request.form['body_type'])
        #Condition
        condition = int(request.form['condition'])



        #form a dataframe with the inpus and run the preprocessor as used in the training 
        row_df = pd.DataFrame([pd.Series([fuel_type,transmission,engine_capacity,kms_driven,color,assembly,body_type,condition])])
        row_df = pd.DataFrame(q_transform.transform(row_df))


        #predict the car selling price
        prediction = model.predict(row_df)
        output=round(prediction[0] / 100000,2)
        return render_template('result.html',prediction_text="Price of your car is {} lacs".format(output))
    
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)














