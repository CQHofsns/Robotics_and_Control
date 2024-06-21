import pygame
import time

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
        
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting")
finally:
    pygame.joystick.quit()
    pygame.quit()