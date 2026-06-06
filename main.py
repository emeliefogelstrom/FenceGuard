import time
import machine
import network

wlan = network.WLAN(mode=network.WLAN.STA)
print("Connecting to wifi...")

# wait for connection
while not wlan.isconnected():
    machine.idle()
    print("waiting...")

# wifi connected
print("Connected. IP: ", wlan.ifconfig()[0])

pir = machine.Pin('P20', machine.Pin.IN)
rtc = machine.RTC()

rtc.ntp_sync('pool.ntp.org')
while not rtc.synced():
    time.sleep(1)
    print("Syncing time...")
print(time.localtime())
time.sleep(2)

dstadjust = 2

last_val = 0

while True:
    val = pir.value()
    if val != last_val:
        hour = time.localtime()[3] + dstadjust
        timestamp = "{}/{}/{} {}:{}:{}".format(
            time.localtime()[0], time.localtime()[1], time.localtime()[2],
            hour, time.localtime()[4], time.localtime()[5]
        )
        if val == 1:
            print("HIGH", timestamp)
        else:
            print("LOW", timestamp)
        last_val = val
    time.sleep(0.1)