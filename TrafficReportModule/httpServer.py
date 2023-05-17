from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
import multiprocessing
import time


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


#@cross_origin()
#class ClientApp:
    # def __init__(self):
    #     self.filename = "inputImage.jpg"
    #     self.classifier = traffic(self.filename)


# insertStatus("I am testing the api now , let me play" , "Warning")
# insertStatus("Now i wolud like to check the two params" , "Error")
# insertStatus("Close to object 40cm" , "Warning")
# insertStatus("Close to object 20cm" , "Error")
# insertStatus("More drivers will be upload" , "Warning")
# insertStatus("Now i wolud like to check the two params" , "Error")

@app.route("/status", methods=['GET'])
@cross_origin()
def home():
    status = trafficReportModule.getStatuses()
    return status
    
    


# @app.route("/predict", methods=['POST'])
# @cross_origin()
# def predictRoute():
#     image = request.json['image']
#     decodeImage(image, clApp.filename)
#     result = clApp.classifier.trafficsign()
#     return jsonify(result)

def startServer():
    app.run(host='0.0.0.0', port=5000)
    
p = multiprocessing.Process(target=startServer, args=())
def startHttpServer(TrafficReportModule):
  global trafficReportModule
  trafficReportModule = TrafficReportModule
  p.daemon = True
  p.start()
  return p
  
  

