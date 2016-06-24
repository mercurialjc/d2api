#!/usr/bin/env python
import requests
import json

def build_api_url(module_name, api_name):
    url = 'http://api.steampowered.com/' + module_name + '/' + api_name + '/v1'
    return url

def get_match_history(api_key, account_id):
    module_name = 'IDOTA2Match_570'
    api_name = 'GetMatchHistory'
    url = build_api_url(module_name, api_name)
    params = {'key'       : api_key, 
              'account_id': account_id}
    r = requests.get(url, params)
    
def main():
    api_key = '73DE414FE4B88E95E48380457489EC4A'
    account_id = '118121815'
    match_history = get_match_history(api_key, account_id)
    json.dumps(match_history, indent=2)

if __name__ == '__main__':
    main()
