import board
import busio 
from digitalio import DigitalInOut, Direction, Pull


DRIVER_MODE_ADDR = 0X00

DRIVER_PWM_ADDR = []
for i in range(0x01,0x13):
    DRIVER_PWM_ADDR.append(i)

DRIVER_OUT_01_06_ADDR = 0x13
DRIVER_OUT_07_12_ADDR = 0x14
DRIVER_OUT_13_18_ADDR = 0x15
DRIVER_OUT_EN = [0x13,0x14,0x15]

DRIVER_UPDATE_ADDR = 0x16
DRIVER_RESET_ADDR = 0x17

class LEDDriver:
    def __init__(self, max_leds, i2c,driver_addr=84):

        #Initialize I2C
        self.i2c = i2c
        self.i2c_driver_addr = driver_addr
        self.max_leds = max_leds

        # Set the output mode of the enable pin with default pulled up
        self.driver_en = DigitalInOut(board.GP22)
        self.driver_en.direction = Direction.OUTPUT

        self.init(self.driver_en)

    def init(self,en_pin):
        # Enable driver
        en_pin.value = True

        # Put chip in normal operation
        self.send_to_driver(self.i2c_driver_addr,bytes([DRIVER_MODE_ADDR,0x01]))

    def set_brightness(self,brightness_percent = 50,output_led = 0):
        brightness_val = int(brightness_percent*255/100)
        if output_led < self.max_leds:
            self.send_to_driver(self.i2c_driver_addr,bytes([DRIVER_PWM_ADDR[output_led],brightness_val]))
    
    def set_output(self,output_led,output_state):
        enable_reg_index = 0
        if output_led < self.max_leds:
            #if output_led <= 5:
            #    enable_reg_index = 0
            #elif (output_led > 5) or ( output_led <= 11):
            #    enable_reg_index = 1
            #    output_led = output_led - 6
            #else:
            #    enable_reg_index = 2
            #    output_led = output_led - 12
        # TODO when switching to the next register the older register is not cleared. Try just bitshifting using the output_led offset
        # and rely on the autoincrement feature
            led_registers = output_state << output_led
            print(output_led)
            led_register0 = led_registers & 0x1F    
            led_register1 = ((led_registers) >> 4) & 0x1F
            led_register2 = ((led_registers) >> 8) & 0x1F        
            self.send_to_driver(self.i2c_driver_addr,bytes([DRIVER_OUT_EN[enable_reg_index],led_register0,led_register1,led_register2]))
            self.send_to_driver(self.i2c_driver_addr,bytes([DRIVER_UPDATE_ADDR,0x00]))
    
    def reset(self):
        en_pin = self.driver_en
        self.send_to_driver(self.i2c_driver_addr,bytes([DRIVER_RESET_ADDR,0x00]))
        en_pin.value = False
    
    def enable(self):
        en_pin = self.driver_en
        en_pin.value = True
        self.send_to_driver(self.i2c_driver_addr,bytes([DRIVER_MODE_ADDR,0x01]))



    def send_to_driver(self,chip_addr,buffer=bytes([0x00])):
        if self.i2c.try_lock():
            self.i2c.writeto(chip_addr,buffer)
            self.i2c.unlock()



        
