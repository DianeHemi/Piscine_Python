from csvreader import CsvReader


if __name__ == "__main__":
    with CsvReader('good.csv', ',', True) as file:
        data = file.getdata()
        header = file.getheader()
        
    with CsvReader('bad.csv', ',', True) as file:
        data = file.getdata()
        header = file.getheader()
    
