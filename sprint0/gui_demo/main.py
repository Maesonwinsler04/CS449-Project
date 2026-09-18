"""Simple PyQt6 GUI demo for CS 449 Sprint 0.

Displays a window containing text, lines, a check box, and radio buttons.
The GUI is not functional; it demonstrates basic PyQt6 widgets and layout.
"""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QCheckBox,
    QRadioButton,
    QVBoxLayout,
    QFrame,
)


class SolitaireWindow(QWidget):
    """Main window for the solitaire game demo."""

    def __init__(self):
        """Build the window and its layout."""
        super().__init__()
        self.setWindowTitle("Peg Solitaire - CS 449 Sprint 0 Demo")
        self.resize(400, 300) #size of the window

        # a layout stacks everything from top to bottom
        main_layout = QVBoxLayout()

        #the text
        main_layout.addWidget(QLabel("Welcome to Peg Solitaire!"))

        #A line
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        main_layout.addWidget(line)


        #more text
        main_layout.addWidget(QLabel("Select your options below:"))

        #radio buttons for game mode
        self.english_mode_radio = QRadioButton("English Mode")
        self.hexagonal_mode_radio = QRadioButton("Hexagonal Mode")
        self.diamond_mode_radio = QRadioButton("Diamond Mode")
        self.english_mode_radio.setChecked(True)  # default selection

        main_layout.addWidget(self.english_mode_radio)
        main_layout.addWidget(self.hexagonal_mode_radio)
        main_layout.addWidget(self.diamond_mode_radio)

        #another line 
        line2 = QFrame()
        line2.setFrameShape(QFrame.Shape.HLine)
        main_layout.addWidget(line2)

        #A checkbox for recording game
        self.record_game_checkbox = QCheckBox("Record Game")
        main_layout.addWidget(self.record_game_checkbox)

        #attach the layout to the window
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SolitaireWindow()
    window.show()
    sys.exit(app.exec())