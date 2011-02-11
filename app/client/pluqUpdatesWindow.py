#!/usr/bin/python

# Author  : Samarth (samarth@blinq.in)
# Date    : 22nd Jan 2011
# Purpose : To display the GUI window for preference section in pluq.it icon
# Comments: This module should be imported in the main icon module which will eventually launch the Preference/setting menu

#!/usr/bin/python



import wx

class Toolbars(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300, 200))

	toolbar = self.CreateToolBar()
   	toolbar.AddSimpleTool(wx.NewId(), wx.Image('1.png',
       				wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'New', 'Long help for New')
   	toolbar.AddSimpleTool(wx.NewId(), wx.Image('2.png',
       				wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Open', 'Long help for Open')
   	toolbar.AddSimpleTool(wx.NewId(), wx.Image('3.png',
       				wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Save', 'Long help for Save')
   	toolbar.Realize()
        

    def OnExit(self, event):
        self.Close()


app = wx.App()
Toolbars(None, -1, 'toolbars')
app.MainLoop()

