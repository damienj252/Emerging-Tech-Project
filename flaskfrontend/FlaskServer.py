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

if __name__ == "__main__":
    app.run() 
    

@app.route('/MNIST', methods=['GET', 'POST'])
def image():
    
    userImage = request.values['imageData']

    print(userImage)

    decodedImage = base64.b64decode(userImage[0:])
    with open ("test.png", "wb") as d:
        d.write(decodedImage)

    model = load_model()

    reshapedImage = reshape()
        
    prediction_array = model.predict(reshapedImage)
    prediction = np.argmax(prediction_array)
  
    print(prediction)
    return{"prediction": str(prediction)}

    def reshape():
        firstImage = Image.open('test.png').convert("L")
        firstImage = ImageOps.fit(firstImage, 28, Image.ANTIALIAS)

        img_sequence = np.array(firstImage).reshape(1, 28, 28, 1)
        return img_sequence