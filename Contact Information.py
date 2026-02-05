import sys
from PyQt5.QtWidgets import *

class ContactApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Contacts")
        self.resize(400, 300)

        self.contacts = {}

        layout = QVBoxLayout()

        self.name_in = QLineEdit()
        self.name_in.setPlaceholderText("Name")
        self.phone_in = QLineEdit()
        self.phone_in.setPlaceholderText("Phone Number")

        layout.addWidget(QLabel("Contact info"))
        layout.addWidget(self.name_in)
        layout.addWidget(self.phone_in)

        row = QHBoxLayout()
        self.add_btn = QPushButton("Add/Update")
        self.del_btn = QPushButton("Delete")
        row.addWidget(self.add_btn)
        row.addWidget(self.del_btn)
        layout.addLayout(row)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search...")
        layout.addWidget(self.search_bar)

        self.contacts_list = QListWidget()
        layout.addWidget(self.contacts_list)

        self.setLayout(layout)

        self.add_btn.clicked.connect(self.save_it)
        self.del_btn.clicked.connect(self.remove_it)
        self.contacts_list.itemClicked.connect(self.load_it)
        self.search_bar.textChanged.connect(self.search_it)

    def save_it(self):
        name = self.name_in.text()
        num = self.phone_in.text()

        if name and num:
            self.contacts[name] = num
            self.refresh_ui()
            self.name_in.clear()
            self.phone_in.clear()

    def remove_it(self):
        name = self.name_in.text()
        if name in self.contacts:
            self.contacts.pop(name)
            self.refresh_ui()
            self.name_in.clear()
            self.phone_in.clear()

    def load_it(self, item):
        text = item.text()
        name = text.split(" - ")[0]
        self.name_in.setText(name)
        self.phone_in.setText(self.contacts[name])

    def refresh_ui(self):
        self.contacts_list.clear()
        for name in self.contacts:
            self.contacts_list.addItem(f"{name} - {self.contacts[name]}")

    def search_it(self):
        txt = self.search_bar.text().lower()
        self.contacts_list.clear()
        for name, phone in self.contacts.items():
            if txt in name.lower() or txt in phone:
                self.contacts_list.addItem(f"{name} - {phone}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ContactApp()
    win.show()
    sys.exit(app.exec_())


