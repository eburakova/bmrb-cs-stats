import streamlit as st
from src import make_charts

st.title("Bio NMR chemical shifts statistics")
st.write(
    """Whether you are setting up NMR experiments, processing or assigning bio NMR spectra, 
it is very helpful to know what signals to expect. With this app you always have the chemical shift statistics at hand!"""
)

st.write("The app is currently only available for proteins")

data_url = 'https://bmrb.io/ref_info/csstats.php?restype=aa&set=full&output=csv'

st.link_button(label='Source data from BMRB', url=data_url)




