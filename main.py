import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from threading import Thread

# File to store the last completed username
TRACK_FILE = "last_username.txt"

# Function to read the last completed username from the file
def get_last_username():
    if os.path.exists(TRACK_FILE):
        with open(TRACK_FILE, "r") as file:
            return file.read().strip()
    return "jij000"  # Default starting username

# Function to save the last completed username to the file
def save_last_username(username):
    with open(TRACK_FILE, "w") as file:
        file.write(username)

# Function to increment username
def increment_username(username):
    prefix = username[:-3]  # "jij"
    number = int(username[-3:]) + 1  # Increment numeric part
    return f"{prefix}{number:03d}"  # Format back to "jijXXX"

# Function to handle the registration in one browser window
def register_account(username, password, phone):
    driver = webdriver.Firefox()
    try:
        # Navigate to the registration page
        driver.get("https://jx2vn.com/api/dang-ky")
        time.sleep(2)  # Wait for the page to load
        
        # Fill in the username field
        username_field = driver.find_element(By.CSS_SELECTOR, "#username")
        username_field.clear()
        username_field.send_keys(username)
        
        # Fill in the password field
        password_field = driver.find_element(By.CSS_SELECTOR, "#password")
        password_field.clear()
        password_field.send_keys(password)
        
        # Fill in the confirm password field
        confirm_password_field = driver.find_element(By.CSS_SELECTOR, "#password2")
        confirm_password_field.clear()
        confirm_password_field.send_keys(password)
        
        # Fill in the phone field
        phone_field = driver.find_element(By.CSS_SELECTOR, "#phone")
        phone_field.clear()
        phone_field.send_keys(phone)
        
        # Submit the form
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Print to console when the job is done
        print(f"Registration complete for username: {username}")
        
        # Wait to observe results
        time.sleep(5)
    finally:
        # Close the browser
        driver.quit()

# Main function to launch multiple windows
def main():
    # Read the last username
    last_username = get_last_username()
    password = "sdfsdf"
    phone = "0123123123"
    
    # Number of accounts to register per run
    num_accounts = 16  # Adjust as needed
    threads = []
    
    for _ in range(num_accounts):
        # Launch a thread for each account registration
        thread = Thread(target=register_account, args=(last_username, password, phone))
        threads.append(thread)
        thread.start()
        print(f"Thread started for username: {last_username}")
        
        # Increment the username
        last_username = increment_username(last_username)
        
    # Save the last username after starting all threads
    save_last_username(last_username)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
