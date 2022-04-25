from parsel import Selector
import requests
import os

def selector_from_response(response):
    text = response.text
    selector = Selector(text=text, type='html')
    return selector
