import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtCore import *
import numpy as np
import skimage.transform


def gen_random_block_image():
    size=(300,400)
    blocks = np.random.randint(0, 2, (3, 4))
    return skimage.util.img_as_ubyte(skimage.transform.resize(blocks, size, order=0, preserve_range=True))


def numpy_to_qimage(arr):
    return QImage(arr.data, arr.shape[1], arr.shape[0], arr.strides[0], QImage.Format_Indexed8)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.refresh_image()
        # self.setGeometry(400, 100, 840, 850)
        self.initUI()
        self.show()

    def initUI(self):
        self.main_layout = QVBoxLayout(self)

        self.img_label = QLabel(self)
        self.draw_image()

        self.refresh_button = QPushButton('Refresh', self)
        self.refresh_button.clicked.connect(self.refresh_and_draw_image)

        self.main_layout.addWidget(self.img_label)
        self.main_layout.addWidget(self.refresh_button)

        self.setLayout(self.main_layout)

    def refresh_image(self):
        self._npimage = gen_random_block_image()
        self._qimage = numpy_to_qimage(self._npimage)
        self._pixmap = QPixmap.fromImage(self._qimage)

    def draw_image(self):
        self.img_label.setPixmap(self._pixmap)

    def refresh_and_draw_image(self):
        self.refresh_image()
        self.draw_image()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())