from pynput import mouse, keyboard


def on_click(x, y, button, pressed):
    if button == mouse.Button.right and not pressed:
        # 当鼠标右键被释放时
        kb = keyboard.Controller()
        kb.press('a')
        kb.release('a')


def on_release(key):
    try:
        if key.char in ['w', 'q', 'e', 'r', 'd', 'f']:
            # 当键盘 W 键被释放时
            kb = keyboard.Controller()
            kb.press('a')
            kb.release('a')
    except AttributeError:
        pass


with mouse.Listener(on_click=on_click) as mouse_listener , keyboard.Listener(on_release=on_release) as keyboard_listener:
    # 保持程序运行
    print('开始执行')
    mouse_listener.join()
    keyboard_listener.join()





