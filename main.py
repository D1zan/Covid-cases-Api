import requests 
import json
import random

#Make a class
class Covid:
    def __innit__(self, cases, todayDeaths, recovered, affectedCountries ):
        self.cases = cases
        self.todayDeaths = todayDeaths
        self.recovered = recovered
        self.affectedCountries = affectedCountries
    def display_info(self):
        print(f"Cases Today: {self.cases}")
        print(f"Deaths Total: {self.todayDeaths}")
        print(f"Recoveries: {self.recovered}")
        print(f"Countries affected: {self.affectedCountries}")

#Getting the data, get request
    def fetch_covid_us(covid_data):
        url = f"https://disease.sh/v3/covid-19/historical/us"
        response = requests.get(url)

        if response.status_code == 200:
            covid_data = response.json()
            return covid_data
        else:
            print(f"Sorry, that is not related to my information knowledge")
            return None
        
    def fetch_covid_canada(covid_data):
        url = f"https://disease.sh/v3/covid-19/historical/canada"
        response = requests.get(url)

        if response.status_code == 200:
            covid_data = response.json()
            return covid_data
        else:
            print(f"Sorry, that is not related to my information knowledge")
            return None
        
    def fetch_covid_brazil(covid_data):
        url = f"https://disease.sh/v3/covid-19/historical/brazil"
        response = requests.get(url)

        if response.status_code == 200:
            covid_data = response.json()
            return covid_data
        else:
            print(f"Sorry, that is not related to my information knowledge")
            return None
        
    def fetch_covid_ghana(covid_data):
        url = f"https://disease.sh/v3/covid-19/historical/ghana"
        response = requests.get(url)

        if response.status_code == 200:
            covid_data = response.json()
            return covid_data
        else:
            print(f"Sorry, that is not related to my information knowledge")
            return None
        
    def fetch_covid_portugal(covid_data):
        url = f"https://disease.sh/v3/covid-19/historical/portugal"
        response = requests.get(url)

        if response.status_code == 200:
            covid_data = response.json()
            return covid_data
        else:
            print(f"Sorry, that is not related to my information knowledge")
            return None
            

#Creating an object for the class
def covid_info(covid_json):
    covid = Covid(
                    covid_json["cases"],
                    covid_json["todayDeaths"],
                    covid_json["recovered"],
    )
    return covid()


#User interaction
print()
print("Hi, Welcome to Covid Information center")
print("These are the countries with the available information to you: ")
print("Brazil, " "\n" "United States " "\n" "Canada, " "\n" "Ghana, " "\n" "Portugal." )
print()


if user_input == "Brazil":
    print(covid_info)
elif "Portugal":
    print(covid_info(covid_json))
elif "Canada":
    print(covid_info)
elif "United States":
    print(covid_info)
elif "Portugal":
    print(covid_info)
else: 
    "Please pick from the list given"

#Ask user to pick a country
country = input("Which country would you like to ask about?: ")


#Ask user to pick a question 

questions = int(input("(1) How many cases of covid in total? \n (2)How many people have died from covid? \n (3)How many people in total have recovered? " ))


# print the country + the answer to the picked question