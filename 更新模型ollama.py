import subprocess


def update_single_model(model_name):
    try:
        # 明确指定编码为 utf-8
        result = subprocess.run(['ollama', 'pull', model_name], capture_output=True, text=True, encoding='utf-8', check=True)
        print(f"成功更新模型 {model_name}:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"更新模型 {model_name} 时出错: {e.stderr}")


def update_all_models():
    try:
        # 明确指定编码为 utf-8
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, encoding='utf-8', check=True)
        lines = result.stdout.strip().split('\n')
        # 跳过标题行
        model_names = [line.split()[0] for line in lines[1:]]

        for model_name in model_names:
            update_single_model(model_name)
    except subprocess.CalledProcessError as e:
        print(f"获取模型列表时出错: {e.stderr}")


if __name__ == "__main__":
    # 更新单个模型
    # update_single_model('llama2')

    # 更新所有模型
    update_all_models()