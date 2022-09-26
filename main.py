from wordcloud import WordCloud
import matplotlib.pyplot as plt

''' load data of stop words and novel text '''
def loading_data():
    # reading of mobydick novel data
    with open('data/mobydick.txt', 'r') as f:
        text_book = f.readlines()

    # reading of stop words data
    with open('data/stop-words.txt', 'r') as f:
        stop_words = f.readlines()
    return text_book, stop_words

''' 
stop_words: stop words are in array of text format as read from file
returns: stop_word_preprocessed: stop_words in list format
'''
def preprocessing_stop_words(stop_words):
    stop_word_preprocessed = []
    is_start = False
    for stop_word_raw in stop_words:
        # starting to calculate the stop words from 'a' as it can be analysed via the text file
        if not is_start and stop_word_raw == 'a\n':
            is_start = True
        # if is_start = True depicts stop words can be analysed after 'a' text is analysed in the file.
        # stop words are >= 2 which will ignore "\n" from the list
        # "stop_word_raw not in stop_word_preprocessed" is used for getting only unique stop words len(stop_word_array) == 1 
        # is used to verify stop word should be of length 1
        stop_word_array = stop_word_raw.split(' ')
        if is_start and len(stop_word_raw) >= 2 and stop_word_raw not in stop_word_preprocessed and len(stop_word_array) == 1:
            stop_word_preprocessed.append(stop_word_raw.replace('\n', ''))
    return stop_word_preprocessed

''' 
sentence: contains single sentence of a textbook in string format
returns: preprocessed sentence by removing symbols, making sentence lowercase and splitting sentence into words  
'''
def preprocessing_sentence(sentence):
    words_for_removal = ['\n', '  ', '.', '-', '—', ',', '/', '<', '>', '?',':',';','"','“', '”', '’s', '’ll', '{','}','[',
                        ']','!', '@', '#','$', '%', '^', '&', '*', '(', ')', '_', '+', '*', '`', '~', '=']
    for word_for_removal in words_for_removal:
        sentence = sentence.replace(word_for_removal, ' ')
    sentence = sentence.replace('  ', ' ').lower().split(' ')
    return sentence

''' 
frequency_text: depicts words in comma separated format for example if word1 has frequency 2 and word2 has frequency 3 then text will be of the form
                "word1 word1 word2 word2 word2"
    
returns: NA (saves word-cloud in output file)
'''
def generate_word_cloud(frequency_text):
    word_cloud = WordCloud(collocations = False, background_color = 'white').generate(frequency_text)
    fig, ax = plt.subplots()
    ax.imshow(word_cloud, interpolation='bilinear')
    ax.axis("off")
    fig.set_figheight(10)
    fig.set_figwidth(10)
    plt.savefig('output/word-cloud.png')

''' 
frequency_dict: depicts words and its frequency
    
returns: NA (saves frequency-distribution in output file)
'''
def generate_frequency_distribution(frequency_dict):
    fig, ax = plt.subplots()
    ax.bar(frequency_dict.keys(), height=frequency_dict.values())
    plt.xticks(rotation=90)
    fig.set_figheight(25)
    fig.set_figwidth(25)
    ax.set_title('Frequency Distribution Of Words')
    plt.savefig('output/frequency-distribution.png')

''' 
text_book: depicts the text of whole text_book and having list of sentences
stop_word_preprocessed: depicts stop words in list format
    
returns: words_frequency (all the words with frequency in dictionary format example {word1: frequency1, word2: frequency2})
'''
def get_frequency_of_words(text_book, stop_word_preprocessed):
    words_frequency = {}
    for sentence in text_book:
        # preprocessing in sentence level
        sentence = preprocessing_sentence(sentence)
        for word in sentence:
            # ignoring single letter word which isn't in stop word as well which will be essentially symbols which need not be considered for word count
            if word in stop_word_preprocessed or len(word) <= 1:
                continue
            # finding uniqueness of a word
            if word not in words_frequency:
                words_frequency[word] = 1
            else:
                words_frequency[word] += 1
    return words_frequency

''' 
sorted_frequency_list: depicts the sorted version of frequency list
number_of_words: depicts selection of top x words where x = number_of_words
    
returns: frequency_text (all the frequenly occuring word in the textual form For example if Word1 appears 5 times and word2 appears 2 times
                        then the text will be "word1 word1 word1 word1 word1 word2 word2" This is the word cloud's format
         frequency_dict (all the words with frequency in dictionary format example {word1: frequency1, word2: frequency2})
     
'''
def display_get_top_list(sorted_frequency_list, number_of_words=100):
    frequency_text = ''
    frequency_dict = {}
    for f_list in reversed(sorted_frequency_list[-1*number_of_words:]):
        print("Word:", f_list[0].title(), "Frequency:", f_list[1])
        # creating text for word cloud
        frequency_text += (f_list[0].title() + ' ') * f_list[1]
        frequency_dict[f_list[0].title()] = f_list[1]
    return frequency_text, frequency_dict
    
    
def main():
    text_book, stop_words = loading_data()
    stop_word_preprocessed = preprocessing_stop_words(stop_words)
    # these are few words analysed which were causing issue in calculating the actual word count, so these words are removed from 
    # the sentence 
    words_frequency = get_frequency_of_words(text_book, stop_word_preprocessed)

    # sorting the list by frequency
    sorted_frequency_list = [[k,v] for k, v in sorted(words_frequency.items(), key=lambda item: item[1])]

    # printing the required list and getting back the frequenly occuring text for visualization
    frequency_text, frequency_dict = display_get_top_list(sorted_frequency_list, 100)

    # creation of word cloud
    generate_word_cloud(frequency_text)
    # generating frequency distribution of words
    generate_frequency_distribution(frequency_dict)


if __name__ == '__main__':
    main()
