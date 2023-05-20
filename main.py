import sys
from UIWidget import *

app = QtWidgets.QApplication(sys.argv)
window = UIWidget()
window.show()
sys.exit(app.exec())