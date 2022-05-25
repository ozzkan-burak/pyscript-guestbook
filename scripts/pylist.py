from datetime import datetime as dt

class PyItem(PyItemTemplate):
    def on_click(self, evt=None):
        self.data["deleted"] = not self.data["deleted"]
        self.strike(self.data["deleted"])
        self.select("input").element.checked = self.data["deleted"]

    def render_content(self):
        string = " 📖 ".join([self.data[f] for f in self.labels])
        created_time = self.data["created_at"].strftime("%d %b-%y %H:%M")
        return string + "<br/>" + f"<small class='timestamp'>🕒 invited at: {created_time}</small>"

class PyList(PyListTemplate):
    item_class = PyItem

    def add(self, item):
        if isinstance(item, str):
            name, email = [x.strip() for x in item.split(',')]

            item = {"name": name, "email": email, "deleted": False, "created_at": dt.now()}

        super().add(item, labels=['name', "email"], state_key="deleted")