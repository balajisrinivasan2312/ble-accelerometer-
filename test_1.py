from bluepy.btle import Scanner, DefaultDelegate
import struct
import time

class Scan_attribute(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print(f"Discovered device {dev.addr}")
        if dev.addr == '0x009078563412':
            accel_data = self.parse_acceleration_data(dev)
            print(f"Accelerometer Data: {accel_data}")

            # Check if the tag is moving or stationary based on accelerometer data
            is_moving = self.is_tag_moving(accel_data)

            if not is_moving:
                # If the tag is stationary, interact with the iBeacon
                self.interact_with_ibeacon()

    def parse_acceleration_data(self, dev):
        accel_data_raw = dev.getValueText(0x08)
            if accel_data_raw:
                accel_data = struct.unpack('hhh', bytes.fromhex(accel_data_raw))
                return accel_data
        return None

    def is_tag_moving(self, accel_data):
        # Implement your logic to determine if the tag is moving based on accelerometer data
        # This can be based on a threshold, variance, or any other criteria
        # For simplicity, let's assume the tag is moving if the acceleration on any axis is above a threshold
        threshold = 100
        return any(abs(accel) > threshold for accel in accel_data)

    def interact_with_ibeacon(self):
        # Implement your logic to interact with the iBeacon
        # This could include sending data to the iBeacon, triggering actions, etc.
        print("Interacting with iBeacon")

# Replace 'YOUR_BLE_TAG_MAC_ADDRESS' with the MAC address of your BLE tag
scanner = Scanner().withDelegate(Scan_attribute())

while True:
    devices = scanner.scan(5.0)  # Scan for 5 seconds
    time.sleep(1)  # Add a delay between scans to avoid excessive scanning
