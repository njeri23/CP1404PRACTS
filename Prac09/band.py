class Band:
    """Represent a Band object with a list of musicians."""

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        musician_str = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_str})"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return "\n".join(result)
