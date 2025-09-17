 
import numpy as np
from ela_converter import convert_to_ela_image

image_size = (128, 128)

def prepare_image(image_path):
    ela_image = convert_to_ela_image(image_path)
    image = ela_image.resize(image_size)
    return np.array(image).astype(np.float32).reshape(-1, 128, 128, 3) / 255.0