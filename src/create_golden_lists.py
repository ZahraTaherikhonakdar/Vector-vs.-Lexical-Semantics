from collections import OrderedDict
import json
from src import preprocess_data


def create_golden_lists(words, relatedwords, score, out):
    data = {}
    data['golden'] = []
    test1 = preprocess_data.delete_duplicate_words(words)
    for x in test1:
        array = {}
        array[x] = []
        r = []
        w = OrderedDict()
        for k in range(1, len(words)):
            if x == words[k] and float(score[k]) > 0 :
                r.append(relatedwords[k])
                for h in range(1, len(words)):
                    if relatedwords[k] == words[h] and float(score[h]) > 0 :
                        r.append(relatedwords[h])
        w[x] = preprocess_data.delete_duplicate_words(r)
        data['golden'].append(w)
    j = json.dumps(data)
    with open(out, 'w') as f:
        f.write(j)
    print(f'saved golden lists: \n{out}')
    return data

def save_golden_lists(golden_dataset, output_file):
    with open(golden_dataset, 'r') as token:
        lines = token.readlines()
        token1 = []
        token2 = []
        score = []

        for x in lines:
            token1.append(x.split()[0])
            token2.append(x.split()[1])
            score.append(x.split()[3])

        create_golden_lists(token1, token2, score, output_file)