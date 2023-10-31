import pywhatkit as kit
import time

# List of phone numbers to send messages
phone_numbers = ["+911234567890", "+919876543210"]

# Message to send
message = "Hello, this is a test message from pywhatkit!"

# Number of messages to send
num_messages = 5

# Time to send the first message (24 hour format)
hours = 10
minutes = 0

for phone_number in phone_numbers:
    for i in range(num_messages):
        # Send the message
        kit.sendwhatmsg(phone_number, message, hours, minutes)

        # Print a confirmation message
        print(f"Message sent to {phone_number} at {hours}:{minutes}")

        # Increment the time for the next message
        minutes += 1
        if minutes > 59:
            minutes = 0
            hours += 1
            if hours > 23:
                hours = 0

        # Wait for a while before sending the next message
        time.sleep(60)
