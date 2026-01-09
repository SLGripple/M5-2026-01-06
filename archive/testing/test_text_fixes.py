"""
Unit tests for clean_library_data module
"""
import unittest
import pandas as pd
from datetime import datetime
from clean_library_data import clean_text, days_on_loan



class TestCleanText(unittest.TestCase):
    """Test the clean_text function"""
    
    def test_removes_quotes(self):
        """Test that quotes are removed"""
        data = pd.Series(['"Hello"', '"World"'])
        result = clean_text(data)
        self.assertEqual(result[0], 'Hello')
        self.assertEqual(result[1], 'World')
    
    def test_fixes_date(self):
        """Test that invalid date is corrected"""
        data = pd.Series(['32/05/2023', '01/05/2023'])
        result = clean_text(data)
        self.assertEqual(result[0], '31/05/2023')
        self.assertEqual(result[1], '01/05/2023')
    
 
        
# Run tests
if __name__ == '__main__':
    unittest.main()