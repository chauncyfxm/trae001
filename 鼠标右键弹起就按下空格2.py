from pynput import mouse, keyboard

开关 = False
def on_click(x, y, button, pressed):
    global 开关
    if button == mouse.Button.right and not pressed and 开关:
        # 当鼠标右键被释放时

        print("鼠标:按了一下a按键")
        kb = keyboard.Controller()
        kb.press('a')
        kb.release('a')

    if button == mouse.Button.x1 and not pressed:
        开关 = not 开关



def on_release(key):
    global 开关
    try:
        if key.char in ['w', 'q', 'e', 'r', 'd', 'f'] and 开关:
            # 当键盘 W 键被释放时

            kb = keyboard.Controller()
            print("键盘:按了一下a按键")
            kb.press('a')
            kb.release('a')

    except AttributeError:
        pass


with mouse.Listener(on_click=on_click) as mouse_listener , keyboard.Listener(on_release=on_release) as keyboard_listener:
    # 保持程序运行
    print('开始执行')
    mouse_listener.join()
    keyboard_listener.join()





