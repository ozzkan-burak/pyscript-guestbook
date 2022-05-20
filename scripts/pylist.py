
from cProfile import label
from datetime import datetime as dt

class PyItem(PyItemTemplate):
  pass

class PyList(PyListTemplate):
  item_class = PyItem

  def add(self, item):
    if isinstance(item,str):
      item = {"content": item, "created_at": dt.now()}
    super().add(item, labels=['content'])