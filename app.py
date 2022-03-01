import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import plotly.express as px
from sklearn import datasets
import time

st.set_page_config(layout="wide")
st.title("""ANALYSIS OF CHANGES IN FOOD PRICES IN KENYA
GROUP 3 PRESENTATION
""")
st.header("Collaborators")
st.text("""
Eltonjohn Oketch
Kiprop Amos
Rehema Owino
Jane Ngala
Lydya Obare
Mary Njuguna
""")
st.header("Introduction")
st.text("""
The market through supply and demand, is the main arbiter 
of how the available food is distributed within a country.
Food price volatility informs consumers and price analysts the availability 
of food in a given region. Surges in food prices reduce the purchasing power 
of households that are weakly linked to the markets and thus pose a 
challenge when endeavoring to adequately feed the poor. 
This leads the poor to limit their food consumption and shift to even 
less balanced diets with harmful effects on health.
This research finds that food price volatility is caused by a number of
factors such as the supply and demand, climatic changes, population explosion,
inflation rates, government subsidies and the current trends including pandemics,
calamities,war and natural disasters.

""")

#climate
st.subheader("Annual Rainfall")
column_left, column_right = st.columns(2)
with column_left:
    df = pd.read_csv("D:\group3\group3\climate.csv")
    df = df.rename(columns={'year': 'index'}).set_index('index')
    chart_data = pd.DataFrame(df, columns=["annual_rainfall"])
    st.bar_chart(chart_data)

with column_right:
    st.subheader("Description")
    st.write("""
    This bar graph shows the rainfall patterns since 2006 till 2020.
    The values of rainfall are averages per year.
    """)

# #food_produced_percapita
st.subheader("food_produced_percapita")
column_left, column_right = st.columns(2)
with column_left:
    df1 = pd.read_csv("food.csv")
    df1 = df1.rename(columns={'year': 'index'}).set_index('index')
    st.bar_chart(df1)

with column_right:
    st.subheader("Description")
    st.write("""
    This bar graph shows the food productio per capita since 2006.
    
    
    """)

#CPI
st.subheader("CPI")
column_left, column_right = st.columns(2)
with column_left:
    df2 = pd.read_csv("D:\group3\group3\cpi.csv")
    df2 = df2.rename(columns={'year': 'index'}).set_index('index')
    st.bar_chart(df2)

with column_right:
    st.subheader("Description")
    st.write("""
    This bar graph shows the CPI trend from 2006 to 2020.
    The CPI is the overall caltulation of inflation.
    """)

# # #Commodity Prices since 2004
# st.subheader("Commodity Prices since 2004")
# column_left, column_right = st.columns(2)
# with column_left:
#     df3 = pd.read_csv("D:\group3\group3\commodity_prices.csv")

#     st.write(df3.head())

# with column_right:
#     st.subheader("Description")
#     st.write("""
#     This line graph shows the relationship between
#     GDP growth per year
#     """)
# GDP_Growth
st.subheader("GDP_Growth")
column_left, column_right = st.columns(2)
with column_left:
    # st.write("GDP_Growth")
    df_gdp_growth = pd.read_csv("gdp_growth.csv")
    df_gdp = df_gdp_growth.rename(columns={'year': 'index'}).set_index('index')
    st.bar_chart(df_gdp)

with column_right:
    st.subheader("Description")
    st.write("""
    This bar graph shows the GDP growth patterns since 2006 to 2020.
    """)
#Project Analysis
st.subheader("Analysis of food price fluctuation")
column_left, column_right = st.columns(2)
with column_left:
    df_maize = pd.read_csv("maize_data.csv")
    df_maize = df_maize.rename(columns={'year': 'index'}).set_index('index')
    chart_data = pd.DataFrame(df_maize, columns=["price of maize"])
    st.line_chart(df_maize)

with column_right:
    st.subheader("Description")
    st.write("""
    This line graph shows the overall food fluctuation.
    This analysis was important because maize is the most consumed product.
    """)

# #Price_Rainfall
st.subheader("Price_Rainfall")
column_left, column_right = st.columns(2)
with column_left:
    df_rain = pd.read_csv("rainfall_price.csv")
    df_rains = df_rain.rename(columns={'year': 'index'}).set_index('index')
    st.write("Line_chart")
    st.line_chart(df_rains)

with column_right:
    st.subheader("Description")
    st.write("""
    This line graph provides the contrast between the changes of
    prices and rainfall. From the line graph the price price patterns have 
    an inverse relationship with the rainfall patterns.
    """)

# Economic_growth_price
st.subheader("Economic_growth_price")
column_left, column_right = st.columns(2)
with column_left:

    df_economy = pd.read_csv("economic_growth_price.csv")
    df_economic = df_economy.rename(columns={
        'year': 'index'
    }).set_index('index')
    st.write("Line_chart")
    st.line_chart(df_economic)

with column_right:
    st.subheader("Description")
    st.write("""
    This line graph provides a contrast between economic growth pattern
    and average commodity price changes.
    """)
# Economic_growth_price
# st.subheader("Comparision ")
# column_left, column_right = st.columns(2)
# with column_left:

#     df_comodity = pd.read_csv("commodity_prices.csv")
#     df_comodities = df_comodity.rename(columns={
#         'year': 'index'
#     }).set_index('index')
#     st.write("Line_chart")
#     st.line_chart(df_comodities)

# with column_right:
#     st.subheader("Description")
#     st.write("""
#     This line graphs compare the price changes of different commodities over time
#     """)
# #Sidebar

#
# st.sidebar.button("hello")
st.sidebar.selectbox("MENU", [
    "Home", "Annual Rainfall", "Food Produced", "CPI", "GDP Growth",
    "Analysis", "Prices vs rainfall", "Economic Growth", "Conclusion",
    "Recommendation"
])
#Conclusion
st.header("Conclusion")
st.text("""
The study concludes that the food price crisis 
and food insecurity are a reality in Kenya and necessary interventions 
are required to deal with it. 


""")
#Recommendation
st.header("Recommendation")
st.text("""
Inflation was proportional to price fluctuations, we therefore recommend 
the Government of Kenya to use wage and price controls to regulate inflation.
Maize is hit the worst when there is inflation, therefore, 
we recommend that the Consumer Authority of Kenya ensures 
maize production is maximized throughout the Year to reduce chances of hoarding or 
adverse fluctuation of prices. 
Price was seen to fluctuate most when levels of rainfall were low, 
we recommend the Government of Kenya to put in place alternative 
water resources such as the irrigation schemes to sustain productivity 
throughout the year.

""")
