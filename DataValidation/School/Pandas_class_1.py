import pandas

data1 = open('./school_test_data/Performance_Summary_By_Merchant.csv', 'r', encoding='UTF-8')
data2 = open('./school_test_data/Performance_Summary_By_Merchant copy.csv', 'r', encoding='UTF-8')

class Comparison:

    def __init__(self):
        self.data1 = pandas.DataFrame()
        self.data2 = pandas.DataFrame()
        self.bool_table = pandas.DataFrame()
        self.discrepancies = []
        self.matches = []
        self.column_names = []

    def load(self, report_1, report_2):
        # Convert Report 1 Data to DataFrame
        self.data1 = pandas.read_csv(report_1)
        # Convert Report 2 Data to Dict
        self.data2 = pandas.read_csv(report_2)
        self.column_names = list(self.data1)

    def modify(self, col, row, val, report_number):
        #@TODO ask adam how to do tertiary operators in python
        if report_number == 1:
            self.data1.iloc[col, row] = val
        else:
            self.data2.iloc[col, row] = val

    def list_discrepancies(self):
        for row_idx, row in enumerate(self.bool_table):
            for col_idx, col in enumerate(self.column_names):
                if self.bool_table.iloc[row_idx, col_idx] != True:
                    self.discrepancies.append(self.data1.iloc[row_idx, :])
                    self.discrepancies.append(self.data2.iloc[row_idx, :])
                elif self.bool_table.iloc[row_idx, col_idx] != False:
                    self.matches.append(self.data1.iloc[row_idx, :])
                    self.matches.append(self.data2.iloc[row_idx, :])



        return self.discrepancies

    def bool_compare(self):
        #@TODO note: modification
        self.modify(0, 0, 0, 1)
        self.bool_table = self.data1 == self.data2
        return self.bool_table


tester = Comparison()
tester.load(data1, data2)

tester.bool_compare()
print(tester.list_discrepancies())
print(tester.matches)


