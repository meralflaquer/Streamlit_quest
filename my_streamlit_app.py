#!/usr/bin/env python3Python 3.9.4 (v3.9.4:1f2e3088f3, Apr  4 2021, 12:32:44) 
#[Clang 6.0 (clang-600.0.57)] on darwin
#Type "help", "copyright", "credits" or "license()" for more information.


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

st.title('Welcome to the Car Data Analyses application for WCS!')


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)

checkbox = st.checkbox("Show Dataset")
print(checkbox)
if checkbox:
    df


st.title("Correlation Analysis")

#Selectbox-measure selection
st.header("Select the column:")
measures = df.select_dtypes(['float64', 'int64']).columns

# Scatterplot
plt.figure()
scatter_x = st.selectbox('X axis :', measures)
scatter_y = st.selectbox('Y axis :', measures)
fig= px.scatter(df, x=scatter_x, y=scatter_y, title='Correlation', color_discrete_sequence=['gold'])
plt.title("Scatterplot")
st.plotly_chart(fig)



st.write('\n')


#Selectbox-continent selection
st.header("Select a continent: ")
continent_choice = st.selectbox("Select a continent :", df["continent"].unique())
df_choice = df[df["continent"]==continent_choice]

# Scatterplot
plt.figure()
sns.scatterplot(x=scatter_x, y=scatter_y, data=df_choice)
st.pyplot()


# Correlation positive
st.header("A positive correlation")
plt.figure()
fig1, ax1 = plt.subplots()
ax1.scatter(x = "weightlbs", y = "cubicinches", data = df)
plt.xlabel("weightlbs")
plt.ylabel("cubicinches")
plt.title("Weight and displacement")
st.pyplot(fig1)

st.write("Positive correlation: the 2 variables move in the same direction.")

# Correlation négative
st.header("A negative correlation")
plt.figure()
fig2, ax2 = plt.subplots()
ax2.scatter(x = "weightlbs", y = "mpg", data = df)
plt.xlabel("weightlbs")
plt.ylabel("mpg")
plt.title("Weight and mpg")
st.pyplot(fig2)

st.write("Negative correlation: when the weightlbs variable increases, the mpg variable decreases.")



## Distribution Analyses ##

st.title("Distribution Analysis")

#Measure Selection/dropdown
st.header("Select a variable:")
radio_choice = st.radio("Select a variable :", measures)

# Boxplot and Histogram
plt.figure()
plt.subplots(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.boxplot(x = radio_choice, y = "continent", data = df)
plt.title("Boxplot")

plt.subplot(1, 2, 2)
sns.distplot(df[radio_choice])
plt.title("Histogram")
st.pyplot()

#Continent selection/dropdown
st.header("Select a continent:")
cont_choice = st.radio("Select a continent :", df["continent"].unique())
df_cont = df[df["continent"]==cont_choice]

# Boxplot and Histogram
plt.figure()
plt.subplots(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.boxplot(x = radio_choice, y = "continent", data = df_cont)
plt.title("Boxplot")

plt.subplot(1, 2, 2)
sns.distplot(df_cont[radio_choice])
plt.title("Histogram")
st.pyplot()

#Boxplot ex
st.header("Horsepower Boxplot in Europe ")
df_eur = df[df["continent"]==" Europe."]
plt.figure()
sns.boxplot(x = "hp", y = "continent", data = df_eur)
plt.title("Boxplot")
st.pyplot()

st.write("We observe: a median around 80, a minimum around 50, a maximum around 120 as well as an outlier in the high values.")
st.write("Data visualization after filtering the dataset on the continent of Europe :")
st.write(df_eur.describe())

#Histogram Ex
st.header("Example : Horsepower Histogram in Europe")
plt.figure()
sns.distplot(df_eur["hp"])
plt.title("Histogram")
st.pyplot()
