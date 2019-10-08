def solution(str1, str2):
    str1_words = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    str2_words = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]

    unique_words = set(str1_words).union(set(str2_words))

    intersection = 0
    union = 0

    if unique_words:
        for word in unique_words:
            str1_word_count = str1_words.count(word)
            str2_word_count = str2_words.count(word)
            intersection += min(str1_word_count, str2_word_count)
            union += max(str1_word_count, str2_word_count)
        answer = int(intersection/union * 65536)
    else:
        answer = 65536
    return answer
