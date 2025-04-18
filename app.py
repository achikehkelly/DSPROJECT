import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('vehicles_us.csv')

# Clean out extreme values
df = df[(df['price'] > 1000) & (df['price'] < 100000) & 
        (df['odometer'] > 0) & (df['odometer'] < 300000)]

# Header
st.header(" Vehicle Market Explorer")

# Checkbox for filtering electric vehicles
show_electric = st.checkbox("Show only electric vehicles")

if show_electric:
    df = df[df["fuel"] == "electric"]

# Histogram of vehicle prices
fig1 = px.histogram(df, x="price", nbins=50, title="Distribution of Vehicle Prices")
st.plotly_chart(fig1)

# Scatter plot of price vs odometer
fig2 = px.scatter(df, x="odometer", y="price", color="condition",
                  title="Price vs. Odometer by Condition",
                  labels={"odometer": "Odometer (miles)", "price": "Price (USD)"})
st.plotly_chart(fig2)