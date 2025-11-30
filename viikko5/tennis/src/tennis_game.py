
CALLS = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty"
}

DEUCE = "Deuce"
DEUCE_MIN_POINTS = 3


class TennisPlayer:
    def __init__(self, name: str):
        self.name = name
        self.points = 0

    def add_point(self):
        self.points += 1

    def get_call(self):
        return CALLS.get(self.points)

    def is_beyond_deuce(self):
        return self.points > DEUCE_MIN_POINTS

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.first_player = TennisPlayer(player1_name)
        self.second_player = TennisPlayer(player2_name)

    def get_player(self, player_name) -> TennisPlayer | None:
        if self.first_player.name == player_name:
            return self.first_player
        elif self.second_player.name == player_name:
            return self.second_player
        return None

    def won_point(self, player_name):
        player = self.get_player(player_name)
        if player is not None:
            player.add_point()

    def get_score_equal_points(self) -> str:
        points = self.first_player.points
        call = CALLS.get(points)

        if points == DEUCE_MIN_POINTS or not call:
            return DEUCE

        return f"{call}-All"

    def get_score_beyond_deuce(self) -> str | None:
        leader = self.first_player if self.first_player.points > self.second_player.points else self.second_player
        difference = abs(self.first_player.points - self.second_player.points)

        if difference == 1:
            return f"Advantage {leader.name}"

        return f"Win for {leader.name}"

    def get_score(self):

        # Equal points
        if self.first_player.points == self.second_player.points:
            return self.get_score_equal_points()

        # Beyond a deuce
        if self.first_player.is_beyond_deuce() or self.second_player.is_beyond_deuce():
            return self.get_score_beyond_deuce()

        # Unequal points, not beyond a deuce
        first_score = CALLS.get(self.first_player.points)
        second_score = CALLS.get(self.second_player.points)

        return f"{first_score}-{second_score}"

