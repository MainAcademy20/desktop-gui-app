from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QComboBox, QLineEdit
from models import Text, List, db

db.create_tables([Text, List])

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
new_list = QLineEdit()
line_edit = QLineEdit()
button1 = QPushButton('Add')
button2 = QPushButton('Delete')
add_list_btn = QPushButton('New List')

texts = QComboBox()
lists = QComboBox()

txts = [t.text for t in Text.select()]
lists_models = [l for l in List.select()]
if not lists_models:
    lists_models.append(List.create(name='Default'))

lists.addItems([l.name for l in lists_models])
texts.addItems([txt.text for txt in lists_models[0].texts])

layout.addWidget(lists)
layout.addWidget(new_list)
layout.addWidget(add_list_btn)
layout.addWidget(line_edit)
layout.addWidget(button1)
layout.addWidget(texts)
layout.addWidget(button2)

window.setLayout(layout)
window.show()


def on_button1_click():
    user_value = line_edit.text()
    if not user_value:
        return
    current_list = List.get(name=lists.currentText())
    Text.create(text=user_value, list_=current_list)
    texts.addItem(user_value)


def on_button2_click():
    selected = texts.currentText()
    idx = texts.currentIndex()
    current_list = lists.currentText()
    Text.delete().where(
        (Text.text == selected) & (Text.list_.name == current_list) ).execute()
    texts.removeItem(idx)


def list_create():
    new_list_name = new_list.text()
    List.create(name=new_list_name)
    lists.addItem(new_list_name)


def on_select_list():
    texts.clear()
    list_name = lists.currentText()
    list_model = List.get(name=list_name)
    print('--------------')
    for txt_model in list_model.texts:
        texts.addItem(txt_model.text)
    print('########')
    # texts.addItems()


lists.currentTextChanged.connect(on_select_list)
add_list_btn.clicked.connect(list_create)
button1.clicked.connect(on_button1_click)
button2.clicked.connect(on_button2_click)
app.exec()
