from nccom.app import NcComGUI
import sys

if __name__ == '__main__':
    app = NcComGUI(sys.argv)
    sys.exit(app.launch())

