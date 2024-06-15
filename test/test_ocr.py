import time

from app import OcrManager, OCR_MAX_TASK_ID, auto_detect_wechat_lib_dir, auto_detect_wechat_ocr_path


def ocr(callback: callable):
    if not callback: raise Exception("callback is None")
    wechat_ocr_dir = auto_detect_wechat_ocr_path()
    wechat_dir = auto_detect_wechat_lib_dir()
    ocr_manager = OcrManager(wechat_dir)
    # 设置WeChatOcr目录
    ocr_manager.SetExePath(wechat_ocr_dir)
    # 设置微信所在路径
    ocr_manager.SetUsrLibDir(wechat_dir)
    # 设置ocr识别结果的回调函数
    ocr_manager.SetOcrResultCallback(callback)
    # 启动ocr服务
    ocr_manager.StartWeChatOCR()
    # 开始识别图片
    ocr_manager.DoOCRTask(r"img/1.png")
    time.sleep(1)
    while ocr_manager.m_task_id.qsize() != OCR_MAX_TASK_ID: pass
    # 识别输出结果
    ocr_manager.KillWeChatOCR()


def test_ocr():
    def ocr_result_callback(img_path: str, results: dict):
        assert isinstance(results.get('ocrResult'), list)
        assert results.get('ocrResult')[0].get('text') == 'GitLab Community Edition'
        print(results.get('ocrResult')[1].get('text'))

    ocr(ocr_result_callback)
