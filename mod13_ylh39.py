import unittest
import forms
import time
import datetime
#导入date



class TestSymbol(unittest.TestCase):

    def test_symbol(self):
        #检查symbol是不是小于7个的大写字母
        self.assertTrue(forms.symbol.data.isupper() and len(forms.symbol.data) <= 7, "Symbol must be upper case and less than 7 characters")
    def test_chart_type(self):
        #检查chart_type是不是1或者2
        self.assertTrue(forms.chart_type.data == "1" or forms.chart_type.data == "2", "Chart type must be 1 or 2")
    def time_series(self):
        #如果time_series不是1，2，3，4，就报错
        self.assertTrue(forms.time_series.data == "1" or forms.time_series.data == "2" or forms.time_series.data == "3" or forms.time_series.data == "4", "Time series must be 1, 2, 3, or 4")
    def test_start_date(self):
        #如果start_date不是YYYY-MM-DD格式的日期，就报错
        self.assertTrue(forms.start_date.data == date.today(), "Start date must be in YYYY-MM-DD format")
    def test_end_date(self):
        #如果end_date不是YYYY-MM-DD格式的日期，就报错
        self.assertTrue(forms.end_date.data == date.today(), "End date must be in YYYY-MM-DD format")

if __name__ == "__main__":
    unittest.main()