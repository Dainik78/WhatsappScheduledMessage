# WhatsappScheduledMessage
This script will send a specified number of messages to each phone number in the phone_numbers list. The time for each message is incremented by one minute.

Please note that you need to have the WhatsApp web page open in your default browser for pywhatkit to work. Also, be aware of WhatsApp’s usage policies to avoid getting your number banned for spamming.

Remember to replace "+911234567890" and "+919876543210" with the actual phone numbers you want to send messages to. The phone numbers should be in international format.

Also, replace "Hello, this is a test message from pywhatkit!" with the actual message you want to send.

You can adjust num_messages, hours, and minutes according to your needs. The hours and minutes specify the time to send the first message in 24-hour format. The script will wait for one minute (time.sleep(60)) before sending the next message
