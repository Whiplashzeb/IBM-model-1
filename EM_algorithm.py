class EMprocessing:
    def __init__(self, foreign_sentences_embedding, native_sentences_embedding, foreign_index_to_word,
                 native_index_to_word):
        self.foreign_sentences_embedding = foreign_sentences_embedding
        self.native_sentences_embedding = native_sentences_embedding
        self.foreign_index_to_word = foreign_index_to_word
        self.native_index_to_word = native_index_to_word

        self.t = {}
        self.denominator = {}

        for i in range(len(self.foreign_sentences_embedding)):
            for native_word in self.native_sentences_embedding[i]:
                for foreign_word in self.foreign_sentences_embedding[i]:
                    if (native_word, foreign_word) in self.t.keys():
                        self.t[(native_word, foreign_word)] += 1
                    else:
                        self.t[(native_word, foreign_word)] = 1
                    if foreign_word in self.denominator.keys():
                        self.denominator[foreign_word] += 1
                    else:
                        self.denominator[foreign_word] = 1

        for key in self.t.keys():
            self.t[key] = (1.0 / self.denominator[key[1]])

    def em_algorithm(self):
        threshold = 1e-3
        avg_change = 1

        s = {}  # key is native embedding, value is number
        count = {}  # key is (native_embedding, foreign_embdding), value is number
        total = {}  # key is foreith_embdding, value is number

        while avg_change > threshold:
            print(avg_change)
            sum_change = 0.0
            count.clear()
            total.clear()

            for i in range(len(self.foreign_sentences_embedding)):
                s.clear()
                for native_word in self.native_sentences_embedding[i]:
                    s[native_word] = 0.0
                    for foreign_word in self.foreign_sentences_embedding[i]:
                        s[native_word] += self.t[(native_word, foreign_word)]

                for native_word in self.native_sentences_embedding[i]:
                    for foreign_word in self.foreign_sentences_embedding[i]:
                        if (native_word, foreign_word) in count.keys():
                            count[(native_word, foreign_word)] += self.t[(native_word, foreign_word)] / s[native_word]
                        else:
                            count[(native_word, foreign_word)] = self.t[(native_word, foreign_word)] / s[native_word]
                        if foreign_word in total.keys():
                            total[foreign_word] += self.t[(native_word, foreign_word)] / s[native_word]
                        else:
                            total[foreign_word] = self.t[(native_word, foreign_word)] / s[native_word]

            for foreign_word in self.foreign_index_to_word:
                for native_word in self.native_index_to_word:
                    if (native_word, foreign_word) in count.keys():
                        new_t = count[(native_word, foreign_word)] / total[foreign_word]
                        sum_change += abs(new_t - self.t[(native_word, foreign_word)])
                        self.t[(native_word, foreign_word)] = new_t

            avg_change = sum_change / len(self.t)
