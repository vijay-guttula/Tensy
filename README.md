# Dog or Cat Classifier Using TensorFlow

## Getting Started

This app uses docker which is only avaible on `Window10 Pro or Enterprize` , this doesnt run on `Windows Home`  but is accessible easily in case of other OS
I recommend using an `Ubuntu` or `Mac` or any `linux` based OS and install `docker`, go to this [link](https://docs.docker.com/get-docker/) for details.
    
    $sudo apt install docker.io

This program needs to be run in `Python3` only. So if you need to install python3's pip use the following command

    $sudo apt install python3 python3-pip

After installing pip3, run the requirements.

    $pip3 install -r requirements.txt

## Now to run the program,

First you need to load the dataset from `docker`.

    $sudo docker run -p 8501:8501 --name=pets -v "/<----the address of the pets folder--->/pets/:/models/pets/1" -e MODEL_NAME=pets tensorflow/serving

#### Please see that you need to specify the address clearly.

You can close the `terminal` or start a new one, either ways it runs in the background, you can check by the following command.

    $sudo docker ps

Now run the flask server.

    $python3 app.py

You'll find the page in `localhost:5000` or `127.0.0.1:5000`, open the link in your browser.

Upload the image, and click the button to send, and you'll find the result.

## In Case of any error based on missing modules or modules not found 

    $pip3 install <module_name>

