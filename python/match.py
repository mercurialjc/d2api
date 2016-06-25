#!/usr/bin/env python
import requests
import json
import traceback
import sys
import subprocess

api_key = '73DE414FE4B88E95E48380457489EC4A'
game_modes = ['None', 'All Pick', 'Captain\'s Mode', 'Random Draft',
              'Single Draft', 'All Random', 'Intro', 'Diretide',
              'Reverse Captain\'s Mode', 'The Greeviling', 'Tutorial',
              'Mid Only', 'Least Played', 'New Player Pool'
              'Compendium Matchmaking', 'Captain\'s Draft']
terminal_width = int(subprocess.check_output(['stty', 'size']).split()[1])

def print_horizontal_line(line_type):
    for i in range(1, terminal_width):
        sys.stdout.write(line_type)
    print

def build_api_url(module_name, api_name):
    url = 'http://api.steampowered.com/' + module_name + '/' + api_name + '/v1'
    return url

def get_game_mode_id(game_mode):
    game_mode_id = -1
    try:
        game_mode_id = game_modes.index(game_mode)
    except ValueError as ve:
        print_horizontal_line('~')
        traceback.print_exc()
        print ve
        print_horizontal_line('~')
    finally:
        return game_mode_id

def get_heroes(params):
    module_name = 'IEconDOTA2_570'
    api_name = 'GetHeroes'
    url = build_api_url(module_name, api_name)
    heroes = None
    try:
        r = requests.get(url, params)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print_horizontal_line('~')
        traceback.print_exc()
        print e
        print_horizontal_line('~')
    else:
        try:
            heros = r.json()
        except ValueError as ve:
            print_horizontal_line('~')
            traceback.print_exc()
            print ve
            print_horizontal_line('~')
    finally:
        return heroes

def get_match_history(params):
    module_name = 'IDOTA2Match_570'
    api_name = 'GetMatchHistory'
    url = build_api_url(module_name, api_name)
    match_history = None
    try:
        r = requests.get(url, params)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print_horizontal_line('~')
        traceback.print_exc()
        print e
        print_horizontal_line('~')
    else:
        try:
            match_history = r.json()
        except ValueError as ve:
            print_horizontal_line('~')
            traceback.print_exc()
            print ve
            print_horizontal_line('~')
    finally:
        return match_history

def print_formatted_match_history(match_history):
    pretty_match_history = []
    params_get_heroes = {'key': api_key,
                         'language': 'zh',
                         'itemizedonly': 'True'}
    heroes = get_heroes(params_get_heroes)
    result = match_history['result']
    matches = result['matches']
    print 'Latest Matches'
    print 'Hero\t\tTime Finished\t\tResult\t\tK/D/A\t\tLevel'
    print_horizontal_line('-')
            
def main():
    account_id = '118121815'
    game_mode_id = get_game_mode_id('All Pick')
    params = {'key': api_key,
              'account_id': account_id,
              'game_mode_id': game_mode_id}
    match_history = get_match_history(params)
    print_formatted_match_history(match_history)

if __name__ == '__main__':
    main()
