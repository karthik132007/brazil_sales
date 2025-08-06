import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
    customer_state = df['customer_state'].value_counts().head(10).reset_index()
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

