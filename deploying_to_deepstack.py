"""
The code below is used to deploy our models to Deepstack AI server
NOTE: The returned json is printed onto our terminal when the code runs
"""
import requests
from io import  open

model = open("FruitsDetect.onnx","rb").read()
config = open("config.json","rb").read()

response = requests.post("http://localhost:80/v1/vision/addmodel",
            files={"model":model,"config":config},data={"name":"FruitsDetect"}).json()

print(response)
