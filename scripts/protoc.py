import subprocess
import os


def check_protoc_installed():
    try:
        subprocess.check_call(["protoc", "--version"], stdout=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        raise Exception("Protocol Buffers compiler (protoc) is not installed.")


def generate_protobuf(python_out, proto_path, proto_file):
    # 构建 protoc 命令
    command = f'protoc --python_out="{python_out}" --proto_path="{proto_path}" "{proto_file}"'

    # 执行命令
    try:
        subprocess.check_call(command, shell=True)
        print(f"Generated Python files from {proto_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating Python files: {e}")


if __name__ == "__main__":
    check_protoc_installed()
    protobuf_dir = '..\\protobuf'
    _abs = os.path.abspath
    init_lines = []
    for e in os.listdir(protobuf_dir):
        if not e.endswith('.proto'): continue
        init_lines.append(f'from . import {e[0:-6]}_pb2')
        generate_protobuf(
            _abs(f'{protobuf_dir}\\output'),
            _abs(protobuf_dir),
            _abs(f'{protobuf_dir}\\{e}'),
        )
    with open(_abs(f'{protobuf_dir}\\output\\__init__.py'), 'w') as f:
        f.write('\n'.join(init_lines))
        f.write('\n')
    print("All done.")
