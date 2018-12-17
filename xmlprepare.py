import numpy as np
import xml.etree.ElementTree as ET
from collections import Counter
import nltk
from utils import read_xml, read
def tokenize(strs):
    """
    the tokenizer
    """
    tmp_text = nltk.word_tokenize(strs)
    text = []
    for w in tmp_text:
        if w == "'s" or w == "'t" or w == "n't" or w == "t's":
            text.append(w)
        else:
            w = w.replace('.', ' . ')
            w = w.replace("'", " ' ")
            w = w.replace("' t", "n't")
            w = w.replace("555", " 555 ")
            w = w.replace("+", " + ")
            w = w.replace("/", " / ")
            # w = w.replace("pm", " pm ")
            # w = w.replace("am", " am ")
            ws = nltk.word_tokenize(w)
            for sw in ws:
                text.append(sw)
    return text


if __name__ == '__main__':
    # dataset_txt = read("./dataset/14semeval_laptop/train.txt")
    # dataset_xml = read_xml("./dataset/Laptops_Train.xml")
    # #dataset_xml = read_xml("testxml.xml")
    # print("txt:", len(dataset_txt))
    # print("xml:", len(dataset_xml))
    with open("./embeddings/aaa.txt") as f:
        for line in f:
            print(line)


