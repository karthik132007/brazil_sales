import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import requests
# Load your data
df = pd.read_csv('cleaned.csv')

# Dark theme color setup
background_color = '#0E1117'
text_color = '#FAFAFA'
bar_color = '#FF4B4B'

#  Interactive Pie Chart – Payment Type
def payment_type_pie(df):
    payment_counts = df['payment_type'].value_counts().reset_index()
    payment_counts.columns = ['payment_type', 'count']

    fig = px.pie(
        payment_counts,
        names='payment_type',
        values='count',
        title=' ',
        color_discrete_sequence=['#FF4B4B', '#FAFAFA', '#262730', '#888888']
    )

    fig.update_layout(
        paper_bgcolor=background_color,
        plot_bgcolor=background_color,
        font_color=text_color,
        title_font_color=text_color,
        legend_title_font_color=text_color,
        legend=dict(bgcolor='#262730'),
    )

    return fig


# Interactive Bar Chart – Review Distribution
def review_distribution_bar(df):
    reviews = df['review_category'].value_counts().reset_index()
    reviews.columns = ['review_category', 'count']

    fig = px.bar(
        reviews,
        x='review_category',
        y='count',
        title=' ',
        color_discrete_sequence=[bar_color]
    )

    fig.update_layout(
        paper_bgcolor=background_color,
        plot_bgcolor='#262730',
        font_color=text_color,
        xaxis_title='Review Category',
        yaxis_title='Count',
        title_font_color=text_color,
    )

    return fig


# Interactive Line Chart – Monthly Sales
def monthly_sales_line(df):
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['month'] = df['order_purchase_timestamp'].dt.month_name()
    month_order = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]

    month_count = df['month'].value_counts().reindex(month_order).fillna(0).astype(int)
    month_df = pd.DataFrame({
        'month': month_count.index,
        'orders': month_count.values
    })

    fig = px.line(
        month_df,
        x='month',
        y='orders',
        title='Monthly Sales',
        markers=True,
        line_shape='linear'
    )

    fig.update_layout(
        paper_bgcolor=background_color,
        plot_bgcolor=background_color,
        font_color=text_color,
        xaxis_title='Month',
        yaxis_title='Number of Orders',
        title_font_color=text_color,
    )

    return fig

def sales_by_state(df):
    # Count and select top 10 states
    customer_state = df['customer_state_full'].value_counts().head(10).reset_index()
    customer_state.columns = ['state', 'sales']

# Plotly bar chart (horizontal)
    fig = px.bar(
        customer_state,
        x='sales',
        y='state',
        orientation='h',
        #title='Sales by Customer State',
        color='sales',  # Optional: adds gradient color based on value
        color_continuous_scale='Reds'
    )

    fig.update_layout(
        yaxis=dict(autorange="reversed"),  # So highest is at the top
        plot_bgcolor="#0E1117",  # Optional dark background
        paper_bgcolor="#0E1117",
        font_color="#FAFAFA"
    )
    return fig

def top_catageries(df):
    top_categories = df['product_category_name'].value_counts().head(10).reset_index()
    top_categories.columns = ['category', 'count']

    fig = px.treemap(
    top_categories,
    path=['category'],
    values='count',
    title='Top 10 Most Bought Product Categories',
    subtitle='In Portuguese'
    )

    fig.update_layout(
    paper_bgcolor='#0E1117',
    plot_bgcolor='#0E1117',
    font_color='#FAFAFA',
    title_font_color='#FAFAFA'
    )
    return fig

def scatter_plot(df):
    scatter_fig = px.scatter(
    df,
    x='product_volume',
    y='freight_value',
    color='review_category',
    title='Freight Value vs Product Volume',
    labels={'product_volume': 'Product Volume (cm³)', 'freight_value': 'Freight Cost (R$)'},
        opacity=0.6
    )
    return scatter_fig;
def regression_plot(df):
    df_filtered = df[(df['product_weight_g'] < 5000) & (df['price'] < 2000)]
    fig = px.scatter(
    df_filtered,
    x='product_weight_g',
    y='price',
    trendline='ols',
    labels={'product_weight_g': 'Weight (g)', 'price': 'Price (R$)'}
)
    fig.update_layout(template='plotly_dark')
    return fig
# helper.py

def load_brazil_geojson():
    url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
    response = requests.get(url)
    return response.json()

def get_state_level_data(df):
    """Group data by customer state and compute average price and freight"""
    state_data = df.groupby('customer_state')[['price', 'freight_value']].mean().reset_index()
    state_data.columns = ['state', 'avg_price', 'avg_freight']
    return state_data

import plotly.express as px

def price_map(state_data, geojson):
    fig = px.choropleth(
        state_data,
        geojson=geojson,
        locations='state',            # column in your df
        featureidkey='properties.sigla',  # field in geojson
        color='avg_price',            # metric to color
        color_continuous_scale='Viridis',
        scope='south america'         # optional
    )
    fig.update_layout(
    paper_bgcolor="#0E1117",  # background of the whole chart
    plot_bgcolor="#0E1117",   # background of the plotting area
    geo=dict(
        bgcolor="#0E1117"     # background of the map region
    ),
    font_color="white"        # optional: keep text visible on dark
)

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig


def freight_map(state_data, geojson):
    fig = px.choropleth(
        state_data,
        geojson=geojson,
        locations='state',

        featureidkey='properties.sigla',
        color='avg_freight',
        color_continuous_scale='Blues',
        scope='south america'
    )
    fig.update_layout(
    paper_bgcolor="#0E1117",  # background of the whole chart
    plot_bgcolor="#0E1117",   # background of the plotting area
    geo=dict(
        bgcolor="#0E1117"     # background of the map region
    ),
    font_color="white"        # optional: keep text visible on dark
)

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

import plotly.graph_objects as go

def globe_freight_map(df):
    # Manually mapping Brazilian state codes to approximate lat/lon
    state_coords = {
        'AC': [-8.77, -70.55],
        'AL': [-9.71, -35.73],
        'AM': [-3.07, -60.02],
        'AP': [1.41, -51.77],
        'BA': [-12.97, -38.50],
        'CE': [-3.72, -38.54],
        'DF': [-15.83, -47.86],
        'ES': [-19.19, -40.34],
        'GO': [-16.64, -49.31],
        'MA': [-2.55, -44.30],
        'MG': [-19.92, -43.94],
        'MS': [-20.51, -54.54],
        'MT': [-12.64, -55.42],
        'PA': [-1.46, -48.49],
        'PB': [-7.06, -35.55],
        'PE': [-8.28, -35.07],
        'PI': [-8.28, -43.68],
        'PR': [-25.43, -49.27],
        'RJ': [-22.91, -43.17],
        'RN': [-5.81, -36.59],
        'RO': [-11.22, -62.80],
        'RR': [1.89, -61.22],
        'RS': [-30.03, -51.23],
        'SC': [-27.59, -48.55],
        'SE': [-10.90, -37.07],
        'SP': [-23.55, -46.63],
        'TO': [-10.25, -48.25]
    }

    # Grouping freight value by customer state
    state_data = df.groupby('customer_state')['freight_value'].mean().reset_index()
    state_data['lat'] = state_data['customer_state'].map(lambda x: state_coords.get(x, [None])[0])
    state_data['lon'] = state_data['customer_state'].map(lambda x: state_coords.get(x, [None])[1])

    fig = go.Figure()

    fig.add_trace(go.Scattergeo(
        lon=state_data['lon'],
        lat=state_data['lat'],
        text=state_data['customer_state'] + "<br>Avg Freight: R$" + state_data['freight_value'].round(2).astype(str),
        mode='markers',
        marker=dict(
            size=9,
            color=state_data['freight_value'],
            colorscale='Viridis',
            colorbar_title="Freight (R$)",
            line=dict(width=0)
        )
    ))

    fig.update_geos(
        projection_type="orthographic",
        showland=True, landcolor="rgb(10, 10, 10)",
        oceancolor="rgb(40, 40, 80)",
        showocean=True,
        bgcolor="#0E1117"
    )

    fig.update_layout(
        paper_bgcolor="#0E1117",
        plot_bgcolor="#0E1117",
        font_color="white",
        margin={"r":0,"t":30,"l":0,"b":0},
        title_text='3D Globe View: Freight Cost by Customer State',
        title_font_color='white'
    )

    return fig


def freight_price_weight_3d(df):
    # Drop rows with NaNs to avoid plot glitches
    df = df.dropna(subset=['freight_value', 'price', 'product_weight_g'])

    fig = go.Figure(data=[go.Scatter3d(
        x=df['price'],
        y=df['freight_value'],
        z=df['product_weight_g'],
        text=None,
        mode='markers',
        marker=dict(
            size=4,
            color=df['freight_value'],  # Color by freight
            colorscale='Inferno',
            opacity=0.8,
            colorbar=dict(title='Freight (R$)')
        )
    )])

    fig.update_layout(
        title='3D Plot: Price vs Freight vs Weight',
        scene=dict(
            xaxis_title='Price (R$)',
            yaxis_title='Freight Value (R$)',
            zaxis_title='Weight (g)',
            bgcolor="#0E1117"
        ),
        paper_bgcolor="#0E1117",
        plot_bgcolor="#0E1117",
        font_color="white",
        margin=dict(l=0, r=0, b=0, t=30)
    )

    return fig
