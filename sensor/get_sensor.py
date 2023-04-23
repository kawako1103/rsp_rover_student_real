# -*- coding: utf-8 -*-
# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# BMX055
# This code is designed to work with the BMX055_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/products

##smbusのsmbusのapiは(https://pypi.org/project/smbus2/)から参照できます。
import smbus #これインストールみたいなのが必要そう
import time

ACCL_ADDR = 0x19
GYRO_ADDR = 0x69
MAGN_ADDR = 0x13 

# Get I2C bus
bus = smbus.SMBus(1)

# BMX055 Accl address, 0x18(24)
# Select PMU_Range register, 0x0F(15)
#		0x03(03)	Range = +/- 2g
time.sleep(0.1)
bus.write_byte_data(ACCL_ADDR, 0x0F, 0x03)
time.sleep(0.1)
# BMX055 Accl address, 0x18(24)
# Select PMU_BW register, 0x10(16)
#		0x08(08)	Bandwidth = 7.81 Hz
bus.write_byte_data(ACCL_ADDR, 0x10, 0x08)
time.sleep(0.1)
# BMX055 Accl address, 0x18(24)
# Select PMU_LPW register, 0x11(17)
#		0x00(00)	Normal mode, Sleep duration = 0.5ms
bus.write_byte_data(ACCL_ADDR, 0x11, 0x00)

time.sleep(0.1)

####
# BMX055 Gyro address, 0x68(104)
# Select Range register, 0x0F(15)
#		0x04(04)	Full scale = +/- 125 degree/s
bus.write_byte_data(GYRO_ADDR, 0x0F, 0x04)
time.sleep(0.1)
# BMX055 Gyro address, 0x68(104)
# Select Bandwidth register, 0x10(16)
#		0x07(07)	ODR = 100 Hz
bus.write_byte_data(GYRO_ADDR, 0x10, 0x07)
time.sleep(0.1)
# BMX055 Gyro address, 0x68(104)
# Select LPM1 register, 0x11(17)
#		0x00(00)	Normal mode, Sleep duration = 2ms
bus.write_byte_data(GYRO_ADDR, 0x11, 0x00)
time.sleep(0.1)

####

####
# BMX055 Mag address, 0x10(16)
# Select Mag register, 0x4B(75)
#		0x83(121)	Soft reset
bus.write_byte_data(MAGN_ADDR, 0x4B, 0x01)
time.sleep(0.1)
# BMX055 Mag address, 0x10(16)
# Select Mag register, 0x4C(76)
#		0x00(00)	Normal Mode, ODR = 10 Hz
bus.write_byte_data(MAGN_ADDR, 0x4C, 0x00)
time.sleep(0.1)
# BMX055 Mag address, 0x10(16)
# Select Mag register, 0x4E(78)
#		0x84(122)	X, Y, Z-Axis enabled
bus.write_byte_data(MAGN_ADDR, 0x4E, 0x84)
time.sleep(0.1)
# BMX055 Mag address, 0x10(16)
# Select Mag register, 0x51(81)
#		0x04(04)	No. of Repetitions for X-Y Axis = 9
bus.write_byte_data(MAGN_ADDR, 0x51, 0x04)
time.sleep(0.1)
# BMX055 Mag address, 0x10(16)
# Select Mag register, 0x52(82)
#		0x0F(15)	No. of Repetitions for Z-Axis = 15
bus.write_byte_data(MAGN_ADDR, 0x52, 0x0F)
time.sleep(0.1)

####


	##get sensor value for a while
    # BMX055 Accl address, 0x18(24)
    # Read data back from 0x02(02), 6 bytes
    # xAccl LSB, xAccl MSB, yAccl LSB, yAccl MSB, zAccl LSB, zAccl MSB
    
def accl():
    xAccl = yAccl = zAccl = 0
	
    try:
        data = bus.read_i2c_block_data(ACCL_ADDR, 0x02, 6)

		# Convert the data to 12-bits
        
        xAccl = ((data[1] * 256) + (data[0] & 0xF0)) / 16
        if xAccl > 2047 :
            xAccl -= 4096
        yAccl = ((data[3] * 256) + (data[2] & 0xF0)) / 16
        if yAccl > 2047 :
            yAccl -= 4096
        zAccl = ((data[5] * 256) + (data[4] & 0xF0)) / 16
        if zAccl > 2047 :
            zAccl -= 4096

    except IOError as e:
        print("I/O error({0}): {1}".format(e.error, e.strerror))
        
    return xAccl, yAccl, zAccl

def gyro():
    # BMX055 Gyro address, 0x68(104)
    # Read data back from 0x02(02), 6 bytes
    # xGyro LSB, xGyro MSB, yGyro LSB, yGyro MSB, zGyro LSB, zGyro MSB
    xGyro = yGyro = zGyro = 0
    
    try:
        data = bus.read_i2c_block_data(GYRO_ADDR, 0x02, 6)
        time.sleep(1)
        
        # Convert the data
        xGyro = data[1] * 256 + data[0]
        if xGyro > 32767 :
            xGyro -= 65536
        yGyro = data[3] * 256 + data[2]
        if yGyro > 32767 :
            yGyro -= 65536
        zGyro = data[5] * 256 + data[4]
        if zGyro > 32767 :
            zGyro -= 65536
 
    except IOError as e:
        print("I/O error({0}): {1}".format(e.error, e.strerror))

    return xGyro, yGyro, zGyro

def mag():
    # BMX055 Mag address, 0x10(16)
    # Read data back from 0x42(66), 6 bytes
    # X-Axis LSB, X-Axis MSB, Y-Axis LSB, Y-Axis MSB, Z-Axis LSB, Z-Axis MSB
    xMag = yMag = zMag = 0
    
    try:
        data = bus.read_i2c_block_data(MAGN_ADDR, 0x42, 6)
        time.sleep(1)

		# Convert the data
        xMag = ((data[1] * 256) + (data[0] & 0xF8)) / 8
        if xMag > 4095 :
            xMag -= 8192
        yMag = ((data[3] * 256) + (data[2] & 0xF8)) / 8
        if yMag > 4095 :
            yMag -= 8192
        zMag = ((data[5] * 256) + (data[4] & 0xFE)) / 2
        if zMag > 16383 :
            zMag -= 32768
            
    except IOError as e:
        print("I/O error({0}): {1}".format(e.error, e.strerror))

    return xGyro, yGyro, zGyro


