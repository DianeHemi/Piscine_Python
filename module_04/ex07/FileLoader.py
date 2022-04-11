from Komparator import Komparator
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

    komp = Komparator(data)
    
    # komp.compare_box_plots("Sex", "Height")
    
    komp.density("Sex", "Height")
    
    # komp.compare_histograms()

    
    
    
if __name__ == '__main__':
	main()