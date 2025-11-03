"""
# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# First subplot
ax1.plot(x, y1, color='blue', label='Sine')
ax1.set_title('Sine Function')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')
ax1.legend()

# Second subplot
ax2.plot(x, y2, color='red', label='Cosine')
ax2.set_title('Cosine Function')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.legend()

# Show the plots
plt.tight_layout()
plt.show()



# Sample data
data = np.random.randn(100)

# Create a figure with a histogram and a density plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Histogram
ax1.hist(data, bins=10, color='skyblue', edgecolor='black')
ax1.set_title('Histogram')
ax1.set_xlabel('Value')
ax1.set_ylabel('Frequency')

# Density plot
#ax2.hist(data, bins=10, density=True, color='skyblue', edgecolor='black', alpha=0.6)
data_density = np.linspace(min(data), max(data), 100)
ax2.plot(data_density, (1/(np.sqrt(2 * np.pi))) * np.exp(-0.5 * (data_density)**2), color='red')
ax2.set_title('Density Plot')
ax2.set_xlabel('Value')
ax2.set_ylabel('Density')

# Show the plots
plt.tight_layout()
plt.show()

"""
import numpy as np

# Sample data
data1 = np.random.normal(1, 10, 10)
data2 = np.random.normal(10, 20, 10)
data = [data1, data2]
print(data)

# Create a figure with a box plot and a violin plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Box plot
ax1.boxplot(data, patch_artist=True)
ax1.set_title('Box Plot')
ax1.set_xlabel('Data Sets')
ax1.set_ylabel('Value')

# Violin plot
ax2.violinplot(data, showmeans=False, showmedians=True)
ax2.set_title('Violin Plot')
ax2.set_xlabel('Data Sets')
ax2.set_ylabel('Value')

# Show the plots
plt.tight_layout()
plt.show()
