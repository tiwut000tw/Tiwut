import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

class CustomWebEnginePage(QWebEnginePage):
    def createWindow(self, _type):
        return self

class TiwutApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tiwut")

        self.browser = QWebEngineView()
        
        custom_page = CustomWebEnginePage(self)
        self.browser.setPage(custom_page)
        
        self.browser.setUrl(QUrl("https://tiwut.de/"))

        self.setCentralWidget(self.browser)
        
        self.resize(1280, 800)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TiwutApp()
    window.show()
    sys.exit(app.exec())