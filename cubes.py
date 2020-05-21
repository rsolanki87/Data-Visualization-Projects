import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolor='none', s=40)

# Set title and label axes.
plt.title("Cubed Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Set the range for the axes.
plt.axis([0, 5100, 0, 125100000000])

plt.show()
