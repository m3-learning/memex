import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class DragDropExample(QWidget):
    def __init__(self):
        super(DragDropExample, self).__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Drag and drop a file here.")
        layout.addWidget(self.label)
        
        self.setLayout(layout)
        
        self.setWindowTitle('Drag and Drop Example')
        self.setAcceptDrops(True)
        self.show()
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            self.label.setText(f"File path: {path}")
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DragDropExample()
    sys.exit(app.exec_())
