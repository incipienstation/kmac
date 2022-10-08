from soynlp.utils import DoublespaceLineCorpus
from soynlp.noun import LRNounExtractor_v2


def parse_data(path):
    sentences = DoublespaceLineCorpus(path, iter_sent=True)
    noun_extractor = LRNounExtractor_v2(verbose=True)
    nouns = noun_extractor.train_extract(sentences)

    res = ""
    for key in nouns:
        for i in range(nouns[key][0]):
            res += key
            res += " "

    return res
