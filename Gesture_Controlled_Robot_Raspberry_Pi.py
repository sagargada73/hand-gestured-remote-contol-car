from mpu6050 import mpu6050 		#Importing mph module and time function and GPIO modules
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)			#GPIO config to BCM mode

GPIO.setup(6, GPIO.OUT)		#Assigning Output pins
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
sensor = mpu6050(0x69)			#assigning address as 69


while True:
    accelerometer_data = sensor.get_accel_data()	#Calling the function to measure the sensor data
    print accelerometer_data
    x=accelerometer_data['x']		#Assigning the sensor axis values to different variables
    y=accelerometer_data['y']		# for further processing
    z=accelerometer_data['z']
    print x
    print y
    print z
    #STOP
    if (z>10.5):			#Threshold value for Stop and other positions like below
        D0=GPIO.output(6, GPIO.LOW)	
        D1=GPIO.output(13, GPIO.LOW)
        D2=GPIO.output(19, GPIO.LOW)
        D3=GPIO.output(26, GPIO.LOW)
        print 'STOP'
    
     #forward
    elif (x<-2):
        D0=GPIO.output(6, GPIO.HIGH)
        D1=GPIO.output(13, GPIO.LOW)	#From the configuration table you can match the values for each motion
        D2=GPIO.output(19, GPIO.HIGH)
        D3=GPIO.output(26, GPIO.LOW)
        print 'FORWARD'
        time.sleep(0.5)

     #backward
    elif (x>3):
        D0=GPIO.output(6, GPIO.LOW)
        D1=GPIO.output(13, GPIO.HIGH)
        D2=GPIO.output(19, GPIO.LOW)
        D3=GPIO.output(26, GPIO.HIGH)
        print 'BACKWARD'
        time.sleep(0.5)		# giving delay for the motor to react

     #RIGHT
    elif (y>0):
        D0=GPIO.output(6, GPIO.LOW)
        D1=GPIO.output(13, GPIO.HIGH)
        D2=GPIO.output(19, GPIO.HIGH)
        D3=GPIO.output(26, GPIO.LOW)
        print 'RIGHT'
        time.sleep(0.5)

     #LEFT
    elif (y<0):
        D0=GPIO.output(6, GPIO.HIGH)
        D1=GPIO.output(13, GPIO.LOW)
        D2=GPIO.output(19, GPIO.LOW)
        D3=GPIO.output(26, GPIO.HIGH)
        print 'LEFT'
        time.sleep(.5)

    time.sleep(1)			#Giving delay for measurement
    
