from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

class TableModel(QAbstractTableModel):
    def __init__(self, data) -> None:
        super().__init__()
        self._data_list_dict = [row for row in data]
        self._data = [list(row.values()) for row in self._data_list_dict]
        self._headers = list(self._data_list_dict[0].keys())

    def columnCount(self, parent=QModelIndex()):
        return len(max(self._data, key=len))
    
    def rowCount(self, parent=QModelIndex()):
        return len(self._data)
    
    def headerData(self, section, orientation, role):
        if (role == Qt.DisplayRole and orientation == Qt.Horizontal):
            return self._headers[section].upper()
        if (role == Qt.DisplayRole and orientation == Qt.Vertical):
            return section
         
    
    def data(self, index, role=Qt.DisplayRole):
            if role == Qt.DisplayRole:
                return  self._data[index.row()][index.column()]