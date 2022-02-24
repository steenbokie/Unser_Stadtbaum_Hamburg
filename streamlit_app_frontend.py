# Streamlit app frontend

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import PIL

from streamlit_option_menu import option_menu



st.title('**Mein Stadtbaum in Hamburg**            :deciduous_tree:')

with open('startseite.md') as f:
    startseite = f.read()
#picture ![Image_startseite](https://user-images.githubusercontent.com/93773591/154812307-9dece0db-b72d-466c-80c3-1d086f8a0978.jpg)
#-------------------------------------------------------------------------------------------------------
#load_data
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
#-------------------------------------------------------------------------------------------------------
#sidebar
#with st.sidebar:
#     selected = option_menu("Main Menu", ["Startseite", 'Dein Stadtbaum', 'Deine Map'],
#         icons=['house', 'tree', 'circle'], menu_icon="cast", default_index=1)
#     selected

rad =st.sidebar.radio("Navigation",["Startseite","Dein Stadtbaum","Dein Stadtteil","Deine Map","Entdecke Hamburg", "Deine Story"])

#-------------------------------------------------------------------------------------------------------
#sidebar_navigation
if rad == "Startseite": #verschiedene Sidebar Navigationspunkte und dessen Infos und funktionen
    #df = pd.DataFrame(data = data) # datenset definieren is not defined jet
    st.write("Herzlich Willkommen") #text für die Seite
    st.markdown(startseite, unsafe_allow_html=False)



#-------------------------------------------------------------------------------------------------------
#sidebar_options #Dein Stadtbaum

if rad == "Dein Stadtbaum": #verschiedene Sidebar Navigationspunkte und dessen Infos und funktionen
    #df = pd.DataFrame(data = data) # datenset definieren is not defined jet
    st.write("Entdecke welche Baumarten in Hamburgs Bezirken stehen: ") #text für die Seite

    # options = st.selectbox(
    #      'wähle deine Kategorien',
    #       baume_df.sorte_deutsch.unique() )

    selction_baum = st.selectbox("Wähle eine Baumart", baume_df.sorte_deutsch.unique().tolist())
    selection_df = baume_df.loc[(baume_df["sorte_deutsch"] == selction_baum)]



    plt.figure(figsize=(8,8)) # Adjust plot width and height in inches
    ax = sns.countplot(x = "bezirk" , data = selection_df)
    plt.title("Neighborhood distribution") # Provides the title

    st.pyplot(plt,use_container_width=True)
    st.write('Dir wird folgende Baumsorte angezeigt:',selction_baum)

#-------------------------------------------------------------------------------------------------------
#sidebar_options #Deine Map
if rad == "Deine Map":
        st.write("Schau dich in Hamburg um und entdecke viele tolle Baumarten")

        #Map classic

st.markdown("**Deine interaktive Map   :earth_africa:**")


st.write("Schau dich in Hamburg um und entdecke viele tolle Baumarten")
st.write("Wenn du auf die Symbole auf der Map klickst, kannst du die Deteils zu deinem Baum sehen.")

#Map of Hamburg

#st.map(filter_XY)

with st.echo():
    import streamlit as st
    from streamlit_folium import folium_static
    import folium

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
#sidebar_options #Dein Stadtteil
if rad == "Dein Stadtteil":
                st.write("Wähle deine Daten aus und finde heraus, welche Baumarten sich in deiner Gegend befinden")

                st.sidebar.selectbox("Wähle deinen Stadtteil", sorted(baume_df.stadtteil.unique().tolist()))

       #st.sidebar.selectbox.sort_values(by='Stadtteil',ascending=True, inplace=True)



#-------------------------------------------------------------------------------------------------------
#sidebar_options #Entdecke Hamburg

if rad == "Entdecke Hamburg":
        st.write("Stelle dir dein ganz persönliches Datenset zusammen")

        options = st.multiselect(
     'Wähle deine Baumsorten',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
        options = st.multiselect(
        'Wähle deinen Stadtteil',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])

#-------------------------------------------------------------------------------------------------------
#sidebar_options #Deine Story

if rad == "Deine Story":
                text= st.sidebar.text_area("Erzähl uns deine Geschichte")
                st.write()
                button1 = st.sidebar.button("Text hinzufügen")
                if button1:
                    st.write(text)
