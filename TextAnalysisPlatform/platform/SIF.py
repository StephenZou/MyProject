import jieba
import numpy as np


def sentence_embedding(sentence, frequency, model, main_components):
    words = jieba.cut(sentence)
    max_fre = max(frequency.values())
    sentence_vec = np.zeros_like(model.wv['测试'])
    words = [w for w in words if w in model]
    alpha = 1e-4
    for w in words:
        weight = alpha/(alpha + frequency.get(w, max_fre))
        sentence_vec += weight * model.wv[w]
    sentence_vec /= len(words)
    # 减去主成分
    sentence_vec = sentence_vec - sentence_vec.dot(main_components.transpose())*main_components
    return sentence_vec
