import csv


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.file_obj = open(filename, "r")
        self.header = header
        self.header_data = None
        self.top = skip_top
        self.bot = skip_bottom
        self.sep = ','
        self.data = []

        
        
    def __enter__(self):
        if self.filename is None:
            print("Invalid filename")
            self = None
            return self
        
        data = csv.reader(self.file_obj, delimiter=self.sep)
        column = len(next(data))
        size = 0

        for row in data:
            if len(row) != column:
                raise IndexError("Invalid number of columns !")
            for element in row:
                if element is None or element == "":
                    raise TypeError("Empty row !")
            if size >= self.top:
                if self.bot == 0 or (self.bot != 0 and size <= self.bot):
                    self.data.append(row)
            size += 1
            
        return self
        
        
        
        
        
        
    def __exit__(self, type, value, traceback):
        self.file_obj.close()
        return True
            
            
    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Returns:
        nested list (list(list, list, ...)) representing the data.
        """
        
        
        
        
        return self.data
    
    
    
    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """

        if self.header is False:
            return None
        if self.header is True and self.top == 0:
            self.header_data = self.data[0]
        else:
            self.header_data = self.data[self.top]

        return self.header_data
        