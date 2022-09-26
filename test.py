from main import preprocessing_stop_words, preprocessing_sentence, get_frequency_of_words, display_get_top_list
import unittest


class TestStringMethods(unittest.TestCase):

    def test_stop_words_preprocessing(self):
        self.assertEqual(preprocessing_stop_words(stop_words=['a\n','Test Fail\n','SW1\n','SW2']), ['a', 'SW1', 'SW2'])

    def test_get_frequency_of_words(self):
        self.assertEqual(get_frequency_of_words(['This is a textbook\n', 'It has many pages\n', 'Few pages are present in mandarin'], ['a', 'are', 'is', 'in', 'it']), {'this': 1, 'textbook': 1, 'has': 1, 'many': 1, 'pages': 2, 'few': 1, 'present': 1, 'mandarin': 1})
        
    def test_preprocessing_sentence(self):
        self.assertEqual(preprocessing_sentence('This^^^is a textbook\n!@#$'), ['this', '', 'is', 'a', 'textbook', '', '', ''])
    
    def test_display_get_top_list(self):
        self.assertEqual(display_get_top_list([['These', 10], ['Good', 20], ['Words', 30]], number_of_words=100), ('Words '*30+'Good '*20+'These '*10, {'Words': 30, 'Good': 20, 'These': 10}))

if __name__ == '__main__':
    unittest.main()
