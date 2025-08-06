import streamlit as st
import pandas as pd
from helper import payment_type_pie, review_distribution_bar, monthly_sales_line, sales_by_state, top_catageries,scatter_plot,regression_plot,get_state_level_data, price_map, freight_map,load_brazil_geojson,globe_freight_map,freight_price_weight_3d
import plotly.express as px

# Load Data
df = pd.read_csv('cleaned.csv')
df10 = df

# Preprocess for monthly sales
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['month'] = df['order_purchase_timestamp'].dt.month_name()
month_count = df['month'].value_counts()
month_order = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
month_count.index = month_count.index.str.strip().str.title()
month_count = month_count.loc[month_order]

# Sidebar - Personal Info
st.sidebar.title("Karthikeya Kumar")
st.sidebar.write("~Aspiring AI/ML Comrade")
st.sidebar.write("A 2nd year B.Tech student with a passion for AI/ML")
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Connect with Me")
st.sidebar.markdown("""
[![GitHub](https://img.shields.io/badge/-GitHub-black?logo=github&style=flat-square)](https://github.com/your-username)  
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin&style=flat-square)](https://www.linkedin.com/in/karthikeya2k7)  
""", unsafe_allow_html=True)

# Main Title
st.title("📊 Sales Dashboard")
st.write("Sales in Brazil during 2017 - 2018")

# Tabs
tab1, tab2 ,tab3= st.tabs(['Sales Overview', 'Advanced Visuals','Sales Prediction'])

with tab1:
    st.header("Sales Summary")
    st.write("📋 Sample of Cleaned Dataset")
    st.dataframe(df10)

    st.markdown("<br>", unsafe_allow_html=True)
    with st.container(border=True):
        st.plotly_chart(monthly_sales_line(df), use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h4 style='text-align: center; color: white;'>Payment Type</h4>", unsafe_allow_html=True)
        st.plotly_chart(payment_type_pie(df), use_container_width=True)

    with col2:
        st.markdown("<h4 style='text-align: center; color: white;'>Sales by State</h4>", unsafe_allow_html=True)
        st.plotly_chart(sales_by_state(df), use_container_width=True)
    with st.container(border=True):
        st.markdown("<h4 style='text-align: center; color: white;'>Top Product Categories</h4>", unsafe_allow_html=True)
        st.plotly_chart(top_catageries(df), use_container_width=True)
with tab2:
    st.header("📈 Advanced Visuals & Insights")
    st.write("""
        Dive deeper into customer behavior and delivery performance.
        Explore how delivery time affects review scores, and spot patterns in customer satisfaction.
    """)
    
    st.plotly_chart(scatter_plot(df))
    df['customer_state'] = df['customer_state'].str.upper()
    state_data = get_state_level_data(df)
    brazil_geojson = load_brazil_geojson()
    col1, col2 = st.columns(2)
    # for feature in brazil_geojson['features']:
    #             print(feature['properties'])
    #             break  # just look at one for now
    # print(state_data['state'].unique())

    with col1:
        st.markdown("<h4 style='text-align: center; color: white;'>Average price by State</h4>", unsafe_allow_html=True)
        st.plotly_chart(price_map(state_data, brazil_geojson), use_container_width=True)

    with col2:
            st.markdown("<h4 style='text-align: center; color: white;'>Average Fright Value by State</h4>", unsafe_allow_html=True)
            
            st.plotly_chart(freight_map(state_data, brazil_geojson), use_container_width=True)
            #print(state_data['state'].unique())
            brazil_geojson = load_brazil_geojson()
    with st.container(border=True):
        with col1:
            st.subheader("3D Globe View")
            st.write("Explore freight costs across Brazil in a 3D-ish globe view.")
            st.plotly_chart(globe_freight_map(df), use_container_width=True)
        with col2:
            st.subheader("3D Scatter Plot")
            st.write("Hover to see product-wise freight, price, and weight.")
            st.plotly_chart(freight_price_weight_3d(df), use_container_width=True)       

with tab3:
    st.header("🚧 Sales Prediction Coming Soon...")
    st.info("This section is under construction. Stay tuned for more insights 🚀")