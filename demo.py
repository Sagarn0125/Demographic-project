import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

st.set_page_config(page_title="Demographic Data Analysis", layout="wide")

st.title("🌍 Demographic Data Analysis Dashboard")

# Load data
df = pd.read_csv("DemographicData.xls")

# FIX: Arrow compatibility
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].astype(str)

# Preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Data types
st.subheader("Data Types")
st.write(df.dtypes)

# Summary
st.subheader("Statistical Summary")
st.write(df.describe())

# Missing values
st.subheader("Missing Values")
st.write(df.isnull().sum())

# Birth Rate Histogram
st.subheader("Birth Rate Distribution")
fig, ax = plt.subplots()
ax.hist(df['Birth rate'], bins=10)
ax.set_xlabel("Birth Rate")
ax.set_ylabel("Countries")
st.pyplot(fig)

# Internet Users Histogram
st.subheader("Internet Users Distribution")
fig, ax = plt.subplots()
ax.hist(df['Internet users'], bins=10)
ax.set_xlabel("Internet Users (%)")
ax.set_ylabel("Countries")
st.pyplot(fig)

# Scatter plot
st.subheader("Birth Rate vs Internet Users")
fig, ax = plt.subplots()
ax.scatter(df['Birth rate'], df['Internet users'], alpha=0.6)
ax.set_xlabel("Birth Rate")
ax.set_ylabel("Internet Users (%)")
st.pyplot(fig)

# Correlation
st.subheader("Correlation")
st.write(df['Birth rate'].corr(df['Internet users']))

# Income group comparison
high = df[df['Income Group'] == 'High income']['Internet users']
low = df[df['Income Group'] == 'Low income']['Internet users']

t_stat, p_val = ttest_ind(high, low, equal_var=False)

st.subheader("T-Test (High vs Low Income)")
st.write("t-statistic:", t_stat)
st.write("p-value:", p_val)
