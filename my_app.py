import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown('Mein **_Stadtbaum_ Hamburg**:palm_tree: :evergreen_tree: :deciduous_tree:')

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

    return filter_df

baume_df = load_data()



# options = st.selectbox(
#      'wähle deine Kategorien',
#       baume_df.sorte_deutsch.unique() )

selction_baum = st.selectbox("Select a Tree species", baume_df.art_latein.unique().tolist())
selection_df = baume_df.loc[(baume_df["art_latein"] == selction_baum)]

st.write('You selected:', selction_baum)

plt.figure(figsize=(8,8)) # Adjust plot width and height in inches
ax = sns.countplot(x = "bezirk" , data = selection_df)
plt.title("Neighborhood distribution") # Provides the title

st.pyplot(plt,use_container_width=True)
