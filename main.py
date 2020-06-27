import datetime
import hashlib

import requests

from PyQt5 import QtWidgets, QtCore
# from PyQt5.QtGui import QPixmap

from ui.main_window import Ui_MainWindow


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main window

    Args:
        QtWidgets ([type]): [description]
        Ui_MainWindow ([type]): user interface for main window
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.url = 'http://35.228.157.42'
        self.chanel = 'hub'
        self.login = ''
        self.password = ''
        self.channelEdit.setText('hub')
        self.sendButton.pressed.connect(self.send_message)
        self.sendButton.setShortcut('Ctrl+Return')
        self.enterButton.pressed.connect(self.checkEnter)
        self.channelButton.pressed.connect(self.changeChanel)
        self.last_timestamp = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)

    def checkEnter(self):
        """Performs user authentication
        """
        self.login = self.usernameInput.text()
        temp = hashlib.sha384()
        temp.update(self.passwordInput.text().encode('utf-8'))
        self.password = temp.hexdigest()
        self.enterButton.close()
        self.splashScreen.close()
        self.usernameInput.close()
        self.passwordInput.close()

    def changeChanel(self):
        """Responsible for changing the "channel", or connecting to the default channel
        """
        self.chanel = self.channelEdit.text()
        self.textBrowser.clear()
        if self.channelEdit.text() == '':
            self.chanel = 'hub'
            self.channelEdit.setText('hub')
        response = requests.get(self.url + '/get_messages',
                                params={'after': self.last_timestamp}
                                )
        messages = response.json()['messages']

        for message in messages:
            dt = datetime.datetime.fromtimestamp(message['timestamp'])
            dt = dt.strftime('%H:%M:%S %d/%m/%Y')
            self.textBrowser.append('<div class="container"><h3>' +
                                    '@hub: ' +
                                    message['username'] +
                                    '</h3><p>' +
                                    message['text'] +
                                    '</p><span class="date-right">' +
                                    dt + '</span></div>')
            self.textBrowser.append('\n')
            self.last_timestamp = message['timestamp']

    def send_message(self):
        """Sending a user message to the server
        """
        # username = self.lineEdit.text()
        # temp = hashlib.sha384()
        # temp.update(self.lineEdit_2.text().encode('utf-8'))
        # password = temp.hexdigest()
        username = self.login
        password = self.password
        text = self.textEdit.toPlainText()
        chanel = self.chanel
        if text == '':
            return
        if chanel == '':
            chanel = 'hub'
        # pass
        # message
        requests.get(self.url+'/send_message',
                     json={
                        'username': username,
                        'password': password,
                        'text': text,
                        'chanel': chanel,
                        }
                     )
        self.textEdit.setText('')

    def update_messages(self):
        """Receiving information from the server about connected users and
        their chat messages
        """
        response = requests.get(self.url + '/get_messages',
                                json={
                                    'after': self.last_timestamp,
                                    'chanel': self.chanel
                                    }
                                )
        messages = response.json()['messages']

        for message in messages:
            dt = datetime.datetime.fromtimestamp(message['timestamp'])
            dt = dt.strftime('%H:%M:%S %d/%m/%Y')
            self.textBrowser.append('<div class="container"<h3>' +
                                    '@hub: ' +
                                    message['username'] +
                                    '</h3><p>'+message['text'] +
                                    '</p><span class="date-right">' +
                                    dt + '</span></div>')
            self.textBrowser.append('\n')
            self.last_timestamp = message['timestamp']


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ExampleApp()
    window.setFixedSize(480, 779)
    window.show()
    app.exec()
