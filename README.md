![Alt text](./assets/logo.png)

# Monkeytype Automation with Selenium

This project automates the process of logging into Monkeytype using GitHub credentials and simulates typing on the website using Selenium.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Google Chrome Browser

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/monkeytype-automation.git
   cd monkeytype-automation
   ```

2. **Install Required Python Packages**

   ```sh
   pip install -r requirements.txt
   ```

   Or install manually:
   ```sh
   pip install selenium python-dotenv webdriver-manager
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the root directory of the project and add your GitHub login credentials:

   ```env
   LOGIN_ID=your_github_username
   LOGIN_PASSWORD=your_github_password
   ```

4. **ChromeDriver Management**

   ChromeDriver is automatically downloaded and managed by `webdriver-manager`. No manual installation is required. The correct version matching your Chrome browser will be automatically selected.

## Usage

1. **Run the Script**

   ```sh
   python3 MonkeyType.py
   ```

   This script will:

   - Open Monkeytype website
   - Accept cookies
   - Log in using GitHub credentials
   - Switch back to the game window
   - Simulate typing words

2. **Quit the Script**

   The script will run indefinitely, typing words on Monkeytype. Press `Enter` in the terminal to quit the script and close the browser.

## Notes

- ChromeDriver is automatically managed and will match your installed Google Chrome version.
- The `.env` file should be kept secure and not shared with others, as it contains your GitHub credentials.

## Troubleshooting

- **Element Not Found**: If the script fails to find an element, it might be due to changes in the Monkeytype website. Check the XPath or selectors used in the script.
- **ChromeDriver Compatibility**: ChromeDriver is automatically managed by `webdriver-manager` and should always match your Chrome version. If you encounter issues, try updating Chrome or reinstalling dependencies.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Selenium](https://www.selenium.dev/)
- [Monkeytype](https://monkeytype.com/)

---

Feel free to customize the content as needed.
