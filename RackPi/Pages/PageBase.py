from Utilities.Drawer import Drawer

class PageBase:
    drawer: Drawer = None
    config = None
    nextUpdate = 0

    def __init__(self, drawer: Drawer, config):
        self.drawer = drawer
        self.config = config

    def EnterPage(self):
        self.nextUpdate = 0

    def LeavePage(self):
        pass

    def CanUpdate(self, timer):
        if self.nextUpdate > 0:
            self.nextUpdate -= 1
            return False
        else:
            self.nextUpdate = timer
            return True

    def UpdateCanvas(self):
        self.drawer.ClearCanvas()
        self.drawer.WriteOnCanvas("    -NOT SET-", line=1)

    def OnLongPress(self):
        self.nextUpdate = 0