import time

try:
    from NanoIotController import NanoIot

    nano_test = NanoIot('test', 'http://192.168.56.1:8000/')
    nano_test.controls()
except:
    time.sleep(10)




