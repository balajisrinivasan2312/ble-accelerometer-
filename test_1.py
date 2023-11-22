from bluepy.btle import Scanner, DefaultDelegate
import struct
import time #this is to import all the library files necessary for the sensor interaction

class Scan_attribute(DefaultDelegate):
    def __init__(read):
        DefaultDelegate.__init__(read) #this piece of code is used to scan the sensor details into the gateway module

    def handleDiscovery(read, dev, isNewDev, isNewData):
        if isNewDev: #to find the ID of the Tag as there will be various ble tags in the range of the gateway
            print(f"Discovered device {dev.addr}")
        if dev.addr == '0x009078563412': #MAC address of the sensor sensed
            accel_data = read.parse_acceleration_data(dev)
            print(f"Accelerometer Data: {accel_data}") #the accel data is the complete raw data from the accelerometer sensor when moved or not moved

            # Check if the tag is moving or stationary based on accelerometer data
            is_moving = read.is_tag_moving(accel_data) #to check the data when the sensor detects the object moving 

            if not is_moving:
                # If the tag is stationary, interact with the iBeacon
                read.interact_with_ibeacon() #when not in motion the sensor send arbituary signals to the gateway about being under the threshold value

    def parse_acceleration_data(read, dev):
        accel_data_raw = dev.getValueText(0x08) #the values obtained from the accelerometer through parsing data in a timely manner
            if accel_data_raw:
                accel_data = struct.unpack('hhh', bytes.fromhex(accel_data_raw)) #the unpack function in the python breaks the raw data into 3 various axis datae of 16 bits
                return accel_data
        return None #when the accelerometer tag is in idle condition, the sensor just gives null value as the axis doesn't move

    def is_tag_moving(read, accel_data):
        
        threshold = 100
        return any(abs(accel) > threshold for accel in accel_data) #the abs command provides the absolute value of the accelerometer data and with the calculated null value data which equates to the threshold value

    def interact_with_ibeacon(read):
        # Implement your logic to interact with the iBeacon
        # This could include sending data to the iBeacon, triggering actions, etc.
        print("Interacting with iBeacon")

scanner = Scanner().withDelegate(Scan_attribute())

while True:
    devices = scanner.scan(5.0)  # Scan for 5 seconds
    time.sleep(1)  # Add a delay between scans to avoid excessive scanning
