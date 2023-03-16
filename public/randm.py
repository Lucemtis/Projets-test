import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog
from PyQt5.QtCore import Qt

class RandomWordGenerator(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Lecture de fichier texte')
        
        # Ajout du bouton pour choisir un fichier
        self.button = QPushButton('Choisir un fichier', self)
        self.button.clicked.connect(self.chooseFile)
        self.button.setGeometry(50, 50, 200, 30)

    def chooseFile(self):

        # Ouvre la boîte de dialogue pour choisir un fichier texte
        fileDialog = QFileDialog()
        fileDialog.setNameFilter('Fichier texte (*.txt)')
        fileName = fileDialog.getOpenFileName(self, 'Choisir un fichier', '', 'Fichier texte (*.txt)')[0]

        # Ouvrir le fichier texte contenant la banque de mots
        with open(fileName) as f:
            self.words = f.readlines()

        # Supprimer les caractères de nouvelle ligne ("\n") de chaque mot
        self.words = [word.strip() for word in self.words]

        # Créer le bouton pour lancer le randomiseur
        self.button = QPushButton("Générer un mot aléatoire", self)
        self.button.clicked.connect(self.generate_random_word)

        # Créer l'étiquette pour afficher le mot aléatoire
        self.label = QLabel("", self)
        self.label.setAlignment(Qt.AlignCenter)

        # Créer le layout vertical pour la fenêtre
        layout = QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Définir les styles QSS pour la fenêtre et le bouton
        self.setStyleSheet("""
            QWidget {
                background-color: #1a1a1a;
                font-size: 24px;
                color: white;
            }
            QPushButton {
                background-color: #2c2c2c;
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 24px;
                margin: 4px 2px;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: #4f4f4f;
            }
            """)

    def generate_random_word(self):
        # Générer un mot aléatoire à partir de la liste de mots
        random_word = random.choice(self.words)

        # Afficher le mot aléatoire dans l'étiquette
        self.label.setText(random_word)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = RandomWordGenerator()
    generator.show()
    sys.exit(app.exec_())
