class Player:
    def __init__(self, name, team, nationality, goals, assists):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.goals = goals
        self.assists = assists
    
    def __str__(self):
        return "{:20} {:3} {:>2} + {:<2} = {:<3}".format(self.name, self.team, self.goals, self.assists, self.goals + self.assists)
