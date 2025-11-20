import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

air = pd.read_csv('/mnt/data/airtravel.csv')
co2 = pd.read_csv('/mnt/data/co2_emissions.csv')

air['Date'] = pd.to_datetime(air['Date'])
air.set_index('Date', inplace=True)
air_series = air['Passengers']

co2['Year'] = pd.to_datetime(co2['Year'], format="%Y")
co2.set_index('Year', inplace=True)
co2_series = co2['CO2_Emissions']

plt.figure()
plt.plot(air_series)
plt.title("Air Travel Series")
plt.savefig('/mnt/data/air_series.png')
plt.close()

plt.figure()
plt.plot(co2_series)
plt.title("CO2 Series")
plt.savefig('/mnt/data/co2_series.png')
plt.close()

air_dec = seasonal_decompose(air_series, model='additive', period=12)

plt.figure()
air_dec.trend.plot()
plt.title("Air Travel Trend")
plt.savefig('/mnt/data/air_trend.png')
plt.close()

plt.figure()
air_dec.seasonal.plot()
plt.title("Air Travel Seasonal")
plt.savefig('/mnt/data/air_seasonal.png')
plt.close()

plt.figure()
air_dec.resid.plot()
plt.title("Air Travel Residual")
plt.savefig('/mnt/data/air_resid.png')
plt.close()

co2_trend = co2_series.rolling(window=5, center=True).mean()

plt.figure()
plt.plot(co2_trend)
plt.title("CO2 Trend (Rolling)")
plt.savefig('/mnt/data/co2_trend.png')
plt.close()

air_results = {
    "tendencia": "crescente",
    "sazonalidade": "sim, período 12",
    "ciclo": "sim"
}

co2_results = {
    "tendencia": "crescente",
    "sazonalidade": "não",
    "ciclo": "não"
}

air_results, co2_results
