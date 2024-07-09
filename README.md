# Bulk Messenger Message Sender

This script automates the process of sending messages to a list of Facebook profiles using Selenium WebDriver and an Excel file containing the profile links and corresponding messages.

### Prerequisites

Make sure you have the following installed on your system:

1. Python 3.x
2. Google Chrome browser
3. The following Python libraries:
    - `pandas`
    - `selenium`
    - `webdriver-manager`

You can install the required Python libraries using pip:

```sh
pip install pandas selenium webdriver-manager
```

### Setup

1. **Excel File**: Prepare an Excel file named `data.xlsx` with two columns: `Profile Link` and `Message`. This file should be in the same directory as your script.

    Example `data.xlsx` format:

    | Profile Link                     | Message                 |
    |----------------------------------|-------------------------|
    | https://www.facebook.com/profile | Hello! This is a test.  |
    | https://www.facebook.com/profile2 | Hi there! How are you? |

2. **Chrome Profile**: Ensure you have a Chrome profile set up. The default profile is usually named `Default`. You can find the profile in your Chrome user data directory, typically located at `C:\Users\<YourUsername>\AppData\Local\Google\Chrome\User Data`.

### Usage

1. **Clone the Repository**:

2. **Update User Data Directory and Profile Directory**: In the script, update the `user_data_dir` and `profile_dir` variables with your Chrome user data directory and profile directory.

3. **Run the Script**:

    ```sh
    python pages.py
    ```

### Script Details

The script performs the following actions:

1. **Load the Excel File**: The script reads `data.xlsx` to get the profile links and messages.
2. **Configure Chrome Options**: Sets up Chrome options including maximizing the window and disabling extensions, popups, and infobars.
3. **Send Messages**: For each profile link and message in the Excel file, the script:
    - Navigates to the profile link.
    - Clicks the "Message" button.
    - Enters the message in the text area.
    - Sends the message.
4. **Error Handling**: If an error occurs during any step, the script captures a screenshot and logs the error.
