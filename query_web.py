# query_web.py (Template file)

import urllib.request    # used to get data from the web
import csv               # used for reading a csv

# Here is the URL of the New Zealann environmental data
# The data is updated daily.
marine_data = ('https://www.stats.govt.nz/assets/Uploads'
               '/Environmental-economic-accounts'
               '/Environmental-economic-accounts-2020-tables/Download-data'
               '/marine-economy-2007-18.csv')
expenditure_data = ('https://www.stats.govt.nz/assets/Uploads'
                    '/Environmental-economic-accounts'
                    '/Environmental-economic-accounts-2020-tables/Download-data'
                    '/environmental-protection-expenditure-account-2009-18.csv')
energy_data = ('https://www.stats.govt.nz/assets/Uploads'
               '/Environmental-economic-accounts'
               '/Environmental-economic-accounts-2020-tables/Download-data'
               '/renewable-energy-stock-account-2007-18.csv')


def get_csv_data_from_url(url):
    url_response = urllib.request.urlopen(url)
    url_data = url_response.readlines()
    url_data = [line.decode('utf-8') for line in url_data]
    reader = csv.reader(url_data)
    datalist = list(reader)
    return datalist


# Part 1
def display_detail_data(data):

    # Replace the following lines with your code to print out the details
    print("Function has not been implemented")

# You can test your function by uncomment the following lines
# data = get_csv_data_from_url(marine_data)
# display_detail_data(data)


# Part 2
def display_GDP_data_year(data, year):
    # Replace the following lines with your code to print out the
    # GDP for the particular year
    return "NOT ATTEMPTED"


# Test your function by uncomment the following lines
# data = get_csv_data_from_url(marine_data)
# print(display_GDP_data_year(data, '2009'))
