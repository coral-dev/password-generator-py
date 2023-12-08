# Password Generator README

## Overview

This Python script is a simple, interactive password generator. It creates a custom password based on user inputs, allowing the user to specify the number of letters, symbols, and numbers in the password. The script uses Python's `random` module to ensure that each generated password is unique and unpredictable.

## Requirements

- Python 3.x
- `constants.py` file containing:
  - `letters` (a list of letter characters)
  - `symbols` (a list of symbol characters)
  - `numbers` (a list of numeric characters)

## Installation

No additional installation is required beyond ensuring Python 3.x is installed on your system. Place `constants.py` in the same directory as this script.

## Usage

1. Run the script:
   ```bash
   python main.py
   ```
2. Follow the on-screen prompts to input:
   - The desired number of letters in the password.
   - The desired number of symbols in the password.
   - The desired number of numbers in the password.

The script will then generate a password based on these specifications and display it.

## Features

- Interactive user input for customizing password length and composition.
- Randomized character selection for enhanced security.
- Combines letters, symbols, and numbers to create a robust password.

## Limitations

- The strength of the generated password depends on the `constants.py` file's character sets.
- This script does not check for password complexity beyond the inclusion of specified character types.

## Contributing

Contributions to improve the script or expand its capabilities are welcome. Please ensure that all contributions adhere to best coding practices and include appropriate documentation.

## License

This script is provided "as is", without warranty of any kind. You are free to use, modify, and distribute it as needed.