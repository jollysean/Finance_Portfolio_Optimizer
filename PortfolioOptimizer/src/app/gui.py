# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 25 2009)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.grid

m_mniExitId = 1000

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__  ( self, parent, id = wx.ID_ANY, title = u"Portfolio Optimizer", pos = wx.DefaultPosition, size = wx.Size( 568,402 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Portfolio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_panel4 = wx.Panel( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText7 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Starting date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer11.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )
		
		self.m_startingdate = wx.DatePickerCtrl( self.m_panel, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		bSizer11.Add( self.m_startingdate, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		bSizer14.Add( bSizer11, 0, wx.EXPAND, 5 )
		
		bSizer101 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Enter stock symbols:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer101.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.EXPAND, 5 )
		
		self.m_symbolinput = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_CAPITALIZE|wx.TE_CENTRE|wx.TE_NO_VSCROLL )
		self.m_symbolinput.SetMinSize( wx.Size( 200,-1 ) )
		
		bSizer101.Add( self.m_symbolinput, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_addbutton = wx.Button( self.m_panel, wx.ID_ANY, u"Add to portfolio", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.m_addbutton, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer14.Add( bSizer101, 1, wx.EXPAND, 5 )
		
		bSizer9.Add( bSizer14, 0, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook4 = wx.Notebook( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_TOP )
		self.m_panel41 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer131 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_stocklist = wx.ListCtrl( self.m_panel41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		bSizer131.Add( self.m_stocklist, 3, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel41.SetSizer( bSizer131 )
		self.m_panel41.Layout()
		bSizer131.Fit( self.m_panel41 )
		self.m_notebook4.AddPage( self.m_panel41, u"Risk Summary", True )
		self.m_panel6 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_corgrid = wx.grid.Grid( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_corgrid.CreateGrid( 0, 0 )
		self.m_corgrid.EnableEditing( False )
		self.m_corgrid.EnableGridLines( True )
		self.m_corgrid.EnableDragGridSize( False )
		self.m_corgrid.SetMargins( 0, 0 )
		
		# Columns
		self.m_corgrid.EnableDragColMove( False )
		self.m_corgrid.EnableDragColSize( True )
		self.m_corgrid.SetColLabelSize( 30 )
		self.m_corgrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_corgrid.EnableDragRowSize( True )
		self.m_corgrid.SetRowLabelSize( 80 )
		self.m_corgrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_corgrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer17.Add( self.m_corgrid, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel6.SetSizer( bSizer17 )
		self.m_panel6.Layout()
		bSizer17.Fit( self.m_panel6 )
		self.m_notebook4.AddPage( self.m_panel6, u"Correlations", False )
		
		bSizer13.Add( self.m_notebook4, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer9.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_rfRadBoxChoices = [ u"^IRX", u"^TNX" ]
		self.m_rfRadBox = wx.RadioBox( self.m_panel, wx.ID_ANY, u"Risk Free Rate", wx.DefaultPosition, wx.DefaultSize, m_rfRadBoxChoices, 1, wx.RA_SPECIFY_ROWS )
		self.m_rfRadBox.SetSelection( 0 )
		bSizer91.Add( self.m_rfRadBox, 0, wx.ALL, 5 )
		
		m_meanCalcRadBoxChoices = [ u"Log Normal", u"Simple" ]
		self.m_meanCalcRadBox = wx.RadioBox( self.m_panel, wx.ID_ANY, u"Mean Calculation Method", wx.DefaultPosition, wx.DefaultSize, m_meanCalcRadBoxChoices, 1, wx.RA_SPECIFY_ROWS )
		self.m_meanCalcRadBox.SetSelection( 0 )
		bSizer91.Add( self.m_meanCalcRadBox, 0, wx.ALL, 5 )
		
		self.m_clearSelButton = wx.Button( self.m_panel, wx.ID_ANY, u"Remove Selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer91.Add( self.m_clearSelButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_clearAllButton = wx.Button( self.m_panel, wx.ID_ANY, u"Remove All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer91.Add( self.m_clearAllButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer9.Add( bSizer91, 0, wx.ALIGN_RIGHT, 5 )
		
		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		bSizer3.Add( bSizer8, 2, wx.EXPAND|wx.ALL, 5 )
		
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
		self.m_addbutton.Bind( wx.EVT_BUTTON, self.m_addButtonClick )
		self.m_stocklist.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.stockSelected )
		self.m_rfRadBox.Bind( wx.EVT_RADIOBOX, self.rfrChanged )
		self.m_meanCalcRadBox.Bind( wx.EVT_RADIOBOX, self.meanCalcMethChanged )
		self.m_clearSelButton.Bind( wx.EVT_BUTTON, self.removeSelClicked )
		self.m_clearAllButton.Bind( wx.EVT_BUTTON, self.removeAllClicked )
		self.Bind( wx.EVT_MENU, self.m_mniExitClick, id = m_mniExitId )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def startDateChanged( self, event ):
		event.Skip()
	
	def m_addButtonClick( self, event ):
		event.Skip()
	
	def stockSelected( self, event ):
		event.Skip()
	
	def rfrChanged( self, event ):
		event.Skip()
	
	def meanCalcMethChanged( self, event ):
		event.Skip()
	
	def removeSelClicked( self, event ):
		event.Skip()
	
	def removeAllClicked( self, event ):
		event.Skip()
	
	def m_mniExitClick( self, event ):
		event.Skip()
	

