# Import library requests to send request to url
# Import Beautifulsoup to scrape data from the url
import requests
from bs4 import BeautifulSoup
  
def get_data(euros):
    url = f"https://www.bookmyforex.com/currency-converter/eur-to-inr/"
    r = requests.get(url)
    sor = BeautifulSoup(r.text, "html.parser")

    # The live value of 1 euro is stored in following section of website
    temp = sor.find("span", {'class':"first_live_trade"})

    # Get the text part of the section ex. '1 EUR =91.7052 INR'
    # Split text from = sign and store the later part in a variable
    INR_part = temp.getText().split('=')[1]

    # Now split the right side part of = sign from 'space' to eliminate INR
    # and get the numerical value. Convert it into float
    val = float(INR_part.split(' ')[0])

    # The value of euros will be euros*value of 1 euro
    print('The current value of 10 euros is:', round(val*euros,2), 'INR')

curr = float(input("Enter Euros to be converted to INR:"))
get_data(curr)