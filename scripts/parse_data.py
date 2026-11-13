from nba_api.stats.endpoints import scoreboardv3

# Starting off with testing for development stage

# Used a fixed date to check the functionality of the API endpoint
scoreboard = scoreboardv3.ScoreboardV3(game_date="2026-11-11")

# Outputs the scoreboard object's string representation
# print(scoreboard)

# Lists out numerous methods and attributes that can be used for this object
# print(dir(scoreboard))

normalized_dict = scoreboard.get_normalized_dict()

print(normalized_dict.keys())

print(type(normalized_dict["LineScore"][0]))
print(normalized_dict["LineScore"][0].keys())