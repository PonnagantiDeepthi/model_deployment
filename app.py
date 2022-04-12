from flask import Flask, render_template, request, redirect, url_for, session
import cv2
from tensorflow.keras.preprocessing.image import img_to_array
import os
import numpy as np
from tensorflow.keras.models import model_from_json
import livelines_net
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check')
def liveness():
    return livelines_net
if __name__ == "__main__":
    app.run(debug=True)