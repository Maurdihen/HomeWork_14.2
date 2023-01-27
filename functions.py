import sqlite3


def search_by_title(title):
    try:
        with sqlite3.connect("data/netflix.db") as con:
            cur = con.cursor()
            sqlite_query = """
            SELECT title, country, release_year, listed_in, description
            FROM netflix
            WHERE title = ?
            ORDER BY release_year DESC
            LIMIT 1
            """
            cur.execute(sqlite_query, (title,))
            executed_query = cur.fetchall()
            result = executed_query[0]
            return {'title': result[0],
                    'country': result[1],
                    'release_year': result[2],
                    'genre': result[3],
                    'description': result[4]}
    except:
        raise ValueError(f'По запросу {title}, нет данных')


def search_by_release_year(from_, to):
    try:
        with sqlite3.connect("data/netflix.db") as con:
            cur = con.cursor()
            sqlite_query = """
            SELECT title, release_year
            FROM netflix
            WHERE release_year BETWEEN ? AND ?
            LIMIT 100
            """
        cur.execute(sqlite_query, (from_, to,))
        executed_query = cur.fetchall()
        result = []
        for i in range(len(executed_query)):
            result.append({
                'title': executed_query[i][0],
                'release_year': executed_query[i][1]
            })
        return result
    except:
        raise ValueError(f'В промежутке между {from_} и {to} не было найдено фильмов или сериалов')


def group_by_age(rat):
    try:
        with sqlite3.connect('data/netflix.db') as con:
            cur = con.cursor()
            sqlite_query = """
            SELECT title, rating, description
            FROM netflix
            WHERE rating = ?
            """
            result = []
            for r in rat:
                cur.execute(sqlite_query, (r,))
                executed_query = cur.fetchall()
                for i in range(len(executed_query)):
                    result.append({
                        'title': executed_query[i][0],
                        'rating': executed_query[i][1],
                        'description': executed_query[i][2]
                    })
        return result
    except:
        raise ValueError(f'По запросу {rat} в базе данных ничего не найдено.')


def search_by_genre(genre):
    try:
        with sqlite3.connect('data/netflix.db') as con:
            cur = con.cursor()
            sqlite_query = """
            SELECT title, description
            FROM netflix
            WHERE listed_in LIKE ?
            ORDER BY release_year DESC
            LIMIT 10
            """
            result = []
            cur.execute(sqlite_query, (genre,))
            executed_query = cur.fetchall()
            for i in range(len(executed_query)):
                result.append({
                    'title': executed_query[i][0],
                    'description': executed_query[i][1]
                })
        return result
    except:
        raise ValueError(f'По запросу {genre} в базе данных ничего не найдено. Возможно вы ошиблись'
                         f' с названием жанра.')


def search_by_actors(actors_1, actors_2):
    with sqlite3.connect('data/netflix.db') as con:
        cur = con.cursor()
        sqlite_query = """
        SELECT netflix.cast
        FROM netflix
        WHERE netflix.cast LIKE ?
        AND netflix.cast LIKE ?
        """
        cur.execute(sqlite_query, ('%'+actors_1+'%', '%'+actors_2+'%',))
        executed_query = cur.fetchall()
        dict_actors = {}
        for executed in executed_query:
            for actors in executed:
                for actor in actors.split(', '):
                    if actor in dict_actors.keys():
                        dict_actors[actor] += 1
                    elif actor != actors_1 and actor != actors_2:
                        dict_actors[actor] = 1
        result = []
        for key, value in dict_actors.items():
            if value >= 2:
                result.append(key)
        return ", ".join(result)


def search_by_type_genre_year(type, year, genre):
    with sqlite3.connect('data/netflix.db') as con:
        cur = con.cursor()
        sqlite_query = """
        SELECT title, description
        FROM netflix
        WHERE type = ?
        AND release_year = ?
        AND listed_in = ?
        """
        cur.execute(sqlite_query, (type, year, genre,))
        executed_query = cur.fetchall()
        result = []
        for i in range(len(executed_query)):
            result.append({
                'title': executed_query[i][0],
                'description': executed_query[i][1]
            })
        return result

