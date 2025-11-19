#Por meio dos datasets airtravel.csv e co2_emissions.csv, trace suas
#Séries Temporais.
#Em seguida, para cada uma das Séries, realize a sua decomposição e
#responda as seguintes perguntas:
#a. A série possui Tendência? Se sim, que tipo?
#b. A série possui Sazonalidade? Se sim, qual o período que ela acontece?
#c. A série apresenta um Ciclo? Se sim, por qual razão?

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

dAirtravel = pd.read_csv('Cap-7/Data/airtravel.csv',delimiter=',',index_col='Date', parse_dates=['Date'])
dAirtravel = dAirtravel.sort_index()
decomposition = seasonal_decompose(dAirtravel['Passengers'], period=12, model='additive')
decomposition.plot()
plt.show()

#a. A série possui Tendência? Se sim, que tipo?
# Sim, tendência de aumento.
#b. A série possui Sazonalidade? Se sim, qual o período que ela acontece?
# Sim, sazonalidade de 12 meses, picos em Julho-Agosto e mínimas em Janeiro-Fevereiro
#c. A série apresenta um Ciclo? Se sim, por qual razão?
# Não, a variação é dominada pela tendência e pela sazonalidade.

dEmissions = pd.read_csv('Cap-7/Data/co2_emissions.csv',delimiter=',')
dEmissions['Date'] = pd.to_datetime(dEmissions['Year'], format='%Y')
dEmissions = dEmissions.set_index('Date')

decompositionEm = seasonal_decompose(dEmissions['CO2_Emissions'],model='additive',period=10)
decompositionEm.plot()
plt.show()

#a. A série possui Tendência? Se sim, que tipo?
# Sim, tendência de queda de 1990 até 2020.
#b. A série possui Sazonalidade? Se sim, qual o período que ela acontece?
# Não possui Sazonalidade pois emissões de CO2 não variam sazonalmente.
#c. A série apresenta um Ciclo? Se sim, por qual razão?
# Sim, oscilações plurianuais que podem ser explicadas por ciclos econômicos