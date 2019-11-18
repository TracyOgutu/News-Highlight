
import urllib.request,json 
# will help us create a connection to our API URL and send a request and json modules that will format the JSON response to a Python dictionary
from .model import Source, Article



api_key=None
base_url=None 
articles_url= None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['API_KEY']

    base_url= app.config['SOURCE_BASE_URL']
    print('********base source url*******')
    print(base_url)

    articles_url = app.config['ARTICLE_BASE_URL']
    print('*******base article url*********')
    print(articles_url)

def process_source(source_list):
    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country=source_item.get('country')

        source_object = Source(id,name,description,url,category,language,country)
        source_results.append(source_object)

    return source_results

def get_source(category):
    get_source_url = base_url.format(category,api_key)
    print('********get_source_url***********')
    print(get_source_url)
    
    #SOURCE_BASE_URL='https://newsapi.org/v2/sources?language=en&category=entertainment&apiKey=7c6b555e9d0b472bbc7e5ce294d6783b'
    
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read() #using the read function to get the response and store it in the variable
        get_source_response = json.loads(get_source_data) #converting JSON response to a python dictionary using the json.loads function

        source_results = None

        if get_source_response['sources']:
            source_result_list=get_source_response['sources']
            source_results=process_source(source_result_list) #process_results is a function that takes in the list of dictionary objects and returns a list of movie objects

    return source_results


def process_articles(article_list):
    article_object=[]

    for article_item in article_list:
        id = article_item.get('id')
        author=article_item.get('author')
        title=article_item.get('title')
        description=article_item.get('description')
        url=article_item.get('url')
        image=article_item.get('urlToImage')
        date=article_item.get('publishedAt')

        article_result=Article(id,author,title,description,url,image,date)
        article_object.append(article_result)

    return article_object

def get_articles(id):
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    get_articles_url=articles_url.format(id,api_key)

    print(f'*******{get_articles_url}*******')
    print(get_articles_url)
    with urllib.request.urlopen(get_articles_url) as url:
        articles_results = json.loads(url.read())
        articles_object = None
        if articles_results['articles']:
            articles_object = process_articles(articles_results['articles'])
    return articles_object







    