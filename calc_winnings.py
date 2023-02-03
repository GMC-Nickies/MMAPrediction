import pandas as pd
from oddscalculator import *

data = pd.read_csv("output_bets.csv")

all_odds_dec = []

only_women = 0
only_men = 1

if only_women == 1:
	data = data[data["Gender"].str.contains("M")==False]
elif only_men == 1:
	data = data[data["Gender"].str.contains("F")==False]

data.reset_index(inplace=True)

all_odds_amer = data['Odds']
outcomes = data['Outcome']

"""
print(data)
print(all_odds_amer)
print(outcomes)
"""

for x in all_odds_amer:
	this_odds = AmericanOdds(x)
	all_odds_dec.append(this_odds.decimal)

winnings = []
winnings_only_fav = []
winnings_only_underdogs = []

bet_per_match = 5
total_bet = bet_per_match * len(outcomes)

num_favs = 0
num_under = 0

acc = 1

counter = 0
counter2 = 0

for x in outcomes:
	this_odds = all_odds_amer[counter]
	if this_odds > 0:
		num_under += 1
		if outcomes[counter] == 1:
			print('right')
			winnings.append(bet_per_match * all_odds_dec[counter])
			winnings_only_underdogs.append(bet_per_match * all_odds_dec[counter])
		else:
			print('wrong!')
			winnings.append(0)
			winnings_only_underdogs.append(0)
	else:
		num_favs += 1
		if outcomes[counter] == 1:
			print('right')
			winnings.append(bet_per_match * all_odds_dec[counter])
			winnings_only_fav.append(bet_per_match * all_odds_dec[counter])
		else:
			print('wrong!')
			winnings.append(0)
			winnings_only_fav.append(0)
	counter += 1
	counter2 += 1
	sum_winnings = sum(winnings)
	sum_winnings_only_fav = sum(winnings_only_fav)
	sum_winnings_only_underdogs = sum(winnings_only_underdogs)
	total_bet = (num_favs + num_under) * bet_per_match
	total_bet_only_favs = bet_per_match * num_favs
	total_bet_only_underdogs = bet_per_match * num_under

sum_winnings = sum(winnings)
sum_winnings_only_fav = sum(winnings_only_fav)
sum_winnings_only_underdogs = sum(winnings_only_underdogs)
total_bet = (num_favs + num_under) * bet_per_match
total_bet_only_favs = bet_per_match * num_favs
total_bet_only_underdogs = bet_per_match * num_under

print("Winnings (percent gain):")
print("Bet on all matches: " + str(round((sum_winnings / total_bet), 2)))
print("Bet on only favorite-predicted-to-win matches: " + str(round((sum_winnings_only_fav / total_bet_only_favs),2)))
print("Bet on only underdog-predicted-to-win matches: " + str(round((sum_winnings_only_underdogs / total_bet_only_underdogs),2)))
print("Assuming " + str(bet_per_match) + " dollar bet per fight:")
print("Betting on all " + str(num_favs + num_under) + " matches, we each would have made " + str(round((sum_winnings - total_bet), 2)) + " dollars.")
print("That means we'd each come out with " + str(sum_winnings) + " dollars after risking " + str(total_bet) + " dollars.")
print("Betting on only the " + str(num_favs) + " favorite-predicted-by-the-AI-to-win matches, we each would have made " + str(round((sum_winnings_only_fav - total_bet_only_favs),2)) + " dollars.")
print("That means we'd each come out with " + str(round(sum_winnings_only_fav,2)) + " dollars after risking " + str(total_bet_only_favs) + " dollars.")
print("Betting on only the " + str(num_under) + " underdog-predicted-by-the-AI-to-win matches, we each would have made " + str(round((sum_winnings_only_underdogs - total_bet_only_underdogs),2)) + " dollars.")
print("That means we'd each come out with " + str(round(sum_winnings_only_underdogs,2)) + " dollars after risking " + str(total_bet_only_underdogs) + " dollars.")



"""
num_right = 0
bets_only_favs = []
for x in outcomes:
	this_odds = all_odds_amer[counter]
	if this_odds < 0:
		counter2 += 1
		num_favs += 1
		if outcomes[counter] == 1:
			print('right')
			num_right += 1
			print(all_odds_dec[counter])
			winnings_only_fav.append(bet_per_match * all_odds_dec[counter])
		else:
			print('wrong!')
			winnings_only_fav.append((bet_per_match * -1))
		bets_only_favs.append(bet_per_match)
		if counter2 == 7:
			bet_per_match = bet_per_match * 1.5
			counter2 = 0
		print(bet_per_match)
		print(sum(winnings_only_fav))
	counter += 1

sum_winnings_only_fav = sum(winnings_only_fav)
total_bet_only_favs = sum(bets_only_favs)
test = bet_per_match * num_favs

print(sum_winnings_only_fav)
print(total_bet_only_favs)

print("Winnings (percent gain):")

print("Bet on only favorite-predicted-to-win matches: " + str(round((sum_winnings_only_fav / total_bet_only_favs),2)))

print("Betting on only the " + str(num_favs) + " favorite-predicted-by-the-AI-to-win matches, we each would have made " + str(round((sum_winnings_only_fav - total_bet_only_favs),2)) + " dollars.")
print("That means we'd each come out with " + str(round(sum_winnings_only_fav,2)) + " dollars after risking " + str(total_bet_only_favs) + " dollars.")

print (num_right / num_favs)
"""