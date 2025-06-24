class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rating = []

    def __str__(self):
        if self.avg_rating() > 0:
            rating_info = f"{len(self.rating)} ratings, average {self.avg_rating():.1f} points"
        elif self.avg_rating() == 0:
            rating_info = "no ratings"

        return (
            f"{self.title} ({self.seasons} seasons)\n"
            f"genres: {', '.join(self.genres)}\n"
            f"{rating_info}"
            )
    
    def avg_rating(self):
        if len(self.rating) > 0:
            avg_rating_calc = sum(self.rating) / len(self.rating)
        elif len(self.rating) == 0:
            avg_rating_calc = 0
        return avg_rating_calc
        


    def rate(self, rating: int):
        self.rating.append(rating)


def minimum_grade(rating: float, series_list: list):
    meets_min = []
    for series in series_list:
        if series.avg_rating() >= rating:
            meets_min.append(series)
    return meets_min


def includes_genre(genre: str, series_list: list):
    in_genre = []
    for series in series_list:
        for each in series.genres:
            if genre in each:
                in_genre.append(series)
    return in_genre



if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)