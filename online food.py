import streamlit as st
import pandas as pd
import pymysql

df = pd.read_csv(r"C:\Users\Bhuvaneswari\Downloads\Python\ONINE_FOOD_DELIVERY_ANALYSIS.csv")
st.title("online food delivery dashboard")  
total_orders = len(df)
total_revenue = df["Final_Amount"].sum()
avg_order_value = df["Final_Amount"].mean()
avg_delivery_time = df["Delivery_Time_Min"].mean()
avg_delivery_rating = df["Delivery_Rating"].mean()
profit_margin = df["Profit_Margin"].mean()

cancelled = df[df["Order_Status"] == "Cancelled"]
cancellation_rate = (len(cancelled) / total_orders) * 100

st.write("Total Orders:", total_orders)
st.write("Total Revenue:", total_revenue)
st.write("Average Order Value:", avg_order_value)
st.write("Average Delivery Time:", avg_delivery_time)
st.write("Cancellation Rate:", cancellation_rate)
st.write("Average Delivery Rating:", avg_delivery_rating)
st.write("Profit Margin %:", profit_margin)

