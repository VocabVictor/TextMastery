def bidirectional_maximum_match(text, word_dict):
    result = []  # 存储分词结果
    max_length = max(len(word) for word in word_dict)  # 词典中最长词的长度

    while text:
        # 正向最大匹配
        forward_word = text[:max_length]      # 从头开始取最长词的长度的子串
        while len(forward_word) > 1 and forward_word not in word_dict:
            forward_word = forward_word[:-1]  # 若不在词典中，则逐渐缩小子串的长度

        # 逆向最大匹配
        reverse_word = text[-max_length:]     # 从尾部开始取最长词的长度的子串
        while len(reverse_word) > 1 and reverse_word not in word_dict:
            reverse_word = reverse_word[1:]   # 若不在词典中，则逐渐缩小子串的长度

        # 根据规则确定最终的分词结果
        if len(forward_word) <= len(reverse_word):
            result.append(forward_word)
            text = text[len(forward_word):]
        else:
            result.append(reverse_word)
            text = text[:len(text) - len(reverse_word)]

    return result

# 示例用法
word_dictionary = ["分词", "算法", "介绍", "最大", "匹配"]
text = "分词算法介绍最大匹配"
result = bidirectional_maximum_match(text, word_dictionary)
print(result)