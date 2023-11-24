import struct

def extract_ble_values(raw_data):
    # Extracting accelerometer data
    accel_data = struct.unpack('hhh', bytes.fromhex(raw_data[10:22]))
    
    # Extracting battery information
    battery_info = struct.unpack('B', bytes.fromhex(raw_data[22:24]))[0]
    
    return accel_data, battery_info


raw_data_list = [
    "0201060303E1FF1216E1FFA10364FFF4000FFF003772A33F23AC",
    "0201060303E1FF1216E1FFA10364FFF60011FF003772A33F23AC",
    "0201060303E1FF1216E1FFA10364FFF40011FF033772A33F23AC"
]

for raw_data in raw_data_list:
    accel_data, battery_info = extract_ble_values(raw_data)
    print(f"Accelerometer Data: X={accel_data[0]}, Y={accel_data[1]}, Z={accel_data[2]}")
    print(f"Battery Information: {battery_info}")
    print("------")
