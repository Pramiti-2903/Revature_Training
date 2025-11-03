
import matplotlib.pyplot as plt

'''
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a line plot
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()




# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 10]

# Create a bar plot
plt.bar(categories, values, color='skyblue')
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Sales")
plt.show()



# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a scatter plot
plt.scatter(x, y, color='red')
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

'''
#Customizing Plots (Titles, Labels, Legends)

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

# Create a plot with customizations
plt.plot(x, y1, marker='o', label='Series 1', color='blue')
plt.plot(x, y2, marker='x', label='Series 2', color='green')

# Customizing the plot
plt.title("Customized Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()



