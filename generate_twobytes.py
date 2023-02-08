"""Build a program to generates 2 Bytes for an AV:
a. Byte1: angle of steering values from 0 to 359 
  (how many bits do you need ?)
  359 = 0x167 = 0001 0110 0111 (9 bits)
b. Byte 2 : the first bit is allocated to the previous task,
   7 other bits are dedicated to represent speed in miles. (0-127)
   127dec = 0x7F = 0111 1111"""

import random


def generate_twobytes():
    # generate random value for two parameters within the range
    steering_angle = random.randint(0, 359)
    vehicle_speed = random.randint(0, 127)

    # get the value of the 8th bit of steering angle
    steering_angle_signature = steering_angle & 256

    # get the value of the 0-7th bits of steering angle
    byte_1 = steering_angle & 255

    # put the 8th bit value of steering angle to 7th bit of vehicle sppe
    if steering_angle_signature == 0:
        byte_2 = vehicle_speed
    if steering_angle_signature == 256:
        byte_2 = vehicle_speed + 128

    # convert decimal value to hex value
    two_byte_hex = hex(256 * byte_1 + byte_2)
    return two_byte_hex


if __name__ == '__main__':
    twobytes = generate_twobytes()
    print(twobytes)
