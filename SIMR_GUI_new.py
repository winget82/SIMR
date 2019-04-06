import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class SIMR(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.program()
        
    def program(self):

        # File Menu Options
        newProject = QAction('&New Project', self)
        newProject.setStatusTip('Start a new project')
        #saveApp.triggered.connect()

        saveProject = QAction('&Save Project', self)        
        saveProject.setStatusTip('Save your current project')
        #saveApp.triggered.connect()

        closeApp = QAction(QIcon('exit.png'), '&Exit', self)        
        closeApp.setStatusTip('Close and exit SIMR')
        closeApp.triggered.connect(qApp.quit)

        # Edit Menu Options
        undoAction = QAction('&Undo', self)
        undoAction.setStatusTip('Undo your last action')

        redoAction = QAction('&Redo', self)
        redoAction.setStatusTip('Redo your last action')

        # Read Menu Options
        readKJV = QAction('&King James Version', self)
        readKJV.setStatusTip('Read from the King James Version')

        readKJVwStrongs = QAction("&KJV w/ Strong's", self)
        readKJVwStrongs.setStatusTip("Read from the KJV with Strong's numbers")

        readSept = QAction('&Septuagint', self)
        readSept.setStatusTip('Read from the Septuagint')

        readBerean = QAction('&Berean', self)
        readBerean.setStatusTip('Read from the Berean Bible')

        # Books Menu Options
        numberInScripture = QAction('&Number In Scripture', self)
        numberInScripture.setStatusTip('Read from "Number in Scripture" by E. W. Bullinger')

        howToEnjoyTheBible = QAction('&How To Enjoy The Bible', self)
        howToEnjoyTheBible.setStatusTip('Read from "How to Enjoy the Bible" by E. W. Bullinger')

        witnessOfTheStars = QAction('&Witness Of The Stars', self)
        witnessOfTheStars.setStatusTip('Read from "Witness of the Stars" by E. W. Bullinger')

        # TWI Menu Options
        scriptureIndex = QAction('&Scripture Index', self)
        scriptureIndex.setStatusTip('Get scripture index for The Way International resources')

        # Mapping Menu Options
        drawMap = QAction('Draw Map', self)
        drawMap.setStatusTip('Draw Bible map')

        # Help Menu Options
        about = QAction('About', self)
        about.setStatusTip('See information about this application')

        self.statusBar()

        menubar = self.menuBar()

        # File Menu
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newProject)
        fileMenu.addAction(saveProject)
        fileMenu.addAction(closeApp)
        
        # Edit Menu
        editMenu = menubar.addMenu('&Edit')
        editMenu.addAction(undoAction)
        editMenu.addAction(redoAction)

        # Read Menu
        readMenu = menubar.addMenu('&Read')
        readMenu.addAction(readKJV)
        readMenu.addAction(readKJVwStrongs)
        readMenu.addAction(readSept)
        readMenu.addAction(readBerean)

        # Books Menu
        booksMenu = menubar.addMenu('&Books')
        booksMenu.addAction(numberInScripture)
        booksMenu.addAction(howToEnjoyTheBible)
        booksMenu.addAction(witnessOfTheStars)

        # TWI Menu
        twiMenu = menubar.addMenu('&TWI')
        twiMenu.addAction(scriptureIndex)

        # Mapping Menu
        mappingMenu = menubar.addMenu('&Mapping')
        mappingMenu.addAction(drawMap)

        # Help Menu
        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(about)
        

        self.setGeometry(600, 600, 600, 400)
        self.setWindowTitle('SIMR - Scripture Indices and Ministry Resources')    
        self.show()
    
    def buttonClick(self):
        alert = QMessageBox()
        alert.setText('Button has been clicked')
        alert.exec_()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    simr = SIMR()
    sys.exit(app.exec_())