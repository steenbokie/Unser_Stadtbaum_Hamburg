import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('**Mein Stadtbaum in Hamburg**            :deciduous_tree:')

with open('startseite.md') as f:
    startseite = f.read()

def load_data():

        data_baume = pd.read_csv('final_data_techlabs.csv', sep =';') #csv file einlesen und seperator angeben (hier semicolon, sonst komma)

        # in einer neuen Liste (mit inner list) sortieren wir die für uns wichtigen Spalten heraus
        filter_df = data_baume[['Y', 'X', 'art_latein', 'art_deutsch', 'sorte_deutsch', 'pflanzjahr', 'kronendurchmesser',
                    'stammumfang', 'strasse', 'hausnummer', 'stadtteil', 'bezirk']]

        filter_df.dropna(subset=['Y', 'X', 'art_latein', 'art_deutsch', 'stadtteil', 'bezirk'], inplace = True) #mit dropNA werden alle values bzw. deren Zeilen aussortiert, die 0 oder NA beinhalten

        # Fehler in den Bezirken ausbessern -> Eimsb??ttel wird zu Eimsbüttel
        filter_df.replace({'bezirk': 'Eimsb??ttel'}, 'Eimsbüttel',inplace =True)

        # Fehler in den Stadtteilen ausbessern -> ?? wird zu Ü
        filter_df['stadtteil'] = filter_df['stadtteil'].str.replace('??','ü',regex = False)

        # Leerzeichen in den Koordinaten entfernen
        filter_df['X'] = filter_df['X'].str.replace(' ','')
        filter_df['Y'] = filter_df['Y'].str.replace(' ','')

        # Fehler in sorte_deutsch ausbessern -> ?? wird zu individuell, siehe unten
        filter_df.replace({'sorte_deutsch': 'Holl??ndische-Linde'}, 'Holländische-Linde',inplace =True)
        filter_df.replace({'sorte_deutsch': 'Gemeine Esche, Gew??hnliche Esche'}, 'Gemeine Esche, Gewöhnliche Esche',inplace =True)
        filter_df.replace({'sorte_deutsch': 'F??chertanne, Ginkgo'}, 'Fächertanne, Ginkgo',inplace =True)
        filter_df.replace({'sorte_deutsch': 'Gemeine Hainbuche, Wei??buche'}, 'Gemeine Hainbuche, Weißbuche',inplace =True)
        filter_df.replace({'sorte_deutsch': 'Sp??ths Erle'}, 'Späths Erle',inplace =True)
        filter_df.replace({'sorte_deutsch': "Stra??en-Esche, Esche 'Westhof Glorie'"}, "Straßen-Esche, Esche 'Westhof Glorie'",inplace =True)
        filter_df.replace({'sorte_deutsch': "Einbl??ttrige Robinie, Schein-Akazie 'Monophylla'"}, "Einblättrige Robinie, Schein-Akazie 'Monophylla'",inplace =True)
        filter_df.sort_values(by='sorte_deutsch',ascending=True,inplace=True)
        #sorted(filter_df.art_deutsch.unique().tolist())

        return filter_df
baume_df = load_data() #call funktion here

rad =st.sidebar.radio("Navigation",["Startseite","Dein Stadtbaum","Dein Stadtteil","Deine Map","Dein Filter", "Deine Story"])

if rad == "Startseite": #verschiedene Sidebar Navigationspunkte und dessen Infos und funktionen
    #df = pd.DataFrame(data = data) # datenset definieren is not defined jet
    st.write("Hello You ") #text für die Seite
    st.markdown(startseite, unsafe_allow_html=False)

if rad == "Dein Stadtbaum": #verschiedene Sidebar Navigationspunkte und dessen Infos und funktionen
    #df = pd.DataFrame(data = data) # datenset definieren is not defined jet
    st.write("Entdecke welche Baumarten in Hamburgs Bezirken stehen ") #text für die Seite

    # options = st.selectbox(
    #      'wähle deine Kategorien',
    #       baume_df.sorte_deutsch.unique() )

    selction_baum = st.selectbox("Select a Tree species", baume_df.sorte_deutsch.unique().tolist())
    selection_df = baume_df.loc[(baume_df["sorte_deutsch"] == selction_baum)]

    st.write('You selected:', selction_baum)

    plt.figure(figsize=(8,8)) # Adjust plot width and height in inches
    ax = sns.countplot(x = "bezirk" , data = selection_df)
    plt.title("Neighborhood distribution") # Provides the title

    st.pyplot(plt,use_container_width=True)


if rad == "Deine Map":
        st.write("Schau dich in Hamburg um und entdecke viele tolle Baumarten")


if rad == "Dein Stadtteil":
                st.write("Wähle deine Daten aus und schau welch Baumarten sich in deiner gegend befinden")

                st.sidebar.selectbox("Wähle deinen Stadtteil", sorted(baume_df.stadtteil.unique().tolist()))

       #st.sidebar.selectbox.sort_values(by='Stadtteil',ascending=True, inplace=True)

if rad == "Dein Filter":
        st.write("Stelle dir dein ganz persönliches Datenset zusammen")

        options = st.multiselect(
     'Wähle deine Baumsorten',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
        options = st.multiselect(
        'Wähle deinen Stadtteil',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])



if rad == "Deine Story":
                text= st.sidebar.text_area("Erzähl uns deine Geschichte")
                st.write()
                button1 = st.sidebar.button("Text hinzufügen")
                if button1:
                    st.write(text)
