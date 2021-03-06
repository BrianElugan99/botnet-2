'''
Created on Mar 31, 2010

@author: victorhg
'''
import unittest
from yahoo  import *

class TestGeoApi(unittest.TestCase):

    def setUp(self):
        self.yahoo = YahooGeoPlanetSearch()

    def test_return_woeid(self):
        woeid_dublin = 560743 #from yahoo
        self.yahoo.place_search("Dublin")
        self.assertEqual(1, self.yahoo.num_places())
        self.assertEqual(woeid_dublin, self.yahoo.woeid()) 

    def test_return_woeid_saoPaulo(self):
        woeid_dublin = 455827 #from yahoo
        self.yahoo.place_search("Sao Paulo")
        self.assertEqual(1, self.yahoo.num_places())
        self.assertEqual(woeid_dublin, self.yahoo.woeid())
        
    def test_number_places_without_search(self):
        self.assertRaises(SearchNotPlacedError, self.yahoo.num_places)
        
    
    def test_woeid_without_search(self):
        self.assertRaises(SearchNotPlacedError, self.yahoo.woeid)
    
    def test_ivanlid_search_expect_error(self):
        try:
            self.yahoo.place_search("")
            self.fail("should not arrive here")
        except InvalidSearchError:
            pass
                          
    def test_invalid_search(self):
        self.yahoo.place_search("John Joe Town")
        self.assertEqual(0, self.yahoo.num_places())
        self.assertRaises(InvalidSearchError, self.yahoo.woeid)

class TestWeatherRSS(unittest.TestCase):
    def testRssAccess(self):
        yahoo = YahooWeatherSearch()
        woeid_dublin = 455827
        yahoo.forecast(woeid_dublin)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_return_woeid']
    unittest.main()