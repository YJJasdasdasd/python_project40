import speech_recognition as sr

try:
    while True:
        r = sr.Recognizer()

        # 마이크에서 음성을 받습니다.
        with sr.Microphone() as source:
            print("음성을 입력하세요")
            audio = r.listen(source)

        # 한국어 음성을 인식하여 반환합니다.
        try:
            print("음성변환: " + r.recognize_google(audio, language='ko-KR'))
        except sr.UnknownValueError:
            print('오디오를 이해할 수 없습니다.')
        except sr.RequestError as e:
            print(f'에러가 발생하였습니다. 에러원인: {e}')

except KeyboardInterrupt:
    pass
