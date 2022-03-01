
import streamlit as st
import pandas as pd
import folium
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_folium import folium_static
from load_data import load_data


def app():


    st.title('**Dein Stadtbaum in Hamburg**            :deciduous_tree:')
    st.header('Deine Baumsorten    :leaves:')
    baume_df = load_data()[1]

    #Selectbox für Artenverteilung über Bezirke
    st.write("Entdecke welche Baumsorten in Hamburgs Bezirken stehen") #text für die Seite

    selection_baum = st.selectbox("Wähle eine Baumsorte", baume_df.sorte_deutsch.unique().tolist(), index=4)
    selection_df1 = baume_df.loc[(baume_df["sorte_deutsch"] == selection_baum)]

    st.write('Dir wird folgende Baumsorte angezeigt:', selection_baum)

    plt.figure(figsize=(8,8)) # Adjust plot width and height in inches
    ax = sns.countplot(x = "bezirk" , data = selection_df1)
    plt.title("Verteilung der gewählten Baumsorte über die Bezirke") # Provides the title

    st.pyplot(plt,use_container_width=True)

    #------------------------------------------------------------------------------------------------------------------------------------
    #Selectbox für Älteste Bäume in Bezirke
    st.header('Deine Top Ten    :fallen_leaf:')
    st.markdown("Die 10 ältesten Bäume in deinem Stadtteil   ")

    selection_stteil = st.selectbox("Wähle deinen Stadtteil", baume_df.stadtteil.unique().tolist())
    selection_df2= baume_df.loc[(baume_df["stadtteil"] == selection_stteil)]

    st.write('Dein gewählter Stadtteil:', selection_stteil)

    #largest 10
    map_df = selection_df2.nlargest(10, 'alter')


#--------------------------------------------------------------------------------------------------------------------
#Map of Hamburg

#st.map(filter_XY)
    with st.echo():

        m = folium.Map(location=[53.529518, 9.847574], zoom_start=11) # initiate map

        #sampled_df = map_df.sample(100) # use a small sample to not overload memory

        tooltip = "Click me!" # add label
        for c, row in map_df.iterrows():    # use sampled_df here if sample is used above
            if row["X"] and row["Y"]:# if both lat and lon are found add them to the map
        #         mapit = folium.Map( location=[coord[0], coord[1]])
                folium.Marker(
            [row["X"], row["Y"]], popup=f"{row['art_deutsch']}, Pflanzjahr: {row['pflanzjahr']}, Alter des Baumes: {row['alter']}", tooltip=tooltip,).add_to(m)
            else: # add exception for entries with misisng lat or lon
                continue


        # call to render Folium map in Streamlit
        folium_static(m)
