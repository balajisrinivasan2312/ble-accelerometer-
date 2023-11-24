import struct

def parse_ble_advertisement(raw_data):
    try:
        # Convert hexadecimal string to bytes
        raw_bytes = bytes.fromhex(raw_data)

        # Unpack common BLE advertisement fields
        length, = struct.unpack('B', raw_bytes[:1])
        data_type, = struct.unpack('B', raw_bytes[1:2])
        flags, = struct.unpack('B', raw_bytes[2:3])

        print(f"Length: {length}")
        print(f"Data Type: {data_type}")
        print(f"Flags: {flags:02X} (Binary: {bin(flags)})")

    
        company_identifier, = struct.unpack('<H', raw_bytes[3:5])
        ibeacon_identifier, = struct.unpack('<H', raw_bytes[5:7])
        uuid = raw_bytes[7:23].hex().upper()
        major, minor, measured_power = struct.unpack('>HHb', raw_bytes[23:28])

        print(f"Company Identifier: {company_identifier:04X}")
        print(f"iBeacon Identifier: {ibeacon_identifier:04X}")
        print(f"UUID: {uuid}")
        print(f"Major: {major}")
        print(f"Minor: {minor}")
        print(f"Measured Power: {measured_power}")

    

    except Exception as e:
        print(f"Error parsing data: {e}")

# Example usage with the provided raw data
raw_data_list = [
    "0201060303E1FF1216E1FFA10364FFF4000FFF003772A33F23AC",
    "0201061AFF4C00021553594F4F4B534F4349414C444953544500000000E8",
    "0201060303E1FF1216E1FFA10364FFF60011FF003772A33F23AC",
    "0201061AFF4C00021553594F4F4B534F4349414C444953544500000000E8",
    "0201060303E1FF1216E1FFA10364FFF40011FF033772A33F23AC",
    "0201061AFF4C00021553594F4F4B534F4349414C444953544500000000E8"
]

for raw_data in raw_data_list:
    print(f"Raw Data: {raw_data}")
    parse_ble_advertisement(raw_data)
