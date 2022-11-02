from gtts import gTTS
from playsound import playsound
import os

# # 경로를 .py파일의 실행 경로로 이동. 현재 경로로 이동
# text = '안녕하세요. 쩨이입니다.'

# # text에 저장한 글자 음성으로 저장, 언어 선택
# tts = gTTS(text=text, lang='ko')
# # 저장한 파일 이름 설정
# tts.save(r"./sound.mp3")

# # 저장한 음성파일 실행
# playsound("sound.mp3")

# 현제 경로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# yo.txt파일을 열어 내용을 read_file변수에 입력
file_path = 'yo.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_file = f.read()

# read_file의 내용을 음성파일로 저장
tts = gTTS(text=read_file, lang='ko')
tts.save('myText.mp3')

# 음성파일 실행
playsound('myText.mp3')
