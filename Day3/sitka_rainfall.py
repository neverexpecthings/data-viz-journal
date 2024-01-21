import matplotlib.pyplot as plt
from pathlib import Path
import csv
from datetime import datetime

path3 = Path("weather_data/sitka_weather_2021_full.csv")
lines3 = path3.read_text().splitlines()

reader3 = csv.reader(lines3)
header_row3 = next(reader3)

dates3, rainfall = [], []

for row in reader3:
    prcp_index = header_row3.index("PRCP")
    date_index = header_row3.index("DATE")
    current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
    try:
        prcp = float(row[prcp_index])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates3.append(current_date)
        rainfall.append(prcp)

# Plot the daily rainfall.
plt.style.use("classic")
fig3, ax3 = plt.subplots()
ax3.plot(dates3, rainfall, color="red")

# Format Plot.
ax3.set_title("Daily Rainfall Amounts, Sitka, 2021.", fontsize=20)
ax3.set_xlabel("", fontsize=16)
fig3.autofmt_xdate()
ax3.set_ylabel("PRCP", fontsize=16)
ax3.tick_params(labelsize=16)

plt.show()
