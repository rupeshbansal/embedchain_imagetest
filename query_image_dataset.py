from embedchain import App
from embedchain.config.llm.base_llm_config import BaseLlmConfig

app = App()

text = sys.argv[1]
print(app.query(text, config = BaseLlmConfig(query_type = "Images")))
