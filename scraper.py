import requests
from bs4 import BeautifulSoup

def main(args):
    carbonDioxide = requests.get('https://climate.nasa.gov/vital-signs/carbon-dioxide/')
    globalTemperature = requests.get('https://climate.nasa.gov/vital-signs/global-temperature/')
    seaLevelMinimum = requests.get('https://climate.nasa.gov/vital-signs/arctic-sea-ice/')
    seaLevel = requests.get('https://climate.nasa.gov/vital-signs/sea-level/')

    if 200 not in {carbonDioxide.status_code, globalTemperature.status_code, seaLevelMinimum.status_code, seaLevel.status_code}:
        print('One or more page(es) are not loading correctly')
        exit()

    carbonDioxideSoupData = BeautifulSoup(carbonDioxide.content, 'html.parser').find("div", {"class": "value"}).text.split(' ')[0].strip()
    globalTemperatureSoupData = BeautifulSoup(globalTemperature.content, 'html.parser').find("div", {"class": "value"}).text.split('°')[0].strip()
    seaLevelMinimumSoupData = BeautifulSoup(seaLevelMinimum.content, 'html.parser').find("div", {"class": "change_number"}).text.strip()
    seaLevelSoupData = BeautifulSoup(seaLevel.content, 'html.parser').find("div", {"class": "value"}).text.strip().split(' ')[0]

    return {'carbonDioxide' : float(carbonDioxideSoupData), 'globalTemperature' : float(globalTemperatureSoupData), 'seaLevelMinimum' : float(seaLevelMinimumSoupData), 'seaLevelCurrent' : float(seaLevelSoupData)}
