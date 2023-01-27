from flask import Flask, render_template
from functions import *


app = Flask(__name__)


@app.route('/movie/<title>')
def movie_page(title):
    page = search_by_title(title)
    return render_template('movie.html', page=page)


@app.route('/movie/<int:year_from>/to/<int:year_to>')
def movie_by_year(year_from, year_to):
    page = search_by_release_year(year_from, year_to)
    return render_template('movie_by_year.html', page=page, year_from=year_from, year_to=year_to)


@app.route('/rating/children')
def movie_by_rating_children():
    page = group_by_age(['G'])
    return render_template('movie_by_rating.html', page=page, rating="G")


@app.route('/rating/family')
def movie_by_rating_family():
    page = group_by_age(["G", "PG", "PG-13"])
    return render_template('movie_by_rating.html', page=page, rating='G, PG, PG-13')


@app.route('/rating/adult')
def movie_by_rating_adult():
    page = group_by_age(['R', 'NC-17'])
    return render_template('movie_by_rating.html', page=page, rating='R, NC-17')


@app.route('/genre/<genre>')
def movie_by_genre(genre):
    page = search_by_genre(genre)
    return render_template('movie_by_genre.html', page=page, genre=genre)


app.run()