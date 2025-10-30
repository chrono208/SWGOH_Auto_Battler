import pyautogui
import time

# Function to perform the desired mouse actions
def perform_mouse_macro():
    # Get the current mouse position
    original_position = pyautogui.position()

    # Click at the current position
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()

    # Slide left by 40 pixels
    pyautogui.move(-930, 0, duration=0.5)

    # Move up by 1000 pixels
    pyautogui.move(0, -650, duration=0.5)

    time.sleep(8)
    # Click again
    pyautogui.click()

    # Move back to the original position
    pyautogui.moveTo(original_position[0], original_position[1], duration=0.5)

# Give some time to switch to the desired application
time.sleep(5)

# Loop for 500 times
for _ in range(500):
    # Call the function to perform the mouse macro
    perform_mouse_macro()

    # Wait for 2 minutes before the next iteration
    time.sleep(80)