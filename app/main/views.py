from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source,get_articles
from ..model import Source

    
@main.route('/') #route decorator
def index():#index() is the view function

    general_news = get_source('entertainment')
    print('*************general news*********************')
    print(general_news)
    sports_news=get_source('sports')
    business_news=get_source('business')

    title='News Feed'

    return render_template('index.html',title = title,entertainment=general_news,sports=sports_news,business=business_news)
   

@main.route('/article/<id>')
def article(id):

    article = get_articles(id)
    print('*************get_article****************')
    print(article)

    title='Article hub'

    return render_template('article.html',title = title,id=id,article = article)

