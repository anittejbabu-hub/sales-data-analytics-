import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv("data/sales.csv")

st.title("Retail Sales Analytics Dashboard")

category_sales = data.groupby("Category")["Sales"].sum().reset_index()

fig = px.bar(category_sales, x="Category", y="Sales", title="Sales by Category")

st.plotly_chart(fig)