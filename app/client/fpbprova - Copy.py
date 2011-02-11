import  wx
import wx.lib.agw.foldpanelbar as fpb
import wx.lib.scrolledpanel as scrolled

class Extended(wx.Frame):
    
    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition,
                 size=(700,650), style=wx.DEFAULT_FRAME_STYLE):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        splitter = wx.SplitterWindow(self, -1, style=wx.CLIP_CHILDREN |
                                     wx.SP_LIVE_UPDATE | wx.SP_3D)

        self._leftWindow1 = scrolled.ScrolledPanel(splitter, -1)

        # ALWAYS USE SIZERS!!!
        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)

        self.remainingSpace = wx.Panel(splitter, -1, style=wx.SUNKEN_BORDER)

        wx.StaticText(self.remainingSpace, -1,
                      "Use your imagination for what kinds of things to put in this window...",
                      (15,30))

        # USE SIZERS!!
        self._leftWindow1.SetSizer(self.mainsizer)

        self.ReCreateFoldPanel(0)

        self._leftWindow1.SetVirtualSize((220, 1000))
        # SETUP THE SCROLLEDPANEL        
        self._leftWindow1.SetupScrolling()
        self._pnl.SetMinSize((200, -1))
        splitter.SplitVertically(self._leftWindow1, self.remainingSpace, 200)


    def ReCreateFoldPanel(self, fpb_flags):

        # delete earlier panel
        self._leftWindow1.DestroyChildren()

        # recreate the foldpanelbar
        self._pnl = fpb.FoldPanelBar(self._leftWindow1, -1, wx.DefaultPosition,
                                     wx.Size(-1,-1), fpb_flags)

        item = self._pnl.AddFoldPanel("Caption Colours", collapsed=False)

        self._pnl.AddFoldPanelWindow(item, wx.StaticText(item, -1, "Adjust The First Colour"),
                                     fpb.FPB_ALIGN_WIDTH, 5, 20) 

        # RED color spin control
        self._rslider1 = wx.Slider(item, -1, 0, 0, 255)
        self._pnl.AddFoldPanelWindow(item, self._rslider1, fpb.FPB_ALIGN_WIDTH, 2, 20) 

        # GREEN color spin control
        self._gslider1 = wx.Slider(item, -1, 0, 0, 255)
        self._pnl.AddFoldPanelWindow(item, self._gslider1, fpb.FPB_ALIGN_WIDTH, 0, 20) 

        # BLUE color spin control
        self._bslider1 = wx.Slider(item, -1, 0, 0, 255)
        self._pnl.AddFoldPanelWindow(item, self._bslider1, fpb.FPB_ALIGN_WIDTH,  0, 20) 
        
        self._pnl.AddFoldPanelSeparator(item)

        self._pnl.AddFoldPanelWindow(item, wx.StaticText(item, -1, "Adjust The Second Colour"),
                                     fpb.FPB_ALIGN_WIDTH, 5, 20) 

        # RED color spin control
        self._rslider2 = wx.Slider(item, -1, 0, 0, 255)
        self._pnl.AddFoldPanelWindow(item, self._rslider2, fpb.FPB_ALIGN_WIDTH, 2, 20) 

        # GREEN color spin control
        self._gslider2 = wx.Slider(item, -1, 0, 0, 255)
        self._pnl.AddFoldPanelWindow(item, self._gslider2, fpb.FPB_ALIGN_WIDTH, 0, 20) 

        # BLUE color spin control
        self._bslider2 = wx.Slider(item, -1, 0, 0, 255)
        self._pnl.AddFoldPanelWindow(item, self._bslider2, fpb.FPB_ALIGN_WIDTH, 0, 20) 

        self._pnl.AddFoldPanelSeparator(item)
        
        button1 = wx.Button(item, wx.ID_ANY, "Apply To All")
        self._pnl.AddFoldPanelWindow(item, button1)

        # read back current gradients and set the sliders
        # for the colour which is now taken as default

        style = self._pnl.GetCaptionStyle(item)
        col = style.GetFirstColour()

        self._rslider1.SetValue(col.Red())
        self._gslider1.SetValue(col.Green())
        self._bslider1.SetValue(col.Blue())

        col = style.GetSecondColour()
        self._rslider2.SetValue(col.Red())
        self._gslider2.SetValue(col.Green())
        self._bslider2.SetValue(col.Blue())

        # put down some caption styles from which the user can
        # select to show how the current or all caption bars will look like

        item = self._pnl.AddFoldPanel("Caption Style", False)

        currStyle =  wx.RadioButton(item, wx.ID_ANY, "&Vertical Gradient")
        self._pnl.AddFoldPanelWindow(item, currStyle, fpb.FPB_ALIGN_WIDTH,
                                     fpb.FPB_DEFAULT_SPACING, 10)
        
        currStyle.SetValue(True)

        radio1 = wx.RadioButton(item, wx.ID_ANY, "&Horizontal Gradient")
        radio2 = wx.RadioButton(item, wx.ID_ANY, "&Single Colour")
        radio3 = wx.RadioButton(item, wx.ID_ANY, "&Rectangle Box")
        radio4 = wx.RadioButton(item, wx.ID_ANY, "&Filled Rectangle Box")

        self._pnl.AddFoldPanelWindow(item, radio1, fpb.FPB_ALIGN_WIDTH, fpb.FPB_DEFAULT_SPACING, 10) 
        self._pnl.AddFoldPanelWindow(item, radio2, fpb.FPB_ALIGN_WIDTH, fpb.FPB_DEFAULT_SPACING, 10) 
        self._pnl.AddFoldPanelWindow(item, radio3, fpb.FPB_ALIGN_WIDTH, fpb.FPB_DEFAULT_SPACING, 10) 
        self._pnl.AddFoldPanelWindow(item, radio4, fpb.FPB_ALIGN_WIDTH, fpb.FPB_DEFAULT_SPACING, 10) 

        self._pnl.AddFoldPanelSeparator(item)

        self._single = wx.CheckBox(item, -1, "&Only This Caption")
        self._pnl.AddFoldPanelWindow(item, self._single, fpb.FPB_ALIGN_WIDTH,
                                     fpb.FPB_DEFAULT_SPACING, 10) 

        # one more panel to finish it

        cs = fpb.CaptionBarStyle()
        cs.SetCaptionStyle(fpb.CAPTIONBAR_RECTANGLE)

        item = self._pnl.AddFoldPanel("Misc Stuff", collapsed=True,
                                      cbstyle=cs)

        button2 = wx.Button(item, wx.NewId(), "Collapse All")        
        self._pnl.AddFoldPanelWindow(item, button2) 
        self._pnl.AddFoldPanelWindow(item, wx.StaticText(item, -1, "Enter Some Comments"),
                                     fpb.FPB_ALIGN_WIDTH, 5, 20) 
        self._pnl.AddFoldPanelWindow(item, wx.TextCtrl(item, -1, "Comments"),
                                     fpb.FPB_ALIGN_WIDTH, fpb.FPB_DEFAULT_SPACING, 10)

        # ADD THE FOLDPANELBAR TO THE SIZER!
        self.mainsizer.Add(self._pnl, 1, wx.EXPAND)
        self.mainsizer.Layout()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = Extended(None, title="FoldPanelBar Extended Demo")
    frame.Show()
    app.MainLoop()
    
