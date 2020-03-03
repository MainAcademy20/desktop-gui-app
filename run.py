from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QComboBox, QLineEdit
from models import Text

Text.create_table()

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
line_edit = QLineEdit()
button1 = QPushButton('Add')
button2 = QPushButton('Delete')

combobox = QComboBox()
texts = [t.text for t in Text.select()]
combobox.addItems(texts)

layout.addWidget(line_edit)
layout.addWidget(button1)
layout.addWidget(combobox)
layout.addWidget(button2)

window.setLayout(layout)
window.show()


def on_button1_click():
    user_value = line_edit.text()
    if not user_value:
        return

    Text.create(text=user_value)
    combobox.addItem(user_value)


def on_button2_click():
    selected = combobox.currentText()
    idx = combobox.currentIndex()
    Text.delete().where(Text.text == selected).execute()
    combobox.removeItem(idx)


button1.clicked.connect(on_button1_click)
button2.clicked.connect(on_button2_click)
app.exec()
