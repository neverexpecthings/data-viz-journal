import matplotlib.pyplot as plt
from pathlib import Path
import csv
from datetime import datetime

path2 = Path("weather_data/death_valley_2021_simple.csv")
lines2 = path2.read_text().splitlines()

reader2 = csv.reader(lines2)
header_row2 = next(reader2)

dates2, highs2, lows2 = [], [], []

for row in reader2:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high2 = int(row[3])
        low2 = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates2.append(current_date)
        highs2.append(high2)
        lows2.append(low2)

#  Plot the high and low temperature.
plt.style.use("classic")
fig2, ax2 = plt.subplots()
ax2.plot(dates2, highs2, color="red", alpha=0.5)
ax2.plot(dates2, lows2, color="blue", alpha=0.5)
ax2.fill_between(dates2, highs2, lows2, facecolor="blue", alpha=0.1)

# Format plot.
title = "Daily High and Low Temperatures, 2021\nDeath Valey, CA"
ax2.set_title(title, fontsize=20)
ax2.set_xlabel("", fontsize=16)
fig2.autofmt_xdate()
ax2.set_ylabel("Temperature (F)", fontsize=16)
ax2.tick_params(labelsize=16)

plt.show()
