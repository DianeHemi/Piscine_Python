from HowManyMedals import howManyMedals
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

    print(howManyMedals(data, 'Kjetil Andr Aamodt'))
    # {1992: {’G’: 1, ’S’: 0, ’B’: 1},
    # 1994: {’G’: 0, ’S’: 2, ’B’: 1},
    # 1998: {’G’: 0, ’S’: 0, ’B’: 0},
    # 2002: {’G’: 2, ’S’: 0, ’B’: 0},
    # 2006: {’G’: 1, ’S’: 0, ’B’: 0}}
    
    
    
if __name__ == '__main__':
	main()