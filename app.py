# load libraries
import pandas as pd
import numpy as np
import nbformat as nbf
import matplotlib.pyplot as plt
import plotly_express as px
import streamlit as st

# load data
df = pd.read_csv('csv_files/vehicles_us.csv', parse_dates=['date_posted'])

st.header('Dashboard for Exploring Vehicle Sales Ads Data', anchor='intro')

# Let user know the checkbox filters the data
st.write('Dashboard Filters:')

# Create a checkbox for filtering based on is_new
is_new = st.checkbox('Display New Vehicles Only', value=False)

# Filter the DataFrame based on the is_new checkbox
if is_new:
    filtered_df = df[df['condition'] == True]
else:
    filtered_df = df

# create a scatter plot of price by model year using plotly.express
fig = px.scatter(filtered_df, 
                 x='model_year', 
                 y='price', 
                 color='condition',
                 title='Price by Model Year',
                 labels={'model_year': 'Model Year', 'price': 'Price', 'condition': 'Condition'}
                 )


# Plot the price by model_year scatterplot via streamlit
st.plotly_chart(fig, use_container_width=True)

# Plot a histogram of model_year
fig_my = px.histogram(filtered_df, 
                   x='model_year', 
                   title='Histogram of Model Year',
                   labels={'model_year': 'Model Year', 'count': 'Count'}
                  )

# update the x-axis range to start from 1950 and end at the maximum model year
# fig.update_xaxes(range=[1980,max(df['model_year'])])

# update the y-axis title
fig_my.update_yaxes(title_text='Number of Listings')

# Plot the histogram of model_year via streamlit
st.plotly_chart(fig_my, use_container_width=True)

# Provide a header to indicate the data table follows
st.header('Data Table', anchor='data-table')

# Display the filtered DataFrame
st.write(filtered_df)
