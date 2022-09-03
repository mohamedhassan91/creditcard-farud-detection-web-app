import numpy as np 
from flask import Flask ,jsonify,render_template,request
import pickle 
from threading import Thread

app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def Home():
    return render_template("index.html")    

@app.route("/predict", methods = ["post"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]    
    prediction = model.predict(features)
    if int(prediction)== 1:
        prediction ='Given transaction is fraud'
    else:
        prediction ='Given transaction is NOT fraud'           
    return render_template("index.html",prediction_text = prediction )


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
