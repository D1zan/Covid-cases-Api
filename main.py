import requests 
import json

def color_text(code):
    return "\33[{code}m".format(code=code)
    
def draw_ascii_art():
    art = """
              .
           ,'/ \`.
          |\/___\/|
          \\'\   /`/
           `.\ /,'
              |
              |
             |=|
        /\  ,|=|.  /\\
    ,'`.  \/ |=| \/  ,'`.
  ,'    `.|\ `-' /|,'    `.
,'   .-._ \ `---' / _,-.   `.
   ,'    `-`-._,-'-'    `.
  '                       `

    """
    return art

#Make a class
class Covid:
    def __innit__(self, country, cases, deaths, recovered ):
        self.cases = cases
        self.deaths = deaths
        self.recovered = recovered
        self.country = country
    def display_info(self):
        print(f"Country: {self.country}")
        print(f"Cases Today: {self.cases}")
        print(f"Deaths Total: {self.deaths}")
        print(f"Recoveries: {self.recovered}")

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
                    covid_json["deaths"],
                    covid_json["recovered"],
    )
    return covid()


#User interaction
colorTest = color_text(32) + draw_ascii_art()
print("Hi, Welcome to Covid Information center")
print(colorTest)
while True:
    print("These are the countries with the available information to you: ")
    print("Brazil,\nUnited States, \nCanada,\nGhana,\nPortugal. ")
    
   
    
    country = input("Which country would you like to ask about?: ").lower().strip()
    covid_info = fetch_covid_info(country)
    
    if not covid_info:
        continue
    
    # calculate the totals by iterating
    cases_dictionary = covid_info["timeline"]["cases"] 
    # We name the dictionary, set a variable to 0 which is reffering to the values in cases_dictionary. 
    sumCases = 0
    #The for loop grabs the variable sumCases and adds the values to itself, so the  user won't see a big list of numbersk
    for cases in cases_dictionary.values():
        sumCases += cases

    deaths_dictionary = covid_info["timeline"]["deaths"]
    sumDeaths = 0 
    for deaths in deaths_dictionary.values():
        sumDeaths += deaths
        
    recoveries_dictionary = covid_info["timeline"]["recovered"]
    sumRecoveries = 0
    for recoveries in recoveries_dictionary.values():
        sumRecoveries += recoveries 

    #print(country)
    # print(json.dumps(covid_info, indent=4))
#Ask user to pick a question 
    print("\nPlease pick numbers 1-3")
    print("*** Numbers may be inaccurate***")
    questions = input("(1) How many cases of covid in total? \n(2) How many people have died from covid? \n(3) How many people in total have recovered?  " )
    
    
    if questions == "1":
        print(f"\n{sumCases} is the amount of cases in {country}")
        # print(covid_info["timeline"]["cases"])
    elif questions == "2":
        print(f"\n{sumDeaths} is the amount of deaths in {country}")
    elif questions == "3": 
        print(f"\n{sumRecoveries} is the amount of recoveries in {country}")
    else:
        print("Please enter numbers between 1-3, try again:")

# print the country + the answer to the picked question
    keep_going = input("Would you like to ask about another country? (y/n): ").lower().strip()
    if keep_going == "n":
        break
    print("Thank you for your research")
    


