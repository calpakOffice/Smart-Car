import json
import os

from TrafficReportModule.DriveStatus import DriveStatus

class TrafficReportModule:
    def __init__(self):
        self.statuses = []
        self.path = "./TrafficReportModule/status.json"
        with open(self.path, 'w') as json_file:
            json.dump(self.statuses, json_file)
    def insertStatus( self,description , severaty):
        newStatus= DriveStatus(description,severaty)
        statuses = []
        fileAlreadyExists = os.path.isfile(self.path) 
        if fileAlreadyExists:
            with open(self.path,'r') as openFile:
                statuses = json.load(openFile)
        statuses.append(newStatus.__dict__)
        with open(self.path, 'w') as json_file:
            json.dump(statuses, json_file, 
                        indent=4,  
                        separators=(',',': '))

    def getStatuses(self):
        with open(self.path,'r') as openFile:
            jsonStr = json.load(openFile)
            return jsonStr