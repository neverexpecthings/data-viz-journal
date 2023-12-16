import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.scatter(2, 4, s=200)

# set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set siza of tick labels.
ax.tick_params(labelsize=14)

plt.show()
