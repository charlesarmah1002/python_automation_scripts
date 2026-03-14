import pywhatkit as kit
import time

message = """Hi, good evening
How are you doing?
My name is Wesley from Boafou, I took your contact details after registering you with the Boafou app on WhatsApp

Please use this link to join our Community to allow us to reach out to our support staff and also make contributions.

Note: We run periodic competitions that could earn you some prizes.

Thank you.
https://chat.whatsapp.com/Gwu7GOe23g983WeYIwmFfp
"""

numbers = [
    "+233599056413",
    "+233545815392",
    "+233551951956",
    "+233278959295",
    "+233592840122",
    "+233591070759",
    "+233557005154",
    "+233530230854",
    "+233553291790",
    "+233594267872",
    "+233599912062"
]

for number in numbers:
    try:
        kit.sendwhatmsg_instantly(number, message, wait_time=60, tab_close=False)
        print(f"Message sent to {number}")
        time.sleep(120)  # delay to avoid spam detection
    except Exception as e:
        print(f"Failed to send to {number}: {e}")
