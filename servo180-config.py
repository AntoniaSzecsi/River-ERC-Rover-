import time
from adafruit_servokit import ServoKit
servo180_1 = 400
servo180_2 = 2700

kit = ServoKit(channels=16)
kit.servo[0].set_pulse_width_range(servo180_1, servo180_2)

while True: 
  kit.servo[0].angle = 180
  time.sleep(1)
  kit.servo[0].angle = 0
  time.sleep(1)
