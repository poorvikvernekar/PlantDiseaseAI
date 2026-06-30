import tensorflow as tf
import numpy as np

CLASS_NAMES = [

    'Apple - Apple Scab',
    'Apple - Black Rot',
    'Apple - Cedar Apple Rust',
    'Apple - Healthy',
    'Blueberry - Healthy',
    'Cherry - Powdery Mildew',
    'Cherry - Healthy',
    'Corn - Cercospora Leaf Spot',
    'Corn - Common Rust',
    'Corn - Northern Leaf Blight',
    'Corn - Healthy',
    'Grape - Black Rot',
    'Grape - Esca (Black Measles)',
    'Grape - Leaf Blight',
    'Grape - Healthy',
    'Orange - Huanglongbing (Citrus Greening)',
    'Peach - Bacterial Spot',
    'Peach - Healthy',
    'Bell Pepper - Bacterial Spot',
    'Bell Pepper - Healthy',
    'Potato - Early Blight',
    'Potato - Late Blight',
    'Potato - Healthy',
    'Raspberry - Healthy',
    'Soybean - Healthy',
    'Squash - Powdery Mildew',
    'Strawberry - Leaf Scorch',
    'Strawberry - Healthy',
    'Tomato - Bacterial Spot',
    'Tomato - Early Blight',
    'Tomato - Late Blight',
    'Tomato - Leaf Mold',
    'Tomato - Septoria Leaf Spot',
    'Tomato - Spider Mites',
    'Tomato - Target Spot',
    'Tomato - Yellow Leaf Curl Virus',
    'Tomato - Mosaic Virus',
    'Tomato - Healthy'
]

def predict_disease(image_path):

    model = tf.keras.models.load_model(
        'ai_model/trained_model.keras'
    )

    image = tf.keras.preprocessing.image.load_img(
        image_path,
        target_size=(128, 128)
    )

    image_array = tf.keras.preprocessing.image.img_to_array(
        image
    )

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    prediction = model.predict(
        image_array
    )

    result_index = np.argmax(
        prediction
    )

    return CLASS_NAMES[result_index]