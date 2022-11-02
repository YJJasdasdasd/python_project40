#  행을 분리(또는 종료)하는 데 사용되는 linesep을 사용하기 위해 os 임포트
from os import linesep
import googletrans

translator = googletrans.Translator()

# 아랍어로 작성된 파일 객체 생성
read_file_path = r"arabic.txt"
# 한글로 번역된 글자를 저장할 파일명 설정
write_file_path = r"ko.txt"

# 객체 생성된파일 열기
with open(read_file_path, 'r', encoding="UTF-8") as f:
    readLines = f.readlines()

# 열린 파일의 글자를 한글로 변환
for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
    # 파일로 저장
    with open(write_file_path, 'a', encoding='UTF8') as f:
        f.write(result1.text + '\n')
