import pygame
import time
import RPi.GPIO  as GPIO

#KHỞI TẠO GPIO PINs:
BASE= 12
SHOULDER= 13
ELBOW= 19

freq= 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(BASE, GPIO.OUT)
GPIO.setup(SHOULDER, GPIO.OUT)
GPIO.setup(ELBOW, GPIO.OUT)

base= GPIO.PWM(BASE, freq)
shoulder= GPIO.PWM(SHOULDER, freq)
elbow= GPIO.PWM(ELBOW, freq)

base.start(0)
shoulder.start(0)
elbow.start(0)

# HÀM SET GÓC CHO SERVO
def set_servo_angle(angle, pin, position):
    duty_cycle= 2+ (angle/18)
    GPIO.output(pin, True)
    position.ChangeDutyCycle(duty_cycle)
    time.sleep(0.05)
    GPIO.output(pin, False)
    position.ChangeDutyCycle(0)
    

## KHỞI TẠO PYGAME
pygame.init()

## KHỞI TẠO JOYSTICK
pygame.joystick.init()

## CHECK XEM JOYSTICK CÓ KẾT NỐI KHÔNG
if pygame.joystick.get_count()== 0:
    print("Không có kết nối")
    pygame.quit()
    exit()

joystick= pygame.joystick.Joystick(0)
joystick.init()

print("Controller được khởi tạo thành công")
print(f"Tên controller: {joystick.get_name}")
print(f"Số trục: {joystick.get_numaxes()}")
print(f"Số nút: {joystick.get_numbuttons()}")

try:
    while True:
        for event in pygame.event.get():
            if event.type== pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")
            #elif event.type== pygame.JOYBUTTONUP:
                #print(f"Button {event.button} pressed")
            elif event.type== pygame.JOYAXISMOTION:
                axis= event.axis
                value= event.value
                print(f"Axis {axis} moved to {value}")

                if axis== 0:
                    angle= (value+1)*90
                    set_servo_angle(angle, BASE, base)
                elif axis== 1:
                    angle= (value+1)*90
                    set_servo_angle(angle, SHOULDER, shoulder)
        
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting")
finally:
    base.stop()
    GPIO.cleanup()
    pygame.joystick.quit()
    pygame.quit()