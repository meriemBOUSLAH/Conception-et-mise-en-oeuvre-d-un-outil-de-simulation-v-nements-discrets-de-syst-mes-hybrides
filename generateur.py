
class gen:

  def __init__(self):

    self.state = 's'
    self.output =  {'job' : None}
    self.input = {}

  def internal_func(self):
      if self.state == 's':
         self.state = 's'
      #return self.state

  def external_func(self,t):
        pass

  def lambda_func(self):
      if self.state == 's':

          self.output['job'] = True
          return self.output

  def get_Ta(self):
    if self.state =='s':
      return 2
    else :
        return -1