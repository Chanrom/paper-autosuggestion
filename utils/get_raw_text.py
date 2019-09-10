#coding=utf-8
import os

def get_raw_doc(direcory):

    files = os.list_dir(direcory)

    corpus = []
    for file in files:

        doc = []

        # parse latex source code, convert to txt
        cmd_res = os.system(r"detex %s > %s"%(file, file + ".txt"))
        with open(file + ".txt", 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if len(line.strip()) == 0:
                    continue
                multi_sents = line.split('.')
                for sent in multi_sents:
                    doc.append(sent)


        # tokenize
        # omit
        tokenized_doc = []
        for sent in doc:
            words = sent.split(' ')
            tokenized_doc.append(words)

        corpus.append(tokenized_doc)

    return corpus




