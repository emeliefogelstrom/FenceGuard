import machine
import time

pir = machine.Pin('P20', machine.Pin.IN)

while True:
    print(pir.value())
    time.sleep(2)