import tkinter as tk
import subprocess
import configparser

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

# 获取Python文件路径并去除引号
python_file_path = config.get('Paths', 'python_file', fallback='').strip('"')

# 初始化子进程变量
process = None

# 定义按钮点击事件
def toggle_process():
    global process
    if process is None:
        if python_file_path:
            try:
                process = subprocess.Popen(['python', python_file_path])
                button.config(text='关闭程序')
            except Exception as e:
                print(f'执行文件时出错: {e}')
        else:
            print('未找到配置文件中的Python文件路径。')
    else:
        process.terminate()
        process.wait()
        process = None
        button.config(text='执行Python文件')

# 创建主窗口
root = tk.Tk()
root.geometry('300x300')
root.title('执行Python文件')

# 创建按钮
button = tk.Button(root, text='执行Python文件', command=toggle_process)
button.pack(pady=20)

# 运行主循环
root.mainloop()