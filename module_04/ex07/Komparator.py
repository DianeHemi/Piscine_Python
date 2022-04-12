from MyPlotLib import MyPlotLib
import matplotlib.pyplot as plt
import seaborn as sns

class Komparator:
    def __init__(self, df):
        self.df = df
        
    def compare_box_plots(self, categorical_var, numerical_var):
        """
        Displays a box plot with several boxes to compare how the distribution of the 
        numerical variable changes if we only consider the subpopulation which belongs to 
        each category. There should be as many boxes as categories. 
        For example, with Sex and Height, we would compare the height distributions of 
        men vs. women with two boxes on the same graph
        """
        cat = self.df[categorical_var].unique()

        dc = {}
        for elem in cat:
            dc[elem] = self.df[self.df[categorical_var] == elem][numerical_var]

        MyPlotLib.box_plot(dc, cat)
        
        
        
    def density(self, categorical_var, numerical_var):
        """
        Displays the density of the numerical variable. Each subpopulation should be 
        represented by a separate curve on the graph
        """
        cat = self.df[categorical_var].unique()
        for elem in cat:
            sns.kdeplot(self.df[numerical_var][self.df[categorical_var] == elem].dropna(), label=elem)
        plt.title('Density by {cat}'.format(cat=categorical_var))
        plt.show()
        
        
    def compare_histograms(self, categorical_var, numerical_var):
        """
        Plots the numerical variable in a separate histogram for each category. 
        As an extra, you can use over lapping histograms with a color code
        """
        cat = self.df[categorical_var].unique()
        for elem in cat:
            sns.distplot(self.df[numerical_var][self.df[categorical_var] == elem].dropna(), label=elem, kde=False)
        plt.title('Density by {cat}'.format(cat=categorical_var))
        plt.show()