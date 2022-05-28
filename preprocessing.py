import pandas as pd

class Pre_Processing:
    '''
    This is the Pre_Processing class
    '''

    def __init__(self,data,percentage_missing_value):
        self.data=data
        self.percentage_missing_value=percentage_missing_value

    def drop_column(self):
        '''
        This function deletes the columns which has more than 60% missing values
        
        Returs : The head of the dataframe after deleting all columns which has more than 60% missing values
        '''
        for col in self.data.columns:
            if(self.data[col].isnull().sum()*100 / len(self.data) >60.000000):
                self.data.drop(col,axis=1,inplace=True)
        return self.data.head()


    def fill_missing_values(self):
        '''
        This function fills all the missing values of the dataframe.
        
        Returns : Returns the head of the dataframe after filling the missing values of each column with its mode.
        '''
        cateogry_columns=self.data.select_dtypes(include=['object']).columns.tolist()
        integer_columns=self.data.select_dtypes(include=['int64','float64']).columns.tolist()
        for column in self.data:
            if self.data[column].isnull().any():
                    self.data[column].fillna(self.data[column].mode()[0],inplace=True)
        return self.data.head()
       

    def dummies(self):
        '''
        This function creates a dummy dataframe.
        
        Returns : The head of the dummy dataframe.
        '''
        dummy_dataset = pd.get_dummies(self.data, columns = ['Make','Model','Variant','Fuel_Type','Body_Type'])
        return dummy_dataset.head()



