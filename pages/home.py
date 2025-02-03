import streamlit as st

# Title
st.title("Ticket Pricing Analysis and Prediction")

# Introduction
st.write("""
## Welcome to the Ticket Pricing Analysis App! 🎟️
This application is designed to analyze and predict train ticket prices using a real-world dataset. 
Through this app, you'll explore patterns in ticket purchases, journey details, delays, and pricing. 
Our goal is to provide actionable insights and accurate predictions using machine learning models.
""")

# Dataset Overview
st.write("""
## Dataset Overview 📊
This dataset contains detailed information about train ticket purchases, including transaction details, 
journey specifics, and passenger preferences. Below is a detailed description of the dataset's columns:

### Column Descriptions:
| **Field**                 | **Description** |
|---------------------------|-----------------|
| **Transaction ID**        | Unique identifier for an individual train ticket purchase. |
| **Date of Purchase**      | Date the ticket was purchased. |
| **Time of Purchase**      | Time the ticket was purchased. |
| **Purchase Type**         | Whether the ticket was purchased online or directly at a train station. |
| **Payment Method**        | Payment method used (Contactless, Credit Card, or Debit Card). |
| **Railcard**              | Whether the passenger is a National Railcard holder (Adult, Senior, Disabled, or None). Railcard holders get a 1/3 discount. |
| **Ticket Class**          | Seat class for the ticket (Standard or First). |
| **Ticket Type**           | Type of ticket: Advance (1/2 off, purchased a day prior), Off-Peak (1/4 off, used outside peak hours), or Anytime (full price). |
| **Price**                 | Final cost of the ticket. |
| **Departure Station**     | Station to board the train. |
| **Arrival Destination**   | Station to exit the train. |
| **Date of Journey**       | Date the train departed. |
| **Departure Time**        | Time the train departed. |
| **Arrival Time**          | Scheduled arrival time (can be on the day after departure). |
| **Actual Arrival Time**   | Actual arrival time (can be on the day after departure). |
| **Journey Status**        | Whether the train was on time, delayed, or cancelled. |
| **Reason for Delay**      | Reason for the delay or cancellation. |
| **Refund Request**        | Whether the passenger requested a refund after a delay or cancellation. |

### Key Highlights:
- **Total Records**: This dataset includes detailed records of ticket purchases, providing ample data for analysis and modeling.
- **Categorical and Numerical Data**: Columns like payment methods, ticket types, and journey status are categorical, while price and ticket class are numerical.
- **Target Variable**: The primary focus is to predict the **Price** of tickets based on other features.

""")

# App Navigation
st.write("""
## How to Navigate the App 🚀
1. **Visualizations**: Explore patterns and relationships between features (e.g., journey duration vs. price).
2. **Correlations**: Discover feature correlations using heatmaps and analyze embeddings.
3. **Predictions**: Use our machine learning models to predict ticket prices.
4. **Delay Analysis**: Analyze the impact of delays and cancellations on ticket prices and refunds.

---

We hope this app helps you uncover valuable insights. Feel free to provide feedback or share suggestions! 😊
""")
