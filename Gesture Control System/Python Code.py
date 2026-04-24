import serial
import time
import pyautogui

ArduinoSerial = serial.Serial('COM3', 9600)  # change port
time.sleep(2)

while True:
    incoming = ArduinoSerial.readline().decode('utf-8').strip()
    print(incoming)

    if 'Play/Pause' in incoming:
        pyautogui.press('space')

    elif 'Rewind' in incoming:
        pyautogui.hotkey('ctrl', 'left')

    elif 'Forward' in incoming:
        pyautogui.hotkey('ctrl', 'right')

    elif 'Vup' in incoming:
        pyautogui.press('volumeup')

    elif 'Vdown' in incoming:
        pyautogui.press('volumedown')
