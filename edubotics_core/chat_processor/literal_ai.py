from chainlit.data import ChainlitDataLayer


# update custom methods here (Ref: https://github.com/Chainlit/chainlit/blob/4b533cd53173bcc24abe4341a7108f0070d60099/backend/chainlit/data/__init__.py)
class CustomLiteralDataLayer(ChainlitDataLayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
