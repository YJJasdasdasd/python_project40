import qrcode

# qr_data = 'www.naver.com'
# qr_img = qrcode.make(qr_data)

# save_path = qr_data+'.png'
# qr_img.save(save_path)

# txt파일 열기
file_path = 'qrcode.txt'
with open(file_path) as f:
    # txt파일 변수에 리스트 형태로 저장
    read_lines = f.readlines()
    # 리스트 형태로 저장된 변수를 여러변 읽기위해 for문으로 사용
    for line in read_lines:
        line = line.strip()
        print(line)
        # qrcode생성
        qr_data = line
        qr_img = qrcode.make(qr_data)
        # 생성된 qrcode 이미지로 저장
        save_path = qr_data + '.png'
        qr_img.save(save_path)
