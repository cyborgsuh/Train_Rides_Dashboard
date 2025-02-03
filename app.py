import streamlit as st
import streamlit_themes as st_theme
st_theme.set_preset_theme('Sandy')#Tropical,Sandy,Midnight

Home=st.Page('pages/home.py',title='Main Page',icon=':material/home:')
Visulization=st.Page('pages/Visualization.py',title='Visualization',icon=':material/analytics:')
Model=st.Page('pages/Model.py',title='Model',icon=':material/insights:')

pg=st.navigation(
{       
        "Home":[Home],
        "Visualization":[Visulization],
        "Price Prediction":[Model],
}
)
pg.run()