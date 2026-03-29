data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.month

monthly_sales = data.groupby("Month")["Sales"].sum()

monthly_sales.plot(kind="line")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()