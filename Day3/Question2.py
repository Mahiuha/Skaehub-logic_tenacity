#2.Write a Python program to create a plot (of lines) of 
# total deaths, confirmed, recovered and active cases 
# Country wise where deaths greater than 200

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import matplotlib.pyplot as plt

# 
data = pd.read_csv('covid_data.csv', usecols=["Country/Region", "Last Update", "Confirmed", "Deaths", "Recovered"])
print('Deaths')
print(data.loc[data['Deaths'] > 200])
print('Confirmed')
print(data.loc[data['Confirmed']>0])
print('REcovered')
print(data.loc[data['Recovered']>0])

#order_by_date = data.sort_values(by='Last Update')
#print(order_by_date)

# data.plot()
# plt.show()

#death_or_200 = order_by_date = data.sort_values(by='Last Update')
#print()



data= pd.read_csv('covid_data.csv', usecols = ['Last Update', 'Country/Region', 'Confirmed', 'Deaths', 'Recovered'])
data['Active'] = data['Confirmed'] - data['Deaths'] - data['Recovered']
 
result = data.groupby(["Country/Region"])["Deaths", "Confirmed", "Recovered", "Active"].sum().reset_index()
result = result.sort_values(by='Deaths', ascending=False)
result = result[result['Deaths']>200]


df = pd.DataFrame(result, columns = ("Country/Region", "Confirmed", "Deaths", "Recovered"))

fig, ax =plt.subplots(figsize=(12,5))
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')

pp = PdfPages("question2.pdf")
pp.savefig(fig, bbox_inches='tight')
pp.close()
plt.figure()
plt.plot(result['Country/Region'], result['Deaths'],color='red')
plt.plot(result['Country/Region'], result['Confirmed'],color='green')
plt.plot(result['Country/Region'], result['Recovered'], color='blue')
plt.plot(result['Country/Region'], result['Active'], color='black')
 
plt.title('Total Deaths(>200), Confirmed, Recovered and Active Cases by Country')
plt.show()


