import json
from itertools import chain

def pytrec_avg_w2v(g,name):
    array = [g]
    j = 0
    c = 0
    r = 1
    array_cosine = {}
    array_cosine["cosine"] = []
    # /////////cosine///////////////////
    overal_cosine = {}
    overal_cosine["w2v_{}".format(name)] = []
    sum_cosine_ndcg = 0
    cosine_array = []
    l = []
    num = 0
    for x in array:
        sample = str(x)
        with open('output/pytrec/pytrec_eval_per_word/{}/pytrec_result_perword/pytrec_{}.json'.format(name,sample)) as k:
            result = json.load(k)

        sum_cosine_ndcg += result[0]["cosine"][0][sample][0][j]["w2v_{}".format(name)]["ndcg"]

        num += 1
    # //////cosine///////////
    avg_cosine_ndcg = sum_cosine_ndcg / num
    cosine_array.append(
        [ "ndcg :", avg_cosine_ndcg])
    overal_cosine["w2v_{}".format(name)].append(cosine_array)
    array_cosine["cosine"].append(overal_cosine)

    j += 1

    j = json.dumps([array_cosine])
    with open('output/avg/w2v/ndcg_avg_{}.json'.format(name), 'w') as f:
         f.write(j)
    with open('output/avg/w2v/ndcg_avg_{}.json'.format(name)) as f:
         data = json.load(f)
    print("result is ", data)

def pytrec_avg_tfidf(g,name):
    array = [g]
    j = 0
    c = 0
    r = 1
    array_cosine = {}
    array_cosine["cosine"] = []
    # /////////cosine///////////////////
    overal_cosine = {}
    overal_cosine["tf_idf"] = []
    sum_cosine_ndcg = 0
    cosine_array = []
    l = []
    num = 0
    for x in array:
        sample = str(x)
        with open('output/pytrec/tfidf_pytrec_perword/{}/pytrec_result_perword/pytrec_{}.json'.format(name,sample)) as k:
            result = json.load(k)

        sum_cosine_ndcg += result[0]["cosine"][0][sample][0][j]["tf_idf"]["ndcg"]

        num += 1
    # //////cosine///////////
    avg_cosine_ndcg = sum_cosine_ndcg / num
    cosine_array.append(
        [ "ndcg :", avg_cosine_ndcg])
    overal_cosine["tf_idf"].append(cosine_array)
    array_cosine["cosine"].append(overal_cosine)

    j += 1

    j = json.dumps([array_cosine])
    with open('output/avg/tf_idf/ndcg_avg_{}.json'.format(name), 'w') as f:
         f.write(j)
    with open('output/avg/tf_idf/ndcg_avg_{}.json'.format(name)) as f:
         data = json.load(f)
    print("result is ", data)

