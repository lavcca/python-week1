text="""
인생은 짧고 삶은 생각보다 빠르게 지나간다.
어떤 날은 인생이 참 힘들게 느껴지고 어떤 날은 인생이 아름답게 느껴진다.
사람들은 삶에서 선택을 하며 그 선택이 인생을 바꾼다고 말한다.
우리는 인생에서 실수를 통해 배우고 고통 속에서 성장한다.
인생은 항상 쉽지 않지만 인생은 우리에게 많은 것을 가르쳐 준다.
Life is short and life is strange.
Sometimes life feels unfair, and sometimes it feels beautiful.
People say that life is about choices, and every choice matters.
In life, we learn from mistakes, and we grow from pain.
Life is not always easy, but life is always teaching us something.
"""

import pandas as pd
import re

clean_text = re.sub(r"[^a-zA-Z\s]", "", text.lower())
clean_text_kr = re.sub(r"[^가-힣\s]", "", text)

tokens_raw = (clean_text + " " + clean_text_kr).split()

stopwords = {"is", "and", "a", "the", "to", "of"}
stopwords_kr = { "은", "는", "이", "가", "을", "를", "에서", "에게", "에게서", "하지만", "그리고", "어떤", "우리에게"}
all_stopwords = stopwords | stopwords_kr

s_raw = pd.Series(tokens_raw)

print("📌 전체 단어 TOP 20")
print(s_raw.value_counts().head(20))

# Stopwords 제거
def remove_josa(word):
    return re.sub(r"(은|는|이|가|을|를|에서|에게|에게서)$", "", word)

tokens_clean = []

for w in tokens_raw:
    w_clean = remove_josa(w)
    if w_clean and w_clean not in all_stopwords:
        tokens_clean.append(w_clean)

s_clean = pd.Series(tokens_clean)

print("\n📌 Stopwords 제거 후 TOP 20")
print(s_clean.value_counts().head(20))
