import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title='US Futures Margin Lookup',
    page_icon='🇺🇸'
)

url = "https://docs.google.com/spreadsheets/d/1Pmjl2XfifK1DjX9r_lT6ZCYGMSNr9wYlZ7Is6uC071s/edit?usp=sharing"

conn = st.experimental_connection("gsheet", type=GSheetsConnection)
futures = conn.read(spreadsheet=url)


"# 🇺🇸 US Futures Margin Lookup"
"(Based on 7/21/2023 data)"

futures_selection = st.selectbox("Pick a futures contract", futures['Futures'].to_list())

b0, b1 = st.columns(2)
b0.metric(label="Initial Margin", value=futures[futures['Futures'] == futures_selection]['Initial Margin'].iloc[0])
b1.metric(label="Maintain Margin", value=futures[futures['Futures'] == futures_selection]['Maintain Margin'].iloc[0])

