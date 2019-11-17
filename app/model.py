class Source:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        self.id=id
        self.name=name
        self.description = description
        self.url = 'https://abcnews.go.com'
        self.category=category
        self.language=language
        self.country=country

class Article:

    def __init__(self,id,author,title,description,url,image,date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image= image
        self.date = date

    