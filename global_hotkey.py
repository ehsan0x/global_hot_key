import os
import shutil
from datetime import datetime

from mss import mss
from pynput import keyboard

print(
    'List of shortcuts:'
    '\n{:16}Delete Log and Info folder'
    '\n{:16}Run pgsloader'
    '\n{:16}Kill pgsloader'
    '\n{:16}Run Clicker'
    '\n{:16}Take screenshot'
    '\n{:16}Exit'.format('alt+ctrl+q:', 'alt+ctrl+w:', 'alt+ctrl+e:',
                         'k:', 'shift+ctrl+z:', 'alt+ctrl+x:')
)


def delete_log_info():
    game_info_path = "C:/Game_Info"
    game_logs_path = "C:/Game_Logs"

    # keeps the read-only file intact in the folders
    # deletes the rest of the files
    if os.path.exists(game_info_path):
        shutil.rmtree(game_info_path, ignore_errors=True)

    if os.path.exists(game_logs_path):
        shutil.rmtree(game_logs_path, ignore_errors=True)


def pgs_loader():
    try:
        os.startfile('C:/Program Files/pgsLoaderX64/pgsLoader_x64.exe')
    except FileNotFoundError:
        print('The file you are trying to access does not exist.')


def pgs_killer():
    try:
        os.system("taskkill /f /im pgsLoader*")
        os.system("start C:\Windows\explorer.exe")
    except FileNotFoundError:
        print('The file you are trying to access does not exist.')


# def load_pos():
#     try:
#         os.startfile('C:/POS')
#     except FileNotFoundError:
#         print('The directory you are trying to open does not exist.')
#
#
# def load_pos_sales_app():
#     try:
#         os.startfile('C:/POSTechSupport/Demo_PointOfSalesApp')
#     except FileNotFoundError:
#         print('The directory you are trying to open does not exist.')


# <ctrl>+<shift>+z
def screenshot():
    mss().shot()
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = current_time + '.png'
    os.rename('monitor-1.png', filename)

    # HOMEPATH from environment variables refers to current user directory
    # os.path.join concatenates the two parts of the path to Pictures folder
    shutil.move(filename, os.path.join(os.environ['HOMEPATH'], "Pictures"))


def load_clicker():
    try:
        os.startfile('clicker\\clicker.exe')
    except FileNotFoundError:
        print('The clicker file was not found.\nPlease make sure the file is placed correctly.')


# <alt>+<ctrl>+x
def exit_program():
    exit()


with keyboard.GlobalHotKeys({
    '<alt>+<ctrl>+q': delete_log_info,
    '<alt>+<ctrl>+w': pgs_loader,
    '<alt>+<ctrl>+e': pgs_killer,
    # '<alt>+<ctrl>+r': load_pos,
    # '<alt>+<ctrl>+t': load_pos_sales_app,
    '<ctrl>+<shift>+z': screenshot,
    'k': load_clicker,
    '<alt>+<ctrl>+x': exit_program}) as h:
    h.join()
