from photoshop import Application
from photoshop.constants import LayerKind
from photoshop.constants import Adobe
from datetime import datetime

app = Application()

layers = app.activeDocument.layerSets.getByName("template")

data = {
    "project": "test_project",
    "datetime": str(datetime.today())
}
for layer in layers:
    # print(layer.textItem.name)
    layer.textItem.contents = data.get(layer.textItem.contents, "")
