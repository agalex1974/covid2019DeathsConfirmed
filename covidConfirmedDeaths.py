import pandas as pd
import matplotlib.pyplot as plt

country = 'Brazil'

dfConfirmed = pd.read_csv("https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
dfDeaths = pd.read_csv("https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")

dfnew = dfDeaths.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
        var_name="Date",
        value_name="Deaths")
dfnew['Date'] = pd.to_datetime(dfnew['Date'])

dfCountryDeath = dfnew[dfnew['Country/Region']==country]

dfnew = dfConfirmed.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
        var_name="Date",
        value_name="Confirmed")
dfnew['Date'] = pd.to_datetime(dfnew['Date'])

dfCountryConfirmed = dfnew[dfnew['Country/Region']==country]

dfCountryConfirmed.set_index('Date', inplace= True)
dfCountryDeath.set_index('Date', inplace= True)

plt.style.use('ggplot')
dfCountryDeath.plot(y='Deaths', label='Deaths by Covid in ' + country)
dfCountryConfirmed.plot(y='Confirmed', label='Confirmed cases of Covid-19 in ' + country)
plt.show()
