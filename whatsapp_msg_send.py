
import pywhatkit as pw
# import pyautogui
import time
import pyfiglet
from colorama import init, Fore, Style
init(autoreset=True)

# def countdown(seconds,phone_number,message,send_hour,send_minute):
#     for remaining in range(seconds, 0, -1):
#         # Clear the screen
#         print("\033c", end="")
#         print(f"{Fore.LIGHTGREEN_EX + Style.BRIGHT  } Message will be sent at {send_hour:02}:{send_minute:02}")
#     # Schedule the message
#         # phone_number = "+91"+phone_number
#         print(f"{Fore.CYAN + Style.BRIGHT  } phone no = +91 {phone_number} \n Massage =  { message}  \n    time =  { str(send_hour)} h  { str(send_minute+ 1)} m")

#         # Create the countdown banner
#         banner = pyfiglet.figlet_format(str(remaining), font="digital")

#         # Print the countdown banner in green
#         print(Fore.GREEN + Style.BRIGHT + banner)

#         # Wait for one second
#         time.sleep(1)

#     # Clear the screen for the final message
#     print("\033c", end="")

    # Print the final message
    # final_message = pyfiglet.figlet_format("msg send", font="digital")
    # print(Fore.RED + Style.BRIGHT + final_message)


def _priunt_msg():
    init(autoreset=True)
    # Print banner
    banner = pyfiglet.figlet_format("WP Sender", font="big")  # Use a larger font style
    print(Fore.YELLOW + Style.BRIGHT + "----------------------------------------------------------------------------------")
    print(Fore.YELLOW + Style.BRIGHT + banner)  # Change color and style
    print(Fore.YELLOW + Style.BRIGHT + "----------------------------------------------------------------------------------")
    print(Fore.RED + Style.BRIGHT + "created by drx  \t you can send whatsapp msg by time delay")  # Change color and style

while True:
    print("\033c", end="")
    _priunt_msg()
    print(Fore.CYAN + Style.BRIGHT + "----------------------------------------------------------------------------------")
    print(Fore.CYAN + Style.BRIGHT + "----------------------------------------------------------------------------------")
    
    # Get user inputs
    phone_number = input("Enter the phone number (without country code, e.g., XXXXXXXXXX): ")
    message = input("Enter the message: ")
    delay_minutes = int(input("Enter the delay time in minutes: "))

    # Get the current local time
    current_time = time.localtime()

    # Extract the hour and minute (already in 24-hour format)
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min

    # Calculate the time to send the message
    send_minute = current_minute + delay_minutes

    # Adjust the hour and minute if send_minute exceeds 59
    if send_minute >= 60:
        send_hour = (current_hour + send_minute // 60) % 24
        send_minute = send_minute % 60
    else:
        send_hour = current_hour
    current_seconds = current_hour * 3600 + current_minute * 60
    send_seconds = send_hour * 3600 + send_minute * 60
    delay_seconds = send_seconds - current_seconds

    print(f"{Fore.LIGHTGREEN_EX + Style.BRIGHT  } Message will be sent at {send_hour:02}:{send_minute:02}")
    # Schedule the message
    phone_number = "+91"+phone_number
    print(f"{Fore.CYAN + Style.BRIGHT  } phone no = {phone_number} \n Massage =  { message}  \n    time =  { str(send_hour)} h  { str(send_minute+ 1)} m")

    # countdown(delay_seconds,phone_number,message,send_hour,0)
    print("pleass wait...........")
    pw.sendwhatmsg(phone_number, message, int(send_hour), int(send_minute+1))

    # time.sleep(5)
    print(f"{Fore.LIGHTRED_EX + Style.BRIGHT  } Opened WhatsApp Web")

    # Wait for a while to ensure WhatsApp Web has loaded and the message box is focused
    time.sleep(5)

    # Press Enter to send the message
    # pyautogui.press('enter')
    print('Message successfully delivered')
