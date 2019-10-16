import numpy as np
import re
import text_rank
import SIF
from gensim.models import FastText
from scipy.spatial.distance import cosine
import os


class summary(object):
    def __init__(self):
        module_path = os.path.dirname(__file__)
        self.frequency = self.get_frequency()
        self.main_components = self.get_main_components()
        self.model = FastText.load(module_path + '/files/summar_word2vec.model')

    @staticmethod
    def get_frequency():
        frequency = {}
        module_path = os.path.dirname(__file__)
        with open(module_path + '/files/frequency.txt', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if line.isspace():
                    continue
                split = line.split(':')
                if len(split) == 2:
                    frequency[split[0]] = np.float(split[1])
                else:
                    print(line)
        return frequency

    # 返回所有语料的主成分
    @staticmethod
    def get_main_components():
        return np.array([[-0.4075085, 0.46341956, 0.22864994, -0.37592185, 0.57946825,
                          0.3223162, 0.5950196, 0.575565, -0.77002096, 0.00721647,
                          -0.04891372, 0.02568915, 1.1436454, -0.3816676, -0.664325,
                          -0.02268074, -0.28247282, 0.40628374, -0.22506855, -1.3382728,
                          -0.3288292, 0.3479149, 0.18223703, 0.51829654, 0.15035069,
                          0.0768308, -1.4970351, 0.5827559, 0.9541795, 0.17189902,
                          -0.1513894, 0.05673018, -0.60152435, 0.34114635, -0.1435481]], dtype=np.float32)

    def get_corrlations(self, text):
        if isinstance(text, list):
            text = ' '.join(text)
        sub_sentences = text_rank.split_sentence(text)
        sentence_vector = SIF.sentence_embedding(text, self.frequency, self.model, self.main_components)
        correlations = {}
        for sub_sentence in sub_sentences:
            sub_sen_vec = SIF.sentence_embedding(sub_sentence, self.frequency, self.model, self.main_components)
            correlation = cosine(sentence_vector, sub_sen_vec)
            correlations[sub_sentence] = correlation
        return sorted(correlations.items(), key=lambda x: x[1], reverse=True)

    def get_summary_simple_by_sen_embedding(self, text, constraint=200):
        return text_rank.get_summarization_simple(text, self.get_corrlations, constraint)
