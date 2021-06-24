import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
#from __future__ import print_function

data = pd.read_csv('covid_data.csv', usecols=["Country/Region", "Last Update", "Confirmed", "Deaths", "Recovered"])

#result = data.groupby('Country/Region').sum().sort_values(by='Confirmed', ascending=False)(by='Last Update')[:20]


order_by_date = data.sort_values(by='Confirmed')
file_sort = data.sort_values(by='Confirmed', ascending=False)[:20]

result = order_by_date.groupby('Country/Region').max().sort_values(by='Confirmed', ascending=False)[:20]

result1 = order_by_date.groupby('Country/Region').sum().sort_values(by='Confirmed', ascending=False)[:20]


#print(result)

df = pd.concat([result, result1], axis=1)
print(df)


##generate pdf file

df = pd.DataFrame(file_sort, columns = ("Country/Region", "Last Update", "Confirmed", "Deaths", "Recovered"))

fig, ax =plt.subplots(figsize=(12,12))
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')

pp = PdfPages("question1.pdf")
pp.savefig(fig, bbox_inches='tight')
pp.close()