# Name: Ana Albesa
# email: albesaaa@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: 11/9/23
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates that I can create a simple PyDev project in Eclipse and execute an API call using a URL.
# Citations:
# 1. API (https://apilist.fun/api/the-sports-db --> https://www.thesportsdb.com/api.php?ref=apilist.fun --> https://www.thesportsdb.com/api/v1/json/3/all_leagues.php)
# 2. GET Requests (https://www.datacamp.com/tutorial/making-http-requests-in-python)
# 3. Status Code (https://restfulapi.net/http-status-200-ok/)
# 4. Max Function (https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression)
# Anything else that's relevant: N/A

import json
import requests

class League:
    def __init__(self):
        response = requests.get('https://www.thesportsdb.com/api/v1/json/3/all_leagues.php')
        
        # I used a status code to avoid errors
        if response.status_code == 200:
            json_string = response.text
            # I used text instead of content because I needed the data as a string
            parsed_json = json.loads(json_string)
            
            # The data I want to extract is a distinct count of each sport mentioned in the data.
            distinct_counts = {}
            
            for sports in parsed_json['leagues']:
                strSport = sports['strSport']
                if strSport in distinct_counts:
                    distinct_counts[strSport] += 1
                else:
                    distinct_counts[strSport] = 1   
                    
            print("Sport Tally:")
            for Sport, count in distinct_counts.items():
                print(f"{Sport}: {count}")
            
            # I wanted to highlight the most played sport in the league.  
            max_Sport, max_count = max(distinct_counts.items(), key=lambda x: x[1])
            print(f"The most popular sport in the league is '{max_Sport}' with a tally of {max_count}!")
        else:
            print("FAIL")   