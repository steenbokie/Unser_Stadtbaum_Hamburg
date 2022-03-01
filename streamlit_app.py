# app2.py

import startseite
import dein_stadtteil
import deine_plots
import dein_stadtbaum
import streamlit as st
from streamlit_option_menu import option_menu



PAGES = {
    "Startseite": startseite,
    "Dein Stadtbaum": dein_stadtbaum,
    "Dein Stadtteil": dein_stadtteil,
    "Deine Analyse": deine_plots



    }

with st.sidebar:
         selected = option_menu("Menü", ['Startseite', 'Dein Stadtbaum','Dein Stadtteil', 'Deine Analyse'],
             icons=['house', 'tree', 'circle', 'sun'], menu_icon="cast", default_index=1)
         selected

pages = PAGES[selected]
pages.app()
