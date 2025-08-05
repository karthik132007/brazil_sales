import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('cleaned.csv')
background_color = '#0E1117'
text_color = '#FAFAFA'
bar_color = '#FF4B4B'
# pie chart for payment type
def payment_type_pie(df):
    payment_counts = df['payment_type'].value_counts()

    # Define custom colors (make the first one your primary)
    custom_colors = ['#FF4B4B', '#FAFAFA', '#262730', '#888888']

    # Create figure with dark background
    fig, ax = plt.subplots(facecolor='#0E1117')  # Outer figure background
    wedges, texts, autotexts = ax.pie(
        payment_counts,
        labels=payment_counts.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=custom_colors[:len(payment_counts)]  # Limit colors to number of slices
    )

    # Make the pie itself circular
    ax.axis('equal')  

    # Set title with light-colored text
    ax.set_title('Payment Type Distribution', color='#FAFAFA', fontsize=14)

    # Customize text labels (slice labels + percentage)
    for text in texts:
        text.set_color('#FAFAFA')
    for autotext in autotexts:
        autotext.set_color('#FAFAFA')

    # Add legend with white text
    ax.legend(labels=payment_counts.index, loc='best', facecolor='#262730', labelcolor='#FAFAFA')

    return fig

# Review distribution bar chart 
def review_distribution_bar(df):
    reviews = df['review_category'].value_counts()

    # Set dark theme colors
 

    # Create figure and axes with dark background
    fig, ax = plt.subplots(facecolor=background_color)
    ax.set_facecolor('#262730')  # Inner plot area background

    # Plot bars
    ax.bar(reviews.index, reviews, color=bar_color)

    # Titles and labels
    ax.set_title("Review Distribution", color=text_color, fontsize=14)
    ax.set_xlabel("Review Category", color=text_color)
    ax.set_ylabel("Count", color=text_color)

    # Make ticks readable
    ax.tick_params(colors=text_color)

    # Rotate x labels if needed
    plt.setp(ax.get_xticklabels(), rotation=15, ha='right')

    return fig

def monthly_sales_line():
    df['order_purchase_timestamp']=pd.to_datetime(df['order_purchase_timestamp'])
    df['month']=df['order_purchase_timestamp'].dt.month_name()
    month_count=df['month'].value_counts()
    month_order = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

    month_count.index = month_count.index.str.strip().str.title()
    month_count = month_count.loc[month_order]
    fig, ax = plt.subplots(facecolor=background_color)
    ax.plot(month_count.index,month_count.values,color=bar_color)
    ax.set_title("Mothly sales",color=text_color)
    ax.set_xlabel("Months",color=text_color)
    ax.set_ylabel("Values",color=text_color)
    ax.tick_params(colors=text_color)
    plt.setp(ax.get_xticklabels(), rotation=15, ha='right')
    return fig
