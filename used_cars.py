import altair as alt
import pandas as pd
import streamlit as st

st.header('Used Cars')
st.subheader('Streamlit App')


@st.cache_data()
def get_data():
    df = pd.read_csv('used_cars.csv')
    sample = df.sample(n=2000, random_state=1)
    return sample


sample = get_data()


st.markdown("### Data Preview")
st.dataframe(sample.head())


st.markdown("### Plot")
xvar = st.radio('X-Axis', options=['age', 'kilometer'])

s = alt.selection_point(fields=['vehicleType'], bind='legend')

fig = alt.Chart(sample).add_selection(s).mark_circle().encode(
    x=alt.X(xvar),
    y=alt.Y('price'),
    color=alt.condition(s, 'vehicleType', alt.value('lightgrey'))
)


st.altair_chart(fig, use_container_width=True)
