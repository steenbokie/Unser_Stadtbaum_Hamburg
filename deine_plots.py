# app2.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import PIL
from streamlit_folium import folium_static
import folium

from load_data import load_data

#st.map(filter_XY)
#Map classic



def app():
    baume_df = load_data()[1]

    st.title('**Deine Analysen in Hamburg**            :deciduous_tree:')
    #Map of Hamburg
    #interactive plots with plotly

    st.header("**Interaktionsplots   :chart_with_upwards_trend: :chart_with_downwards_trend:**")

    import plotly.express as px

    fig = px.scatter(data_frame = baume_df, x="alter", y="kronendurchmesser", color="sorte_deutsch", range_x = [-30,350], range_y = [-5,35], labels = {"alter":"Alter [y]", "kronendurchmesser":"Kronendurchmesser [m]", "sorte_deutsch":"Sorte"})

    # Plot!
    st.plotly_chart(fig, use_container_width=False)

    #-------------------------------------------------------------------------------------------------------
    #box plot

    st.header("**Box Plots   :bar_chart:**")

    #Boxplots für Kronendurchmesser bei Baumarten – ein paar Arten herausfiltern -> wähle deine Lieblingsbaumarten

    #
    # plt.figure(figsize=(12, 5))  # Make the figure wider than default (12cm wide by 5cm tall)
    # sns.boxplot(x="bezirk", y="Alter", data=baume_df)  # Make boxplot of BPXSY1 stratified by age group

    import plotly.graph_objects as go

    fig2 = px.box(data_frame = baume_df, x="bezirk", y="kronendurchmesser", color="bezirk", labels = {"kronendurchmesser":"Kronendurchmesser [m]", "bezirk":"Bezirk"}) #"sex": "Payer Gender",  "day": "Day of Week"
    fig2.update_traces(boxpoints=False)

    st.plotly_chart(fig2, use_container_width=True)

    #-------------------------------------------------------------------------------------------------------
