from text_miner import *

path_set = ['./input/input.txt']

f = open('./output/output.txt', 'w', encoding="utf-8")
for path in path_set:
    f.write(parse_data(path))

f.close()
