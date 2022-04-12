from MyPlotLib import MyPlotLib
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

    plot = MyPlotLib()
    
    # plot.histogram(data, ["Height", "Weight"])
    
    plot.density(data, ["Height", "Weight"])
    
    # plot.pair_plot(data, ["Height", "Weight"])
    
    # plot.box_plot(data, ["Height", "Weight"])
    
    
    
if __name__ == '__main__':
	main()