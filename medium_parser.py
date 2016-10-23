import sys
import requests
from bs4 import BeautifulSoup, NavigableString

invalid_tags = ['b', 'i', 'u', 'strong', 'p', 'em', 'a']

def clean_text(tag):
    if tag.name in invalid_tags:
        s = ""

        for c in tag.contents:
            if not isinstance(c, NavigableString):
                c = clean_text(c)
            s += unicode(c)

        tag = s

    return tag


def simplify(url):
    data_arr = []
    page = requests.get(url).content
    soup_page = BeautifulSoup(page, 'html.parser')
    stuff = soup_page.find_all('p')
    title = soup_page.find('h1', {'class': lambda x: 'graf--title' in x.split()})
    try:
        title_string = title.string.encode('ascii', 'ignore')
        # data_arr.append(title_string)
    except:
        pass
    for datum in stuff:
        try:
            new_datum = clean_text(datum)
            new_datum_string = new_datum.encode('ascii', 'ignore')
            data_arr.append(new_datum_string)
        except:
            pass

    article_string = " ".join(data_arr)
    return(title_string, article_string)


# if __name__ == '__main__':
    # simplify(sys.argv[1])
