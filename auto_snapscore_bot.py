import pyautogui
import time
import sys
from colorama import init, Fore, Style
from pynput import keyboard
import threading

# Initialize colorama for colored console output
init(autoreset=True)

# Global flags
sequence_running = False  # To prevent overlapping sequences
stop_bot = False          # To signal the bot to stop

def on_press_f(key):
    """
    Listener callback for recording positions when 'f' key is pressed.
    """
    try:
        if key.char.lower() == 'f':
            return False  # Stop listener
    except AttributeError:
        pass  # Ignore special keys

def wait_for_f():
    """
    Wait for the user to press the 'f' key.
    """
    with keyboard.Listener(on_press=on_press_f) as listener:
        listener.join()

def get_coordinate(prompt):
    """
    Prompt the user to move the cursor to a specific UI element and press 'f' to record its position.
    """
    print(f"{Fore.YELLOW}{prompt}")
    print(f"{Fore.CYAN}Move your cursor to the desired location and press 'f' to record the position.")
    wait_for_f()
    x, y = pyautogui.position()
    print(f"{Fore.GREEN}Recorded position: ({x}, {y})\n")
    return (x, y)

def confirm_positions(positions):
    """
    Display the recorded positions and ask for user confirmation.
    """
    print(f"{Fore.MAGENTA}You have set the following positions:")
    for key, value in positions.items():
        print(f"  {key}: {value}")
    confirm = input(f"{Fore.YELLOW}Are these positions correct? (y/n): ").lower()
    if confirm != 'y':
        print(f"{Fore.RED}Let's start over.\n")
        main()
    else:
        print(f"{Fore.GREEN}Positions confirmed. You can now press 'i' to start the bot or 'esc' to exit.\n")

def perform_actions_round1(positions):
    """
    Perform the first round of automated actions using pyautogui.
    Includes clicking Arrow Down and Multisnap.
    """
    try:
        # Move to Camera Icon and click
        print(f"{Fore.CYAN}Round 1: Moving to Camera Icon at position {positions['camera_icon']} and clicking...")
        pyautogui.moveTo(positions['camera_icon'][0], positions['camera_icon'][1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # Click Arrow Down
        print(f"{Fore.CYAN}Round 1: Clicking Arrow Down at position {positions['arrow_down']}...")
        pyautogui.moveTo(positions['arrow_down'][0], positions['arrow_down'][1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # Click Multisnap
        print(f"{Fore.CYAN}Round 1: Clicking Multisnap at position {positions['multisnap']}...")
        pyautogui.moveTo(positions['multisnap'][0], positions['multisnap'][1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # Click Take Picture Button 7 times
        print(f"{Fore.CYAN}Round 1: Clicking Take Picture Button 7 times at position {positions['take_picture']}...")
        for i in range(7):
            pyautogui.moveTo(positions['take_picture'][0], positions['take_picture'][1], duration=0.2)
            pyautogui.click()
            time.sleep(0.5)
            print(f"{Fore.GREEN}Round 1: Clicked {i+1}/7")
        
        # Click Edit and Send
        print(f"{Fore.CYAN}Round 1: Clicking Edit and Send at position {positions['edit_send']}...")
        pyautogui.moveTo(positions['edit_send'][0], positions['edit_send'][1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # Click Send To
        print(f"{Fore.CYAN}Round 1: Clicking Send To at position {positions['send_to']}...")
        pyautogui.moveTo(positions['send_to'][0], positions['send_to'][1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # Click Shortcut
        print(f"{Fore.CYAN}Round 1: Clicking Shortcut at position {positions['shortcut']}...")
        pyautogui.moveTo(positions['shortcut'][0], positions['shortcut'][1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # Click Select All
        print(f"{Fore.CYAN}Round 1: Clicking Select All at position {positions['select_all']}...")
        pyautogui.moveTo(positions['select_all'][0], positions['select_all'][1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # Click Send
        print(f"{Fore.CYAN}Round 1: Clicking Send at position {positions['send']}...")
        pyautogui.moveTo(positions['send'][0], positions['send'][1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        print(f"{Fore.GREEN}Round 1 completed successfully!\n")

    except Exception as e:
        print(f"{Fore.RED}An error occurred during Round 1: {e}\n")

def perform_actions_round2(positions):
    """
    Perform the second round of automated actions using pyautogui.
    Excludes clicking Arrow Down and Multisnap.
    """
    try:
        # Move to Camera Icon and click
        print(f"{Fore.CYAN}Round 2: Moving to Camera Icon at position {positions['camera_icon']} and clicking...")
        pyautogui.moveTo(positions['camera_icon'][0], positions['camera_icon'][1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # Click Take Picture Button 7 times
        print(f"{Fore.CYAN}Round 2: Clicking Take Picture Button 7 times at position {positions['take_picture']}...")
        for i in range(7):
            pyautogui.moveTo(positions['take_picture'][0], positions['take_picture'][1], duration=0.2)
            pyautogui.click()
            time.sleep(0.5)
            print(f"{Fore.GREEN}Round 2: Clicked {i+1}/7")
        
        # Click Edit and Send
        print(f"{Fore.CYAN}Round 2: Clicking Edit and Send at position {positions['edit_send']}...")
        pyautogui.moveTo(positions['edit_send'][0], positions['edit_send'][1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # Click Send To
        print(f"{Fore.CYAN}Round 2: Clicking Send To at position {positions['send_to']}...")
        pyautogui.moveTo(positions['send_to'][0], positions['send_to'][1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # Click Shortcut
        print(f"{Fore.CYAN}Round 2: Clicking Shortcut at position {positions['shortcut']}...")
        pyautogui.moveTo(positions['shortcut'][0], positions['shortcut'][1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # Click Select All
        print(f"{Fore.CYAN}Round 2: Clicking Select All at position {positions['select_all']}...")
        pyautogui.moveTo(positions['select_all'][0], positions['select_all'][1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # Click Send
        print(f"{Fore.CYAN}Round 2: Clicking Send at position {positions['send']}...")
        pyautogui.moveTo(positions['send'][0], positions['send'][1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        print(f"{Fore.GREEN}Round 2 completed successfully!\n")

    except Exception as e:
        print(f"{Fore.RED}An error occurred during Round 2: {e}\n")

def start_sequence(positions):
    """
    Start the automated sequence immediately upon pressing 'i'.
    Executes Round 1 and then continuously executes Round 2 until 'p' is pressed.
    """
    global sequence_running, stop_bot
    if sequence_running:
        print(f"{Fore.YELLOW}A sequence is already running. Please wait until it finishes.\n")
        return
    sequence_running = True
    stop_bot = False
    try:
        # Execute Round 1 once
        perform_actions_round1(positions)
        
        # Continuously execute Round 2 until stop_bot is True
        while not stop_bot:
            perform_actions_round2(positions)
    finally:
        sequence_running = False

def on_press_listener(key, positions):
    """
    Listener callback for 'i', 'p', and 'esc' keys.
    """
    global stop_bot
    try:
        if key.char.lower() == 'i':
            # Start the sequence in a separate thread
            threading.Thread(target=start_sequence, args=(positions,), daemon=True).start()
        elif key.char.lower() == 'p':
            # Signal the bot to stop
            if sequence_running:
                print(f"{Fore.YELLOW}Stop signal received. Stopping the bot after the current round completes...\n")
                stop_bot = True
            else:
                print(f"{Fore.YELLOW}Bot is not running.\n")
        elif key == keyboard.Key.esc:
            # Exit the bot gracefully
            print(f"\n{Fore.RED}Exiting the bot. Goodbye!")
            stop_bot = True
            return False  # Stop listener
    except AttributeError:
        pass  # Ignore special keys

def main():
    """
    Main function to set up the bot and start listening for key presses.
    """
    positions = {}
    print(f"{Fore.BLUE}=== Auto Snapscore Bot Setup ===\n")

    # Record positions for all required UI elements
    positions['camera_icon'] = get_coordinate("Step 1: Move to the CAMERA ICON and press 'f'")
    positions['arrow_down'] = get_coordinate("Step 2: Move to the ARROW DOWN and press 'f'")
    positions['multisnap'] = get_coordinate("Step 3: Move to the MULTISNAP and press 'f'")
    positions['take_picture'] = get_coordinate("Step 4: Move to the TAKE PICTURE BUTTON and press 'f'")
    positions['edit_send'] = get_coordinate("Step 5: Move to the EDIT AND SEND BUTTON and press 'f'")
    positions['send_to'] = get_coordinate("Step 6: Move to the SEND TO BUTTON and press 'f'")
    positions['shortcut'] = get_coordinate("Step 7: Move to the SHORTCUT BUTTON and press 'f'")
    positions['select_all'] = get_coordinate("Step 8: Move to the SELECT ALL BUTTON and press 'f'")
    positions['send'] = get_coordinate("Step 9: Move to the SEND BUTTON and press 'f'")

    # Confirm all recorded positions
    confirm_positions(positions)

    print(f"{Fore.BLUE}=== Bot is ready ===")
    print(f"{Fore.YELLOW}Press the 'i' key to start the Snapscore process.")
    print(f"{Fore.YELLOW}Press the 'p' key to stop the bot.")
    print(f"{Fore.YELLOW}Press the 'esc' key to exit the bot.\n")

    # Start the keyboard listener
    with keyboard.Listener(on_press=lambda key: on_press_listener(key, positions)) as listener:
        listener.join()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Bot aborted by user.")
        sys.exit()
