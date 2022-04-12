import pandas as pd
import matplotlib.pyplot as plt

class MyPlotLib:
    @staticmethod
    def histogram(data, features):
        """
        plots one histogram for each numerical feature in the list
        """
        data[features].hist(grid=True)
        plt.show()
        
    @staticmethod
    def density(data, features):
        """
        plots the density curve of each numerical feature in the list
        """
        data[features].plot.kde(grid=True)
        plt.show()

    @staticmethod  
    def pair_plot(data, features):
        """
        Plots a matrix of subplots (also called scatter plot matrix). 
        On each subplot shows a scatter plot of one numerical variable against
        another one. The main diagonal of this matrix shows simple histograms.
        """
        df = []
        for element in features:
            df.append(data[element])
        df = pd.DataFrame(df).transpose()
        
        pd.plotting.scatter_matrix(df)

        plt.show()
     
    @staticmethod   
    def box_plot(data, features):
        """
        Displays a box plot for each numerical variable in the dataset.
        """
        df = []
        for element in features:
            df.append(data[element])
        df = pd.DataFrame(df).transpose()
        
        df.plot.box()
        plt.xticks(ticks=range(1, len(features) + 1), labels=features)

        plt.show()