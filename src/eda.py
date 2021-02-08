import pandas as pd
import numpy as np
import sklearn
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import rcParams
import os

def data(path):  
    df = pd.read_csv(path,sep=";")
    return


def eda(df):
    df2 = df.copy()
    df2['age'] = (df2['age'] / 365).round().astype('int')
    
    bins= [30,35,40,45,50,55,60,65]
    labels = ["30-35","35-40","40-45","45-50","50-55","55-60","60-65"]
    df2['AgeGroup'] = pd.cut(df2['age'], bins=bins, labels=labels, right=False)
    rcParams['figure.figsize'] = 11, 8
    ageGroup = plt.figure()
    sns.countplot(x='AgeGroup', hue='cardio', data = df2)
    
    ageBox = plt.figure()
    sns.boxplot(x='cardio',y='age',data=df2)
    
    cardio = df2[df2.cardio == 1]
    cardioFeature = plt.figure()
    cardio_cate = cardio.loc[:,['cholesterol','gluc', 'smoke', 'alco', 'active']]
    sns.countplot(x="variable", hue="value",data= pd.melt(cardio_cate))
    
    noncardio = df2[df2.cardio == 0]
    noncardio_cate = noncardio.loc[:,['cholesterol','gluc', 'smoke', 'alco', 'active']]
    noncardioFeature = plt.figure()
    sns.countplot(x="variable", hue="value",data= pd.melt(noncardio_cate))
    
    gender= plt.figure()
    sns.countplot(x='gender', hue='cardio', data = df)
    
    df.hist()
    
    corr = df.corr()
    corrPlot= plt.figure()
    sns.heatmap(corr, annot=True)
    
    df2['ponderIndex'] = df2['weight']/(df2['height']/100)**3
    bins= [0,3,7,11,15,19,23,27,31,35,39,44]
    labels = ["0-3","3-7","7-11","11-15","15-19","19-23","23-27","27-31","31-35","35-39","39-44"]
    df2['PIGroup'] = pd.cut(df2['ponderIndex'], bins=bins, labels=labels, right=False)
    ponderIndex = plt.figure()
    sns.countplot(x='PIGroup', hue='cardio', data = df2)
    
    df2['ponderIndex'].describe().to_csv("../test/testoutput/ponderIndex.csv")
    
     
    line_x1 = np.linspace(50, 250, 1000)
    line_y1 = 11*((line_x1/100)**3)
    line_x2 = np.linspace(50, 250, 1000)
    line_y2 = 15*((line_x1/100)**3)
    PIScatter = plt.figure() 
    sns.scatterplot(x='height',y='weight', hue='cardio', data = df)
    plt.plot(line_x1, line_y1, color='r')
    plt.plot(line_x2, line_y2, color='r')
    
    
    ageGroup.savefig('../test/testoutput/ageGroup.png')
    ageBox.savefig('../test/testoutput/ageBox.png')
    cardioFeature.savefig('../test/testoutput/cardioFeature.png')
    noncardioFeature.savefig('../test/testoutput/noncardioFeature.png')
    gender.savefig('../test/testoutput/gender.png')
    ponderIndex.savefig('../test/testoutput/ponderIndex.png')
    PIScatter.savefig('../test/testoutput/PIScatter.png')
    #histplot.figure.savefig('../data/out/hist.png')
    corrPlot.savefig('../test/testoutput/corrPlot.png')
       
    return



def describe(df):
    df['age'] = (df['age']/365).round().astype('int')
    df.describe().to_csv("../test/testoutput/description.csv")
    return