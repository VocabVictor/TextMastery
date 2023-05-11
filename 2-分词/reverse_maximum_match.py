def reverse_maximum_match(text, word_dict):
    result = []                                          # 存储分词结果
    max_length = max(len(word) for word in word_dict)    # 词典中最长词的长度

    while text:
        word = text[-max_length:]                        # 从尾部开始取最长词的长度的子串
        while len(word) > 1 and word not in word_dict:
            word = word[1:]                              # 若不在词典中，则逐渐缩小子串的长度
        result.insert(0, word)                           # 将分词结果插入到列表的开头
        text = text[:len(text) - len(word)]              # 剩余文本继续进行分词

    return result

# 示例用法
word_dictionary = ["分词", "算法", "介绍", "最大", "匹配"]
text = "分词算法介绍最大匹配"
result = reverse_maximum_match(text, word_dictionary)
print(result)