import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application
## import ridge regressor model and standard Scaler pickle
ridge_model = pickle.load(open('models/Ridge.pkl','rb'))
standard_scaler_model = pickle.load(open('models/Scaler_model.pkl','rb'))

## Route for Home Page 
@app.route('/',methods = ['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature=float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled = standard_scaler_model.transform([[Temperature,RH,Rain,FFMC,Classes,Region]])
        result = ridge_model.predict(new_data_scaled)

        return render_template('home.html',result = result[0])

    
    else:
        return render_template('home.html')










if __name__=="__main__":
    app.run(host="0.0.0.0")
