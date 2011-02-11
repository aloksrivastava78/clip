#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
# Main module file for Pluq-It GUI on windows.                                          #
# The GUI for PluqIt is based on wxPython and its supporting libs.                      #
# wxPython needs to be installed to make this script work.                              #
# There are some images also which needs to be present in the resp folder.              #
# The main starting point for invoking any gui is the tary icon of Pluq-It              #
# Rest GUI windows can be interpreted by following the tray class                       #
# For any ref/pointers kindly also refer to wxPython demo (its based on ref to that)    #
# Links will be shared separately.							#
# 											#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

import wx
from wx.lib.wordwrap import wordwrap
import wx.lib.agw.toasterbox as TB
import wx.lib.agw.foldpanelbar as fpb
import  wx.wizard as wiz
import images
from cStringIO import StringIO
import wx.lib.scrolledpanel as scrolled
import  wx.lib.buttons  as  buttons



# This variable will hold the total number of updates need to be shown in xControl
# Basically this will be fetched from Server and will be constantly pushed/polled
PluqIt_Num_of_Updates = 1




#####################################
#	 Login Dialog Box           #
#####################################
class LoginDialog(wx.Dialog):
	def __init__(self, *args, **kwargs):
		super(LoginDialog, self).__init__(*args, **kwargs)
		# Attributes		
		self.panel = LoginPanel(self)	
		# Layout
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.panel, 1, wx.EXPAND)
		self.SetSizer(sizer)
		self.SetInitialSize()
	def GetUsername(self):
		return self.panel.GetUsername()
	def GetPassword(self):
		return self.panel.GetPassword()


class LoginPanel(wx.Panel):
	def __init__(self, parent):
		super(LoginPanel, self).__init__(parent)
		# Attributes
		self._username = wx.TextCtrl(self)
		self._passwd = wx.TextCtrl(self, style=wx.TE_PASSWORD)	
		# Layout
		sizer = wx.FlexGridSizer(2, 2, 8, 8)
		sizer.Add(wx.StaticText(self, label="Username:"),
			  0, wx.ALIGN_CENTER_VERTICAL)
		sizer.Add(self._username, 0, wx.EXPAND)
		sizer.Add(wx.StaticText(self, label="Password:"),
			  0, wx.ALIGN_CENTER_VERTICAL)
		sizer.Add(self._passwd, 0, wx.EXPAND)
		msizer = wx.BoxSizer(wx.VERTICAL)
		msizer.Add(sizer, 1, wx.EXPAND|wx.ALL, 20)

		btnszr = wx.StdDialogButtonSizer()
		button = wx.Button(self, wx.ID_OK)
		button.SetDefault()
	
		btnszr.AddButton(button)
		msizer.Add(btnszr, 0, wx.ALIGN_CENTER|wx.ALL, 12)
		btnszr.Realize()
		self.Bind(wx.EVT_BUTTON, self.OnSubmit,button)
		
		self.SetSizer(msizer)
		
	
	def GetUsername(self):
		return self._username.GetValue()
	
	
	def GetPassword(self):
		return self._passwd.GetValue()
	
	
	def OnSubmit(self,event):
		print self._username.GetValue()
		print self._passwd.GetValue()
		self.Close()


###########################################################################################
# PluqIt_XControl_UpdateFolder : this is the main class which would take care GUI lay out #
#                                 of all update folders                                   #
# The main xControl class which will take care of displaying the Pluq-It Updates	  #
# Its current form is collapsable version of wxPython AGW library.			  #
# The UI TO-DO scope includes:	  							  #
# 1. Changing the collapsed version itself completely, as search for better option is	  #
#    in progress.									  #
# 2. Enhancing the current version. At present it may not be looking that good due to	  #	
#    lack of logo/pictures								  #
# 3. Any suggestions/ideas??								  #
#											  #
###########################################################################################



class FoldTestPanel(wx.Panel):

    def __init__(self, parent, id, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.NO_BORDER | wx.TAB_TRAVERSAL):
        
        wx.Panel.__init__(self, parent, id, pos, size, style)

        self.CreateControls()
        self.GetSizer().Fit(self)
        self.GetSizer().SetSizeHints(self)
        self.GetSizer().Layout()

        self.Bind(fpb.EVT_CAPTIONBAR, self.OnPressCaption)


    def OnPressCaption(self, event):
	print "caption pressed!!"
        event.Skip()



    



    def CreateControls(self):
	
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        
        subpanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                            wx.NO_BORDER | wx.TAB_TRAVERSAL)
        sizer.Add(subpanel, 1, wx.GROW | wx.ADJUST_MINSIZE, 5)

        #subsizer = wx.BoxSizer(wx.VERTICAL)
	subsizer = wx.GridBagSizer(hgap = 2, vgap = 2)
        #subpanel.SetSizer(subsizer)
        

	item5_bmp = wx.Bitmap("face-monkey.png", wx.BITMAP_TYPE_PNG)
        #item7.SetValue(True)
	#b7 = wx.BitmapButton(self, -1, item7_bmp, (8, 8),(item7_bmp.GetWidth()+10, item7_bmp.GetHeight()+10))
	b5 = wx.BitmapButton(self, -1, item5_bmp,style = wx.BORDER_NONE)
        #subsizer.Add(b7, (1,0), flag = wx.ALIGN_LEFT | wx.ALL, border = 0)
	subsizer.Add(b5,pos = (0,0))



        #item6 = wx.TextCtrl(subpanel, wx.ID_ANY, "All update text will go here", wx.DefaultPosition, wx.DefaultSize,
        #                    wx.TE_MULTILINE)
	item6 = wx.StaticText(subpanel, wx.ID_ANY, "All update text will go here", wx.DefaultPosition, wx.DefaultSize)
	subsizer.Add(item6, pos = (0,1), flag = wx.EXPAND)


	item7_bmp = wx.Bitmap("twt.png", wx.BITMAP_TYPE_PNG)
        #item7.SetValue(True)
	#b7 = wx.BitmapButton(self, -1, item7_bmp, (8, 8),(item7_bmp.GetWidth()+10, item7_bmp.GetHeight()+10))
	b7 = wx.BitmapButton(self, -1, item7_bmp,style = wx.BORDER_NONE)
        #subsizer.Add(b7, (1,0), flag = wx.ALIGN_LEFT | wx.ALL, border = 0)
	subsizer.Add(b7,pos = (1,0))


        item8_bmp = wx.Bitmap("fb.png", wx.BITMAP_TYPE_PNG)
        #item7.SetValue(True)
	#b8 = wx.BitmapButton(self, -1, item8_bmp, (8, 8),(item8_bmp.GetWidth()+10, item8_bmp.GetHeight()+10))
	b8 = wx.BitmapButton(self, -1, item8_bmp,style = wx.BORDER_NONE)
	self.Bind(wx.EVT_BUTTON, NotCollapsed.OnButtonReadMore, b8)
        #subsizer.Add(b8, (1,1), flag = wx.ALIGN_RIGHT | wx.ALL, border = 0)
	subsizer.Add(b8, pos = (1,1)) 


	# a flat text button to show read more content
        b9 = buttons.GenButton(self, -1, 'Read More..', style=wx.BORDER_NONE)
        b9.Bind(wx.EVT_BUTTON, NotCollapsed.OnButtonReadMore)
        subsizer.Add(b9, pos = (1,3))
	

	#item9 = wx.StaticLine(self,-1)
	#subsizer.Add(item9) 
	
	# make the last row and col be stretchable
	subsizer.AddGrowableCol(2)
	subsizer.AddGrowableRow(2)
	
	subpanel.SetSizer(subsizer)
	subpanel.Fit()



        """item7 = wx.RadioButton(subpanel, wx.ID_ANY, "Instead of this, there will be a FB Logo", wx.DefaultPosition,
                               wx.DefaultSize, 0)
        item7.SetValue(True)
        subsizer.Add(item7, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        item8 = wx.RadioButton(subpanel, wx.ID_ANY, "Instead of this, there will be a Twitter Logo", wx.DefaultPosition,
                               wx.DefaultSize, 0)
        item8.SetValue(False)
        subsizer.Add(item8, 0, wx.ALIGN_LEFT | wx.ALL, 5) """







#################################################################################
# Class to show update window boxes                                             #
# wx.Frame        :the default class from which its derived                     #
# update_list_num :the number of updates which needs to be shown                #
#################################################################################

class NotCollapsed(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition,
                 size=(300,500), style=wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        


	# added for scrolled panel
	self.scrolledPanel = scrolled.ScrolledPanel(self, -1,size=(250, 300), style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER)
	self.scrolledPanel.SetBackgroundColour('WHITE')

	#self.SetIcon(GetMondrianIcon())
        self.SetMenuBar(self.CreateMenuBar())

        self.statusbar = self.CreateStatusBar(2, wx.ST_SIZEGRIP)
        self.statusbar.SetStatusWidths([-4, -3])
        self.statusbar.SetStatusText("(c) Pluq It Status!!", 0)
        self.statusbar.SetStatusText("SISO Technologies Pvt Ltd!", 1)

	# ALWAYS USE SIZERS!!!   for scrolled panel
        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)

	#fgs1 = wx.FlexGridSizer(cols=6, vgap=4, hgap=4)

        # this creates the main FoldPanelBar from afw lib in wxPython
        
	# USE SIZERS!!    added for scrolled panel
        #self.scrolledPanel.SetSizer(self.mainsizer)
	
	self.scrolledPanel.DestroyChildren()

	# self.scrolledPanel added for scrolled panel scorlling
	pnl = fpb.FoldPanelBar(self.scrolledPanel, -1, wx.DefaultPosition, wx.Size(180,30),
                               0)
        #pnl.SetBackgroundColour("white")


	

	# Creating rest of the updates shall be appended to the main FoldPanelBar
	# All the update folders will follow the same pattern
	# The folder GUI pattern can be changed/enhanced based on the group discussion
	# 
	for update_index in range(PluqIt_Num_of_Updates):
		str = "Pluq IT Update %d" % update_index
        	item = pnl.AddFoldPanel(str, collapsed=False)
        	#item.SetBackgroundColour("black")
        	#pnl.AddFoldPanelSeparator(item)
    
		pnl.AddFoldPanelSeparator(item)
		
		"""item7_bmp = wx.Bitmap("twt.png", wx.BITMAP_TYPE_PNG)
	        #item7.SetValue(True)
		#b7 = wx.BitmapButton(self, -1, item7_bmp, (8, 8),(item7_bmp.GetWidth()+10, item7_bmp.GetHeight()+10))
		b7 = wx.BitmapButton(self, -1, item7_bmp,style = wx.BORDER_NONE)
        	#subsizer.Add(b7, (1,0), flag = wx.ALIGN_LEFT | wx.ALL, border = 0)
		#subsizer.Add(b7,pos = (1,0))
		pnl.AddFoldPanelWindow(item, b7)
		

        	item8_bmp = wx.Bitmap("fb.png", wx.BITMAP_TYPE_PNG)
	        #item7.SetValue(True)
		#b8 = wx.BitmapButton(self, -1, item8_bmp, (8, 8),(item8_bmp.GetWidth()+10, item8_bmp.GetHeight()+10))
		b8 = wx.BitmapButton(self, -1, item8_bmp,style = wx.BORDER_NONE)
		#subsizer.Add(b8, (1,1), flag = wx.ALIGN_RIGHT | wx.ALL, border = 0)
		#subsizer.Add(b8, pos = (1,1)) 
		pnl.AddFoldPanelWindow(item,b8)
		self.Bind(wx.EVT_BUTTON, self.OnButtonReadMore, b8)
		


		# a flat text button to show read more content
        	b9 = buttons.GenButton(self, -1, 'Read More..', style=wx.BORDER_NONE)
	        #subsizer.Add(b9, pos = (1,3))
 		pnl.AddFoldPanelWindow(item,b9)
		b9.Bind(wx.EVT_BUTTON, self.OnButtonReadMore)
		http://yergler.net/talks/desktopapps_uk/"""

		newfoldpanel = FoldTestPanel(item, wx.ID_ANY)

		pnl.AddFoldPanelWindow(item, newfoldpanel)

        	

        
       
       
       
       
        self.pnl = pnl
	
        #pnl.SetMinSize((200, -1))

	
	# applying the color setting to all the panels
	col1 = "white"
	col2 = "white"
	style = fpb.CaptionBarStyle()
        style.SetFirstColour(col1)
        style.SetSecondColour(col2)
	mystyle = fpb.CAPTIONBAR_SINGLE
	style.SetCaptionStyle(mystyle)
        pnl.ApplyCaptionStyleAll(style)
	

	# USE SIZERS!!    added for scrolled panel
        self.scrolledPanel.SetSizer(self.mainsizer)
	# ADD THE FOLDPANELBAR TO THE SIZER!
        self.mainsizer.Add(pnl, 1, wx.EXPAND)
        self.mainsizer.Layout()
	self.scrolledPanel.SetVirtualSize((220, 1000))
        # SETUP THE SCROLLEDPANEL        
        self.scrolledPanel.SetupScrolling()
	"""fgs1.Add(pnl,-1,wx.EXPAND)
	self.scrolledPanel.SetSizer( fgs1 )
        self.scrolledPanel.SetAutoLayout(1)
        self.scrolledPanel.SetupScrolling()"""
	
   
    def OnButtonReadMore(self,event):

	print "read more !!!"    
	msg = "This window will show the full length text of updates.\n\n" + \
              "Happy Pluq-ing " + wx.VERSION_STRING + "!!"
        dlg = wx.MessageDialog(self, msg, "Full length text",
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        #dlg.Destroy()

    def CreateMenuBar(self):

        FoldPanelBarTest_Quit = wx.NewId()
        FoldPanelBarTest_About = wx.NewId()
        
        menuFile = wx.Menu()
        menuFile.Append(FoldPanelBarTest_Quit, "E&xit\tAlt-X", "Quit This Program")

        helpMenu = wx.Menu()
        helpMenu.Append(FoldPanelBarTest_About, "&About...\tF1", "Show About Dialog")

        self.Bind(wx.EVT_MENU, self.OnQuit, id=FoldPanelBarTest_Quit)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=FoldPanelBarTest_About)

        value = wx.MenuBar()
        value.Append(menuFile, "&File")
        value.Append(helpMenu, "&Help")

        return value


    # Event Handlers

    def OnQuit(self, event):

        # True is to force the frame to close
        self.Close(True)


    def OnAbout(self, event):

        msg = "This is the about live updates window of Pluq-It.\n\n" + \
              "Happy Pluq-ing " + wx.VERSION_STRING + "!!"
        dlg = wx.MessageDialog(self, msg, "About Pluq It",
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


    def OnCollapseMe(self, event):

        item = self.pnl.GetFoldPanel(0)
        self.pnl.Collapse(item)

    def OnExpandMe(self, event):

        self.pnl.Expand(self.pnl.GetFoldPanel(0))
        self.pnl.Collapse(self.pnl.GetFoldPanel(1))

    def PluqIt_UpdateStatus_xControl(self,panel):
        pass




###################################################################
# 								  #
#  	  Supporting function for PluqIt installation		  #
#								  #
###################################################################
def makePageTitle(wizPg, title):
    sizer = wx.BoxSizer(wx.VERTICAL)
    wizPg.SetSizer(sizer)
    title = wx.StaticText(wizPg, -1, title)
    title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
    sizer.Add(title, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
    sizer.Add(wx.StaticLine(wizPg, -1), 0, wx.EXPAND|wx.ALL, 5)
    return sizer

#----------------------------------------------------------------------

class TitledPage(wiz.WizardPageSimple):
    def __init__(self, parent, title):
        wiz.WizardPageSimple.__init__(self, parent)
        self.sizer = makePageTitle(self, title)




################################################################################
# Creating a task bar icon Class		                               #
# This serves as the main class for our gui                                    #
# as has been advised, its better to put all classes(gui pages) in other files #
# and then invoke them from here itself FROM THE DIFFERENT functions           #
################################################################################

class PluqItTaskBarIcon(wx.TaskBarIcon):
    ID_PLUQIT_LOGIN = wx.NewId()
    ID_PLUQIT_ABOUTUS = wx.NewId()
    ID_PLUQIT_XCONTROL = wx.NewId()
    ID_PLUQIT_STATUS_UPDATE = wx.NewId()
    ID_PLUQIT_INSTALL = wx.NewId()
    def __init__(self):
        super(PluqItTaskBarIcon, self).__init__()

        # Setup
        icon = wx.Icon("face-monkey.png", wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

        # Event Handlers
        self.Bind(wx.EVT_MENU, self.OnMenu)

    def CreatePopupMenu(self):
        """Base class virtual method for creating the
        popup menu for the icon.
        """
        menu = wx.Menu()
	menu.Append(PluqItTaskBarIcon.ID_PLUQIT_XCONTROL,"xControl")
	menu.AppendSeparator()
	menu.Append(PluqItTaskBarIcon.ID_PLUQIT_INSTALL,"INSTALL!!")
	menu.AppendSeparator()
	menu.Append(PluqItTaskBarIcon.ID_PLUQIT_STATUS_UPDATE,"Status Update")
        menu.Append(PluqItTaskBarIcon.ID_PLUQIT_LOGIN, "Login")
        menu.Append(PluqItTaskBarIcon.ID_PLUQIT_ABOUTUS, "About Us!")
        menu.AppendSeparator()
        menu.Append(wx.ID_CLOSE, "Exit")
        return menu

    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
    # This serves as our main on-menu (sys tray icon function) which would #
    # in turn call different						   #
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

    def OnMenu(self, event):
        evt_id = event.GetId()
        if evt_id == PluqItTaskBarIcon.ID_PLUQIT_LOGIN:
           self.dialog = LoginDialog(None,title="Pluqi-t Login!!!")
	   self.dialog.ShowModal()
        elif evt_id == PluqItTaskBarIcon.ID_PLUQIT_ABOUTUS:
           self.OnAboutUsBox()
        elif evt_id == wx.ID_CLOSE:
            self.Destroy()
	    self.Exit()
        elif evt_id == PluqItTaskBarIcon.ID_PLUQIT_STATUS_UPDATE:
	    self.OnPopUpStatus()
        elif evt_id == PluqItTaskBarIcon.ID_PLUQIT_XCONTROL:
	    self.OnPluqItXControl()
	elif evt_id == PluqItTaskBarIcon.ID_PLUQIT_INSTALL:
	    self.OnPluqItConfig()
	    pass
        else:
            event.Skip()

    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
    # Display the About dialog box #
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
    def OnAboutUsBox(self):
	pluqit_info = wx.AboutDialogInfo()
        pluqit_info.Name = "Pluq IT!!"
        pluqit_info.Version = "1.0.0"
        pluqit_info.Copyright = "(C) 2011 ChipMonk, Pluq IT"
        pluqit_info.Description =  """A \"Pluq IT\" program is a software program that helps you "
			           keep your data on the go. 
			           \n\n A \"Pliq IT\" is in a pre-beta version phase
		                   to check the environmentm, end-2-end communication and run time
			           run-time environment are correctly installed."""
        pluqit_info.WebSite = ("pluq.it", "Hello World home page")
        pluqit_info.Developers = [ "Alok Srivastava",
                            "Sudhanshu Saxena",
                            "Anand Prakash Yadav",
			    "Samarth V Deo"]

        pluqit_info.License =""" License is hereby grantyed to you the pre-beta version for free"""

        # Then we call wx.AboutBox giving it that info object
        wx.AboutBox(pluqit_info)

    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
    # Open the main xControl window of pluq it		   #
    # All real time updates will be shown in this window.  #
    # This is mainly of chat window unit		   #
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
    def OnPluqItXControl(self):
	print "xcontrol main class"
	
        frame = NotCollapsed(None, title="Pluq It xControl")
        frame.Show()
	    
  
   
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
    # Configure Window to configure the required sets for                     #
    # for Pluq It.                                                            #
    # Once packaged, this may be set aside as a separate class and module     #
    # so that it would serve as our seed.                                     #
    #				                                              #
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


    def OnPluqItConfig(self):
        # Create the wizard and the pages
        #wizard = wx.PreWizard()
        #wizard.SetExtraStyle(wx.WIZARD_EX_HELPBUTTON)
        #wizard.Create(self, self.ID_wiz, "Simple Wizard",
        #              images.WizTest1.GetBitmap())
	f = file('1.png', 'rb')
        data=f.read()
	img=wx.BitmapFromImage(wx.ImageFromStream(StringIO(data)))
        wizard = wiz.Wizard(None, -1, "Dynamic Wizard",wx.BitmapFromImage(wx.ImageFromStream(StringIO(data))) )

        page1 = TitledPage(wizard, "Page 1")
        page2 = TitledPage(wizard, "Page 2")
        page3 = TitledPage(wizard, "Page 3")
        page4 = TitledPage(wizard, "Page 4")
        page5 = TitledPage(wizard, "Page 5")
        self.page1 = page1

        page1.sizer.Add(wx.StaticText(page1, -1, """
This wizard shows the ability to choose at runtime the order
of the pages and also which bitmap is shown.
"""))
        wizard.FitToPage(page1)
        page5.sizer.Add(wx.StaticText(page5, -1, "\nThis is the last page."))

        # Set the initial order of the pages
        page1.SetNext(page2)
        page2.SetPrev(page1)
        page2.SetNext(page3)
        page3.SetPrev(page2)
        page3.SetNext(page4)
        page4.SetPrev(page3)
        page4.SetNext(page5)
        page5.SetPrev(page4)


        wizard.GetPageAreaSizer().Add(page1)
        if wizard.RunWizard(page1):
            wx.MessageBox("Wizard completed successfully", "That's all folks!")
        else:
            wx.MessageBox("Wizard was cancelled", "That's all folks!")
	 


    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
    #	This woould display the status updates #
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
    def OnPopUpStatus(self):
	windowstyle = TB.TB_DEFAULT_STYLE
	tbstyle = TB.TB_SIMPLE
	closingstyle = TB.TB_ONCLICK
	tb = TB.ToasterBox(None, tbstyle, windowstyle, closingstyle)

        #if windowstyle == TB.TB_CAPTION:
        tb.SetTitle("This working would be awsome")

        sizex = 250
        sizey = 200
        tb.SetPopupSize((sizex, sizey))

        posx = 1100
        posy = 550
        tb.SetPopupPosition((posx, posy))
        
        tb.SetPopupPauseTime(4000)
        tb.SetPopupScrollSpeed(8)

        self.PluqIT_Updates(tb)
              
        tb.Play()
	
    def PluqIT_Updates(self,tb):
	tb.SetPopupBackgroundColour("BLACK")
        tb.SetPopupTextColour("WHITE")
        bmp = "1.png"
        #dummybmp = wx.NullBitmap
        
        
        dummybmp = wx.Bitmap(bmp, wx.BITMAP_TYPE_BMP)

        tb.SetPopupBitmap()
        #tb.SetPopupBitmap()

        txtshown = "Working of this would be a great boost!!!"
        
             
        tb.SetPopupText(txtshown)
        #tb.SetPopupTextFont(self.curFont)
	    






########################################################################
# wx.App Instantiation which would serve as the main class for full gui#
########################################################################

class MyApp(wx.App):
	def OnInit(self):
		#self.dialog = LoginDialog(None,title="Pluqi-t Login!!!")
		self.systrayicon = PluqItTaskBarIcon()

		#self.SetTopWindow(self.frame)
		#self.dialog.ShowModal()
		return True






if __name__ == "__main__":
	app = MyApp(False)
	app.MainLoop()



