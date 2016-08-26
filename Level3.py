from collections import Counter
import re

with open("C:\\Users\\vfortunato\\PycharmProjects\\PythonChallenge\\mess.txt", "r") as myFile:
    data = myFile.readlines()
    strTotal = ''.join(data)
    count = Counter(strTotal)
    mostCommon = count.most_common()[-8:]

    print(mostCommon)

    strTranslate = re.sub('[^iaulyetq]', '', strTotal)

    print(strTranslate)
