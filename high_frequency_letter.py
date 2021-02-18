# 글자 중에서 제일 많이 중복되서 들어간 글자 찾기
# 글자를 각각의 키값으로 맵으로 저장한다음에 같은 key 값으로 들어오면 +1 해줌

word = "test"


def highFrequencyLetterCount(word):
    map = {}
    for item in word:
        if map.get(item) == None:
            map[item] = 1
        else:
            map[item] += 1

        # max_key = ""
        # max_value = -1
        # for key in map:
        #     if map[key]>max_value :
        #         max_value = map[key]
        #         max_key = key

        max_key = max(map,key=map.get)
        max_value = map[max_key]

        result = "key는 {} value는 {}".format(max_key,max_value)
    return result


print(highFrequencyLetterCount(word))