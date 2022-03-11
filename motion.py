import RPi.GPIO as GPIO
import time
import sys
pin = [4, 17, 27, 22]
servo = []

# 使用する各社サーボの駆動パルス
T = 50    # パルス周期 [mSec]
f = round( 1/T * 1000 ,1)    # 周波数
neutral = 1500 / 1000    # ニュートラル1500 [μSec → mSec]
variable = 600 / 1000    # 可変範囲±600 [μSec → mSec]

# GPIOの設定
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for num in range(4):
    GPIO.setup(pin[num], GPIO.OUT)
    servo.append(GPIO.PWM(pin[num], f))
    servo[num].start(0)

#スイッチの設定
sw_neck = 5
sw_right = 6
sw_left = 13
sw_banzai = 19
GPIO.setup(sw_neck, GPIO.IN)
GPIO.setup(sw_right, GPIO.IN)
GPIO.setup(sw_left, GPIO.IN)
GPIO.setup(sw_banzai, GPIO.IN)

servo_neck = 0
servo_right = 1
servo_left = 2

# Duty = τ/T * 100 より角度からDuty比を算出
def servo_angle(angle, pin):
    duty = ( (neutral + (angle * variable / 90) ) / T ) * 100    # Duty = τ/T * 100
    servo[pin].ChangeDutyCycle(duty)    #デューティ比を変更

while True:
    try:
        #首を振る
        if(GPIO.input(sw_neck) == GPIO.LOW):
            servo_angle(-60, servo_neck)
            time.sleep(0.5)
            servo_angle(60, servo_neck)
            time.sleep(0.5)
            servo_angle(-60, servo_neck)
            time.sleep(0.5)
            servo_angle(0, servo_neck)
            print("首を振ったよ")
        #左手を挙げる
        if(GPIO.input(sw_left) == GPIO.LOW):
            servo_angle(60, servo_left)
            time.sleep(1)
            servo_angle(0, servo_left)
            print("左手挙げたよ")
        #右手を挙げる
        if(GPIO.input(sw_right) == GPIO.LOW):
            servo_angle(60, servo_right)
            time.sleep(1)
            servo_angle(0, servo_right)
            print("右手を挙げたよ")
        #バンザイ
        if(GPIO.input(sw_banzai) == GPIO.LOW):
            for i in range(2):
                servo_angle(60, servo_left)
                servo_angle(60, servo_right)
                time.sleep(0.5)
                servo_angle(0, servo_left)
                servo_angle(0, servo_right)
                time.sleep(0.5)
            print("バンザイしたよ")

        else:
            print("何も押してないよ")

    except KeyboardInterrupt:
        for num in range(4):
            servo[num].stop()
        GPIO.cleanup()
        print("\n" + "PWMサーボのテストプログラムを終了します。")
        sys.exit()

#Segmentation fault あまり良くなさそうなこと言われてるよ。
#ボタンを押したらどれかのモーションを取る
