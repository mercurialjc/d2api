#!/usr/bin/env python
import requests
import json

api_key = '73DE414FE4B88E95E48380457489EC4A'

def build_api_url(module_name, api_name):
    url = 'http://api.steampowered.com/' + module_name + '/' + api_name + '/v1'
    return url

def get_heroes(language, itemized_only):
    module_name = 'IEconDOTA2_570'
    api_name = 'GetHeroes'
    url = build_api_url(module_name, api_name)
    params = {'key': api_key,
              'language': language,
              'itemized_only': itemized_only}
    heroes = []
    try:
        r = requests.get(url, params)
        print (r.url)
        print (r.text)
        if r.status_code != requests.code.ok:
            raise requests.exception.RequestException
    except requests.exception.RequestException as e:
        print (e)
    else:
        try:
            heros = r.json()
        except ValueError as ve:
            print (ve)
    finally:
        return heroes

def get_match_history(account_id):
    module_name = 'IDOTA2Match_570'
    api_name = 'GetMatchHistory'
    url = build_api_url(module_name, api_name)
    params = {'key'       : api_key, 
              'account_id': account_id}
    match_history = []
    try:
        r = requests.get(url, params)
        if r.status_code != requests.codes.ok:
            raise requests.exception.RequestException
    except requests.exception.RequestException as e:
        print (e)
    else:
        try:
            match_history = r.json()
        except ValueError as ve:
            print (ve)
    finally:
        return match_history

def print_formatted_match_history(match_history):
    heroes = get_heroes(language='zh', itemized_only='true')
    print (heroes)
            
def main():
    account_id = '118121815'
    match_history = get_match_history(account_id)
    print (match_history)
    print_formatted_match_history(match_history)

if __name__ == '__main__':
    main()
