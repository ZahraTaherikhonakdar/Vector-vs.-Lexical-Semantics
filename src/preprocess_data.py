from nltk import word_tokenize
from nltk.corpus import stopwords
import json
from collections import OrderedDict

stop_words = stopwords.words('english')


def preprocess(text):
    text = text.lower()  # To lower
    doc = word_tokenize(text)  # Tokenize to words
    doc = [word for word in doc if word not in stop_words]  # Remove stopwords.
    doc = [word for word in doc if word.isalpha()]  # Remove numbers and special characters
    return doc


# ---DELETING DUPLICATE WORDS---
def delete_duplicate_words(x):
    test = []
    for i in range(0, len(x)):
        if len(test) == 0:
            test.append(x[i])
        if x[i] in test:
            None
        else:
            test.append(x[i])
    return test

# /////remove out of words and zero-goldstanderd words
def remove_words(words):
    outofwords_array = ['word1']
    test=delete_duplicate_words(words)
    final_array=[]
    with open('evaluation/gold_list/gold_list.json') as f:
        data_gold = json.load(f)
    array_withgold = []
    array_withoutgold = []
    for key, value in data_gold.items():
        print("key is ", key)
        print("value is ", value)
        i = 0
        j = 0
        for x in test:
            sample = str(x)
            if value[i][sample] == [] :
              j += 1
              array_withoutgold.append(sample)
              print("nulls issss", value[i])
            else:
               array_withgold.append(sample)
            i += 1

    for i in range(0, len(array_withgold)):
        if array_withgold[i] in outofwords_array:
            None
        else:
            final_array.append(array_withgold[i])

    final=delete_duplicate_words(final_array)
    return final
# //////////////////////
def gold_dataset_perwordd(words):
    with open('evaluation/gold_list/gold_list.json') as f:
        gold_data_final = json.load(f)
    g = 0
    test = delete_duplicate_words(words)
    print("test is:", words)
    for x in test:
        sample = str(x)
        sim_list = {}
        sim_list[sample] = []
        if len(gold_data_final["golden"][g][sample]) != 0:
            a = OrderedDict()
            v = 10
            for k in range(0, len(gold_data_final["golden"][g][sample])):
                a[gold_data_final["golden"][g][sample][k]] = v
                if (a not in sim_list[sample]):
                   sim_list[sample].append(a)
                v -= 1

        j_gold = json.dumps(sim_list)
        print(j_gold)
        with open('output/gold_dataset_perword/gold_{}.json'.format(sample), 'w') as gold:
            gold.write(j_gold)
        g += 1

