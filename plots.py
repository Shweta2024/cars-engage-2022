
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class Plots:
    '''
    This is the Plots class
    '''

    def __init__(self,data,col):
        self.data=data
        self.col=col
    
    def bar_plot(self):
        '''
        This function plots a Bar Chart between the selected column and its count.
        
        Returns : Save the figure in the sub folder inside the static folder.
        '''
        fig = plt.figure(figsize =(10, 7))
        self.data[self.col].value_counts().head(10).plot.bar()
        x=self.col
        plt.xlabel(x)
        plt.ylabel("Count")
        plt.title("Top selling Cars as per their "+x)
        return plt.savefig("static/sub/bar.png")

    def box_plot(self):
        '''
        This function plots a Box Chart of the selected column.
        
        Returns : Save the figure in the sub folder inside the static folder.
        '''
        fig = plt.figure(figsize =(10, 7))
        sns.boxplot(self.data[self.col].head(30),self.data['Ex-Showroom_Price'].head(30))
        plt.title("Boxplot")
        return plt.savefig("static/sub/box.png")
        