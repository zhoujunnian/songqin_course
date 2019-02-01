import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title, pos=wx.DefaultPosition,
                size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):

        wx.Frame.__init__(self, parent, ID, title, pos, size, style)
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        # panel = wx.Panel(self, -1)
        # button = wx.Button(self, 1003, "Close Me")
        # button.SetPosition((15, 15))
        # self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)



app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = MyFrame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
frame.Show(True)     # Show the frame.
app.MainLoop()


