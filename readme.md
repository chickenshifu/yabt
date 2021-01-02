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
**DataCrawler**

The DataCrawler module is one of the most intuitive modules. It will parse whatever data or website you want to be parsed. At this time it is meant to download data from yahoo.finance.
It saves all data into .csv files, as this is one of the most efficient ways to store financial data.

**DataHandler**

The DataHandler module is the building block between Tardis and the DataCrawler. It is given a list of symbols and stores those symbolds into sqlite database.
