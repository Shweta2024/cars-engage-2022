
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

class KMeans_clustering:
    '''
    This is the KMeans_clustering class
    '''
    
    def __init__(self,data):
        self.data=data

    def scaling_features(self):
        '''
        This function scales the values of Ex-Showroom_Price and Displacement.
        
        Returns : The head of the dataframe after scaling Ex-Showroom_Price and Displacement betwween 0 to 1.
        '''
        Scaler = MinMaxScaler()
        for col in ['Ex-Showroom_Price','Displacement']:
            Scaler.fit(self.data[[col]])
            self.data[col] = Scaler.transform(self.data[[col]])
        return self.data.head()
    
    def sum_square_error(self):
        '''
        This function calculates Sum of Square Error and helps in finding optimal value of k.
        
        Returns : Saves the figure of the Elbow Plot in the sub folder inside the static folder.
        '''
        sse = []
        k_range = range(1,10)
        for k in k_range:
            km = KMeans(n_clusters=k)
            km.fit(self.data[['Displacement','Ex-Showroom_Price']])
            sse.append(km.inertia_)
        fig = plt.figure(figsize = (10, 5))
        plt.xlabel('k')
        plt.ylabel('Sum of Square Error')
        plt.title('Elbow Plot')
        plt.plot(k_range,sse)
        #plt.show()
        return plt.savefig("static/sub/elbowPlot.png")
    
    def kmean(self):
        '''
        This function applies K-Means Clustering on Displacement and Ex-Showroom_Price,where k=3.

        Returns : Saves the figure in the sub folder, inside the static folder.
        '''
        km = KMeans(n_clusters=3)
        y_predicted = km.fit_predict(self.data[['Displacement','Ex-Showroom_Price']])
        self.data['cluster'] = y_predicted
        df1 = self.data[self.data.cluster==0]
        df2 = self.data[self.data.cluster==1]
        df3 = self.data[self.data.cluster==2]
        fig = plt.figure(figsize = (10, 5))
        plt.scatter(df1['Displacement'],df1['Ex-Showroom_Price'],color='green',label='Cluster-1')
        plt.scatter(df2['Displacement'],df2['Ex-Showroom_Price'],color='red',label='Cluster-2')
        plt.scatter(df3['Displacement'],df3['Ex-Showroom_Price'],color='yellow',label='Cluster-3')
        plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='black',marker='*',label='centroid')
        plt.title('Scatter plot between Ex-Showroom Price and Displacement')
        plt.legend()
        #plt.show()
        return plt.savefig("static/sub/clustering.png")


