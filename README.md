# Selenium Account Creator

Automated account creation using Selenium.

## Features

- Generates random user data.
- Automates the account registration process.
- Saves user information to a text file.

## Requirements

- Python 3.x
- Selenium
- Faker
- Chrome WebDriver (Ensure it matches your installed version of Chrome)
  
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/EmmaHarutyunyan/selenium-account-creator.git
   cd selenium-account-creator

2.  Install the required packages using requirements.txt:
    ```bash
    pip install -r requirements.txt

3.  Download Chrome WebDriver:
      
    Ensure that the Chrome WebDriver matches your installed version of Chrome. You can download it from ChromeDriver.

4.  Run the script:
    ```bash
    python main.py

Code Explanation

  • generate_random_password: Generates a secure random password of specified length.
  • Faker: Utilizes the Faker library to create realistic names, emails, and other user data.
  • Selenium: Automates the browser to fill out and submit the registration form.
  • Input Handling: Collects generated data and interacts with the web form seamlessly.

Output
User Information:
-----------------
First Name: [First Name]

Last Name:  [Last Name]

Email:      [Email]

Password:   [Password]
