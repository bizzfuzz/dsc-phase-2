
# import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline


class DataSourcing:
  def __init__(self,dataframe):
    self.original = dataframe
    self.dataframe = dataframe
  
  def give_info(self):
    message =  f"""
    ----------------------------------------------------------------------->
    DESCRIPTION OF THE DATAFRAME IN QUESTION:
    ----------------------------------------------------------------------->
    
    Dataframe information => {self.dataframe.info()}
    ------------------------------------------------------------------------------------------------------------------------->
    
    Dataframe shape => {self.dataframe.shape[0]} rows, {self.dataframe.shape[1]} columns
    ------------------------------------------------------------------------------------------------------------------------->    
    
    There are {len(self.dataframe.columns)} columns, namely: {self.dataframe.columns}.  
    ------------------------------------------------------------------------------------------------------------------------->
        
    The first 5 records in the dataframe are seen here:
    ------------------------------------------------------------------------------------------------------------------------->
    {self.dataframe.head()}
    ------------------------------------------------------------------------------------------------------------------------->
       
    The last 5 records in the self.dataframe are as follows: 
    ------------------------------------------------------------------------------------------------------------------------->
    {self.dataframe.tail()}
    ------------------------------------------------------------------------------------------------------------------------->
    
    The descriptive statistics of the dataframe (mean,median, max, min, std) are as follows:
    ------------------------------------------------------------------------------------------------------------------------->
    {self.dataframe.describe()}
    ------------------------------------------------------------------------------------------------------------------------->
    """
    print (message)
  
  def null_count(self):
    return self.dataframe.isnull().sum()
  
  def unique_count(self):
    return self.dataframe.nunique()
  
  def unique_per_column(self):
    print("<----- UNIQUE VALUES IN EACH COLUMN ----->")
    for col in self.dataframe.columns:
      print(f"{col} ({len(self.dataframe[col].unique())} unique)\n {sorted(self.dataframe[col].unique())}")
      print()
    print("<----- END OF UNIQUE VALUES IN EACH COLUMN ----->")
    return
  
  def plot_barplot(self,dataframe,x,y,x_title,y_title):
    fig,ax = plt.subplots(figsize=(10,8))
    
    sns.barplot(data = dataframe,x=x, y=y,orient='h')
    ax.set_title(f"{y_title} vs {x_title}")
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    plt.show()
 
 
data_sourcing = DataSourcing(dataframe=df_raw)
data_sourcing.give_info()

