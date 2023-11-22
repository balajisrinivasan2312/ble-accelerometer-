# ble-accelerometer- 
# Installing Python and Python IDE

This guide will walk you through the steps to install Python and a Python Integrated Development Environment (IDE) on your machine.

## Python Installation

### Windows

1. Download the latest version of Python for Windows from the [official Python website](https://www.python.org/downloads/).

2. Run the installer and make sure to check the box that says "Add Python to PATH" during installation.

3. Follow the on-screen instructions to complete the installation.

4. Verify the installation by opening a command prompt and typing:

    ```bash
    python --version
    ```


### macOS

1. macOS usually comes with Python pre-installed. Open a terminal and type:

    ```bash
    python3 --version
    ```

    If Python is not installed, you will be prompted to install it. Follow the instructions.

2. Alternatively, you can install Python using [Homebrew](https://brew.sh/):

    ```bash
    brew install python
    ```

### Linux

1. Most Linux distributions come with Python pre-installed. Open a terminal and type:

    ```bash
    python3 --version
    ```

    If Python is not installed, you can install it using your package manager (e.g., `sudo apt install python3` for Debian-based systems).

## Installing Visual Studio Code (VSCode)

1. Download and install Visual Studio Code from the [official website](https://code.visualstudio.com/).

2. Open VSCode and install the "Python" extension by Microsoft for a better Python development experience.

    - Press `Ctrl + P` to open the Quick Open dialog.
    - Type `ext install ms-python.python` and press Enter.

3. Restart VSCode to activate the installed extension.

## Verify Installations

1. Open a new terminal in VSCode and type:

    ```bash
    python --version
    ```

    Ensure that VSCode recognizes Python and doesn't show any errors.

2. Create a new Python file (e.g., `hello.py`) and write a simple Python script. Run the script to verify the IDE's functionality.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This guide is licensed under the [MIT License](LICENSE).

Bluetooth Hardware:

Ensure that your computer has Bluetooth hardware. You can check this by running the following command in the terminal:
bash
Copy code
hciconfig
Make sure Bluetooth is enabled.
BlueZ:

BlueZ is the official Linux Bluetooth protocol stack. Most Linux distributions come with BlueZ pre-installed. If not, you can install it using your package manager (e.g., sudo apt-get install bluez on Debian/Ubuntu).
Scanning for iBeacons:
Install Required Tools:

You can use the hcitool and hcidump tools for basic BLE operations. Install them if they're not already present:
bash
Copy code
sudo apt-get install bluez-hcidump
Scan for Devices:

Run the following commands to scan for nearby BLE devices, including iBeacons:
bash
Copy code
sudo hciconfig hci0 up
sudo hcitool lescan
Filter iBeacons:

You can filter the results to only display iBeacons by using hcidump:
bash
Copy code
sudo hcidump --raw
The output will display raw Bluetooth data. Look for advertisements with iBeacon format. iBeacons typically have a specific UUID.
Python Script (Using bluepy):
Install bluepy:

Install the bluepy Python library, which provides a higher-level interface for working with BLE devices:
bash
Copy code
pip install bluepy
Create a Python Script:

Create a Python script to scan for and interact with BLE devices. Below is a simple example:
python
Copy code
from bluepy.btle import Scanner

scanner = Scanner()

# Scan for BLE devices
devices = scanner.scan()

# Print details of found devices
for device in devices:
    print(f"Device {device.addr}: {device.addrType}, RSSI={device.rssi}, {device.getValueText(9)}")
This script uses the Scanner class from bluepy to perform a BLE scan. The device.getValueText(9) extracts the iBeacon UUID.
Run the Script:

Save the script and run it with sudo to ensure it has the necessary permissions to access Bluetooth:
bash
Copy code
sudo python your_script.py
Notes:
iBeacon UUID Format:

iBeacons typically use a UUID (Universally Unique Identifier) for identification. You may need to check the iBeacon specifications or documentation for the specific UUID used by your iBeacon.
Security Considerations:

Depending on the iBeacon configuration, you may need to handle security features such as pairing.
Manufacturer-Specific Tools:

Some iBeacon manufacturers provide their own tools or SDKs for interacting with their devices. Check the manufacturer's documentation for specific instructions.

STEPS I followed
1. Knowledge about the programming language and its attributes.
2. learning about the device and sensor used (BLE)
3. Understanding of the problem statement
4. three main signals from the sensor to be registered: the device in movement, the device when idle and when the device-sensor interact.
5. Last the timing between each inferences as it exhausts battery health of the device.
