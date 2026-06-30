import argparse
import sys
import keyboard

def sys_write(message: str) -> None:
    """Shortens sys.stdout.write and flushes with a newline"""
    sys.stdout.write(message + "\n")

def detect_shortcut() -> None:
    global shortcut_pressed
    shortcut_pressed = True

# def shortcut_listener() -> None:
#     keyboard.add_hotkey("ctrl+m", detect_shortcut)

def acquire_input(message: str) -> str:
    user_input = input(message)
    return user_input

def file_not_detected() -> None:
    while True:
        user_input = acquire_input("acquiring user input: ")
        sys_write(user_input + '\n')

        if keyboard.is_pressed("ctrl+d"):
            sys_write("successfully stopped")
            break

def setup_parser() -> None:
    """Sets up argparse and the arguments"""
    global parser
    global args

    parser = argparse.ArgumentParser()
    
    parser.add_argument("file", help="file you wish to work with", nargs="*")
    parser.add_argument("-n", "--number_output_lines", help="number every output line", action="store_true")
    parser.add_argument("-b", "--number_non_blank_lines", help="number every non-blank lines", action="store_true")

    args = parser.parse_args()

def detect_cat() -> None: # needs a better name for this
    if not args.file:
        file_not_detected()        
    else:
        sys_write("files detected")


def main() -> None:
    setup_parser()
    detect_cat()    


if __name__ == "__main__":
    main()

    