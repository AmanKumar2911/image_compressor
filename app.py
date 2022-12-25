import sys
from PyQt5.QtWidgets import QApplication,QFileDialog, QWidget,QMainWindow,QFrame,QLabel,QLineEdit,QPushButton,QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Image Compressor'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 600
        self.setFixedSize(self.width,self.height)
        self.setObjectName("main_window")
        stylesheet=""
        with open("design.qss",'r') as f:
            stylesheet=f.read()
        self.setStyleSheet(stylesheet)
        self.initUI()
        

        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #main window start---------
        self.single_bubble =QFrame(self)
        self.single_bubble.setObjectName("bubble")
        self.single_bubble.move(50,100)
        self.single_bubble.mousePressEvent = self.single_bubble_clicked

        self.single_bubble_heading=QLabel(self.single_bubble)
        self.single_bubble_heading.setObjectName("bubble_heading")
        self.single_bubble_heading.setText("compress Image")
        self.single_bubble_heading.move(90, 8)

        self.single_bubble_para=QLabel(self.single_bubble)
        self.single_bubble_para.setObjectName("bubble_para")
        self.single_bubble_para.setText("click here to compress single image")
        self.single_bubble_para.move(25, 32)


        self.dir_bubble =QFrame(self)
        self.dir_bubble.setObjectName("bubble")
        self.dir_bubble.move(50,300)
        self.dir_bubble.mousePressEvent=self.dir_bubble_clicked

        self.dir_bubble_heading=QLabel(self.dir_bubble)
        self.dir_bubble_heading.setObjectName("bubble_heading")
        self.dir_bubble_heading.setText("compress Multiple Images")
        self.dir_bubble_heading.move(55, 8)

        self.dir_bubble_para=QLabel(self.dir_bubble)
        self.dir_bubble_para.setObjectName("bubble_para")
        self.dir_bubble_para.setText("want to compress multiple images at once? select the folder and get compressed version of the images in another folder.")
        self.dir_bubble_para.setWordWrap(True)
        self.dir_bubble_para.move(10, 32)
        

        #------------------------single bubble expanded-------------------



        self.single_bubble_expanded =QFrame(self)
        self.single_bubble_expanded.setObjectName("bubble_expanded")
        self.single_bubble_expanded.move(50,100)
        self.single_bubble_expanded.setVisible(False)
        
        self.back_arrow_s = QLabel(self.single_bubble_expanded)
        self.back_arrow_s.move(25, 0)
        self.back_arrow_s.setObjectName("back_arrow")
        self.back_arrow_s.setTextFormat(Qt.RichText)
        self.back_arrow_s.setText("&#8592;")
        self.back_arrow_s.mouseDoubleClickEvent=self.back_arrow_clicked

        self.single_bubble_heading=QLabel(self.single_bubble_expanded)
        self.single_bubble_heading.setObjectName("bubble_heading")
        self.single_bubble_heading.setText("compress Image")
        self.single_bubble_heading.move(90, 8)

        self.select_image_lable=QLabel(self.single_bubble_expanded)
        self.select_image_lable.setObjectName("bubble_para")
        self.select_image_lable.setText("choose Image")
        self.select_image_lable.move(30, 50)

        self.image_path = QLineEdit(self.single_bubble_expanded)
        self.image_path.setObjectName("path_text")
        self.image_path.move(60, 85)

        self.browse_button=QPushButton(self.single_bubble_expanded)
        self.browse_button.setText("...")
        self.browse_button.setObjectName("browse_button")
        self.browse_button.clicked.connect(self.select_file)
        self.browse_button.move(240,85)

        self.select_image_quality=QLabel(self.single_bubble_expanded)
        self.select_image_quality.setObjectName("bubble_para")
        self.select_image_quality.setText("choose Quality")
        self.select_image_quality.move(30, 130)

        self.quality_path = QLineEdit(self.single_bubble_expanded)
        self.quality_path.setObjectName("quality_path_text")
        self.quality_path.move(60, 160)

        self.quality_combo = QComboBox(self.single_bubble_expanded)
        self.quality_combo.addItem("High")
        self.quality_combo.addItem("Medium")
        self.quality_combo.addItem("Low")
        self.quality_combo.move(170,160)
        self.quality_combo.setObjectName("quality_combo")
        self.quality_combo.resize(96,26)

        
        self.compress_image=QPushButton(self.single_bubble_expanded)
        self.compress_image.setText("compress")
        self.compress_image.setObjectName("compress_button")
        self.compress_image.move(100,260)


        #-----------------------end single bubble expanded---------------------

        #--------------------------dir bubble expanded----------------------

        self.dir_bubble_expanded =QFrame(self)
        self.dir_bubble_expanded.setObjectName("bubble_expanded")
        self.dir_bubble_expanded.move(50,100)
        self.dir_bubble_expanded.setVisible(False)

        self.back_arrow_d = QLabel(self.dir_bubble_expanded)
        self.back_arrow_d.move(25, 0)
        self.back_arrow_d.setObjectName("back_arrow")
        self.back_arrow_d.setTextFormat(Qt.RichText)
        self.back_arrow_d.setText("&#8592;")
        self.back_arrow_d.mouseDoubleClickEvent=self.back_arrow_clicked

        self.dir_bubble_heading=QLabel(self.dir_bubble_expanded)
        self.dir_bubble_heading.setObjectName("bubble_heading")
        self.dir_bubble_heading.setText("compress Multiple Images")
        self.dir_bubble_heading.move(70, 8)

        self.select_source_lable=QLabel(self.dir_bubble_expanded)
        self.select_source_lable.setObjectName("bubble_para")
        self.select_source_lable.setText("choose source direcrory")
        self.select_source_lable.move(30, 50)

        self.source_path = QLineEdit(self.dir_bubble_expanded)
        self.source_path.setObjectName("path_text")
        self.source_path.move(60, 85)

        self.browse_source_button=QPushButton(self.dir_bubble_expanded)
        self.browse_source_button.setText("...")
        self.browse_source_button.setObjectName("browse_button")
        self.browse_source_button.move(240,85)

        self.select_dest_lable=QLabel(self.dir_bubble_expanded)
        self.select_dest_lable.setObjectName("bubble_para")
        self.select_dest_lable.setText("choose destination direcrory")
        self.select_dest_lable.move(30, 130)

        self.dest_path = QLineEdit(self.dir_bubble_expanded)
        self.dest_path.setObjectName("path_text")
        self.dest_path.move(60, 160)

        self.browse_dest_button=QPushButton(self.dir_bubble_expanded)
        self.browse_dest_button.setText("...")
        self.browse_dest_button.setObjectName("browse_button")
        self.browse_dest_button.move(240,160)

        self.select_dir_quality=QLabel(self.dir_bubble_expanded)
        self.select_dir_quality.setObjectName("bubble_para")
        self.select_dir_quality.setText("choose Quality")
        self.select_dir_quality.move(30, 205)

        self.quality_dir_path = QLineEdit(self.dir_bubble_expanded)
        self.quality_dir_path.setObjectName("quality_path_text")
        self.quality_dir_path.move(60, 235)

        self.quality_dir_combo = QComboBox(self.dir_bubble_expanded)
        self.quality_dir_combo.addItem("High")
        self.quality_dir_combo.addItem("Medium")
        self.quality_dir_combo.addItem("Low")
        self.quality_dir_combo.move(170,235)
        self.quality_dir_combo.setObjectName("quality_combo")
        self.quality_dir_combo.resize(96,26)

        self.compress_dir=QPushButton(self.dir_bubble_expanded)
        self.compress_dir.setText("compress")
        self.compress_dir.setObjectName("compress_button")
        self.compress_dir.move(100,290)
        

        #---------------------------end dir bubble expanded----------------------

        #--------------------------main window end

        self.show()

    #------------------------functions----------------------

    def select_file(self):
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);JPG,PNG (*.jpg *.png)")
        if fileName:
            print(fileName)
            self.image_path.setText(fileName)

    def back_arrow_clicked(self,  event):
        self.single_bubble.setVisible(True)
        self.dir_bubble.setVisible(True)
        self.single_bubble_expanded.setVisible(False)
        self.dir_bubble_expanded.setVisible(False)

    def single_bubble_clicked(self,event):
        print("single bubble clicked")
        self.single_bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        self.single_bubble_expanded.setVisible(True)
        self.dir_bubble_expanded.setVisible(False)
        
    def dir_bubble_clicked(self,event):
        print("dir bubble clicked")
        self.single_bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        self.single_bubble_expanded.setVisible(False)
        self.dir_bubble_expanded.setVisible(True)
        

        
          
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())