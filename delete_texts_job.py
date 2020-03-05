from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt

from models import Text


def delete_texts(combobox: QComboBox):
    Text.delete().where(Text.text ** 'i%').execute()
    while True:
        idx = combobox.findText('i', Qt.MatchStartsWith)
        if idx == -1:
            return
        combobox.removeItem(idx)
