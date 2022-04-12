import pandas as pd
import matplotlib.pyplot as plt

class MyPlotLib:
    def histogram(self, data, features):
        """
        plots one histogram for each numerical feature in the list
        """
        data[features].hist(grid=True)
        plt.show()
        
    def density(self, data, features):
        """
        plots the density curve of each numerical feature in the list
        """
        data[features].plot.kde(grid=True)
        plt.show()
        
    def pair_plot(self, data, features):
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
        
    def box_plot(self, data, features):
        """
        Displays a box plot for each numerical variable in the dataset.
        """
        df = []
        for element in features:
            df.append(data[element])
        df = pd.DataFrame(df).transpose()
        
        df.plot.box()

        plt.show()