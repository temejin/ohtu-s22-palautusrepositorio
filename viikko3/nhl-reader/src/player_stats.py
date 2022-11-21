class PlayerStats:
    def top_by(players, condition, sort_criterion):
        return sorted(filter(condition, players), key=sort_criterion, reverse=True)

