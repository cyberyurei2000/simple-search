from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
import sys
import search


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        # Window
        self.setWindowTitle("Search Tool")
        #self.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.setFixedSize(640, 480)

        # Menubar
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        file_menu.addAction("Open folder", self.open_directory)
        file_menu.addSeparator()
        file_menu.addAction("Exit", quit)
        help_menu = menu.addMenu("Help")
        help_menu.addAction("About", self.show_about)

        # App Layout
        layout = QtWidgets.QVBoxLayout()

        # Tabs/Layout
        tabs = QtWidgets.QTabWidget()
        layout.addWidget(tabs)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        layout1 = QtWidgets.QVBoxLayout()
        layout2 = QtWidgets.QVBoxLayout()
        layout3 = QtWidgets.QVBoxLayout()
        layout4 = QtWidgets.QVBoxLayout()
        layout5 = QtWidgets.QVBoxLayout()

        self.tab1.setLayout(layout1)
        self.tab1.setDisabled(True)
        self.tab2.setLayout(layout2)
        self.tab2.setDisabled(True)
        self.tab3.setLayout(layout3)
        self.tab3.setDisabled(True)
        self.tab4.setLayout(layout4)
        self.tab4.setDisabled(True)
        self.tab5.setLayout(layout5)
        self.tab5.setDisabled(True)

        tabs.addTab(self.tab1, "Name Search")
        tabs.addTab(self.tab2, "File Extension Search")
        tabs.addTab(self.tab3, "Time && Date Search")
        tabs.addTab(self.tab4, "Size Search")
        tabs.addTab(self.tab5, "String Search")

        # Name Search
        name_flabel = QtWidgets.QLabel("Filename")
        name_text = QtWidgets.QLineEdit()
        name_llabel = QtWidgets.QLabel("Limit")
        name_limit = QtWidgets.QSpinBox()
        name_run = QtWidgets.QPushButton("Run")
        name_limit.setValue(20)
        name_run.clicked.connect(lambda: self.search_run(
            self.directory, name_text.text(), "name", name_limit.text()))
        layout1.addWidget(name_flabel)
        layout1.addWidget(name_text)
        layout1.addWidget(name_llabel)
        layout1.addWidget(name_limit)
        layout1.addWidget(name_run)

        # File Extension Search
        ext_elabel = QtWidgets.QLabel("File Extension")
        ext_text = QtWidgets.QLineEdit()
        ext_llabel = QtWidgets.QLabel("Limit")
        ext_limit = QtWidgets.QSpinBox()
        ext_run = QtWidgets.QPushButton("Run")
        ext_limit.setValue(20)
        ext_run.clicked.connect(lambda: self.search_run(
            self.directory, ext_text.text(), "ext", ext_limit.text()))
        layout2.addWidget(ext_elabel)
        layout2.addWidget(ext_text)
        layout2.addWidget(ext_llabel)
        layout2.addWidget(ext_limit)
        layout2.addWidget(ext_run)

        # Date & Time Search
        dt_dlabel = QtWidgets.QLabel("Date")
        dt_date = QtWidgets.QDateEdit()
        dt_tlabel = QtWidgets.QLabel("Time")
        dt_time = QtWidgets.QTimeEdit()
        dt_llabel = QtWidgets.QLabel("Limit")
        dt_limit = QtWidgets.QSpinBox()
        dt_run = QtWidgets.QPushButton("Run")
        dt_limit.setValue(20)
        dt_run.clicked.connect(lambda: self.search_run(
            self.directory, f"{dt_date.text()} {dt_time.text()}", "date", dt_limit.text()))
        layout3.addWidget(dt_dlabel)
        layout3.addWidget(dt_date)
        layout3.addWidget(dt_tlabel)
        layout3.addWidget(dt_time)
        layout3.addWidget(dt_llabel)
        layout3.addWidget(dt_limit)
        layout3.addWidget(dt_run)

        # Size Search
        size_slabel = QtWidgets.QLabel("Size (bytes)")
        size_sz = QtWidgets.QSpinBox()
        size_llabel = QtWidgets.QLabel("Limit")
        size_limit = QtWidgets.QSpinBox()
        size_run = QtWidgets.QPushButton("Run")
        size_limit.setValue(20)
        size_run.clicked.connect(lambda: self.search_run(
            self.directory, size_sz.text(), "size", size_limit.text()))
        layout4.addWidget(size_slabel)
        layout4.addWidget(size_sz)
        layout4.addWidget(size_llabel)
        layout4.addWidget(size_limit)
        layout4.addWidget(size_run)

        # String Search
        str_slabel = QtWidgets.QLabel("String")
        str_text = QtWidgets.QLineEdit()
        str_llabel = QtWidgets.QLabel("Limit")
        str_limit = QtWidgets.QSpinBox()
        str_run = QtWidgets.QPushButton("Run")
        str_limit.setValue(20)
        str_run.clicked.connect(lambda: self.search_run(
            self.directory, str_text.text(), "str", str_limit.text()))
        layout5.addWidget(str_slabel)
        layout5.addWidget(str_text)
        layout5.addWidget(str_llabel)
        layout5.addWidget(str_limit)
        layout5.addWidget(str_run)

        # Console
        con_label = QtWidgets.QLabel("Console")
        layout.addWidget(con_label)

        #self.console = QtWidgets.QPlainTextEdit()
        #self.console.setReadOnly(True)
        #layout.addWidget(self.console)
        self.console = QtWidgets.QListWidget()
        layout.addWidget(self.console)

        # App Widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Statusbar
        statusbar = QtWidgets.QStatusBar(self)
        statusbar.setStyleSheet('QStatusBar::item {border: None;}')
        self.status_label = QtWidgets.QLabel("Open a directory to start")
        statusbar.addWidget(self.status_label)
        self.setStatusBar(statusbar)

    def open_directory(self) -> None:
        self.console.clear()
        self.directory = f"{QtWidgets.QFileDialog.getExistingDirectory()}/"
        self.status_label.setText(self.directory)

        self.tab1.setDisabled(False)
        self.tab2.setDisabled(False)
        self.tab3.setDisabled(False)
        self.tab4.setDisabled(False)
        self.tab5.setDisabled(False)

    def search_run(self, path: str, user: str, type: str, limit: str) -> None:
        self.console.clear()
        if user:
            search.run(path, user, type, limit)
            #self.console.setPlainText(search.get_results())
            self.console.addItems(search.get_results())

    def show_about(self) -> None:
        text = ("Search Tool\n" + "Developed by cyberyurei2000")

        about = QMessageBox(self)
        about.setWindowTitle("About")
        about.setText(text)
        about.exec()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
