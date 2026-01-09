import unittest
from python.app_refactored import enrich_dateDuration

class TestLibClean(unittest.TestCase):
    
    def setUp(self):
        self.csv_path = r"data\load_data_cleaned.csv"
        self.df = enrich_dateDuration(self.csv_path)

    def test_days_on_loan_column(self):
        "Check Existence of Days On Loan column"
        self.assertIn('Days On Loan',self.df.columns)

    def test_days_on_loan_values(self):
        "Check correctness of Days On Loan values"
        for idx, row in self.df.iterrows():
            expected_days = (row['Book Returned']-row['Book checkout']).days
            self.assertEqual(row['Days On Loan'], expected_days)    
    
if __name__ == '__main__':
        unittest.main()