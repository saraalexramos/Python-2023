# Write your solution here:

class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
        self.num_ratings = 0
        self.rate = 0

    def rate(self, rating: int):
        self.num_ratings += 1
        self.ratings.append(rating)
    
        sum = 0
        for number in self.ratings:
            sum += int(number)
        self.rate = sum / self.num_ratings
        

    def __str__(self):
        genre_string = ", ".join(self.genres)
        if self.num_ratings > 0:
            sum = 0
            for number in self.ratings:
                sum += number
            avg_rating = sum / self.num_ratings
            return f"{self.title} ({self.seasons} seasons) \ngenres: {genre_string} \n{self.num_ratings} ratings, average {avg_rating} points"
        else:
            return f"{self.title} ({self.seasons} seasons) \ngenres: {genre_string} \nno ratings"


def mininum_grade(rating: float, series_list: list):
    new_series_list = []
    for serie in series_list:
        if serie.rate >= rating:
            new_series_list.append(serie)
    return new_series_list


def includes_genre(genre: str, series_list: list):
    pass


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