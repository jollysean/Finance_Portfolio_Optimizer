import wx
import resources.finance as fin
from src.app.MainFrame import *
from resources import *


portfolio = fin.Portfolio()

class PortfolioOptimizer(wx.App):
    def OnInit(self):
        self.m_frame = MainFrame(None, portfolio)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)
        return True
    
if __name__ == '__main__':
    app = PortfolioOptimizer(0)
    app.MainLoop()