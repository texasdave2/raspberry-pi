import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("stock_data_log.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['percent_gain'] = df['percent_gain'].astype(float)

pivot_df = df.pivot(index='timestamp', columns='ticker', values='percent_gain')

plt.figure(figsize=(12, 6))
for ticker in pivot_df.columns:
    plt.plot(pivot_df.index, pivot_df[ticker], marker='o', label=ticker)

plt.title("Stock Percent Gain Over Time")
plt.xlabel("Time")
plt.ylabel("Percent Gain")
plt.legend(title="Ticker")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.savefig("stock_percent_gain_timeseries.png")
plt.show()

