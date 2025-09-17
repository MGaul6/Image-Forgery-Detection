 import argparse
import numpy as np
from keras.models import load_model
from utils import prepare_image

model = load_model('../model/model_casia_run1.h5')
class_names = ['fake', 'real']

parser = argparse.ArgumentParser()
parser.add_argument('--image', required=True, help='Path to the image file')
args = parser.parse_args()

image = prepare_image(args.image)
y_pred = model.predict(image)
y_class = np.argmax(y_pred, axis=1)[0]

print(f"Predicted Class: {class_names[y_class]} with Confidence: {np.amax(y_pred) * 100:.2f}%")
