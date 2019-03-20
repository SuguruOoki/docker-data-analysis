from collections import Counter
import re
from pprint import pprint

pattern = "[,.;?!]"
file_name = "sample.txt"
with open(file_name, encoding="utf-8") as txt:
    t = txt.read()
sentence = t.split("\n")

p = re.compile(pattern)
result = []

for s in sentence:
    # 文中の記号を除去        
    replaced_sentence = re.sub(p, "", s)
   # 空白で分割 
    words = replaced_sentence.split()
    result.extend(words)

cnt = Counter(result)
# 出現頻度が多かった~番目までの要素を出現頻度共に表示
pprint(cnt.most_common(500))
