import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

class Visualization:
    '''
    This is the Visualization class
    '''

    def __init__(self,data,x,y):
        self.data=data
        self.x=x
        self.y=y

    def bar_chart(self):
        '''
        This function plots a Bar Chart between the two selected columns.
        
        Returns : Save the figure in the sub folder inside the static folder.
        '''
        fig = plt.figure(figsize = (10, 5))
        plt.bar(self.data[self.x].head(30),self.data[self.y].head(30), color ='yellow',width = 0.4)
        plt.xlabel(self.x)
        plt.ylabel(self.y)
        plt.title("Bar Plot between "+ self.x +" and "+ self.y)
        return plt.savefig("static/sub/bar2.png") 

    def scatter_chart(self):
        '''
        This function plots a Scatter Plot between the two selected columns.
        
        Returns : Saves the figure in the sub folder inside the static folder.
        '''
        fig = plt.figure(figsize = (10, 5))
        plt.scatter(self.data[self.x].head(100),self.data[self.y].head(100))
        plt.xlabel(self.x)
        plt.ylabel(self.y)
        return plt.savefig("static/sub/scatter2.png")
   
    def correlation(self):
        '''
        This function finds the correlation and plots a heatmap using top correlation.
        
        Returns : Saves the figure in the sub folder inside the static folder.
        '''
        correl=self.data.corr()
        #return correl
        top_corr = correl.index
        plt.figure(figsize=(20,20))
        g=sns.heatmap(self.data[top_corr].corr(),annot=True,cmap="RdYlGn")
        return plt.savefig("static/sub/cor.png")

