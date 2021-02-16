
# https://pypi.org/project/sweetviz/
# https://analyticsindiamag.com/tips-for-automating-eda-using-pandas-profiling-sweetviz-and-autoviz-in-python/

import pandas as pd
import sweetviz as sv

my_dataframe = pd.read_csv("amazon_train.csv") 

my_report = sv.analyze(my_dataframe)
my_report.show_html() # Default arguments will generate to "SWEETVIZ_REPORT.html"