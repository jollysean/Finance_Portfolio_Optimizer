# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 25 2009)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

m_mniExitId = 1000

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__  ( self, parent, id = wx.ID_ANY, title = u"Portfolio Optimizer", pos = wx.DefaultPosition, size = wx.Size( 642,642 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Portfolio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_panel4 = wx.Panel( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Starting date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer14.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )
		
		self.m_startingdate = wx.DatePickerCtrl( self.m_panel, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		bSizer14.Add( self.m_startingdate, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		bSizer9.Add( bSizer14, 0, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_stocklist = wx.ListCtrl( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		bSizer13.Add( self.m_stocklist, 3, wx.ALL|wx.EXPAND, 5 )
		
		bSizer9.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer102 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText6 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Enter stock symbols:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer102.Add( self.m_staticText6, 0, wx.ALIGN_CENTER, 5 )
		
		self.m_symbolinput = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_CAPITALIZE|wx.TE_CENTRE|wx.TE_NO_VSCROLL )
		bSizer102.Add( self.m_symbolinput, 1, wx.ALL, 5 )
		
		self.m_addbutton = wx.Button( self.m_panel, wx.ID_ANY, u"Add to portfolio", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer102.Add( self.m_addbutton, 0, wx.ALIGN_CENTER, 5 )
		
		bSizer9.Add( bSizer102, 0, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer9.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		bSizer3.Add( bSizer8, 2, wx.EXPAND|wx.ALL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_graphpanel = wx.Panel( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10.Add( self.m_graphpanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer3.Add( bSizer10, 3, wx.EXPAND, 5 )
		
		self.m_panel.SetSizer( bSizer3 )
		self.m_panel.Layout()
		bSizer3.Fit( self.m_panel )
		bSizer2.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_menubar = wx.MenuBar( 0 )
		self.m_mnFile = wx.Menu()
		self.m_mnFile.AppendSeparator()
		
		self.m_mniExit = wx.MenuItem( self.m_mnFile, m_mniExitId, u"&Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnFile.AppendItem( self.m_mniExit )
		
		self.m_menubar.Append( self.m_mnFile, u"&File" )
		
		self.SetMenuBar( self.m_menubar )
		
		
		# Connect Events
		self.m_startingdate.Bind( wx.EVT_DATE_CHANGED, self.startDateChanged )
		self.m_stocklist.Bind( wx.EVT_LIST_ITEM_SELECTED, self.stockSelected )
		self.m_addbutton.Bind( wx.EVT_BUTTON, self.m_addButtonClick )
		self.Bind( wx.EVT_MENU, self.m_mniExitClick, id = m_mniExitId )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def startDateChanged( self, event ):
		event.Skip()
	
	def stockSelected( self, event ):
		event.Skip()
	
	def m_addButtonClick( self, event ):
		event.Skip()
	
	def m_mniExitClick( self, event ):
		event.Skip()
	

