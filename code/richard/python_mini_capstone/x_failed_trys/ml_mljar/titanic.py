# work on this on wednesday 2/16

# https://mljar.com/
# https://mljar.com/automl-compare/
# https://github.com/mljar/mljar-supervised

"""AutoML code """
import pandas as pd
from supervised import AutoML

# Load data
train = pd.read_csv("/data/train.csv")
test = pd.read_csv("/data/test.csv")
x_cols = train.columns[2:]

# Train AutoML
automl = AutoML(mode="Compete", total_time_limit=4*3600)
automl.fit(train[x_cols], train["target"])


'''
# Prepare submission
sub = pd.read_csv("/your_path/sample_submission.csv")
sub["target"] = automl.predict_proba(test)[:,1]
sub.to_csv("submission.csv", index=False)
'''