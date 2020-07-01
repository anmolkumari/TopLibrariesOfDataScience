#summarised pandas as per sp2
import pandas as pd
import numpy as np
def main():
    # List of Tuples
    empoyees = [('jack', 34, 'Sydney', 155),
                ('Riti', 31, 'Delhi', 177.5),
                ('Aadi', 16, 'Mumbai', 81),
                ('Mohit', 31, 'Delhi', 167),
                ('Veena', 12, 'Delhi', 144),
                ('Shaunak', 35, 'Mumbai', 135),
                ('Shaun', 35, 'Colombo', 111)
                ]
    # Create a DataFrame object
    empDfObj = pd.DataFrame(empoyees, columns=['Name', 'Age', 'City', 'Marks'])
    print("Contents of the Dataframe : ")
    print(empDfObj)
    print('*** Get the Data type of each column in Dataframe ***')
    # Get a Series object containing the data type objects of each column of Dataframe.
    # Index of series is column name.
    dataTypeSeries = empDfObj.dtypes
    print('Data type of each column of Dataframe :')
    print(dataTypeSeries)
    # Get a Dictionary containing the pairs of column names & data type objects.
    dataTypeDict = dict(empDfObj.dtypes)
    print('Data type of each column of Dataframe :')
    print(dataTypeDict)
    print('*** Get the Data type of a single column in Dataframe ***')
    # get data type of column 'Age'
    dataTypeObj = empDfObj.dtypes['Age']
    print('Data type of each column Age in the Dataframe :')
    print(dataTypeObj)
    print('*** Check if Data type of a column is int64 or object etc in Dataframe ***')
    # Check the type of column 'Age' is int64
    if dataTypeObj == np.int64:
        print("Data type of column 'Age' is int64")
    # Check the type of column 'Name' is object i.e string
    if empDfObj.dtypes['Name'] == np.object:
        print("Data type of column 'Name' is object")
    print('** Get list of pandas dataframe columns based on data type **')
    # Get  columns whose data type is object i.e. string
    filteredColumns = empDfObj.dtypes[empDfObj.dtypes == np.object]
    # list of columns whose data type is object i.e. string
    listOfColumnNames = list(filteredColumns.index)
    print(listOfColumnNames)
    print('*** Get the Data type of each column in Dataframe using info() ***')
    # Print complete details about the data frame, it will also print column count, names and data types.
    empDfObj.info()
if __name__ == '__main__':
    main()