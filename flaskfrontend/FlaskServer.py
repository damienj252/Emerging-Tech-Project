#Adapted from https://stackoverflow.com/questions/43469281/how-to-predict-input-image-using-trained-model-in-keras
# Adapted from: https://stackoverflow.com/questions/1386352/pil-thumbnail-and-end-up-with-a-square-image/8469920#8469920
# reference https://pillow.readthedocs.io/en/3.0.0/reference/Image.html
from flask import Flask as fk
from flask import render_template
from flask import request
import numpy as np
import base64
import tensorflow as tf

from PIL import ImageOps, Image


app = fk(__name__)

@app.route("/")
def calculator():
    return render_template('app/frontend/calculator.html')

@app.route('/uploadImage', methods=['GET', 'POST'])
def uploadImage():
    # Get the image request
    theImage = fk.request.values.get("theImage", " ")
    # Print to console
    print(theImage)

    decodedimage = base64.b64decode(theImage[22:])
    with open("theImage.png", "wb") as f:
        f.write(decodedimage)
    # Respond numbers
    return {"message": theImage}