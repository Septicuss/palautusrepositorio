import requests

class Player:
    def __init__(self, dictionary):
        self.name = dictionary['name']
        self.nationality = dictionary['nationality']
        self.assists = int(dictionary['assists'])
        self.goals = int(dictionary['goals'])
        self.team = dictionary['team']
        self.games = int(dictionary['games'])

    def score(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team:15} {self.goals} + {self.assists} = {self.goals+self.assists}"

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality: str):
        filtered = [ player for player in self.players if player.nationality == nationality ]
        return sorted(filtered, key=lambda player: player.score(), reverse=True)

    def nationalities(self):
        return set(player.nationality for player in self.players)

class PlayerReader:

    def __init__(self, url: str):
        self._url = url

    def get_url(self):
        return self._url

    def get_players(self):
        players = []

        response = requests.get(self._url, timeout=60).json()
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players
