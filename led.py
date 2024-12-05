import RPi.GPIO as GPIO
import time

# BCM 모드 설정
GPIO.setmode(GPIO.BCM)

# 확장 보드 J6 -> GPIO 17로 연결되었다고 가정
relay_pin = 17   # 이 부분 숫자 변경 시 조작led 변경

# GPIO 핀을 출력으로 설정
GPIO.setup(relay_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(relay_pin, GPIO.HIGH)  # 릴레이 활성화
        print("Relay ON")
        time.sleep(2)
        GPIO.output(relay_pin, GPIO.LOW)   # 릴레이 비활성화
        print("Relay OFF")
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()  # 종료 시 GPIO 초기화
