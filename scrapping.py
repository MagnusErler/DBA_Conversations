from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome WebDriver (you need to have Chrome and ChromeDriver installed)
driver = webdriver.Chrome()

# The URL of the website
url = "your_DBA_item"

# Open the webpage
driver.get(url)

# Wait for the user to log in manually
input("Please log in manually and press Enter when ready...")

# Find all the chat items
chat_items = driver.find_elements(By.CLASS_NAME, "messaging-item-clickable")

# Create a text file to save the conversations
with open("conversations.txt", "w", encoding="utf-8") as file:
    for idx, chat_item in enumerate(chat_items, start=1):
        # Open the chat by clicking on it
        chat_item.click()
        
        # Wait for the chat to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "message-centered")))
        
        # Find all the messages in the chat
        messages = driver.find_elements(By.CLASS_NAME, "message")
        
        # Print conversation to show progress
        print(f"Conversation {idx}/{len(chat_items)}:")
        
        # Write the conversation to the text file
        file.write(f"Conversation {idx}/{len(chat_items)}:\n")
        for message in messages:
            # Extract the sender's name
            sender_name = message.find_element(By.CLASS_NAME, "username").text.strip()
            
            # Extract the timestamp
            timestamp = message.find_element(By.CLASS_NAME, "created").text.strip()
            
            # Extract the message text
            message_text = message.find_element(By.CLASS_NAME, "text").text.strip()
            
            # Write the message with sender's name and timestamp to the text file
            file.write(f"{timestamp} - {sender_name}: {message_text}\n")
        
        # Locate and click the "Tilbage til samtaler" button by its text
        back_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Tilbage til samtaler')]")
        back_button.click()
    
    # Close the text file
    file.close()

# Keep the browser window open until you manually close it
input("Press Enter to close the browser...")

# Close the browser
driver.quit()
