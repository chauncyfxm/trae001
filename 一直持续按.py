from pynput import mouse, keyboard
import time
import random
import threading


class InputAutomation:
    def __init__(self):
        # 初始化持续按键开关
        self.continuous_press_enabled = False
        # 初始化键盘控制器
        self.keyboard_controller = keyboard.Controller()

    def on_click(self, x, y, button, pressed):
        # 鼠标右键释放时按下 'a' 键
        if button == mouse.Button.right and not pressed:
            self.keyboard_controller.press('a')
            self.keyboard_controller.release('a')

    def toggle_continuous_press(self, x, y, button, pressed):
        # 鼠标侧键释放时切换持续按键开关状态
        if button == mouse.Button.x1 and not pressed:
            self.continuous_press_enabled = not self.continuous_press_enabled
            status = "打开" if self.continuous_press_enabled else "关闭"
            print(f'开关已经{status}')

    def on_key_release(self, key):
        try:
            # 特定键盘按键释放时按下 'a' 键
            if key.char in ['w', 'q', 'e', 'r', 'd', 'f']:
                self.keyboard_controller.press('a')
                self.keyboard_controller.release('a')
        except AttributeError:
            pass

    def continuous_press_loop(self):
        while True:
            time.sleep(0.05)
            if self.continuous_press_enabled:
                # 生成 0.2 到 0.4 之间的随机小数
                random_interval = random.uniform(0.0503, 0.1835)
                self.keyboard_controller.press('a')
                self.keyboard_controller.release('a')
                time.sleep(random_interval)


if __name__ == "__main__":
    automation = InputAutomation()
    # 创建鼠标监听器
    mouse_listener = mouse.Listener(on_click=automation.toggle_continuous_press)
    # 创建键盘监听器
    # keyboard_listener = keyboard.Listener(on_release=automation.on_key_release)
    # 启动鼠标监听器
    mouse_listener.start()
    # 启动键盘监听器
    # keyboard_listener.start()
    print('开始执行')

    # 创建并启动持续按键循环线程
    continuous_press_thread = threading.Thread(target=automation.continuous_press_loop)
    continuous_press_thread.daemon = True
    continuous_press_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("程序已停止")
    finally:
        # 停止鼠标监听器
        mouse_listener.stop()
        # 停止键盘监听器
        # keyboard_listener.stop()
    