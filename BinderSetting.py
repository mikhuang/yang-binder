import io
import requests


def get_resource_url(res):
    if res["type"] == "gdoc":
        return "https://docs.google.com/document/d/{}/export?format=pdf".format(
            res["id"]
        )
    return None
    # - https://www.howtogeek.com/400707/how-to-share-links-to-your-google-doc-as-a-pdf/ replace “edit?usp=sharing” with “export?format=pdf”


class BinderSetting:
    def __init__(self, settings):
        self.settings = settings

    def buffer_resources(self):
        buffers = []
        for res in self.settings["resources"]:
            url = get_resource_url(res)
            if url:
                print(url)
                content = requests.get(url).content
                buffers.append(io.BytesIO(content))
        return buffers
