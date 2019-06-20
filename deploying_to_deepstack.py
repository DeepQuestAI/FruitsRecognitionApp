import requests
from io import  open

model = open("myCustomResNetModel.onnx","rb").read()
config = open("config.json","rb").read()

response = requests.post("http://localhost:80/v1/vision/addmodel",
            files={"model":model,"config":config},data={"name":"myCustomResNetModel"}).json()

# response = requests.post("http://localhost:80/v1/vision/deletemodel", data={"name":"professiontf2"}).json()
# print(len(response["models"]))
print(response)
