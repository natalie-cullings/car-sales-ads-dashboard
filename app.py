# load libraries
import pandas as pd
import numpy as np
import nbformat as nbf
import matplotlib.pyplot as plt
import plotly_express as px
import streamlit as st

# load data
df = pd.read_csv('./csv_files/vehicles_us_cleaned.csv', parse_dates=['date_posted'])

# Define the desired column order
column_order = ['make', 'model', 'type', 'model_year', 'price', 'odometer', 'condition', 'paint_color', 'cylinders', 'fuel', 'transmission', 'date_posted', 'days_listed']

# Reindex the DataFrame with the desired column order
df = df.reindex(columns=column_order)

# Rename the columns for better readability
df.columns = ['Make', 'Model', 'Type', 'Model Year', 'Price', 'Odometer', 'Condition', 'Paint Color', 'Cylinders', 'Fuel', 'Transmission', 'Date Posted', 'Days Listed']

# Provide a header to indicate the introduction of the dashboard
st.header('Dashboard for Exploring Vehicle Sales Ads Data', anchor='intro')

# Let user know the checkbox filters the data
st.write('Dashboard Filters:')

# Create a checkbox for filtering based on is_new
is_new = st.checkbox('Display New Vehicles Only', value=False)

# Filter the DataFrame based on the is_new checkbox
if is_new:
    df = df[df['Condition'] == 'New']
else:
    df = df

# Create a multiselect for filtering based on vehicle make
make = st.multiselect('Select Make:', df['Make'].unique())

# Filter the DataFrame based on the make multiselect
if make:
    df = df[df['Make'].isin(make)]
else:
    df = df


# Introduce the graphs section
st.write('Graphs', anchor='graphs')    

# create a scatter plot of price by model year using plotly.express
fig = px.scatter(df, 
                 x='Model Year', 
                 y='Price', 
                 color='Condition',
                 title='Price by Model Year'
                 )


# Plot the price by 'Model Year' scatterplot via streamlit
st.plotly_chart(fig, use_container_width=True)

# Plot a histogram of 'Model Year'
fig_my = px.histogram(df, 
                   x='Model Year', 
                   title='Histogram of Model Year',
                   labels={'count': 'Count'}
                  )

# update the x-axis range to start from 1950 and end at the maximum model year
# fig.update_xaxes(range=[1980,max(df['model_year'])])

# update the y-axis title
fig_my.update_yaxes(title_text='Number of Listings')

# Plot the histogram of model_year via streamlit
st.plotly_chart(fig_my, use_container_width=True)

# Provide a header to indicate the data table follows
st.header('Data Table', anchor='data-table')

# Remove commas from display in st.write(df)
df['Model Year'] = df['Model Year'].astype(str)
df['Model Year'] = df['Model Year'].str.replace(',', '')

# Remove the timestamp part of the date_posted column
df['Date Posted'] = df['Date Posted'].dt.date

# Display the DataFrame
st.write(df)


