import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_folium import folium_static
import folium

#Überschrift und Beschreibung
st.markdown('Mein **_Stadtbaum_ Hamburg**:palm_tree: :evergreen_tree: :deciduous_tree:')

def load_data(): # define function here to call it later

    data_baume = pd.read_csv('SB_clean_coordinates.csv', sep =';') #csv file einlesen und seperator angeben (hier semicolon, sonst komma)

    # in einer neuen Liste (mit inner list) sortieren wir die für uns wichtigen Spalten heraus
    filter_df = data_baume[['Y', 'X', 'art_latein', 'art_deutsch', 'sorte_deutsch', 'pflanzjahr', 'kronendurchmesser',
                'stammumfang', 'strasse', 'hausnummer', 'stadtteil', 'bezirk', 'alter']]

    filter_df.dropna(subset=['Y', 'X', 'art_latein', 'art_deutsch', 'stadtteil', 'bezirk'], inplace = True) #mit dropNA werden alle values bzw. deren Zeilen aussortiert, die 0 oder NA beinhalten

    # Fehler in den Bezirken ausbessern -> Eimsb??ttel wird zu Eimsbüttel
    filter_df.replace({'bezirk': 'Eimsb??ttel'}, 'Eimsbüttel',inplace =True)

    # Fehler in den Stadtteilen ausbessern -> ?? wird zu Ü
    filter_df['stadtteil'] = filter_df['stadtteil'].str.replace('??','ü',regex = False)

    # Leerzeichen in den Koordinaten entfernen
#    filter_df['X'] = filter_df['X'].str.replace(' ','')
#    filter_df['Y'] = filter_df['Y'].str.replace(' ','')

    # Fehler in sorte_deutsch ausbessern -> ?? wird zu individuell, siehe unten
    filter_df.replace({'sorte_deutsch': 'Holl??ndische-Linde'}, 'Holländische-Linde',inplace =True)
    filter_df.replace({'sorte_deutsch': 'Gemeine Esche, Gew??hnliche Esche'}, 'Gemeine Esche, Gewöhnliche Esche',inplace =True)
    filter_df.replace({'sorte_deutsch': 'F??chertanne, Ginkgo'}, 'Fächertanne, Ginkgo',inplace =True)
    filter_df.replace({'sorte_deutsch': 'Gemeine Hainbuche, Wei??buche'}, 'Gemeine Hainbuche, Weißbuche',inplace =True)
    filter_df.replace({'sorte_deutsch': 'Sp??ths Erle'}, 'Späths Erle',inplace =True)
    filter_df.replace({'sorte_deutsch': "Stra??en-Esche, Esche 'Westhof Glorie'"}, "Straßen-Esche, Esche 'Westhof Glorie'",inplace =True)
    filter_df.replace({'sorte_deutsch': "Einbl??ttrige Robinie, Schein-Akazie 'Monophylla'"}, "Einblättrige Robinie, Schein-Akazie 'Monophylla'",inplace =True)
    filter_df.sort_values(by='sorte_deutsch', ascending=True, inplace=True)

#    filter_df.rename(columns={"Y": "lon", "X": "lat"}, inplace=True)
#    filter_df[["lon", "lat"]] = filter_df[["lon", "lat"]].apply(pd.to_numeric, errors='coerce', axis=1)

    return filter_df

baume_df = load_data()  # call function here

filter_XY = baume_df[["Y", "X"]]
filter_XY.rename(columns={"Y": "lon", "X": "lat"}, inplace=True)



#Selectbox für Artenverteilung über Bezirke


selection_baum = st.selectbox("Select a Tree species", baume_df.sorte_deutsch.unique().tolist(), index=4)
selection_df1 = baume_df.loc[(baume_df["sorte_deutsch"] == selection_baum)]

st.write('You selected:', selection_baum)

plt.figure(figsize=(8,8)) # Adjust plot width and height in inches
ax = sns.countplot(x = "bezirk" , data = selection_df1)
plt.title("Neighborhood distribution") # Provides the title

st.pyplot(plt,use_container_width=True)


#Selectbox für Älteste Bäume in Bezirke

selection_stteil = st.selectbox("Wähle deinen Stadtteil", baume_df.stadtteil.unique().tolist())
selection_df2= baume_df.loc[(baume_df["stadtteil"] == selection_stteil)]

st.write('You selected:', selection_stteil)

#largest 10
map_df = selection_df2.nlargest(10, 'alter')

#Map of Hamburg

#st.map(filter_XY)

with st.echo():
    import streamlit as st
    from streamlit_folium import folium_static
    import folium

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



#Tool zur Abfrage der Bäume für Straße


title = st.text_input('Straße', 'Hafenstraße')
st.write('Die gewählte Straße ist: ', title)

number = st.number_input('Hausnummer')
st.write('Die gewählte Hausnummer ist: ', number)
