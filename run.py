import os
import importlib
import sys
from data_processing import DataProcess
from EM_algorithm import EMprocessing

importlib.reload(sys)


if __name__ == "__main__":
    foreign_file = os.path.join(os.path.abspath('..'), 'IBM-model-1/data', 'fbis.en.10k')
    native_file = os.path.join(os.path.abspath('..'), 'IBM-model-1/data', 'fbis.zh.10k')

    # 数据预处理
    foreign_data_process = DataProcess(foreign_file)
    native_data_process = DataProcess(native_file)

    foreign_data_process.process()
    native_data_process.process()

    foreign_sentences_embedding, foreign_index_to_word = foreign_data_process.sentences_embedding, foreign_data_process.index_to_word
    native_sentences_embedding, native_index_to_word = native_data_process.sentences_embedding, native_data_process.index_to_word

    # em算法执行
    em_process = EMprocessing(foreign_sentences_embedding, native_sentences_embedding, foreign_index_to_word,
                              native_index_to_word)

    em_process.em_algorithm()
    t = sorted(em_process.t.items(), key=lambda kv: kv[1])

    # 结果存储
    if not os.path.exists(os.path.join(os.path.abspath('..'), 'IBM-model-1/result')):
        os.mkdir(os.path.join(os.path.abspath('..'), 'IBM-model-1/result'))

    result_file_src = os.path.join(os.path.abspath('..'), 'IBM-model-1/result', 't.txt')

    with open(result_file_src, 'w') as file_write:
        for k, v in t.items():
            native_word = native_index_to_word[k[0]]
            foreign_word = foreign_index_to_word[k[1]]
            file_write.write("%s\t%s\t%s\n" % (native_word, foreign_word, v))
