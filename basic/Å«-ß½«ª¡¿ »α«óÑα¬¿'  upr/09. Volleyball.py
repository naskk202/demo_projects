from math import floor
year = input()
holydays_in_year = int(input())
weekends_in_home = int(input())
in_sofia = 48 - weekends_in_home
games_in_sofia = in_sofia * 0.75
games_in_holydays = holydays_in_year - (holydays_in_year / 3)
games = games_in_sofia + games_in_holydays + weekends_in_home
if year == "leap":
    games = games * 1.15
    print(floor(games))
elif year == "normal":
    print(floor(games))
