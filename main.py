from logic import *


def main():
    """Opens the program """
    application = QApplication([])
    window = logic()
    window.show()
    application.exec()


if __name__ == "__main__":
    main()
