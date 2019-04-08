class DataProcess:
    def __init__(self, src_file):
        """
        初始化
        src_file为语料文件
        sentences为语料中的句子
        sentences_embedding为语料转化为索引后句子的list
        word_to_index为单词到索引的dict
        index_to_word为索引到单词的dict
        :param src_file:
        """
        self.__src_file = src_file
        self.__sentences = []
        self.__word_to_index = {}
        self.sentences_embedding = []
        self.index_to_word = {}

    def __read_data(self):
        """
        读取语料
        :return:
        """
        with open(self.__src_file) as fp:
            self.__sentences = fp.readlines()

    def __word_index(self):
        """
        将单词转化为索引
        :param sentences: 语料
        :return:
        """

        index = 0

        for sentence in self.__sentences:
            for word in sentence.split():
                word = word.lower()
                if word not in self.__word_to_index.keys():
                    self.__word_to_index[word] = index
                    self.index_to_word[index] = word
                    index += 1

    def __sentence_to_embedding(self):
        """
        将句子转换为索引的序列
        :return:
        """
        for sentence in self.__sentences:
            sentence_index = []
            for word in sentence.split():
                sentence_index.append(self.__word_to_index[word.lower()])
            self.sentences_embedding.append(sentence_index)

    def process(self):
        """
        运行读取数据，转换索引，以及将句子转换为embedding
        :return:
        """
        self.__read_data()
        self.__word_index()
        self.__sentence_to_embedding()
