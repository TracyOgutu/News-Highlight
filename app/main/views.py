from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source,get_articles
from ..model import Source

    
@main.route('/') #route decorator
def index():#index() is the view function

    # entertainment_news = get_source('entertainment')
    # print(entertainment_news)
    # general_news = get_source('general')
    # sports_news = get_source('sports')
    # science_news = get_source('science')
    # technology_news = get_source('technology')

    general_news = get_source('general')
    print('*************general news*********************')
    print(general_news)

    title='Latest News'

    return render_template('index.html',title = title,general=general_news)
    # , entertainment = entertainment_news, general = general_news, sports = sports_news, 
    # science = science_news, technology = technology_news)

@main.route('/article/<int:id>')
def article(id):

    article = get_articles(id)
    print('*************get_article****************')
    print(article)

    title = f'{id}'

    return render_template('trial.html',title = title,article = article)

