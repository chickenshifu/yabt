#!/usr/local/bin/python3


#DataCrawler Class is passed a list of tuples which it then will parse the heck out of it from yahoo.finance.

import json
import csv
import requests
import os 
import time
import random

class DataCrawler:

    def __init__(self, symbols):

        self.symbols = symbols 

        print("Initiated DataCrawler")
        print("Received symbol list: {}".format(self.symbols))

        self.targets = self.getSymbolUrl()

        

    def getSymbolUrl(self, website=None):

        #Default is yahooFinance, if another website is about to be used, simply put yahooFinance=False and put individual code to else-block

        if website is None:

            targets = list()

            for symbol in self.symbols:
                
                baseUrl = 'https://query2.finance.yahoo.com/v8/finance/chart/{}?symbol={}&period1=0&period2=9999999999&interval=1d'.format(symbol, symbol)

                # baseUrl = 'https://de.finance.yahoo.com/quote/{}/history?period1=01&period2=1609545600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'.format(symbol)
                targets.append((symbol, baseUrl))
        
            return targets


        else:
            None




    def crawlWebsite(self):

        dir_path = os.path.dirname(os.path.realpath(__file__))

        def makeFilename(symbol, directory='data'):
            filename = dir_path + '/' + directory + '/' + '{}'.format(symbol)

            return filename


        def exportToCsv(results):

            with open(filename, 'w') as out:
                csvOut = csv.writer(out)
                csvOut.writerow(['t', 'o', 'h', 'l', 'c'])
                for row in results:
                    csvOut.writerow(row)
            print('Generated {}'.format(filename))


        for url in self.targets:
            
            filename = makeFilename(url[0])
            results = list()

            try:

                targetsJsonResponse = requests.get(url[1]).text
                timestampList = json.loads(targetsJsonResponse)['chart']['result'][0]['timestamp']
                openList = json.loads(targetsJsonResponse)['chart']['result'][0]['indicators']['quote'][0]['open']
                highList = json.loads(targetsJsonResponse)['chart']['result'][0]['indicators']['quote'][0]['high']
                lowList = json.loads(targetsJsonResponse)['chart']['result'][0]['indicators']['quote'][0]['low']
                closeList = json.loads(targetsJsonResponse)['chart']['result'][0]['indicators']['quote'][0]['close']

                time.sleep(3 + random.randint(0,2))
                
                for i in timestampList:
                    results.append((i, openList.pop(), highList.pop(), lowList.pop(), closeList.pop()))


                exportToCsv(results)

                
            except requests.exceptions.RequestException as e:  # This is the correct syntax
                raise SystemExit(e)


        



if __name__ == '__main__':

    symbols = list()
    symbols = ('ADJ.DE', 'BMW.DE', 'DTE.DE', 'SIE.DE', 'PLUG')
    

    dc = DataCrawler(symbols)
    dc.crawlWebsite()
