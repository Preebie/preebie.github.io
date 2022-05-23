import pandas as pd

def rec_algo(user_list, netflix_list = pd.read_csv("../Back End/netflix.csv")):
    movie = 0

    genre_list = []
    rating_list = []
    year_list = []
    for x in netflix_list["listed_in"]:
        x = x.split(", ")
        for y in x:
            if y not in genre_list:
                genre_list.append(y)
    list_genre = []
    for x in genre_list:
        list_genre.append([x, 0])


    for x in netflix_list["release_year"]:
        if x not in genre_list:
            year_list.append(x)
    list_year = []
    for x in year_list:
        list_year.append([x, 0])

    for x in netflix_list["rating"]:
        if x not in rating_list:
            rating_list.append(x)
    list_rating = []
    for x in rating_list:
        list_rating.append([x, 0])

    for x in user_list:
        for y in x:
            if y.lower() == "movie":
                movie += 1
                print(movie)
            elif y.lower()=="tv show":
                movie-=1
        if movie > 0:
            netflix_list = netflix_list[netflix_list['type'] == "Movie"]
        elif movie < 0:
            netflix_list = netflix_list[netflix_list['type'] == "TV Show"]
        else:
            pass

        for y in x:
            for m in list_genre:
                if m[0] == y:
                    m[1]+=1
        print(x)
        list_genre = dict(list_genre)
        max_genre = max(list_genre, key=list_genre.get)

        for y in x:
            for m in list_rating:
                if m[0] == y:
                    m[1] += 1

        list_rating = dict(list_rating)
        max_rating = max(list_rating, key=list_rating.get)

        for y in x:
            for m in list_year:
                if m[0] == y:
                    m[1]+=1

        list_year = dict(list_year)
        max_year = max(list_year, key=list_year.get)

        netflix_list_1 = netflix_list[netflix_list['rating'] == max_rating]
        if netflix_list_1.empty:
            netflix_list_1 = netflix_list
        netflix_list_2 = netflix_list_1[netflix_list_1['listed_in'] == max_genre]
        if netflix_list_2.empty:
            netflix_list_2 = netflix_list_1
        netflix_list_3 = netflix_list_2[netflix_list_2['release_year'] == max_year]
        if netflix_list_3.empty:
            netflix_list_3 = netflix_list_2
        movie = netflix_list_3.sample()
        movie=movie.values.tolist()[0]
        final = [movie[2], movie[3], movie[7], movie[8], movie[9], movie[11], "Description", '']
        print(final)
        while final in user_list:
            movie = netflix_list_3.sample()
            final = [movie[2], movie[3], movie[7], movie[8], movie[9], movie[11], "Description", '']
        print(user_list)
        return movie


