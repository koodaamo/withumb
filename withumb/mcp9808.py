from machine import I2C, Pin


class MCP9808:

   I2C_ADDR = const(0x1f)
   TEMP_REG = const(5)
   
   def __init__(self):
      scl_pin =  Pin(5,Pin.IN, Pin.PULL_UP) # I2C clock pin 
      sda_pin =  Pin(4,Pin.IN, Pin.PULL_UP) # I2C data pin
      self._i2c = I2C(scl=scl_pin, sda=sda_pin, freq=100000)

   def __call__(self):
      raw = self._i2c.readfrom_mem(self.I2C_ADDR, self.TEMP_REG, 2)
      u = (raw[0] & 0x0f) << 4
      l = raw[1] / 16
      if raw[0] & 0x10 == 0x10:
         temp = 256 - (u + l)
      else:
         temp = u + l
      return temp

