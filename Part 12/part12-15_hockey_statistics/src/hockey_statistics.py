import json

filename = input("file name: ")
with open(filename) as file:
    data = file.read()
players = json.loads(data)

for player in players:
    player["points"] = player["goals"] + player["assists"]

print(f"read the data of {len(players)} players")



class Actions:

    def search_for_player(self, player_name):
        print("")
        for player in players:
            if player_name in player.values():
                print(f'{player["name"]:<20} {player["team"]:<4} {player["goals"]:>2} + {player["assists"]:>2} = {(player["points"]):>3}')
                return
        print("No player with that name")

    def teams(self):
        teams = []
        for player in players:
            if player["team"] not in teams:
                teams.append(player["team"])
        teams.sort()
        for team in teams:
            print(team)

    def countries(self):
        countries = []
        for player in players:
            if player["nationality"] not in countries:
                countries.append(player["nationality"])
        countries.sort()
        for country in countries:
            print(country)

    def players_in_team(self, team_name):
        print("")
        team_players = []
        for player in players:
            if team_name in player.values():
                team_players.append(player)
        team_players.sort(key=lambda player: player["points"], reverse=True)
        for player in team_players:
            print(f'{player["name"]:<20} {player["team"]:<4} {player["goals"]:>2} + {player["assists"]:>2} = {(player["points"]):>3}')


    def players_from_country(self, country_name):
        print("")
        country_players = []
        for player in players:
            if country_name in player.values():
                country_players.append(player)
        country_players.sort(key=lambda player: player["points"], reverse=True)
        for player in country_players:
            print(f'{player["name"]:<20} {player["team"]:<4} {player["goals"]:>2} + {player["assists"]:>2} = {(player["points"]):>3}')

    def most_points(self, player_count):
        print("")
        players.sort(key=lambda player: (-player["points"], -player["goals"]))
        for player in players:
            if player_count > 0:
                print(f'{player["name"]:<20} {player["team"]:<4} {player["goals"]:>2} + {player["assists"]:>2} = {(player["points"]):>3}')
                player_count -= 1

    def most_goals(self, player_count):
        print("")
        players.sort(key=lambda player: (-player["goals"], player["games"]))
        for player in players:
            if player_count > 0:
                print(f'{player["name"]:<20} {player["team"]:<4} {player["goals"]:>2} + {player["assists"]:>2} = {(player["points"]):>3}')
                player_count -= 1


class UserInterface:
    def __init__(self):
        self.data = Actions()

    def instructions(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def run(self):
        self.instructions()
        while True:
            print("")
            command = input("command:")

            match command:
                case "0":
                    break
                case "1":
                    self.search_for_player()
                case "2":
                    self.teams()
                case "3":
                    self.countries()
                case "4":
                    self.players_in_team()
                case "5":
                    self.players_from_country()
                case "6":
                    self.most_points()
                case "7":
                    self.most_goals()


    def search_for_player(self):
        player_name = input("name: ")
        self.data.search_for_player(player_name)

    def teams(self):
        self.data.teams()

    def countries(self):
        self.data.countries()

    def players_in_team(self):
        team_name = input("name: ")
        self.data.players_in_team(team_name)

    def players_from_country(self):
        country_name = input("name: ")
        self.data.players_in_team(country_name)

    def most_points(self):
        player_count = int(input("how many: "))
        self.data.most_points(player_count)

    def most_goals(self):
        player_count = int(input("how many: "))
        self.data.most_goals(player_count)

test = UserInterface()
test.run()