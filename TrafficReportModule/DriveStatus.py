import datetime

class DriveStatus:
  def __init__(self, description, severaty):
    self.date = datetime.datetime.now().strftime("%H:%M:%S")
    self.description = description
    self.severaty = severaty