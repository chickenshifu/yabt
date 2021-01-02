#!/usr/local/bin/python3


#DataCrawler Class is passed a list of tuples which it then will parse the heck out of it from yahoo.finance.



import urllib.request
import os 

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

                baseUrl = 'https://de.finance.yahoo.com/quote/{}/history?period1=01&period2=1609545600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'.format(symbol)
                targets.append((symbol, baseUrl))
        
            return targets


        else:
            None





    def crawlWebsite(self):

        dir_path = os.path.dirname(os.path.realpath(__file__))

        def makeFilename(symbol, directory='data'):
            filename = dir_path + '/' + directory + '/' + '{}'.format(symbol)

            return filename


        for url in self.targets:
            filename = makeFilename(url[0])

            try:

                urllib.request.urlretrieve(url[1], filename)

            except urllib.request.ContentTooShortError as e:
                outfile = open(filename, "w")
                outfile.write(e.content)
                outfile.close()



            #Stopped here, change code so that in files only date, open, high, low, close, volume is stored

            



if __name__ == '__main__':

    symbols = list()
    symbols = ('ADJ.DE', 'BMW.DE', 'DTE.DE', 'SIE.DE', 'PLUG')
    
    dc = DataCrawler(symbols)
    dc.crawlWebsite()
