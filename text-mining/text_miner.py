from soynlp.utils import DoublespaceLineCorpus
from soynlp.noun import LRNounExtractor_v2


def parse_data(path):
    sentences = DoublespaceLineCorpus(path, iter_sent=True)
    noun_extractor = LRNounExtractor_v2(verbose=True)
    nouns = noun_extractor.train_extract(sentences)

    remove_word_list = ['수', '것', '등', '안', '못', '대', '경우', '위', '아직', '비', '너무', '많이']
    for word in remove_word_list:
        nouns.pop(word, None)

    res = ""
    for key in nouns:
        for i in range(int(nouns[key][0])):
            res += key
            res += " "

    return res
