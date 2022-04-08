from SpatioTemporalData import SpatioTemporalData
import pandas as pd


class FileLoader:
    @staticmethod
    def load(path):
        """ Display dimensions on dataset and return dataset loaded
        as pandas.DataFrame"""
        try:
            dataset = pd.read_csv(path)
        except Exception:
            return None
        print("Loading dataset of dimensions", dataset.shape[0], "x", dataset.shape[1])
        return dataset
        
    @staticmethod
    def display(df, n):
        """Takes pandas.DataFrame and integer, displays first n rows
        of the dataset if n is positive or the last n rows if n is negative"""
        if n > 0:
            print(df.iloc[0:n])
        elif n < 0:
            print(df.iloc[df.shape[1] - n:])
        
    
    
def main():
    loader = FileLoader()
    data = loader.load("../athlete_events.csv")

    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    # [’Athina’]

    print(sp.where(2016))
    # [’Rio de Janeiro’]
    
    print(sp.when('Athina'))
    # [2004, 1906, 1896]
    
    print(sp.when('Paris'))
    # [1900, 1924]
    
    
    
if __name__ == '__main__':
	main()