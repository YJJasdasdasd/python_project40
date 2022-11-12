import pyaudio
import wave
from playsound import playsound

# 녹음 파일 형식 설정
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
# 녹음 파일 위치 저장
WAVE_OUTPUT_FILENAME = r'./output.wave'

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                input=True, frames_per_buffer=CHUNK)

print("음성녹음을 시작합니다.")

# 음성 녹음
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("음성녹음을 완료하였습니다.")

# 녹음된 음성을 저장
stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print("녹음된 파일을 재생합니다.")
# 저장된 음성파일을 재생합니다.
playsound(WAVE_OUTPUT_FILENAME)
