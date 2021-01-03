#DataHandler feeds the Queue with timeseries data

import pandas as pd
import os

class DataHandler:

    dir_path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, path=dir_path, o=False, h=False, l=False, c=False):

        self.path = path + '/data'
        print("Initialised DataHandler with dir_path: {}".format(self.path))

        

    def importDataToPd(self):
        
        self.dataframes = list()
        all_files = os.listdir(self.dir_path + '/data/') 

        for file in all_files:
            full_filename = str(self.dir_path) + '/data/' + str(file)

            df_file = pd.read_csv(full_filename)
            
            df_file['t'] = pd.to_datetime(df_file['t'], format='%Y-%m-%d %H:%M:%S')
            df_file = df_file.set_index('t')
            
            #Add symbol to column names to better identify data
            df_file.columns = ['o_{}'.format(file), 'h_{}'.format(file), 'l_{}'.format(file), 'c_{}'.format(file)]
#            df_file = df_file.dropna()
            
            self.dataframes.append(df_file)

        #Bring all dataframes together
        self.final_data = pd.concat(self.dataframes, join='outer')
        print(self.final_data)
        return self.final_data


    #Main function - exportData() will by default pass the close price of each asset as return value to consumer
    #but by setting each other variable to True, exportData yields the whole data set.
    def getData(self, price=None):

        self.importDataToPd()
       
        
        if price is None:
            closePrices = [col for col in self.final_data if col.startswith('c')]
            print("### Excerpt of close data for all symbols: ### \n  {}".format(self.final_data[closePrices].head()))
            return self.final_data[closePrices]

        elif price == 'open':
            openPrices = [col for col in self.final_data if col.startswith('o')]
            print("### Excerpt of open data for all symbols: ### \n  {}".format(self.final_data[openPrices].head()))
            return self.final_data[openPrices]

        elif price == 'high':
            highPrices = [col for col in self.final_data if col.startswith('h')]
            print("### Excerpt of high data for all symbols: ### \n  {}".format(self.final_data[highPrices].head()))
            return self.final_data[highPrices]

        elif price == 'low':
            lowPrices = [col for col in self.final_data if col.startswith('l')]
            print("### Excerpt of low data for all symbols: ### \n  {}".format(self.final_data[lowPrices].head()))
            return self.final_data[lowPrices]

        else:
            raise ValueError('Invalid Price argument, use either: open, high or low')
        

if __name__ == '__main__':
    dh = DataHandler(h=True)
    #dh.getData()
    dh.importDataToPd()
