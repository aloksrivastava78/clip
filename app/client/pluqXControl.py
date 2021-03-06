
import wx

ID_READ_ONLY = wx.NewId()

class MenuFrame(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(MenuFrame, self).__init__(*args, **kwargs)
		# Attributes
		self.panel = wx.Panel(self)
		#self.txtctrl = wx.TextCtrl(self.panel,
		#style=wx.TE_MULTILINE)
		t4 = wx.TextCtrl(self, -1, "If supported by the native control, this is red, and this is a different font.",
                        size=(200, 100), style=wx.TE_MULTILINE|wx.TE_RICH2)
        	t4.SetInsertionPoint(0)
        	t4.SetStyle(44, 47, wx.TextAttr("RED", "YELLOW"))
        	points = t4.GetFont().GetPointSize()  # get the current size
        	f = wx.Font(points+3, wx.ROMAN, wx.ITALIC, wx.BOLD, True)
        	t4.SetStyle(63, 77, wx.TextAttr("BLUE", wx.NullColour, f))
		#t4.AddLine()
		t4.AppendText("This would be good")
		# Layout
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		#sizer.Add(self.txtctrl, 1, wx.EXPAND)
		self.panel.SetSizer(sizer)
		self.CreateStatusBar() # For output display
		# Setup the Menu
		menub = wx.MenuBar()
		# File Menu
		filem = wx.Menu()
		filem.Append(wx.ID_OPEN, "Open\tCtrl+O")
		menub.Append(filem, "&File")
		# Edit Menu
		editm = wx.Menu()
		editm.Append(wx.ID_COPY, "Copy\tCtrl+C")
		editm.Append(wx.ID_CUT, "Cut\tCtrl+X")
		editm.Append(wx.ID_PASTE, "Paste\tCtrl+V")
		editm.AppendSeparator()
		editm.Append(ID_READ_ONLY, "Read Only",
		kind=wx.ITEM_CHECK)
		menub.Append(editm, "E&dit")
		self.SetMenuBar(menub)
		# Event Handlers
		self.Bind(wx.EVT_MENU, self.OnMenu)
	def OnMenu(self, event):
		"""Handle menu clicks"""
		evt_id = event.GetId()
		#actions = { wx.ID_COPY : self.txtctrl.Copy,
		#wx.ID_CUT : self.txtctrl.Cut,
		#wx.ID_PASTE : self.txtctrl.Paste }
		#action = actions.get(evt_id, None)
		if 0:
			pass
		elif evt_id == ID_READ_ONLY:
			# Toggle enabled state
			#self.txtctrl.Enable(not self.txtctrl.Enabled)
			pass
		elif evt_id == wx.ID_OPEN:
			box = wx.StaticBox(self, -1, "This is a wx.StaticBox",size=self.GetSize())
		        bsizer = wx.StaticBoxSizer(box, wx.VERTICAL)	
		        t = wx.StaticText(self, -1, "Controls placed \"inside\" the box are really its siblings")
		        bsizer.Add(t, 0, wx.TOP|wx.LEFT, 60)
		        border = wx.BoxSizer()
		        border.Add(bsizer, 1, wx.EXPAND|wx.ALL, 25)
		        self.SetSizer(border)



class MyApp(wx.App):
    def OnInit(self):
        self.frame = MenuFrame(None)
	self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()


