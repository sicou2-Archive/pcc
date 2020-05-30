import matplotlib.pyplot as plt

x_values_5 = range(1, 6)
y_values_5 = [x**3 for x in x_values_5]

x_values_5000 = range(1, 5001)
y_values_5000 = [x**3 for x in x_values_5000]

plt.style.use('bmh')
fig, (ax_1, ax_2) = plt.subplots(1, 2)
ax_1.plot(x_values_5, y_values_5, c='Red', linewidth=5)
# fig, ax_2 = plt.subplots()
ax_2.scatter(x_values_5000, y_values_5000,
             c=y_values_5000, cmap=plt.cm.Reds, s=5)

# Set chart title and label axes.
ax_1.set_title("Cube Numbers", fontsize=24)
ax_1.set_xlabel("Value", fontsize=14)
ax_1.set_ylabel("Cube of Value", fontsize=14)

ax_2.set_title("Cube Numbers", fontsize=24)
ax_2.set_xlabel("Value", fontsize=14)
ax_2.set_ylabel("Cube of Value", fontsize=14)


ax_1.tick_params(axis='both', labelsize=14)
ax_2.tick_params(axis='both', labelsize=14)

plt.show()
