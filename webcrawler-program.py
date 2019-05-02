import os
import urllib.request
from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://careers.karma.life/people')

domain = 'https://careers.karma.life'

guys_info = r.html.find('.thumbnail-hover.circle')


def grab_mail():
    for guy_info in guys_info:
        name = guy_info.find('.name', first=True).text
        link = domain + guy_info.attrs['href']
        r = session.get(link)
        department_and_title = r.html.find('.info', first=True)
        department =
        title = r.html.find('.info', first=True)
        mail = []
        for contact_info in r.html.find('.contact-info a'):
            string = contact_info.attrs['href']
            if string.startswith('mailto:'):
                mail.append(string.replace('mailto:', ''))
        print(mail)
        break


def grab_profile_image():
    if not os.path.exists("./karma/"):
        os.mkdir('./karma')
    for guy_info in guys_info:
        name = guy_info.find('.name', first=True).text
        link = domain + guy_info.attrs['href']
        r = session.get(link)
        image_element = r.html.find('.lazy.u-tertiary-background-color',
                                    first=True)
        if 'data-src' in image_element.attrs:
            urllib.request.urlretrieve(
                image_element.attrs['data-src'], './karma/' + name + '.jpg')


grab_mail()
