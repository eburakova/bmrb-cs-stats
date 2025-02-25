import streamlit as st
from src.make_charts import make_chart
from src import colors, constants
import pandas as pd

st.title("Bio NMR chemical shifts statistics")
st.write(
    """Whether you are setting up NMR experiments, processing or assigning bio NMR spectra, 
it is very helpful to know what signals to expect. With this app you always have the chemical shift statistics at hand!"""
)

st.header("Chart explanation")
st.markdown("""
* The center of each box is the average chemical shift. 
* The width of each box is 3 STD of the chemicalshift distribution.""")

st.markdown("> *The app is currently only available for proteins*")

data_url = 'https://bmrb.io/ref_info/csstats.php?restype=aa&set=full&output=csv'

st.link_button(label='Source data from BMRB', url=data_url)

nucleus = st.selectbox(label='Select nucleus', options=["13C", "15N", "1H"])

df = pd.read_csv(data_url)
df['lower'] = df['avg'] - 1.5*df['std']
df['higher'] = df['avg'] + 1.5*df['std']


colors_nuclei = {
    '1H': colors.color_Hs,
    '13C': colors.color_Cs,
    '15N': colors.color_Ns,
}

color_dict = colors_nuclei[nucleus]

df_nucl = df.loc[df['atom_id'].isin(color_dict.keys()), ['comp_id', 'atom_id', 'lower', 'higher']]

fig = make_chart(df_nucl, color_dict, 
                 leg_title=nucleus,
                 x_range=constants.ppm_ranges[nucleus])

st.plotly_chart(fig)


