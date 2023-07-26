import network
import time

class Wifi:
    def __init__(self, ssid, password=None):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid, password)

        i = 0
        while not (wlan.isconnected() or wlan.status() == network.STAT_GOT_IP):
            print("Waiting to connect:")
            time.sleep(1)
            i += 1
            if i == 10:
                wlan.connect(ssid, password)
                i = 0
                
        print(wlan.ifconfig())
        
if __name__ == '__main__':
    Wifi('YOUR_SSID', 'YOUR_PASSWORD')

