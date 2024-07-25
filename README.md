![Alt text](./assets/logo.png)

# Monkeytype Automation with Selenium

This project automates the process of logging into Monkeytype using GitHub credentials and simulates typing on the website using Selenium.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- ChromeDriver (download and place in the specified directory)
- Google Chrome Browser

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/monkeytype-automation.git
   cd monkeytype-automation
   ```

2. **Install Required Python Packages**

   ```sh
   pip install selenium python-dotenv
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the root directory of the project and add your GitHub login credentials:

   ```env
   LOGIN_ID=your_github_username
   LOGIN_PASSWORD=your_github_password
   ```

4. **Download ChromeDriver**

   Download the appropriate version of ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the `./cd` directory.

## Usage

1. **Run the Script**

   ```sh
   python main.py
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

- Ensure that the ChromeDriver version matches your installed Google Chrome version.
- The `.env` file should be kept secure and not shared with others, as it contains your GitHub credentials.

## Troubleshooting

- **Element Not Found**: If the script fails to find an element, it might be due to changes in the Monkeytype website. Check the XPath or selectors used in the script.
- **ChromeDriver Compatibility**: Ensure your ChromeDriver version is compatible with your installed Chrome browser.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Selenium](https://www.selenium.dev/)
- [Monkeytype](https://monkeytype.com/)

---

Feel free to customize the content as needed.
