import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page title
st.title("Data Analysis Dashboard: Sellers and Payments")
st.write("Nama: Moch Hikmal Abrar")
st.write("Email: m134b4ky2516@bangkit.academy")

# File uploader for sellers dataset
sellers_file = st.file_uploader("Upload Sellers Dataset (CSV)", type="csv")
payments_file = st.file_uploader("Upload Payments Dataset (CSV)", type="csv")

if sellers_file is not None and payments_file is not None:
    # Load datasets
    sellers_df = pd.read_csv(sellers_file)
    payments_df = pd.read_csv(payments_file)

    # Sidebar for dataset information
    st.sidebar.header("Dataset Information")
    st.sidebar.write(f"Sellers dataset has {sellers_df.shape[0]} rows and {sellers_df.shape[1]} columns")
    st.sidebar.write(f"Payments dataset has {payments_df.shape[0]} rows and {payments_df.shape[1]} columns")

    # Show datasets
    st.subheader("Sellers Dataset")
    st.write(sellers_df.head())

    st.subheader("Payments Dataset")
    st.write(payments_df.head())

    # Top 10 cities with most sellers
    st.subheader("Top 10 Cities with Most Sellers")
    city_counts = sellers_df['seller_city'].value_counts().reset_index()
    city_counts.columns = ['seller_city', 'num_sellers']
    top_cities = city_counts.head(10)
    st.write(top_cities)

    # Plot top 10 cities with most sellers
    fig, ax = plt.subplots()
    ax.bar(top_cities['seller_city'], top_cities['num_sellers'], color='skyblue')
    ax.set_title('Top 10 Cities with the Most Sellers')
    ax.set_xlabel('City')
    ax.set_ylabel('Number of Sellers')
    ax.set_xticks(range(len(top_cities['seller_city'])))
    ax.set_xticklabels(top_cities['seller_city'], rotation=45)
    st.pyplot(fig)

    # Payment method usage percentage
    st.subheader("Payment Method Usage Percentage")
    payment_counts = payments_df['payment_type'].value_counts().reset_index()
    payment_counts.columns = ['payment_type', 'count']
    st.write(payment_counts)

    # Calculate percentage of each payment method
    payment_percentage = (payment_counts['count'] / payment_counts['count'].sum()) * 100
    payment_percentage = pd.DataFrame({'payment_type': payment_counts['payment_type'], 'percentage': payment_percentage})

    # Plot payment method percentage
    fig, ax = plt.subplots()
    sns.barplot(data=payment_percentage, x='payment_type', y='percentage', palette='viridis', ax=ax)
    ax.set_title('Payment Method Usage by Percentage')
    ax.set_xlabel('Payment Type')
    ax.set_ylabel('Percentage (%)')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Pie chart for payment method distribution
    fig, ax = plt.subplots()
    ax.pie(payment_percentage['percentage'], labels=payment_percentage['payment_type'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("viridis", len(payment_percentage)))
    ax.set_title('Payment Method Distribution')
    st.pyplot(fig)
else:
    st.warning("Please upload both Sellers and Payments datasets.")