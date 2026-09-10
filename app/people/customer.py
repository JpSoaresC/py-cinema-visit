class Customer:
    def __init__(self, name: str, food: str):
        self.name = name
        self.food = food
    def watch_movie(self, movie: str):
        self.movie = movie
        print(f"{self.name} is watching {self.movie}.")
        pass