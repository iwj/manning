# -*- coding:utf-8 -*-
# 保持原格式，将数据保存到文件里

import pickle

my_list = ["Apple", "Google", "Microsoft", "Twitter", 15548972617]
pickle_file = open("note_p.txt", "w")
pickle.dump(my_list, pickle_file)
pickle_file.close()


pick_load = open("note_p.txt", "r")
recover_list = pickle.load(pick_load)
pick_load.close()
print recover_list
