import sys
sys.path.insert(0, "/Users/rupeshbansal/embedchain")
import os

from embedchain import App
from embedchain.config.llm.base_llm_config import BaseLlmConfig

app = App()

current_path = os.path.dirname(__file__)
data_path = os.path.join(current_path, "data")
app.add(data_path, data_type="images")
