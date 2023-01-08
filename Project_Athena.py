import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import webbrowser

class App(QWidget):

    def __init__(self):
        # Call the class constructor
        super().__init__()


        # Set the window title, positioning, and size
        self.title = 'Athena'
        self.left = 10
        self.top = 60
        self.width = 640
        self.height = 480

        # Initialize the UI
        self.initUI()

    def initUI(self):
        # Set the window title and size
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create a label for the Google Dork entry field
        label = QLabel('Enter a search query:', self)
        label.move(20, 20)

        # Create a line edit widget for the Google Dork entry
        self.entry = QLineEdit(self)
        self.entry.move(20, 50)

        # Create a label for the file type selection combo box
        label2 = QLabel('Select a file type:', self)
        label2.move(20, 90)

        # Create a combo box for file type selection
        self.combo = QComboBox(self)
        self.combo.addItem("All files")
        self.combo.addItem("pdf")
        self.combo.addItem("xlsx")
        self.combo.addItem("docx")
        self.combo.addItem("log")
        self.combo.addItem("sql")
        self.combo.addItem("html")
        self.combo.addItem("ihtml")
        self.combo.addItem("xml")
        self.combo.addItem("txt")
        self.combo.addItem("php")
        self.combo.addItem("mail")
        self.combo.addItem("mdb")
       
        
        self.combo.move(20, 120)

        # Create a search button and connect it to the on_click button
        button = QPushButton('Search', self)
        button.move(20, 150)
        button.clicked.connect(self.on_click)

        # Show the GUI
        self.show()

    @pyqtSlot()
    def on_click(self):
        # Get the Google Dork and file type from the UI elements
        dork = self.entry.text()
        file_type = self.combo.currentText()

        # Make the Google search URL based on the selected file type
        if file_type == "All files":
            url = "https://www.google.com/search?q=" + dork
        else:
            url = "https://www.google.com/search?q=" + dork + " filetype:" + file_type.lower()

        # Open the search URL in the default web browser
        webbrowser.open(url)

if __name__ == '__main__':
    # Create the application and main window
    app = QApplication(sys.argv)
    ex = App()
    # Run the main application loop
    sys.exit(app.exec_())
