class Information:
    '''
    This is the Information class
    '''

    def __init__(self,data):
        self.data=data
    
    def info(self):
        """
        This function shows information about the dataset.
        
        Returns : the shape of the dataset,
                  the datatype of each columns,
                  first five rows of the dataset (i.e. head of dataset),
                  last five rows of the dataset (i.e. tail of dataset),
                  gives the statistical description of the data in the DataFrame.
        """
        dataset_shape = self.data.shape
        dataTypes = self.data.dtypes
        data_head = self.data.head()
        data_tail = self.data.tail()
        data_describe = self.data.describe()
        return [dataset_shape,dataTypes,data_head,data_tail,data_describe]

    def total_missing_values(self):
        """
        This function gives information about the missing values.

        Returns : the total number of missing values in the dataset,
                  the total number of missing values in each columns arranged in non-ascending order,
                  the percentage of missing values in each columns arranged in non-ascending order,
        """
        total_missing=self.data.isnull().sum().sum()
        missing_value=self.data.isnull().sum()
        missing_value=missing_value.sort_values(ascending=False)
        percentage_missing_value=self.data.isnull().sum()*100 / len(self.data)
        percentage_missing_value=percentage_missing_value.sort_values(ascending=False)
        return [total_missing,missing_value,percentage_missing_value]
        