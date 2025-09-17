import os
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from utils import prepare_image

# Set paths
real_dir = '../data/real/'
fake_dir = '../data/fake/'

X, Y = [], []

for folder, label in [(real_dir, 1), (fake_dir, 0)]:
    for file in os.listdir(folder):
        if file.endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(folder, file)
            X.append(prepare_image(img_path))
            Y.append(label)

X = np.vstack(X)
Y = np.array(Y)

X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.2, random_state=42)

model = Sequential([
    Conv2D(32, (5,5), activation='relu', input_shape=(128, 128, 3)),
    Conv2D(32, (5,5), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.2),
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(2, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

es = EarlyStopping(monitor='val_accuracy', patience=3, restore_best_weights=True, mode='max')

model.fit(X_train, Y_train, validation_data=(X_val, Y_val), epochs=30, batch_size=32, callbacks=[es])

model.save('../model/model_casia_run1.h5') 
