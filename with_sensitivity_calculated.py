import struct

def extract_ble_values(raw_data):
    # Extracting accelerometer data
    accel_data = struct.unpack('hhh', bytes.fromhex(raw_data[10:22]))
    
    # Extracting battery information
    battery_info = struct.unpack('B', bytes.fromhex(raw_data[22:24]))[0]
    
    return accel_data, battery_info

def calculate_acceleration(accel_data, sensitivity_x=None, sensitivity_y=-0.5, sensitivity_z=1.23, zero_g_offset=0):
    # Apply sensitivity and zero g offset to each axis
    accel_x = (accel_data[0] - zero_g_offset) * sensitivity_x if sensitivity_x is not None else accel_data[0]
    accel_y = (accel_data[1] - zero_g_offset) * sensitivity_y
    accel_z = (accel_data[2] - zero_g_offset) * sensitivity_z

    return accel_x, accel_y, accel_z

raw_data_list = [
    "0201060303E1FF1216E1FFA10364FFF4000FFF003772A33F23AC",
    "0201060303E1FF1216E1FFA10364FFF60011FF003772A33F23AC",
    "0201060303E1FF1216E1FFA10364FFF40011FF033772A33F23AC"
]

for raw_data in raw_data_list:
    accel_data, battery_info = extract_ble_values(raw_data)
    
    accel_x, accel_y, accel_z = calculate_acceleration(accel_data, sensitivity_x=None, sensitivity_y=-0.5, sensitivity_z=1.23, zero_g_offset=0)
    
    print(f"Accelerometer Data: X={accel_x}, Y={accel_y}, Z={accel_z}")
    print(f"Battery Information: {battery_info}")
    print("------")
