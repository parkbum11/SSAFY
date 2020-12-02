class URLMaker:
    
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest'
    key = ''


    def __init__(self, key):
        self.key = key


    def get_url(self, category='boxoffice', feature='searchWeeklyBoxOfficeList'):
        return f'{self.url}/{category}/{feature}.json?key={self.key}'   