import logging
from serial.tools import list_ports

logging.basicConfig()
logger = logging.getLogger("withumb")
logger.setLevel(logging.INFO)


def get_withumb():
   for port in list_ports.comports():
      if is_withumb(port):
         logger.info("found: %s" % port)
         return port
   return None

def is_withumb(port):
   if port.pid == 60000 and \
      port.vid == 4292 and \
      port.serial_number == "01237FBC":
      return True


wt = get_withumb()

