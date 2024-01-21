import matplotlib.pyplot as plt
from pathlib import Path
import csv
from datetime import datetime

path4 = Path("weather_data/death_valley_2021_full.csv")
lines4 = path4.read_text().splitlines()

reader4 = csv.reader(lines4)
header_row4 = next(reader4)

dates5, rainfall2 = [], []

for row in reader4:
    prcp_index = header_row4.index("PRCP")
    date_index = header_row4.index("DATE")
    current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
    try:
        prcp = float(row[prcp_index])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates5.append(current_date)
        rainfall2.append(prcp)

# Plot the dailyd rainfall.
plt.style.use("classic")
fig4, ax4 = plt.subplots()
ax4.plot(dates5, rainfall2, color="red")

# Format Plot.
ax4.set_title("Daily Rainfall Amounts, Death Valley, 2021.", fontsize=20)
ax4.set_xlabel("", fontsize=16)
fig4.autofmt_xdate()
ax4.set_ylabel("PRCP", fontsize=16)
ax4.tick_params(labelsize=16)

plt.show()
