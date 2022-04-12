import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src import preprocess_data
import xlsxwriter


def eval_tf_idf(data,word_list,name):
    array = preprocess_data.delete_duplicate_words(word_list)
    data1 = []
    for i in data:
        data1.append(" ".join(i))
    print(f'preprocess training data...')
    # settings that you use for count vectorizer will go here
    tfidf_vectorizer = TfidfVectorizer(use_idf=True)
    # just send in all your docs here
    tfidf_vectorizer_vectors = tfidf_vectorizer.fit_transform(data1)
    tfidf_vectorizer_query = tfidf_vectorizer.fit(data1)
    # /////evaluate section/////
    for x in array:
        sample = str(x)
        sort_cosine = []
        query_tfidf = tfidf_vectorizer_query.transform([sample])
        cosineSimilarities = cosine_similarity(query_tfidf, tfidf_vectorizer_vectors).flatten()
        score = np.argsort(cosineSimilarities)[-10:][::-1]
        word = tfidf_vectorizer.vocabulary_.keys()
        vocab = []
        for i in word:
            vocab.append(i)
        for k in score:
            sort_cosine.append([vocab[k]])
        for i in range(len(sort_cosine)) :
            print("::    issssss: ", sort_cosine[i][0])
        workbook = xlsxwriter.Workbook('output/cosine_similarity/tfidf/{}/result_{}.xlsx'.format(name,sample))  # pass the output path as an argument
        worksheet1 = workbook.add_worksheet('cosine_sim_{}'.format(sample))
        a = 0
        h = 0
        if len(sort_cosine) != 0:
            x = 1
            worksheet1.write(0, h, "tf_idf")
            for i in range(len(sort_cosine)):
                    worksheet1.write(x, a, sort_cosine[i][0])
                    # worksheet1.write(x, a + 1, sim)
                    x += 1
            a += 2
            h += 2
        workbook.close()

