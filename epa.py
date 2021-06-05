#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 
#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("epa_Dataset")

#import dataset
df = pd.read_csv('epl.csv')
#First thirty rows
epa = df.head(20)
#Display the table
st.table(epa)
st.header("Visualisation Using Seaborn")
#bar plot
st.subheader("Bar Plot")
sns.barplot(x='Nationality',y='Yellow_Cards',data=epa)
st.pyplot()


#pairplot
st.subheader("Pairplot")
sns.pairplot(epa,hue='Nationality',palette='rainbow')
st.pyplot()

#Correation
st.subheader("Heatmap")
sns.heatmap(epa.corr(),cmap='coolwarm',annot=True)
st.pyplot()
