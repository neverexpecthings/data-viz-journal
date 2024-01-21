import matplotlib.pyplot as plt
from pathlib import Path
import csv

path = Path("weather_data/sitka_weather_07-2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for i, column_header in enumerate(header_row):
#     print(i, column_header)

highs = [int(row[4]) for row in reader]

# Plot temps
plt.style.use("classic")
fig, ax = plt.subplots()
ax.plot(highs, color="red")

# Format plot.
ax.set_tittle("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
