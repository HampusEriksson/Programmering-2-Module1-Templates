# Ditt namn
# Din klass
# Datum
# Skriv färdigt metoderna så att de gör det som är tänkt
# Din kod nedan.
from dataclasses import dataclass


@dataclass
class FootballPlayer:

    name: str
    age: int
    goals: int
    assist: int
    team: str

    def age_up(self):
        # TODO Metoden age_up ska öka spelarens ålder med 1
        pass

    def make_goals(self, goals):
        # TODO Metoden make_goal ska öka spelarens antal mål med värdet på parametern goals
        pass

    def make_assists(self, assists):
        # TODO Metoden make_assists ska öka spelarens antal assit med värdet på parametern assists
        pass

    def change_team(self, new_team):
        # TODO Metoden change_team ska ändra spelarens lag till
        pass
