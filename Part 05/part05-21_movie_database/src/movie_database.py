def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie_list = database
    new_movie = {"name": name, "director": director, "year": year, "runtime": runtime}
    movie_list.append(new_movie)


if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)