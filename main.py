from PyQt6.QtWidgets import *
from PyQt6 import uic

from PyQt6.QtGui import QPixmap, QIcon
#from PyQt6.QtCore import QSize
from popups import CustomPopups
from dialogs import CustomDialogs

from flags import selectFlag
from generateFlags import generateFlags

app = QApplication([])

class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.flagScaleFactor = 0.67

        self.window = uic.loadUi(r"mainwindow.ui")
        self.window.setWindowTitle("Flag Guesser")
        self.window.setWindowIcon(QIcon(r"icons\flag-solid-full.svg"))

        self.flagList = generateFlags()
    
        # MAKES A LIST OF COUNTRIES. FOR PRODUCING HINTS BY INPUTTING INTO ChatGPT
        print(len(self.flagList))
        for i in self.flagList:
            print(i.country)
        exit()

        self.window.submitGuess.released.connect(self.submitGuessFunction)
        self.window.hintButton.released.connect(self.showHint)

        self.selectionIndex = 0
        self.prevIndex = 0
        
        self.selectedFlag = self.buildFlag()
        self.correctAnswers = 0
        self.numQuestions = len(self.flagList)-1
         
    def buildFlag(self):

        self.checkComplete()
        
        while (self.prevIndex == self.selectionIndex):
            selectedFlag, self.selectionIndex = selectFlag(self.flagList)
        
        self.prevIndex = self.selectionIndex
        del self.flagList[self.selectionIndex]

        pixmap = QPixmap(selectedFlag.path)
        pixmap = pixmap.scaled(int(pixmap.width()*self.flagScaleFactor), int(pixmap.height()*self.flagScaleFactor))
        self.window.FLAG.setMinimumSize(int(pixmap.width()*self.flagScaleFactor), int(pixmap.height()*self.flagScaleFactor))
        self.window.FLAG.setPixmap(pixmap)

        #print(len(self.flagList))
        return selectedFlag

    def submitGuessFunction(self):

        inputBox = self.window.inputBox
        guess = inputBox.text()
        guess = guess.lower()
        guess = guess.strip()
        guess = guess.removeprefix("the")
        guess = guess.strip()
        inputBox.setText("")

        if (guess==self.selectedFlag.country.lower().strip().removeprefix("the").strip()):
            answerPopup = CustomPopups(parent=self,message=f"You guessed that the flag was: {guess.title()}\nYou are correct!")
            answerPopup.exec()
            self.correctAnswers += 1
        else:
            answerPopup = CustomPopups(parent=self,message=f"You guessed that the flag was: {guess.title()}.\nYou are wrong. The flag was of {self.selectedFlag.country}.")
            answerPopup.exec()
            

        self.selectedFlag = self.buildFlag()

    def showHint(self):
        hint = CustomPopups(message=self.selectedFlag.hint, parent=self)
        hint.exec()

    def checkComplete(self):

        if(len(self.flagList) == 1):
            endDialog = CustomDialogs(message=f"Quiz complete\n Your score is {self.correctAnswers} out of {self.numQuestions} questions.\n{self.correctAnswers/self.numQuestions*100}%\n Close trainer?", title="Quiz complete", parent= self)
            if endDialog.exec():
                app.closeAllWindows()
                exit()
            else:
                self.flagList = generateFlags()
                self.selectionIndex = 0
                self.prevIndex = 0
        
                self.selectedFlag = self.buildFlag()
                self.correctAnswers = 0
                self.numQuestions = len(self.flagList)

w = mainWindow()
w.window.show()
app.exec()
