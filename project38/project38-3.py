import speech_recognition as sr

try:
    while True:
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("음성을 입력하세요")
            audio = r.listen(source)
        try:
            stt = r.recognize_google(audio, language='ko-KR')
            print("음성변환: " + stt)

            # 음성인식된 글자 중에 "안녕"이 포함되어 있다면 '네 안녕 하세요'를 출력합니다.
            if '안녕' in stt:
                print("네 안녕하세요")
            # 음성인식된 글자 중에 "날씨"가 포함되어 있다면 "정말 날씨가 좋네요"를 출력합니다.
            elif '날씨' in stt:
                print('정말 날씨가 좋네요')

        except sr.UnknownValueError:
            print("오디오를 이해할수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생하였습니다. 에러원인: {e}")

except KeyboardInterrupt:
    pass
