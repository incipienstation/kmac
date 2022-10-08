from noun_extractor import *

path_set = ['./data/test_set0.txt', './data/test_set1.txt']

f = open('./output/output.txt', 'w', encoding="utf-8")
for path in path_set:
    f.write(parse_data(path))

f.close()
