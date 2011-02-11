
import wx
import wx.lib.scrolledpanel as scrolled

ID_READ_ONLY = wx.NewId()

class MenuFrame(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(MenuFrame, self).__init__(*args, **kwargs)
		# Attributes
		self.scrolledpanel = scrolled.ScrolledPanel(self, -1,size=(250, 300), style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER)
		# ALWAYS USE SIZERS!!!   for scrolled panel
	        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)


		sb1 = wx.StaticBox(self, -1, 'BOX0')
		sat1 = wx.CheckBox(self, -1, 'Satellite')
		gsm1 = wx.CheckBox(self, -1, 'GSM')
		wlan1 = wx.CheckBox(self, -1, 'WLAN')
		box = wx.StaticBoxSizer(sb1, wx.VERTICAL)
		box.SetMinSize((80, 60))
		box.Add(sat1, 0, wx.ALL, 5)
		box.Add(gsm1, 0, wx.ALL, 5)
		box.Add(wlan1, 0, wx.ALL, 5)

		self.scrolledpanel.SetSizer(self.mainsizer)
		# ADD THE FOLDPANELBAR TO THE SIZER!
	        self.mainsizer.Add(sb1, 1, wx.EXPAND)
	        self.mainsizer.Layout()
		self.scrolledpanel.SetVirtualSize((220, 1000))
	        # SETUP THE SCROLLEDPANEL        
	        self.scrolledpanel.SetupScrolling()
		
				


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MenuFrame(None)
	self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()


