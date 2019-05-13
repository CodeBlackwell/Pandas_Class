import pandas
from datetime import datetime, timedelta

data1 = open('./school_test_data/Performance_Summary_By_Merchant.csv', 'r', encoding='UTF-8')
data2 = open('./school_test_data/Performance_Summary_By_Merchant copy.csv', 'r', encoding='UTF-8')

print(data1)

class Comparison:
    def __init__(self):
        self.data1 = ''
        self.data2 = ''
    def load(self, report_1, report_2):
        # Convert Report 1 Data to DataFrame
        self.data1 = pandas.read_csv(report_1)
        # Convert Report 2 Data to Dict
        self.data2 = pandas.read_csv(report_2)
