# https://auto.gluon.ai/stable/tutorials/tabular_prediction/tabular-quickstart.html

import autogluon as ag
from autogluon import TabularPrediction as task

train_data = task.Dataset(file_path='https://autogluon.s3.amazonaws.com/datasets/Inc/train.csv')
subsample_size = 500  # subsample subset of data for faster demo, try setting this to much larger values
train_data = train_data.sample(n=subsample_size, random_state=0)
# print(train_data.head())

label_column = 'class'
print("Summary of class variable: \n", train_data[label_column].describe())

dir = 'agModels-predictClass'  # specifies folder where to store trained models
# predictor = task.fit(train_data=train_data, label=label_column, output_directory=dir)

test_data = task.Dataset(file_path='https://autogluon.s3.amazonaws.com/datasets/Inc/test.csv')
y_test = test_data[label_column]  # values to predict
test_data_nolab = test_data.drop(labels=[label_column],axis=1)  # delete label column to prove we're not cheating
print(test_data_nolab.head())

predictor = task.load(dir)  # unnecessary, just demonstrates how to load previously-trained predictor from file

y_pred = predictor.predict(test_data_nolab)
print("Predictions:  ", y_pred)
perf = predictor.evaluate_predictions(y_true=y_test, y_pred=y_pred, auxiliary_metrics=True)