import streamlit as st
import pandas as pd
# pandas data frames 
df=pd.read_csv('cleaned.csv')
df10=df.head(10)
df10=df10.drop(columns='order_purchase_timestamp',axis=1)

# side bar for my info
st.sidebar.title("Karthikeya Kumar")
st.sidebar.write("~Aspring AI/ML Comrade")
st.sidebar.write("A 2nd year B.Tech student with a passion for AI/ML")
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Connect with Me")
st.sidebar.markdown("""
[![GitHub](https://img.shields.io/badge/-GitHub-black?logo=github&style=flat-square)](https://github.com/your-username)  
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin&style=flat-square)](www.linkedin.com/in/karthikeya2k7)  
""", unsafe_allow_html=True)

# main header
st.title("Sales Dashboard")
st.write("Sales in Brazile in year of 2017-2018")

# tabs
tab1,tab2=st.tabs(['Sales Overview','Advanced Visuals'])
with tab1:
    st.header("Sales Summary")
    st.write("Sample Table")
    st.dataframe(df10)
    
with tab2:
    st.header("Advanced Visuals")
