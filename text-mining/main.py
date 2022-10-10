from text_miner import *

src_list = ['advantages.txt', 'disadvantages.txt']

for src in src_list:
    f = open('./output/' + src, 'w', encoding="utf-8")
    f.write(parse_data('./input/' + src))
    f.close()

