from nba_api.stats.endpoints import scoreboardv3

# Starting off with testing for development stage

# Used a fixed date to check the functionality of the API endpoint
scoreboard = scoreboardv3.ScoreboardV3(game_date="2026-11-11")

normalized_dict = scoreboard.get_normalized_dict()

print(normalized_dict.keys())

print(type(normalized_dict["LineScore"][0]))
print(normalized_dict["LineScore"][0].keys())

for selected_team_dict in normalized_dict["LineScore"]:
    print(selected_team_dict['teamCity'] + " " +
          selected_team_dict['teamName'] + ": " +
          str(selected_team_dict['score']) + " Game ID: " +
          selected_team_dict['gameId'])

#pacers_wizards_dict = {normalized_dict["LineScore"][0]["gameId"]: [normalized_dict["LineScore"][0], normalized_dict["LineScore"][1]]}

games = {}

for selected_team_dict in normalized_dict["LineScore"]:

    games_team_dict = {'teamCity': selected_team_dict['teamCity'],
                       'teamName': selected_team_dict['teamName'],
                       'score': selected_team_dict['score'],
                       'wins': selected_team_dict['wins'],
                       'losses': selected_team_dict['losses']}

    if selected_team_dict['gameId'] in games:
        games[selected_team_dict['gameId']].append(games_team_dict)
    else:
        games[selected_team_dict['gameId']] = [games_team_dict]

print(len(games.keys()))

for game_id in games:
    print("Game " + game_id + ": " + str(len(games[game_id])) + " teams")

print()

for game_id in games:
    print(games[game_id][0]['teamCity'] + " " +
          games[game_id][0]['teamName'] + ": " +
          str(games[game_id][0]['score']))
    print(games[game_id][1]['teamCity'] + " " +
            games[game_id][1]['teamName'] + ": " +
            str(games[game_id][1]['score']))
    print()