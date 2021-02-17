
# https://pypi.org/project/sweetviz/
# https://analyticsindiamag.com/tips-for-automating-eda-using-pandas-profiling-sweetviz-and-autoviz-in-python/

import pandas as pd
import sweetviz as sv

my_dataframe = pd.read_csv("data/amazon_train.csv") # amazon dataframe

titanic_train = pd.read_csv("data/train.csv") # titanic train
titanic_test = pd.read_csv("data/test.csv") # titanic test

my_report = sv.analyze(titanic_train)
my_report.show_html() # Default arguments will generate to "SWEETVIZ_REPORT.html"