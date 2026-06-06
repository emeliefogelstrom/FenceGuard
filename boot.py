from network import WLAN

# Connect to WiFi
# SSID is your WiFi connection name and PASSWORD your WiFi password
wlan = WLAN(mode=WLAN.STA)
wlan.connect("MartilleWiFi", auth=(WLAN.WPA2, "wl10com2g"), timeout=5000)
