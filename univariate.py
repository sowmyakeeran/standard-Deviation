class Univariate():
    
    def QuanQual(self,dataset):
        Quan=[]
        Qual=[]
        for columnName in dataset.columns:
            print(columnName)
            if(dataset[columnName].dtypes=="O"):
                #print("Qual")
                Qual.append(columnName)
            else:
                #print("Quan")
                Quan.append(columnName)
        return Quan,Qual
    def frequencyTable(self,dataset,columnName):
        import pandas as pd
        freq=pd.DataFrame(columns=["Unique_Values","Frequency","Relative_Freq","Cumsum"])
        freq["Unique_Values"]=dataset[columnName].value_counts().sort_index().index
        freq["Frequency"]=dataset[columnName].value_counts().sort_index().values
        freq["Relative_Freq"]=(freq["Frequency"]/len(freq))*100
        freq["Cumsum"]=freq["Relative_Freq"].cumsum()
        return freq
    
    def uniAnalysis(self,dataset,quan):
        import pandas as pd
        import numpy as np
        univarite=pd.DataFrame(index=["Mean","Median","Mode","25th","50th","75th","99th","100th",\
                                     "IQR","1.5IQR","Lesser","Greater","Min","Max","Std","Variance"],columns=quan)
        for columnName in quan:
            univarite[columnName]["Mean"]=dataset[columnName].mean()
            univarite[columnName]["Median"]=dataset[columnName].median()
            univarite[columnName]["Mode"]=dataset[columnName].mode()[0]
            univarite[columnName]["25th"]=np.percentile(dataset[columnName],25)
            univarite[columnName]["50th"]=np.percentile(dataset[columnName],50)
            univarite[columnName]["75th"]=np.percentile(dataset[columnName],75)
            univarite[columnName]["99th"]=np.percentile(dataset[columnName],99)
            univarite[columnName]["100th"]=np.percentile(dataset[columnName],100)
            univarite[columnName]["IQR"]=univarite[columnName]["75th"]-univarite[columnName]["25th"]
            univarite[columnName]["1.5IQR"]=1.5*univarite[columnName]["IQR"]
            univarite[columnName]["Lesser"]=univarite[columnName]["25th"]-univarite[columnName]["1.5IQR"]
            univarite[columnName]["Greater"]=univarite[columnName]["75th"]+univarite[columnName]["1.5IQR"]
            univarite[columnName]["Min"]=dataset[columnName].min()
            univarite[columnName]["Max"]=dataset[columnName].max()
            univarite[columnName]["Std"]=dataset[columnName].std()
            univarite[columnName]["Variance"]=dataset[columnName].var()
            
        return univarite