from nba_api.stats.endpoints import scoreboardv3
from datetime import date, timedelta
from requests.exceptions import RequestException

today = date.today()
yesterday = today - timedelta(days=1)

try:
    scoreboard = scoreboardv3.ScoreboardV3(game_date=yesterday.strftime("%Y-%m-%d"))
    normalized_dict = scoreboard.get_normalized_dict()
except RequestException:
    with open("report.txt", "w") as file:
        file.write("There was an error fetching the scoreboard data.")
else:
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

    with open("report.txt", "w") as file:
        if (len(games) == 0):
            file.write("Yesterday's NBA Scoreboard -- " + yesterday.strftime("%Y-%m-%d") + "\n")
            file.write("No games were played yesterday. Check back tomorrow!" + "\n")
        else:
            file.write("Yesterday's NBA Scoreboard -- " + yesterday.strftime("%Y-%m-%d") + "\n")
            file.write("------------------------------------\n\n")
            for game_id in games:
                file.write(games[game_id][0]['teamCity'] + " " +
                            games[game_id][0]['teamName'] + " (" +
                            str(games[game_id][0]['wins']) + "-" +
                         str(games[game_id][0]['losses']) + "): " +
                            str(games[game_id][0]['score']) + "\n")
                file.write(games[game_id][1]['teamCity'] + " " +
                            games[game_id][1]['teamName'] + " (" +
                            str(games[game_id][1]['wins']) + "-" +
                            str(games[game_id][1]['losses']) + "): " +
                            str(games[game_id][1]['score']) + "\n")
                file.write("\n")
