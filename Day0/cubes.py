import matplotlib.pyplot as plt
import matplotlib.cm as cm

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=cm.Blues, s=10)

# set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set siza of tick labels.
ax.tick_params(labelsize=14)

plt.savefig("colored_cubes5000.png", bbox_inches="tight")
# plt.show()
