"""
The code below is used to deploy our models to Deepstack AI server
NOTE: The returned json is printed onto our terminal when the code runs
"""
import requests
from io import  open

# This open the Fruits.onnx, reads it then assign it the reference model
model = open("Fruits.onnx","rb").read()
# This opens the congig.json file, reads it and assign it the reference config
config = open("config.json","rb").read()

# This create the api, give the api it name "FruitsRecognition", and also takes the config file
# it also return a json which is then pointed with reference name reponse
response = requests.post("http://localhost:80/v1/vision/addmodel",
            files={"model":model,"config":config},data={"name":"FruitsRecognition"}).json()

# This print the response to the screen
print(response)