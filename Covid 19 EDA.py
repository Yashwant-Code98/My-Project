import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

df = pd.read_csv('covid_19_india.csv',parse_dates=['Date'],dayfirst=True)
print(df.head())

# Data Pre-Processing !
df = df[['Date','Time','State/UnionTerritory','Cured','Deaths','Confirmed']]
df.columns=['date','time','state','cured','deaths','confirmed']
print(df.head())

print(df.tail())

today = df[df.date == '2020-12-09']
print(today.head())

max_confirmed = today.sort_values(by='confirmed',ascending=False)
print(max_confirmed.head())

top_state_confirmed = max_confirmed
print(top_state_confirmed.head())

# Data Visualization

sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state',y='confirmed',data=top_state_confirmed)
plt.show()

max_cured = today.sort_values(by='cured',ascending=False)
print(max_cured.head())

max_state_cured = max_cured
print(max_state_cured.head())

# Data Visualization
sns.set(rc={'figure.figsize':(8,5)})
sns.barplot(x='state',y='cured',data=max_state_cured,color='red')
plt.show()

max_deaths_confirmed = today.sort_values(by='deaths',ascending=False)
print(max_deaths_confirmed.head())

top_state_deaths = max_deaths_confirmed
print(top_state_deaths.head())

# Data Visualization

sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state',y='deaths',data=top_state_deaths,color='blue')
plt.show()

maha = df[df.state  ==  "Maharashtra"]
print(maha.head())

max_maha_confirmed = maha.sort_values(by='confirmed',ascending=False)
print(max_maha_confirmed.head())
# Max Confirmed Cases In Maharashtra
sns.set(rc={'figure.figsize':(8,5)})
sns.lineplot(x='date',y='confirmed',data=maha,linewidth=4,color='c')
plt.show()

# Max Cured Cases In Maharashtra
max_maha_cured = maha.sort_values(by='cured',ascending=False)
print(max_maha_cured.head())

sns.set(rc={'figure.figsize':(15,10)})
sns.histplot(x='date',y='cured',data=maha)
plt.show()

max_maha_deaths = maha.sort_values(by='deaths',ascending=False)
print(max_maha_deaths.head())

sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='deaths',data=maha,color='blue',linewidth=4)
plt.show()

kerala = df[df.state == "Kerala"]

max_confirmed = kerala.sort_values(by='confirmed',ascending=False)
print(max_confirmed.head())

sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='confirmed',data=kerala,linewidth=5,color='m')

max_cured = kerala.sort_values(by='cured',ascending=False)
print(max_cured.head())

sns.set(rc={'figure.figsize':(8,5)})
sns.lineplot(x='date',y='cured',data=kerala,color='red')

max_deaths = kerala.sort_values(by='deaths',ascending=False)
print(max_deaths.head())

sns.set({'figure.figsize':(15,10)})
sns.scatterplot(x='date',y='deaths',data=kerala)

jk = df[df.state == 'Jammu and Kashmir']
print(jk.head())

max_jk_confirmed = jk.sort_values(by='confirmed',ascending=False)
print(max_jk_confirmed.head())

sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='confirmed',data=jk)

max_jk_cured = jk.sort_values(by='cured',ascending=False)
print(max_jk_cured.head())

sns.set(rc={'figure.figsize':(8,5)})
sns.lineplot(x='date',y='cured',data=jk)

max_jk_deaths = jk.sort_values(by='deaths',ascending=False)
print(max_jk_deaths)

sns.set(rc={'figure.figsize':(8,5)})
sns.lineplot(x='date',y='deaths',data=jk)






