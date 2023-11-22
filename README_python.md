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


