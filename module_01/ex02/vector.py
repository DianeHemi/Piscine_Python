from numpy import isin


class Vector:
    
    def init_list(self, val):
        self.values = val
        if isinstance(self.values[0], float):
            self.shape = (1, len(self.values))
        else:
            self.shape = (len(self.values), len(self.values[0]))
        print(self.values, " ", self.shape)

     
    def init_int(self, val):
        self.values = []
        i = 0
        while i < val:
            self.values.append([i + 0.0])
            i += 1
        self.shape = (len(self.values), 1)
        print(self.values, " ", self.shape)


    def __init__(self, values):
        if isinstance(values, list):
            self.init_list(values)
        elif isinstance(values, int):
            self.init_int(values)
        else:
            self.values = []
            i = values[0]
            while i < values[1]:
                self.values.append([i + 0.0])
                i += 1
            self.shape = (len(self.values), 1)
            print(self.values, " ", self.shape)


    # Only vectors of same dimensions
    def __add__(self, y):
        sum = []
        for i in range(len[self]):
            sum.append([i] + y[i])
        print(sum)
        
      
    #def __radd__(): 
        
        
    
    # Only vector of same dimensions 
    #def __sub__():
         
        
    #def __rsub__():
        
        
       
    # Only scalars 
    #def __truediv__():
        
        
    #def __rtruediv__():
        
        
        
    # Only scalars   
    #def __mul__():
        
        
    #def __rmul__():
        
        
        
    #def __str__():
        
        
        
    #def __repr__():
        
    
    
    # Dot product between two vectors of same shape
    #def dot():
        
    
    
    # Returns the transpose vector (row -> column / column -> row)
    #def T():