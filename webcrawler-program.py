import urllib.request
from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://careers.karma.life/people')

domain = 'https://careers.karma.life'

guys_info = r.html.find('.thumbnail-hover.circle')


for guy_info in guys_info:
    absolute_link = domain + guy_info.attrs['href']
    print(absolute_link)

    '''
    urllib.request.urlretrieve(guy_info.attrs['data-src'], 'practice.jpg')
    break

'''
