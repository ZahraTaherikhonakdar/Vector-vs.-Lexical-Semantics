import pytrec_eval
import pandas as pd
import json
from collections import OrderedDict
import os
def pytrec_eval_per_word(wordsList,name):

    g = 0
    for x in wordsList:
        qrel = 0
        sample = str(x)
        if os.stat('output/cosine_similarity/w2v/{}/result_{}.xlsx'.format(name,sample)).st_size != 0:
           sheet = pd.read_excel('output/cosine_similarity/w2v/{}/result_{}.xlsx'.format(name,sample), sheet_name='cosine_sim_{}'.format(sample))
        else:
          pass
        i = 1
        j = 1
        column_value = []
        columns = len(sheet.columns)
        rows = len(sheet)
        i = 0
        simwords_list = {}
        simwords_list[sample] = []
        sim_list = {}
        sim_list[sample] = []
        if  (sheet.values).any():
            # print("len {} is".format(sample),len(simwords_list[sample]))
            for column in range(0, 2):
                # print("col is:",sheet.columns[column])
                column_value.append(sheet.columns[column])
                w = OrderedDict()
                w[sheet.loc[0][column]] = 10
                w[sheet.loc[1][column]] = 9
                w[sheet.loc[2][column]] = 8
                w[sheet.loc[3][column]] = 7
                w[sheet.loc[4][column]] = 6
                w[sheet.loc[5][column]] = 5
                w[sheet.loc[6][column]] = 4
                w[sheet.loc[7][column]] = 3
                w[sheet.loc[8][column]] = 2
                w[sheet.loc[9][column]] = 1
                # print(cars_list)
                simwords_list[sample].append(w)
            # ---SCORE GOLDEN DATA---
            j = json.dumps(simwords_list)
            with open('output/pytrec/pytrec_eval_per_word/{}/cosine_{}_data.json'.format(name,sample),
                      'w') as f:
                f.write(j)
        try:
            with open('output/gold_dataset_perword/gold_{}.json'.format(sample)) as gold:
                gold_data = json.load(gold)
            for key, value in gold_data.items():
                if value != []:
                    qrel = {
                        key: value[0]
                    }
        except KeyError:
            pass
        try:
            g += 1
            if qrel != 0:
                lis = {}
                lis["overal"] = []
                lis_cosine = {}
                lis_cosine["cosine"] = []
                with open('output/pytrec/pytrec_eval_per_word/{}/cosine_{}_data.json'.format(name,sample)) as f:
                    data = json.load(f)
                array = {}
                array[sample] = []
                r = []
                P = 0
                for column in range(0, 1, 1):
                    # print("q issss", qrel)
                    w3 = OrderedDict()
                    run = {
                        sample: data[sample][column]
                    }
                    evaluator = pytrec_eval.RelevanceEvaluator(
                        # qrel, {'success_1', 'map', 'ndcg','P_5', 'mrr', 'P_10','recall_10'})
                        qrel, {'ndcg'})
                    w3[column_value[column]] = (evaluator.evaluate(run))[sample]
                    r.append(w3)
                array[sample].append(r)
                lis_cosine["cosine"].append(array)
                lis["overal"].append(lis_cosine)
                results = json.dumps([lis_cosine])

                with open('output/pytrec/pytrec_eval_per_word/{}/pytrec_result_perword/pytrec_{}.json'.format(name,sample), 'w') as k:
                    k.write(results)
        except:
           pass

            # results = json.dumps(lis_cosine)

            # ////////////Manhattan////

            # --------euclidean------------

