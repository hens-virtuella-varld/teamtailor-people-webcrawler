import urllib.request
from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://careers.karma.life/people')

guys_info = r.html.find(
    '.thumbnail-hover.circle .img.u-tertiary-background-color')


for guy_info in guys_info:
    urllib.request.urlretrieve(guy_info.attrs['data-src'], 'practice.jpg')
    break
