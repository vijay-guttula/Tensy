import tensorflow as tf
import numpy as np
import json
import requests

SIZE = 128 #this model requires the size as 128 by 128
MODEL_URI = 'http://localhost:8501/v1/models/pets:predict'
CLASSES = ['Cat','Dog']

""" This method takes the image and processes it into the required dimensions"""
def get_prediction(image_path):
    image = tf.keras.preprocessing.image.load_img(
        image_path, target_size = (SIZE,SIZE)
    )
    #coverts the image to numpy array
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis=0)
    

    data = json.dumps({
        'instances': image.tolist()
    })
    
    response = requests.post(MODEL_URI, data=data.encode()) #as this will return a response

    result = json.loads(response.text)
    #return resultpip 
    #print(result)
    prediction = np.squeeze(result['predictions'][0])
    if prediction > 0.8 :
        n = 1
        class_name = CLASSES[n]
    elif prediction < 0.1 :
        n = 0
        class_name = CLASSES[n]
    else :
        n = -1
        class_name = "Definetly not a Dog Or Cat"
    #n = int(prediction > 0.5)
    
    return class_name, prediction

#print(get_prediction('dog.jpeg'))