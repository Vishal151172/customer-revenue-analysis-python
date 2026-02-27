
# Customer Repeat Purchase & Revenue Analysis
# Created by Vishal Sharma


import pandas as pd
import matplotlib.pyplot as plt

print("Project Started Successfully")

# Creating retail dataset

data = {
    "order_id": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    "customer_name": ["Rahul","Priya","Rahul","Amit","Sneha","Rahul","Priya","Sneha","Amit","Arjun"],
    "order_date": ["2023-06-01","2023-06-05","2023-07-10","2023-07-12","2023-08-01",
                   "2023-08-15","2023-09-01","2023-09-05","2023-09-20","2023-10-01"],
    "order_value": [55000,20000,8000,1500,55000,2000,25000,7000,3000,12000]
}

df = pd.DataFrame(data)

print("\nDataset Preview:\n")
print(df)


# Calculating Total Revenue


total_revenue = df["order_value"].sum()

print("\nTotal Revenue:", total_revenue)


# Counting Orders Per Customer

order_counts = df.groupby("customer_name")["order_id"].count()

print("\nOrders Per Customer:\n")
print(order_counts)



# Identifying Repeat Customers

repeat_customers = order_counts[order_counts > 1].index

print("\nRepeat Customer List:\n")
print(repeat_customers)

# Revenue from Repeat Customers

repeat_revenue = df[df["customer_name"].isin(repeat_customers)]["order_value"].sum()

print("\nRevenue from Repeat Customers:", repeat_revenue)


# Revenue from New Customers

new_revenue = df[~df["customer_name"].isin(repeat_customers)]["order_value"].sum()

print("Revenue from New Customers:", new_revenue)


print("\nCheck Full Data:\n")
print(df)

print(df["order_value"].sum())


# Calculating Average Order Value (AOV)

total_orders = len(df)
average_order_value = total_revenue / total_orders

print("\nTotal Orders:", total_orders)
print("Average Order Value:", round(average_order_value, 2))


# Average Order Value for Repeat Customers

repeat_df = df[df["customer_name"].isin(repeat_customers)]
repeat_aov = repeat_df["order_value"].mean()

# Average Order Value for New Customers

new_df = df[~df["customer_name"].isin(repeat_customers)]
new_aov = new_df["order_value"].mean()

print("\nRepeat Customer AOV:", round(repeat_aov, 2))
print("New Customer AOV:", round(new_aov, 2))




# Comparing AOV using Bar Chart

labels = ["Repeat Customers", "New Customers"]
values = [repeat_aov, new_aov]

plt.figure()
plt.bar(labels, values)
plt.title("Average Order Value Comparison")
plt.ylabel("Average Order Value")
plt.xlabel("Customer Type")

plt.show()