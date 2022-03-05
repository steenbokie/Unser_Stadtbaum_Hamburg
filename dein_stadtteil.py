
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

        st.header("Dein Baum :deciduous_tree:")
        st.markdown("**Abfragetool: Welcher Baum steht in deiner Straße, bei deiner Hausnummer?   :wrench: :mailbox_with_mail: :house_with_garden:**")


        # the previous solution was pronoe to typos,
        # now the user can start typing a street from the available in the DF
        street_list = baume_df.strasse.unique().tolist() # get list of streets
        street = st.selectbox('Gibt einen Straßennamen ein:', street_list)
        st.write('Die gewählte Straße ist: ', street)

        # create a DF for the selected street and get the list of available 
        # house numbers
        street_df = baume_df[
            baume_df["strasse"]== street]
        streetnumb_list = street_df.hausnummer.unique().tolist()

        number =  st.selectbox('Gibt einen einen Hausnummer ein:', streetnumb_list)

        # create a DF filtering with the street number combo
        # I engourage you to learn more about filtering with pandas it's :fire:
        selected_baum_df = baume_df[(
            baume_df["strasse"]== street) & (
                baume_df["hausnummer"]== number)]

        # get the final list of trees for the given adress
        trees_list = str(selected_baum_df.art_deutsch.unique().tolist())
        # TODO: join* this list into a more beautiful string

        # print the final message with string formating 
        st.markdown(f'''Deine Bäume in **{street} {number}**:
          {trees_list}''')
        # TODO: show this info more beautiful with markdown or any other approach :) 
