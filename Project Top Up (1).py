import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cervo Market")
        self.setGeometry(100, 100, 400, 300)
        
        self.label_id = QLabel("Player ID:", self)
        self.label_id.setGeometry(50, 50, 200, 30)
        
        self.line_edit_id = QLineEdit(self)
        self.line_edit_id.setPlaceholderText("Enter Player ID")
        self.line_edit_id.setGeometry(50, 80, 300, 30)
        
        self.label_game = QLabel("Choose Game:", self)
        self.label_game.setGeometry(50, 120, 200, 30)
        
        self.combo_box_game = QComboBox(self)
        self.combo_box_game.addItems(["Mobile Legends", "Free Fire", "PUBG", "Clash of Clans", "Slam Dunk", "Call of Duty", "FIFA Mobile"])
        self.combo_box_game.setGeometry(50, 150, 300, 30)
        
        self.label_diamond = QLabel("Select Diamond Amount:", self)
        self.label_diamond.setGeometry(50, 190, 200, 30)
        
        self.combo_box_diamond = QComboBox(self)
        self.combo_box_diamond.addItems(["100", "200", "300", "500", "1000"])
        self.combo_box_diamond.setGeometry(50, 220, 300, 30)
        
        self.button = QPushButton("Top Up", self)
        self.button.setGeometry(150, 260, 100, 30)
        self.button.clicked.connect(self.open_dialog)
    
    def open_dialog(self):
        player_id = self.line_edit_id.text()
        if not player_id:
            QMessageBox.warning(self, "Warning", "Please enter a Player ID.")
            return
        
        game = self.combo_box_game.currentText()
        diamond = self.combo_box_diamond.currentText()
        dialog = Dialog(player_id, game, diamond)
        dialog.exec_()
        
        if dialog.result() == QDialog.Accepted:
            thank_you_dialog = ThankYouDialog()
            thank_you_dialog.exec_()

class Dialog(QDialog):
    def __init__(self, player_id, game, diamond):
        super().__init__()
        self.setWindowTitle("Top Up Confirmation")
        self.setGeometry(200, 200, 400, 350)
        
        self.diamond_price = {
            "100": 10000,
            "200": 20000,
            "300": 30000,
            "500": 50000,
            "1000": 100000
        }
        
        self.label_id = QLabel(f"Player ID: {player_id}", self)
        self.label_id.setGeometry(50, 50, 200, 30)
        
        self.label_game = QLabel(f"Game: {game}", self)
        self.label_game.setGeometry(50, 80, 200, 30)
        
        self.label_diamond = QLabel(f"Diamond Amount: {diamond}", self)
        self.label_diamond.setGeometry(50, 110, 200, 30)
        
        self.label_price = QLabel(f"Price: {self.diamond_price[diamond]} IDR", self)
        self.label_price.setGeometry(50, 140, 200, 30)
        
        self.label_payment = QLabel("Payment Method:", self)
        self.label_payment.setGeometry(50, 170, 200, 30)
        
        self.combo_box_payment = QComboBox(self)
        self.combo_box_payment.addItems(["Credit Card", "PayPal", "Bank Transfer", "Mobile Payment"])
        self.combo_box_payment.setGeometry(50, 200, 300, 30)
        
        self.button_yes = QPushButton("Yes", self)
        self.button_yes.setGeometry(50, 240, 100, 30)
        self.button_yes.clicked.connect(self.accept)
        
        self.button_no = QPushButton("No", self)
        self.button_no.setGeometry(180, 240, 100, 30)
        self.button_no.clicked.connect(self.reject)
    
    def accept(self):
        super().accept()

class ThankYouDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thank You")
        self.setGeometry(300, 300, 300, 200)
        
        self.label = QLabel("Thank you for your purchase!", self)
        self.label.setGeometry(50, 50, 200, 30)
        
        self.button_ok = QPushButton("OK", self)
        self.button_ok.setGeometry(100, 100, 100, 30)
        self.button_ok.clicked.connect(self.close)

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cervo Market")
        self.setGeometry(300, 300, 300, 200)
        
        self.label = QLabel("Welcome to Cervo Market", self)
        self.label.setGeometry(50, 50, 200, 30)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    main_window = MainWindow()
    main_window.show()
    
    widget = Widget()
    widget.show()
    
    sys.exit(app.exec_())