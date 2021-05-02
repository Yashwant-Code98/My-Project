import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ipl = pd.read_csv('matches.csv')

print(ipl.head())

print(ipl['player_of_match'].value_counts())

#Top 5 Player of match
print(ipl['player_of_match'].value_counts()[0:5])

# make a bar plot of player of match
plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_match'].value_counts().index[0:5]),list(ipl['player_of_match'].value_counts()[0:5]),color=['red'])
plt.show()

print(ipl['toss_winner'].value_counts())

# top 5 toss winner team 

print(ipl['toss_winner'].value_counts()[0:5])

#make a bar chart for toss winner

plt.figure(figsize=(8,5))
plt.bar(list(ipl['toss_winner'].value_counts().index[0:5]),list(ipl['toss_winner'].value_counts()[0:5]),color=['blue','red','green','orange','purple'])
plt.show()

print(ipl['winner'].value_counts())

#top 10 winning team
print(ipl['winner'].value_counts()[0:10])

# make a bar chart for most winning teams
plt.figure(figsize=(8,5))
plt.bar(list(ipl['winner'].value_counts().keys()[0:10]),list(ipl['winner'].value_counts()[0:10]),color=['blue'])
plt.show()

print(ipl['result'].value_counts())

batting_first = ipl[ipl['win_by_runs']!=0]
print(batting_first.head())

print(batting_first['win_by_runs'].value_counts())

plt.figure(figsize=(8,5))
plt.hist(list(batting_first['win_by_runs'].value_counts()),bins=10)

batting_second = ipl[ipl['win_by_wickets']!=0]
print(batting_second.head())

plt.figure(figsize=(8,5))
plt.pie(list(batting_second['win_by_wickets'].value_counts()[0:5]),list(ipl['win_by_wickets'].value_counts().index[0:5]),autopct='%0.1f%%')
plt.show()

print(ipl['season'].value_counts())

#top 5 season of match
print(ipl['season'].value_counts()[0:5])

print(ipl['city'].value_counts())
#top 10 city of match 
print(ipl['city'].value_counts()[0:10])

plt.figure(figsize=(15,10))
plt.bar(list(ipl['city'].value_counts().index[0:3]),list(ipl['city'].value_counts()[0:3]),color=['yellow','pink','orange'])
plt.show()

print(ipl['venue'].value_counts())

plt.figure(figsize=(8,5))
plt.bar(list(ipl['venue'].value_counts().keys()[0:5]),list(ipl['venue'].value_counts()[0:5]),color=['c','m','r','k','g'])
plt.show()


