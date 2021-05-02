import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

covid = pd.read_csv('covid_19_pakistan.csv',parse_dates=['Date'],dayfirst=True)

print(covid.head())

# Data Pre-Processing !

covid = covid[['Date','Cases','Deaths','Recovered','Province','City']]
covid.columns = ['date','confirmed','deaths','cured','state','city']

print(covid.head())
print(covid.tail())

today = covid[covid.date == "4/19/2020"]

print(today.head())

max_confirmed_all_state = today.sort_values(by='confirmed',ascending=False)

print(max_confirmed_all_state.head())

top_confirmed_all_state = max_confirmed_all_state

print(top_confirmed_all_state.head())

# Data Visualization !
sns.set(rc={'figure.figsize':(8,5)})
sns.barplot(x='state',y='confirmed',data=top_confirmed_all_state,hue='state')

max_cured_all_state = today.sort_values(by='cured',ascending=False)

print(max_cured_all_state.head())

top_state_cured = max_cured_all_state
print(top_state_cured.head())

sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state',y='cured',data=top_state_cured,hue='state')

max_deaths = today.sort_values(by='deaths',ascending=False)
print(max_deaths.head())

top_state_deaths = max_deaths

print(top_state_deaths.head())

sns.set(rc={'figure.figsize':(15,10)})
sns.histplot(x='state',y='deaths',data=top_state_deaths)


sindh = covid[covid.state == "Sindh"]

max_sindh_confirmed = sindh.sort_values(by='confirmed',ascending=False)
print(max_sindh_confirmed.head())

max_sindh_cured = sindh.sort_values(by='cured',ascending=False)
print(max_sindh_cured.head())

max_sindh_deaths = sindh.sort_values(by='deaths',ascending=False)
print(max_sindh_deaths.head())

# For Confirmed Cases In Sindh !
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='confirmed',data=max_sindh_confirmed,marker='o',linewidth=3)
# For Cured Cases In Sindh !
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='cured',data=max_sindh_cured)
# For Deaths Cases In Sindh !
sns.set(rc={'figure.figsize':(8,5)})
sns.lineplot(x='date',y='deaths',data=max_sindh_deaths)

ic = covid[covid.state == "Islamabad Capital"]
print(ic.head())

max_ic_confirmed = ic.sort_values(by='confirmed',ascending=False)
print(max_ic_confirmed.head())

#For Islamabad Capital Confirmed Cases
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='confirmed',data=max_ic_confirmed)

max_ic_cured = ic.sort_values(by='cured',ascending=False)
print(max_ic_cured.head())

#For Islamabad Capital Confirmed Cases
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='cured',data=max_ic_cured)

max_ic_deaths = ic.sort_values(by='deaths',ascending=False)
print(max_ic_deaths.head())

#For Islamabad Capital Confirmed Cases 
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='deaths',data=max_ic_deaths)

print(covid.head())

gb = covid[covid.state == "Gilgit-Baltistan"]

print(gb.head())

max_gb_confirmed = gb.sort_values(by='confirmed',ascending=False)
print(max_gb_confirmed.head())

#For Gilgit Baltistan Confirmed Cases 
sns.set(rc={'figure.figsize':(8,5)})
sns.lineplot(x='date',y='confirmed',data=max_gb_confirmed)

max_gb_cured = gb.sort_values(by='cured',ascending=False)
print(max_gb_cured.head())

#For Gilgit Baltistan Cured Cases 
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='cured',data=max_gb_cured)

max_gb_deaths = gb.sort_values(by='deaths',ascending=False)
print(max_gb_deaths.head())

#For Gilgit Baltistan Deaths Cases 
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='deaths',data=max_gb_deaths)


