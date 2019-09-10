#coding=utf-8
import os
import argparse

from utils import get_raw_text



parser = argparse.ArgumentParser(description='Sentence AutoSuggestion for English Paper Writing')
parser.add_argument('corpus_dir', type=str, default='./raw_tex_data',
                    help='directory for corpus data')
parser.add_argument('--model_dir', type=str, default='./model_file',
                    help='trained model file')

args = parser.parse_args()


def train_ngram_model(corpus, model_dir, ngram=3):

    # n-gram model

    # dictionay initial
    ngram_dict = {}
    for i in range(N):
        ngram_dict[i] = {}

    for doc in corpus:
        for sent in doc:
            


def main():
    if not os.path.exists(corpus_dir):
        raise Error("Can not find corpus_dir!");

    if not os.path.exists(model_dir):
        print("model_dir not find, create a model_dir: %s"%model_dir)
        os.path.mkdir(model_dir)
        
    # corpus is a list of docs, doc is a list of sentences, sentence is a 
    # list of words, word is string.
    corpus = get_raw_text(corpus_dir)

    train_ngram_model(corpus, model_dir)


if __name__ == '__main__':
    main()
