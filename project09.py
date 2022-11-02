# googletrans를 불러옴
import googletrans

translator = googletrans.Translator()
# 입력한 글을 원하는 언어로 번역해주는 코드 dest = 번역하고싶은 언어 src = 번역할 언어 src는 기본으로 auto 설정
str1 = "행복하세요"
result1 = translator.translate(str1, dest='ar', src='auto')
print((f'행복하세요 => {result1.text}'))

str2 = "I am happy"
result2 = translator.translate(str2, dest='ar', src='en')
print(f"I am  happy => {result2.text}")
