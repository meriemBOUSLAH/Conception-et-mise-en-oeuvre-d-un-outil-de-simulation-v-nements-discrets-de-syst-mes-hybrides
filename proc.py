import math

class proc:

  def __init__(self,name):
      self.name=name
      self.state = 'free'
      self.input = {'req' : None}
      self.output = {'done' : None}

  def internal_func(self):
      if self.state == "busy" :
        self.state="free"

  def external_func(self) :
      if self.state == "free" and self.input['req'] == True :
            self.state="busy"

  def lambda_func(self):
      if self.state == "busy":
            self.output['done'] = True
        return self.output

  def get_Ta(self):
     if self.state=="free":
        return math.inf        #infini

     elif self.state=="busy":

     elif self.state=="busy":
        return 3
     else :
        return -1 #error


