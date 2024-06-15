import winreg
import os
import re

WECHAT_DIR = None
WECHAT_VERSION_DIR_RE = re.compile(r'^\[\d+\.\d+\.\d+\.\d+]$')


def _find_max_number_dir(path, append_extracted=True):
    if not os.path.exists(path): raise Exception(f'{path} not found')
    max_number = -1
    for name in os.listdir(path):
        if not name.isdigit(): continue
        number = int(name)
        if number > max_number: max_number = number
    if max_number == -1: raise Exception(f'no number dir found in {path}')
    return os.path.join(path, str(max_number), 'extracted' if append_extracted else '')


def auto_detect_plugins_dir():
    app_data_dir = os.getenv('APPDATA')
    if not app_data_dir: raise Exception('APPDATA not found')
    return f'{app_data_dir}\\Tencent\\WeChat\\XPlugin\\Plugins'


def auto_detect_wechat_dir():
    def query_wechat_dir():
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Tencent\WeChat', 0, winreg.KEY_READ) as key:
                return winreg.QueryValueEx(key, 'InstallPath')[0]
        except FileNotFoundError:
            return None

    global WECHAT_DIR
    if WECHAT_DIR: return WECHAT_DIR
    WECHAT_DIR = query_wechat_dir()
    if not WECHAT_DIR: raise Exception('WeChat install dir not found')
    return WECHAT_DIR


def auto_detect_wechat_lib_dir():
    wechat_dir = auto_detect_wechat_dir()
    for e in os.listdir(wechat_dir):
        r = WECHAT_VERSION_DIR_RE.search(e)
        if r: return os.path.join(wechat_dir, e)
    raise Exception(f'no version dir found in {wechat_dir}')


def auto_detect_wechat_ocr_path():
    pre_dir = f'{auto_detect_plugins_dir()}\\WeChatOCR'
    path = _find_max_number_dir(pre_dir)
    path = f'{path}\\WeChatOCR.exe'
    if not os.path.exists(path): raise Exception(f'{path} not found')
    return path


def auto_detect_wechat_RadiumWMPF_path():
    pre_dir = f'{auto_detect_plugins_dir()}\\RadiumWMPF'
    path = _find_max_number_dir(pre_dir)
    path = f'{path}\\runtime\\WeChatAppEx.exe'
    if not os.path.exists(path): raise Exception(f'{path} not found')
    return path


if __name__ == '__main__':
    print(auto_detect_wechat_ocr_path())
    print(auto_detect_wechat_RadiumWMPF_path())
    print(auto_detect_wechat_dir())
    print(auto_detect_wechat_lib_dir())
    print(auto_detect_plugins_dir())