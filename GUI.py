import sys
import os
from PyQt5 import QtWidgets, uic
from examples.tunneling import *

"""
Template for GUI
"""

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Represents the main-window of the gui.
        It loads the ui-file.
        """
        super().__init__()
        uic.loadUi(
            os.path.dirname(__file__)+"//widget.ui",
            self,
        )

        self.runButton.pressed.connect(self.run_circuit)
        self.show()
    
    def run_circuit(self):
        """Run the quantum circuit, based on the API key."""

        api_key = str(self.apiKey.text())  # if it's a value box, .value() instead...
        v = rd.random()  # choose a random velocity
        counts = tunneling_circuit(velocity=v, used_backend='qasm_simulator')
        print(counts)

        return counts
    
if __name__ == '__main__':
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)
    
    main_window = MainWindow()
    qapp.exec()