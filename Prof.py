import time
import datetime
import pygame
import pyautogui


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "Dan.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print(f"Its {alarm_time}, Wake Up!!😊😊")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            pyautogui.hotkey("alt-f6")

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        


        time.sleep(1)
        




if __name__=="__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
    

    
