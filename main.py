from flask import Flask, request,render_template
import pickle
import numpy as np
app=Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html' ,prediction_text='')

@app.route('/predict',methods=['POST'])
def predict():
    features = [float (x) for x in request.form.values()]
    ffeatures = [np.array(features)]
    prediction = model.predict(ffeatures)
    output = round(prediction[0])
    return render_template('index.html',prediction_text='The expected price is : {}$'.format(output))


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)

