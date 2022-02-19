import streamlit as st
import pandas as pd #pip install pandas
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import pyplot as plt #pip install matplotlib
import streamlit as st

plt.style.use("ggplot")

st.sidebar.header("Menü")

st.title('**Mein Stadtbaum Hamburg**            :deciduous_tree:')


rad =st.sidebar.radio("Navigation",["Startseite","Dein Stadtteil","Deine Map","Dein Filter", "Deine Story"])


if rad == "Startseite": #verschiedene Sidebar Navigationspunkte und dessen Infos und funktionen
    df = pd.DataFrame(data = data) # datenset definieren is not defined jet
    st.write("you are here in about us page") #text für die Seite





if rad == "Deine Map":
        st.write("Schau dich in Hamburg um und entdecke viele tolle Baumarten")






if rad == "Dein Stadtteil":
                st.write("Wähle deine Daten aus und schau welch Baumarten sich in deiner gegend befinden")

                st.sidebar.selectbox("Wähle deinen Stadtteil",['Finkenwerder', 'St.Pauli', 'Altona-Altstadt', 'Neustadt',
       'Hamburg-Altstadt', 'Rothenburgsort', 'HafenCity', 'St.Georg',
       'Kleiner Grasbrook', 'Hammerbrook', 'Veddel', 'Borgfelde', 'Hamm',
       'Billbrook', 'Horn', 'Billstedt', 'Moorfleet', 'Rotherbaum',
       'Wilhelmsburg', 'Billwerder', 'Rissen', 'Blankenese', 'Sülldorf',
       'Iserbrook', 'Nienstedten', 'Osdorf', 'Lurup', 'Othmarschen',
       'Groß Flottbek', 'Bahrenfeld', 'Ottensen', 'Altona-Nord',
       'Sternschanze', 'Eimsbüttel', 'Eidelstedt', 'Schnelsen',
       'Stellingen', 'Niendorf', 'Lokstedt', 'Hoheluft-West',
       'Harvestehude', 'Hoheluft-Ost', 'Eppendorf', 'Groß Borstel',
       'Alsterdorf', 'Winterhude', 'Langenhorn', 'Uhlenhorst',
       'Fuhlsbüttel', 'Hohenfelde', 'Ohlsdorf', 'Barmbek-Süd',
       'Barmbek-Nord', 'Dulsberg', 'Hummelsbüttel', 'Eilbek', 'Bramfeld',
       'Steilshoop', 'Marienthal', 'Poppenbüttel', 'Wandsbek',
       'Wellingsbüttel', 'Lemsahl-Mellingstedt', 'Duvenstedt',
       'Farmsen-Berne', 'Sasel', 'Jenfeld', 'Tonndorf', 'Bergstedt',
       'Wohldorf-Ohlstedt', 'Rahlstedt', 'Volksdorf', 'Ochsenwerder',
       'Spadenland', 'Tatenberg', 'Allermöhe', 'Kirchwerder', 'Lohbrügge',
       'Reitbrook', 'Neuengamme', 'Bergedorf', 'Neuallermöhe', 'Curslack',
       'Altengamme', 'Neuenfelde', 'Cranz', 'Neugraben-Fischbek',
       'Francop', 'Hausbruch', 'Heimfeld', 'Moorburg', 'Eißendorf',
       'Marmstorf', 'Sinstorf', 'Wilstorf', 'Harburg', 'Langenbek',
       'Rönneburg', 'Neuland', 'Gut Moor'])

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


    #add_selectbox = st.sidebar.selectbox(
    #    "Entdecke deine Stadt",
    #    ("Heatmap", "Wie grün ist dein Stadtteil?", "Baumarten")
    #)

    #add_selectbox = st.sidebar.selectbox(
    #    "Dein Wissen",
    #    ("Facts", "Wusstest du", "Dein kleines Wörterbuch")
    #)
