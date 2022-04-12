from models import train_w2v
from nltk.corpus import brown
from src import create_golden_lists,preprocess_data
from src.eval import evaluation,pytrec_eval_per_word,evaluation_tf_idf,pytrec_eval_perword_tfidf



dataset='dataset/SimLex-999.txt'

token = open(dataset, 'r')
linestoken = token.readlines()
resulttoken1 = []
resulttoken2 = []
resulttoken3 = []

for x in linestoken:
    resulttoken1.append(x.split()[0])
    resulttoken2.append(x.split()[1])
    resulttoken3.append(x.split()[2])
token.close()
def gold():
    gold_dataset=dataset
    print(f'creating gold standard list..\n{gold_dataset}')
    create_golden_lists.save_golden_lists(gold_dataset,'evaluation/gold_list/gold_list.json')

def w2v():
    df1 = brown.words(categories='news')
    df2 = brown.words(categories='editorial')
    print(f'preprocess training data...')
    brown_news_process= [preprocess_data.preprocess(word) for word in df1]
    brown_editorial_process = [preprocess_data.preprocess(word) for word in df2]
    train_w2v.train_model(brown_news_process, "output/models/w2v_models", "brown_news")
    train_w2v.train_model(brown_editorial_process, "output/models/w2v_models", "brown_editorial")


def eval():
    wordsList = preprocess_data.remove_words(resulttoken1)
    preprocess_data.gold_dataset_perwordd(resulttoken1)
    print("finding_similarity...")
    evaluation.finding_similarity(wordsList, 'output/models/w2v_models',"brown_news")
    evaluation.finding_similarity(wordsList, 'output/models/w2v_models', "brown_editorial")
    print("pytrec_eval_per_word...")
    pytrec_eval_per_word.pytrec_eval_per_word(wordsList,"brown_news")
    pytrec_eval_per_word.pytrec_eval_per_word(wordsList, "brown_editorial")


def tf_idf():
    df1 = brown.sents(categories='news')
    df2 = brown.sents(categories='editorial')
    evaluation_tf_idf.eval_tf_idf(df2,resulttoken1,"brown_editorial")
    evaluation_tf_idf.eval_tf_idf(df1, resulttoken1, "brown_news")

def pytrec_tfidf():
    wordsList = preprocess_data.remove_words(resulttoken1)
    preprocess_data.gold_dataset_perwordd(resulttoken1)
    print("pytrec_eval_per_word...")
    pytrec_eval_perword_tfidf.pytrec_eval_per_word(wordsList, "brown_editorial")
    pytrec_eval_perword_tfidf.pytrec_eval_per_word(wordsList, "brown_news")


if __name__ == '__main__':
    gold()
    w2v()
    eval()
    tf_idf() #train tf_idf model and find cosin similarity
    pytrec_tfidf()

