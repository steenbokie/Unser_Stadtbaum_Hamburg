
from load_data import load_data
import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium
import matplotlib.pyplot as plt
import seaborn as sns



def app():

    baume_df = load_data()[1]

    with st.echo():

#-------------------------------------------------------------------------------------------------------
#Map classic
        st.title('**Dein Stadtteil in Hamburg**            :deciduous_tree:')
        st.header("**Deine interaktive Map   :earth_africa:**")


        st.write("Schau dich in Hamburg um und entdecke viele tolle Baumarten")
        original_text = '<p style="color:red">Wenn du auf die Symbole auf der Map klickst, kannst du die Details zu deinem Baum sehen</p>'
        st.markdown(original_text,unsafe_allow_html=True)

    #Map of Hamburg

    #st.map(filter_XY)

        m = folium.Map(location=[53.529518, 9.847574], zoom_start=11) # initiate map

        sampled_df = baume_df.sample(500) # use a small sample to not overload memory

        tooltip = "Click me!" # add label
        for c, row in sampled_df.iterrows():    # use sampled_df here if sample is used above
            if row["X"] and row["Y"]:# if both lat and lon are found add them to the map
        #         mapit = folium.Map( location=[coord[0], coord[1]])
                folium.Marker(
            [row["X"], row["Y"]], popup=f"{row['art_deutsch']}, Pflanzjahr: {row['pflanzjahr']}, Alter des Baumes: {row['alter']}", tooltip=tooltip,).add_to(m)
            else: # add exception for entries with misisng lat or lon
                continue


        # call to render Folium map in Streamlit
        folium_static(m)

#-------------------------------------------------------------------------------------------------------
            #Tool zur Abfrage der Bäume für Straße

        st.header("Deine Baum :deciduous_tree:")
        st.markdown("**Abfragetool: Welcher Baum steht in deiner Straße, bei deiner Hausnummer?   :wrench: :mailbox_with_mail: :house_with_garden:**")

        street = st.text_input('Straße', 'Hafenstraße')
        st.write('Die gewählte Straße ist: ', street)

        number = st.number_input('Hausnummer', step=1)
        st.write('Die gewählte Hausnummer ist: ', number)


        for street in baume_df.strasse:
             print(baume_df['sorte_deutsch'][street], df['alter'][street])

        #     {row['art_deutsch']}, Pflanzjahr: {row['pflanzjahr']}, Alter des Baumes: {row['alter']}
