
class test():

    def __init__(self, fn, ln):
        
        self._fn = fn
        self._ln = ln
        
        #self.full_name();
    
    def full_name(self):
        
        print(self._fn +' '+ self._ln)
    

o1 = test('ishmam','tonmoy')
o1.full_name()
