
import pandas as pd

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
    filter_XY = filter_df[["Y", "X"]]
    filter_XY.rename(columns={"Y": "lon", "X": "lat"}, inplace=True)

    return filter_XY, filter_df 
