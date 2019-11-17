# from app import app
import urllib.request,json 
# will help us create a connection to our API URL and send a request and json modules that will format the JSON response to a Python dictionary
from .model import Source, Article

# Movie = movie.Movie


#getting the api key
api_key=None
 #getting the base url
base_url=None 

article_url= None

def configure_request(app):
    global api_key,base_url,article_url

    api_key = app.config['API_KEY']
    
    base_url= app.config['SOURCE_BASE_URL']
    # print(base_url)
    article_url = app.config['ARTICLE_BASE_URL']

def process_source(source_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country=source_item.get('country')

        if url:
            source_object=Source(id,name,description,url,category,language,country)
            source_results.append(source_object)

    return source_results

def get_source(category):


    get_source_url = base_url.format(category,api_key)
    
    # get_url = 'https://api.themoviedb.org/3/movie/{}?api_key=6d7b3c11acae661cd9252d66dddb2883'
    # get_movies_url = get_url .format(category)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read() #using the read function to get the response and store it in the variable
        get_source_response = json.loads(get_source_data) #converting JSON response to a python dictionary using the json.loads function

        source_results = None

        if get_source_response['sources']:
            source_result_list=get_source_response['sources']
            source_results=process_source(source_result_list) #process_results is a function that takes in the list of dictionary objects and returns a list of movie objects

    return source_results



def process_article(article_list):

    article_results=[]
    for article_item in article_results:
        id = article_item.get('id')
        author=article_item.get('author')
        title=article_item.get('title')
        description=article_item.get('description')
        url=article_item.get('url')
        image=article_item..get('urlToImage')
        date=article_item.get('publishedAt')

        if image:
            article_object=Article(id,author,title,description,url,image,date)
            article_results.append(article_object)
        
    return article_results


def get_article(id):


    get_article_url = base_url.format(id,api_key)
    
    # get_url = 'https://api.themoviedb.org/3/movie/{}?api_key=6d7b3c11acae661cd9252d66dddb2883'
    # get_movies_url = get_url .format(category)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read() #using the read function to get the response and store it in the variable
        get_article_response = json.loads(get_article_data) #converting JSON response to a python dictionary using the json.loads function

        article_results = None

        if get_article_response['articles']:
            article_result_list=get_article_response['articles']
            article_results=process_article(article_result_list) #process_results is a function that takes in the list of dictionary objects and returns a list of movie objects

    return article_results





    