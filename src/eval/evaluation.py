from gensim.models import Word2Vec
import numpy as np
import xlsxwriter
from src import preprocess_data
from itertools import chain

# ---FINDING SIMILARITY---
def finding_similarity(word_list, path, name, self=None):
    array =preprocess_data.delete_duplicate_words(word_list)
    outofwords = 0
    array_outofwords=[]
    for x in array:
        sort_cosine = []
        sample = str(x)
        model = Word2Vec.load("{}/w2v_{}".format(path, name))
        print(f'loading w2v model ...\n {path}/w2v_{name})')
        model.init_sims(replace=True)
        for word in model.wv.key_to_index :
            try:
              # y = model.wv.most_similar(model.wv[sample])
                y = model.wv[sample]
            except KeyError:
                outofwords += 1
                array_outofwords.append(sample)
                break
            try:
              y = model.wv[sample]
            except KeyError:
                break
            sort_cosine.append(["w2v_{}".format(name), model.wv.most_similar([sample])])


        # print(sort_euclidean_dis[6][0])
        workbook = xlsxwriter.Workbook('output/cosine_similarity/w2v/{}/result_{}.xlsx'.format(name,sample)) #pass the output path as an argument
        worksheet1 = workbook.add_worksheet('cosine_sim_{}'.format(sample))


        a = 0
        h = 0
        if len(sort_cosine) != 0:
            for i in range(0, 1):
                sort_c = sort_cosine[i]
                worksheet1.write(0, h, sort_c)
                sort_c1 = sort_cosine
                x = 1
                for word in sort_c1:
                    worksheet1.write(x, a, word)

                    x += 1
                a += 2
                h += 2



        workbook.close()