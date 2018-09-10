import xml.etree.ElementTree as ET
import json
import requests


def find_fave(title_input):
    """Builds an API fetch request from a book title entered by a user into the search bar"""

    with open('Data/DataFiles/config.json', 'r') as config_file:
        config = json.load(config_file)

    dev_key = config['Goodreads_key']

    # TODO: figure out what other substitutions to make such as apostrophes and other special characters
    title_format = title_input.replace(' ', '+')
    goodreads_request = "https://www.goodreads.com/book/title.xml?&key={0}&title={1}".format(
        dev_key, title_format)
    print(goodreads_request)

    # try:
    response = requests.get(goodreads_request)
    root = ET.fromstring(response.content)
    book_root = root.find("book")

    fave_book = dict()
    fave_book["gr_id"] = book_root.find("id").text.strip()

    if (book_root.find("isbn").text != ''):
        fave_book["isbn"] = book_root.find("isbn").text.strip()
    else:
        fave_book["isbn"] = ''
    fave_book["isbn13"] = book_root.find("isbn13").text.strip()
    fave_book["title"] = book_root.find("title").text
    print(fave_book)

    # except:
    #     print("Error. You figure it out.")

    # return fave_book


find_fave('The Sun Also Rises')
