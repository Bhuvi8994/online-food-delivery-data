import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Bhuvaneswari\Downloads\Python\ONINE_FOOD_DELIVERY_ANALYSIS.csv")

st.title("🍔 Online Food Delivery Dashboard")


total_orders = len(df)
total_revenue = df['Order_Value'].sum()
avg_order_value = df['Order_Value'].mean()
avg_delivery_time = df['Delivery_Time_Min'].mean()
cancellation_rate = (df['Order_Status'] == 'Cancelled').mean() * 100
avg_rating = df['Delivery_Rating'].mean()


col1, col2, col3 = st.columns(3)

col1.metric("Total Orders", total_orders)
col2.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col3.metric("Average Order Value", f"₹{avg_order_value:.2f}")

col4, col5, col6 = st.columns(3)

col4.metric("Average Delivery Time", f"{avg_delivery_time:.1f} mins")
col5.metric("Cancellation Rate", f"{cancellation_rate:.1f}%")
col6.metric("Average Delivery Rating", f"{avg_rating:.2f} ⭐")


st.subheader("Orders by City")

city_orders = df['City'].value_counts()

fig1, ax1 = plt.subplots()
ax1.bar(city_orders.index, city_orders.values)
ax1.set_ylabel("Number of Orders")
ax1.set_xlabel("City")

st.pyplot(fig1)



st.subheader("Monthly Revenue Trend")

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.month

monthly_revenue = df.groupby('Month')['Order_Value'].sum()

fig2, ax2 = plt.subplots()
ax2.plot(monthly_revenue.index, monthly_revenue.values, marker='o')
ax2.set_xlabel("Month")
ax2.set_ylabel("Revenue")

st.pyplot(fig2)


st.subheader("Delivery Time Distribution")

fig3, ax3 = plt.subplots()
ax3.hist(df['Delivery_Time_Min'], bins=6)
ax3.set_xlabel("Delivery Time (mins)")
ax3.set_ylabel("Number of Orders")

st.pyplot(fig3)

st.subheader("Payment Mode Distribution")

payment = df['Payment_Mode'].value_counts()

fig5, ax5 = plt.subplots()
ax5.pie(payment.values, labels=payment.index, autopct='%1.1f%%')
ax5.set_title("Payment Mode")

st.pyplot(fig5)

st.subheader("Order Value Distribution")

fig4, ax4 = plt.subplots()
ax4.hist(df['Order_Value'], bins=10)
ax4.set_xlabel("Order Value")
ax4.set_ylabel("Frequency")
ax4.set_title("Order Value Distribution")

st.pyplot(fig4)

st.subheader("Cuisine Popularity")

cuisine = df['Cuisine_Type'].value_counts()

fig2, ax2 = plt.subplots()
ax2.bar(cuisine.index, cuisine.values)
ax2.set_xlabel("Cuisine Type")
ax2.set_ylabel("Orders")
ax2.set_title("Popular Cuisines")

st.subheader("Distance vs Delivery Time")

fig3, ax3 = plt.subplots()
ax3.scatter(df['Distance_km'], df['Delivery_Time_Min'])
ax3.set_xlabel("Distance (km)")
ax3.set_ylabel("Delivery Time (Min)")
ax3.set_title("Distance vs Delivery Time")

st.pyplot(fig3)