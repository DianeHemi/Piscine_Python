from MyPlotLib import MyPlotLib
import matplotlib.pyplot as plt

class Komparator:
    def __init__(self, df):
        """
        df = Dataset
        """
        self.df = df
        
    def compare_box_plots(self, categorical_var, numerical_var):
        """
        Displays a box plot with several boxes to compare how the distribution of the 
        numerical variable changes if we only consider the subpopulation which belongs to 
        each category. There should be as many boxes as categories. 
        For example, with Sex and Height, we would compare the height distributions of 
        men vs. women with two boxes on the same graph
        """
        # Faire un dictionnaire
        dc = {}
        
        cat = self.df.groupby(categorical_var)[numerical_var].unique()
        
        # for index in range(len(self.df[categorical_var])):
        #     dc[self.df[numerical_var][index]] = {self.df[categorical_var][index]}
            

        MyPlotLib.box_plot(cat, list(cat.index))
        
        
        
    def density(self, categorical_var, numerical_var):
        """
        Displays the density of the numerical variable. Each subpopulation should be 
        represented by a separate curve on the graph
        """
        cat = self.df[categorical_var].unique()
        clean = self.df[[categorical_var, numerical_var]].dropna()
        ret = {}
        
        for it in cat:
            tmp = clean[clean[categorical_var] == it]
            ret[it] = tmp

        MyPlotLib.density(ret, cat)
        
        
        
    def compare_histograms(self, categorical_var, numerical_var):
        """
        Plots the numerical variable in a separate histogram for each category. 
        As an extra, you can use over lapping histograms with a color code
        """