from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QColor, QFont
import os
import shutil
extensions = {
    '.py' : 'PyFiles',
    'txt' : 'TextFiles',
    '.png' : 'Png_img_files',
    '.jpeg' : 'Jpeg-img_files',
    '.jpg' : 'Jpg_files',
    '.mp4' : 'Vid_files',
    '.mp3' : 'Aud_files',
    '.rs' : 'Rust_files',
    '.html' : 'Html_files',
    '.css' : 'CSS_Files',
    '.js' : 'JavaScript_Files',
    '.pdf' : "PDFS",
    '.xlsx' : 'Excel files'
}
def ls():
    try:
        path = line_edit.text()
        directories = os.listdir(path)
        label2.setText(f'Files: {str(directories)}')
    except Exception as e:
        label2.setText(str(e))
def sortingFiles(path):
    try:
        directories = os.listdir(path)
        files = []
        #filtering through files and folders to filter out files
        for i in directories:
            psuedoPath = path + f'\{i}'
            if os.path.isfile(psuedoPath):
                files.append(psuedoPath)
        # now the sorting
        if len(files) > 0:
            for j in extensions:
                for i in files:
                    if (j in i) and i != path + f'\main.py':
                        if extensions[j] in directories:
                            shutil.move(i,path + f'\{extensions[j]}')
                        elif extensions[j] not in directories:
                            os.mkdir(path + f'\{extensions[j]}')
                            directories = os.listdir(path)
                            shutil.move(i,path + f'\{extensions[j]}')
                    else:
                        continue
            color = QColor(0, 0, 255)
            # Set the color of the label's text
            label.setStyleSheet("color: %s" % color.name())
            label.setText("Files Successfully Sorted, Path - " + path)
        else:
            color = QColor(255, 0, 0)
            label.setStyleSheet("color: %s" % color.name())
            label.setText("Program exited with an arror, Try again, exit code - 0x0069")
    except Exception as e:
        label.setText(str(e))
def display_text():
    path = line_edit.text()
    sortingFiles(path)
if __name__ == "__main__":
    # Create the application instance
    app = QApplication([])
    # Create the main window
    window = QWidget()
    window.setWindowTitle("SORT-IT")
    # Create widgets
    line_edit = QLineEdit()
    font = QFont("sans serif")
    line_edit.setFont(font)
    line_edit.setTextMargins(5,5,5,5)
    line_edit.setFixedHeight(40)
    line_edit.setPlaceholderText("Enter the path of the file: ")
    button = QPushButton("Sort Files")
    button2 = QPushButton("LS/DIR - (List Files)")
    button2.setFixedHeight(40)
    button.setFixedHeight(40)
    label = QLabel()
    label2 = QLabel()
    button.clicked.connect(display_text)
    button2.clicked.connect(ls)
    layout = QVBoxLayout()
    layout.addWidget(line_edit)
    layout.addWidget(button)
    layout.addWidget(button2)
    layout.addWidget(label)
    layout.addWidget(label2)
    window.setLayout(layout)
    window.setFixedHeight(200)
    window.show()
    app.exec_()
