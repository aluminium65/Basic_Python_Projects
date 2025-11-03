import curses
from curses import wrapper
import time
import random



target_texts = ["The bright autumn leaves swirled and danced across the pavement in a vibrant, colorful ballet.","She finally understood the complex mathematical equation after hours of focused study and deep concentration.",
"Hiking through the dense forest offered a much-needed escape from the hustle and bustle of city life.","He carefully packed his essential belongings into a sturdy backpack, ready for the long journey ahead.",
"The old lighthouse stood tall against the stormy, dark sky, guiding ships safely toward the harbor.","Learning a new language opens up fascinating opportunities to connect with diverse cultures worldwide.",
"A steaming mug of rich, dark hot chocolate felt wonderfully comforting on the chilly winter evening.","The dedicated team worked tirelessly all night long to meet the challenging and important project deadline.",
"Sunlight streamed through the window, illuminating dust motes suspended in the quiet, peaceful morning air.","Reading classic literature provides timeless insights into the human condition and universal emotional experiences."]

target_text = random.choice(target_texts)
typed_text = []

welcome_screen = ("""
 _         _   _____   _ _     _ _       _________                        
|$|       |$| |$$$$$| |$| \\   / |$|     |$$$$$$$$$|                      
|$|       |$| |$|__$| |$|  \\_/  |$|  _____  |$|    __   __   ___       __  __
|$|   _   |$| |$$$$$| |$|       |$| |$$$$$| |$|   |  | |  | |   | | / |   |  |
|$|  / \\  |$| |$|     |$|       |$|         |$|   | /  |--| |     |-  |-- | /
|&|_/   \\_|$| |$|     |$|       |$|         |$|   | \\_ |  | |___| | \\ |__ | \\_


--------------------------------By aluminium-----------------------------------   
""")


def start(stdscr):
    stdscr.clear()
    stdscr.addstr(welcome_screen, curses.color_pair(5))
    stdscr.addstr(12 ,0 ,"[+] Welcome to Typing Speed Test!")
    stdscr.addstr(14 ,0 ,"--> You will be given a sentence to type.")
    stdscr.addstr(15 ,0 ,"--> Type the sentence as fast as possible.")
    stdscr.addstr(17, 0, "--> Press any key to continue....")
    stdscr.getkey()


def overlay_text(stdscr, target, current, wpm=0):
    stdscr.addstr(welcome_screen, curses.color_pair(5))
    stdscr.addstr(12, 0, target)
    stdscr.addstr(14, 0, f"[+] WPM : {wpm}")
    stdscr.addstr(20, 0, "--> Press ESC to quit.", curses.color_pair(3))
    row = 12

    for i, char in enumerate(current):
        correct_char = target[i]
        if char == " ":
            if char != target[i]:
                color = curses.color_pair(2)
                stdscr.addstr(row, i, "_", color)
            else:
                stdscr.addstr(row, i, " ")
        elif char == correct_char:
            color = curses.color_pair(1)
            stdscr.addstr(row, i, char, color)

        else:
            color = curses.color_pair(2)
            stdscr.addstr(row, i, char, color)
        

def tester(stdscr):
    global target_text
    global wpm
    ro, co = stdscr.getmaxyx()
    target_text = target_text[:co]
    wpm = 0
    start_time = time.time()

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(typed_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()


        overlay_text(stdscr, target_text, typed_text, wpm)
        stdscr.refresh()

        if "".join(typed_text) == target_text:
            break

        try:
            key = stdscr.getkey()
        except:
            continue


        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(typed_text) > 0:
                typed_text.pop()
        elif ord(key) == 27:
            break
        elif len(typed_text) < len(target_text):
            typed_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)

    start(stdscr)
    tester(stdscr)
    stdscr.clear()
    stdscr.addstr(welcome_screen, curses.color_pair(5))
    stdscr.addstr(14, 0, "[+] You've completed the text....")
    stdscr.addstr(16, 0, f"[+] WPM : {wpm}")
    stdscr.addstr(18, 0, "--> Press Enter to exit.")
    stdscr.addstr(12, 0, "[GITHUB] https://github.com/aluminium65/")
    stdscr.getkey()
        
wrapper(main)