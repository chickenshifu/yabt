# Welcome to **yabt** - yet another backtesting framework!

**This framework is developed for educational purposes only. If - for any reason - anyone likes to contribute or to fork this project, please feel absolutely free.**

## 1. Strucutre
yabt is to be build on the following fundamental modules:
* DataCrawler
* DataHandler
* Tardis
* Portfolio
* ExecutionHandler
* Riskmanager
* Tradejournal
* Reporter

## 2. Deep dive into each module
![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **DataCrawler**  ![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+)       

The DataCrawler module is one of the most intuitive modules. It will parse whatever data or website you want to be parsed. At this time it is meant to download data from yahoo.finance.
It saves all data into .csv files, as this is one of the most efficient ways to store financial data.

***Ideas for future versions / features***

At the moment it is planned to execute DataCrawler every time a new backtest is run. So new .csv files are generated each time. A future version should include the feature, that DataCrawler (or DataHandler) should search for the already existing data in dir data/ and only append .csv files for missing values (e.g. if you would expand your backtest period to the future).



**DataHandler**

The DataHandler module is the building block between Tardis and the DataCrawler. It is given a list of symbols and stores those symbolds into sqlite database.
