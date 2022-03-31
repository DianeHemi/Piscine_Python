class Vector:
    
    def init_list(self, val):
        self.values = val
        if isinstance(self.values[0], float):
            self.shape = (1, len(self.values))
        else:
            self.shape = (len(self.values), len(self.values[0]))
     
    def init_int(self, val):
        self.values = []
        i = 0
        while i < val:
            self.values.append([i + 0.0])
            i += 1
        self.shape = (len(self.values), 1)

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

    # Only vectors of same dimensions
    def __add__(self, y):
        if self.shape != y.shape:
            print("Error")
            return
        i = 0
        if isinstance(self.values[0], float):
            while i < len(self.values):
                self.values[i] += y.values[i]
                i += 1
        else:
            while i < len(self.values):
                self.values[i][0] += y.values[i][0]
                i += 1
        return self.values

    def __radd__(self, y): 
        if y.shape != self.shape:
            print("Error")
            return
        i = 0
        if isinstance(y.values[0], float):
            while i < len(y.values):
                y.values[i] += self.values[i]
                i += 1
        else:
            while i < len(y.values):
                y.values[i][0] += self.values[i][0]
                i += 1
        return y.values

    # Only vector of same dimensions 
    def __sub__(self, y):
        if self.shape != y.shape:
            print("Error")
            return
        i = 0
        if isinstance(self.values[0], float):
            while i < len(self.values):
                self.values[i] -= y.values[i]
                i += 1
        else:
            while i < len(self.values):
                self.values[i][0] -= y.values[i][0]
                i += 1
        return self.values
        
    def __rsub__(self, y):
        if y.shape != self.shape:
            print("Error")
            return
        i = 0
        if isinstance(y.values[0], float):
            while i < len(y.values):
                y.values[i] -= self.values[i]
                i += 1
        else:
            while i < len(y.values):
                y.values[i][0] -= self.values[i][0]
                i += 1
        return y.values

    # Only scalars 
    def __truediv__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            pass
        else:
            print("Error")
            return
        i = 0
        if self.shape[0] == 1:
            while i < len(self.values):
                self.values[i] /= y
                i += 1
        else:
            while i < len(self.values):
                self.values[i][0] /= y
                i += 1
        return self.values
        
    def __rtruediv__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            pass
        else:
            print("Error")
            return
        i = 0
        if self.shape[0] == 1:
            while i < len(self.values):
                y /= self.values[i]
                i += 1
        else:
            while i < len(self.values):
                y /= self.values[i][0]
                i += 1
        return self.values

    # Only scalars   
    def __mul__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            pass
        else:
            raise TypeError()
        i = 0
        if self.shape[0] == 1:
            while i < len(self.values):
                self.values[i] *= y
                i += 1
        else:
            while i < len(self.values):
                self.values[i][0] *= y
                i += 1
        return self.values
        
    def __rmul__(self, y):
        if isinstance(y, int) or isinstance(y, float):
            pass
        else:
            raise TypeError()
        i = 0
        if self.shape[0] == 1:
            while i < len(self.values):
                y *= self.values[i]
                i += 1
        else:
            while i < len(self.values):
                y *= self.values[i][0]
                i += 1
        return self.values
        
    def __str__(self):
        txt = "["
        i = 0
        if self.shape[0] == 1:
            while i < len(self.values):
                txt += str([self.values[i]])
                if i + 1 < len(self.values):
                    txt += ", "
                i += 1
        else:
            while i < len(self.values):
                txt += "["
                txt += str(self.values[i][0])
                txt += "]"
                if i + 1 < len(self.values):
                    txt += ", "
                i += 1
                    
        txt += "]"
        return txt
        
    def __repr__(self):
        txt = "["
        i = 0
        if self.shape[0] == 1:
            while i < len(self.values):
                txt += str([self.values[i]])
                if i + 1 < len(self.values):
                    txt += ", "
                i += 1
        else:
            while i < len(self.values):
                txt += "["
                txt += str(self.values[i][0])
                txt += "]"
                if i + 1 < len(self.values):
                    txt += ", "
                i += 1
                    
        txt += "]"
        return txt
    
    # Dot product between two vectors of same shape
    def dot(self, y):
        if isinstance(y, Vector) is False or self.shape != y.shape:
            raise TypeError()
        i = 0
        if self.shape[0] == 1:
            while i < len(self.values):
                self.values[i] *= y.values[i]
                i += 1
        else:
            while i < len(self.values):
                self.values[i][0] *= y.values[i][0]
                i += 1
        return self.values

    # Returns the transpose vector (row -> column / column -> row)
    def T(self):
        i = 0
        new_vector = []
        if self.shape[0] == 1:
            while i < len(self.values):
                new_vector.append([self.values[i]])
                i += 1
        else:
            while i < len(self.values):
                new_vector.append(self.values[i][0])
                i += 1
        return new_vector
