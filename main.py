import os

import pytest

os.chdir(os.path.join(os.path.dirname(__file__), 'test'))
pytest.main(["-s", "test_ocr.py"])
