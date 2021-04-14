import numpy as np
import tensorflow as tf
from cv2 import cv2
import base64
import io
import os
import pickle
from flask import Flask, request, redirect, render_template, json

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


model_path = os.path.join(os.path.join(
    os.getcwd(), 'model'), '30.2k_images_model.h5')
label_dictionary_path = os.path.join(os.path.join(
    os.getcwd(), 'model'), 'label_dictionary.pickle')

model = tf.keras.models.load_model(model_path)

with open(label_dictionary_path, 'rb') as fp:
    label_dictionary = pickle.load(fp)

@app.route('/', methods=['POST', 'GET'])
def base():
    if request.method == 'GET':
        return "<h1>Crop AI</h1>"
    if request.method == 'POST':
        if 'InputImg' not in request.files:
            print("No file part")
            return redirect(request.url)
        file = request.files['InputImg']
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filestr = request.files['InputImg'].read()
            img = cv2.imdecode(np.fromstring(
                filestr, np.uint8), cv2.IMREAD_COLOR)

            img = cv2.resize(img, (96, 96), interpolation=cv2.INTER_AREA)

            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            # find the green color
            mask_green = cv2.inRange(hsv, (36, 0, 0), (86, 255, 255))
            # find the brown color
            mask_brown = cv2.inRange(hsv, (8, 60, 20), (145, 255, 255))
            # find the yellow color in the leaf
            mask_yellow = cv2.inRange(hsv, (5, 42, 143), (145, 255, 255))
            # find the black color in the leaf
            mask_black = cv2.inRange(hsv, (100, 100, 100), (127, 127, 127))

            # find any of the four colors(green or brown or yellow or black) in the image
            mask = cv2.bitwise_or(mask_green, mask_brown)
            mask = cv2.bitwise_or(mask, mask_yellow)
            mask = cv2.bitwise_or(mask, mask_black)

            # Bitwise-AND mask and original image
            res = cv2.bitwise_and(img, img, mask=mask)

            # Gaussian blur with 3x3 kernel
            blur_img = cv2.GaussianBlur(res, (3, 3), 0)

            # Histogram equalization
            B, G, R = cv2.split(blur_img)
            output_R = cv2.equalizeHist(R)
            output_G = cv2.equalizeHist(G)
            output_B = cv2.equalizeHist(B)
            img = cv2.merge((output_R, output_G, output_B))

            img = img / 255

            img_array = np.expand_dims(img, axis=0)

            output = label_dictionary[model.predict(img_array)[0].argmax()]

        return output


if __name__ == '__main__':
    app.secret_key = 'qwertyuiop1234567890'
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)
