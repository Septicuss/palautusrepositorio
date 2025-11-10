from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player import PlayerReader
from player import PlayerStats

console = Console()

def build_table(players, season, nationality):
    table = Table(title=f"Season {season} players from {nationality}")
    table.add_column("Released", style="cyan")
    table.add_column("teams", style="magenta")
    table.add_column("goals", style="green", justify="right")
    table.add_column("assists", style="green", justify="right")
    table.add_column("points", style="green", justify="right")

    for player in players[:12]:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.score()))

    return table

def main():
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]
    season = Prompt.ask(prompt="Season", choices=seasons, default="2024-25")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationality = Prompt.ask(prompt="Nationality", choices=stats.nationalities())
        if not nationality or nationality.isspace():
            continue

        players = stats.top_scorers_by_nationality(nationality)
        console.print(build_table(players, season, nationality))

if __name__ == "__main__":
    main()
