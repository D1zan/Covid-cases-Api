import requests 
import json

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

# outside of class##################
#Getting the data, get request
def fetch_covid_info(country):
    url = f"https://disease.sh/v3/covid-19/historical/{country}"
    response = requests.get(url)

    if response.status_code == 200:
        covid_data = response.json()
        return covid_data
    else:
        print(f"\nI am sorry, we are unable to reach that information. Try Again!\n")
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

print("Hi, Welcome to Covid Information center")
while True:
    print("These are the countries with the available information to you: ")
    print("Brazil,\nUnited States, \nCanada,\nGhana,\nPortugal. ")
    country = input("Which country would you like to ask about?: ").lower().strip()
    covid_info = fetch_covid_info(country)
    if not covid_info:
        continue


    #print(country)
    #print(fetch_covid_info(country))
#Ask user to pick a question 
    print("\nPlease pick numbers 1-3")
    questions = int(input("(1) How many cases of covid in total? \n(2) How many people have died from covid? \n(3) How many people in total have recovered? " ))

    if questions == "1":
        print(fetch_covid_info(covid_info("cases")))
    elif questions == "2":
        print(fetch_covid_info(covid_info("todayDeaths")))
    elif questions == "3": 
        print(fetch_covid_info(covid_info("recovered")))
    covid_obj = covid_info
    print(f"{"covid_obj"}")


# print the country + the answer to the picked question
    keep_going = input("Would you like to ask about another country? (y/n): ").lower().strip()
    if keep_going == "n":
        break