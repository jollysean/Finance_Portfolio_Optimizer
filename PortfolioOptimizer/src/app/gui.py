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
		wx.Frame.__init__  ( self, parent, id = wx.ID_ANY, title = u"Portfolio Optimizer", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		
		
		bSizer14.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer101 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Enter stock symbols:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer101.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.EXPAND, 5 )
		
		self.m_symbolinput = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_CAPITALIZE|wx.TE_CENTRE|wx.TE_NO_VSCROLL )
		self.m_symbolinput.SetMinSize( wx.Size( 200,-1 ) )
		
		bSizer101.Add( self.m_symbolinput, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_addbutton = wx.Button( self.m_panel, wx.ID_ANY, u"Add to portfolio", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.m_addbutton, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer14.Add( bSizer101, 1, wx.EXPAND|wx.RIGHT, 5 )
		
		bSizer132 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer132.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_clearSelButton = wx.Button( self.m_panel, wx.ID_ANY, u"Remove Selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer132.Add( self.m_clearSelButton, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_clearAllButton = wx.Button( self.m_panel, wx.ID_ANY, u"Remove All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer132.Add( self.m_clearAllButton, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer14.Add( bSizer132, 0, wx.EXPAND|wx.LEFT, 5 )
		
		bSizer9.Add( bSizer14, 0, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook4 = wx.Notebook( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_TOP )
		self.m_panel41 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
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
		self.m_panel5 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook4.AddPage( self.m_panel5, u"Backtest Statistics", False )
		
		bSizer13.Add( self.m_notebook4, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer9.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel, wx.ID_ANY, u"Analysis" ), wx.VERTICAL )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText7 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Starting date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer11.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )
		
		self.m_startingdate = wx.DatePickerCtrl( self.m_panel, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		bSizer11.Add( self.m_startingdate, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		bSizer91.Add( bSizer11, 0, wx.EXPAND, 5 )
		
		m_rfRadBoxChoices = [ u"^IRX", u"^TNX" ]
		self.m_rfRadBox = wx.RadioBox( self.m_panel, wx.ID_ANY, u"Risk Free Rate", wx.DefaultPosition, wx.DefaultSize, m_rfRadBoxChoices, 1, wx.RA_SPECIFY_ROWS )
		self.m_rfRadBox.SetSelection( 1 )
		bSizer91.Add( self.m_rfRadBox, 0, wx.ALL, 5 )
		
		m_meanCalcRadBoxChoices = [ u"Log Normal", u"Simple" ]
		self.m_meanCalcRadBox = wx.RadioBox( self.m_panel, wx.ID_ANY, u"Mean Calculation Method", wx.DefaultPosition, wx.DefaultSize, m_meanCalcRadBoxChoices, 1, wx.RA_SPECIFY_ROWS )
		self.m_meanCalcRadBox.SetSelection( 0 )
		bSizer91.Add( self.m_meanCalcRadBox, 0, wx.ALL, 5 )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_backtestCB = wx.CheckBox( self.m_panel, wx.ID_ANY, u"Include backtest stats", wx.DefaultPosition, wx.DefaultSize, wx.CHK_2STATE )
		self.m_backtestCB.SetValue(True) 
		bSizer12.Add( self.m_backtestCB, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_analyzeButton = wx.Button( self.m_panel, wx.ID_ANY, u"Run Analysis", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_analyzeButton, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer91.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		sbSizer1.Add( bSizer91, 0, wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		bSizer9.Add( sbSizer1, 0, wx.EXPAND, 5 )
		
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
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_addbutton.Bind( wx.EVT_BUTTON, self.m_addButtonClick )
		self.m_clearSelButton.Bind( wx.EVT_BUTTON, self.removeSelClicked )
		self.m_clearAllButton.Bind( wx.EVT_BUTTON, self.removeAllClicked )
		self.m_stocklist.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.stockSelected )
		self.m_startingdate.Bind( wx.EVT_DATE_CHANGED, self.startDateChanged )
		self.m_rfRadBox.Bind( wx.EVT_RADIOBOX, self.rfrChanged )
		self.m_meanCalcRadBox.Bind( wx.EVT_RADIOBOX, self.meanCalcMethChanged )
		self.m_analyzeButton.Bind( wx.EVT_BUTTON, self.analyzeButtonClicked )
		self.Bind( wx.EVT_MENU, self.m_mniExitClick, id = m_mniExitId )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_addButtonClick( self, event ):
		event.Skip()
	
	def removeSelClicked( self, event ):
		event.Skip()
	
	def removeAllClicked( self, event ):
		event.Skip()
	
	def stockSelected( self, event ):
		event.Skip()
	
	def startDateChanged( self, event ):
		event.Skip()
	
	def rfrChanged( self, event ):
		event.Skip()
	
	def meanCalcMethChanged( self, event ):
		event.Skip()
	
	def analyzeButtonClicked( self, event ):
		event.Skip()
	
	def m_mniExitClick( self, event ):
		event.Skip()
		
###########################################################################
## Class WeightDialogBase
###########################################################################

class WeightDialogBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__  ( self, parent, id = wx.ID_ANY, title = u"Backtest Analysis", pos = wx.DefaultPosition, size = wx.Size( 250,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetExtraStyle( wx.WS_EX_PROCESS_UI_UPDATES )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		self.weightPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self.weightPanel, wx.ID_ANY, u"Enter an allocation percentage for each asset:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_staticText4.Wrap( 150 )
		self.m_staticText4.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer16.Add( self.m_staticText4, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.sliderPanel = wx.Panel( self.weightPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL )
		self.sliderPanel.SetMaxSize( wx.Size( -1,600 ) )
		
		gSizer2 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.m_staticText11 = wx.StaticText( self.sliderPanel, wx.ID_ANY, u"Microsoft", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gSizer2.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_slider16 = wx.Slider( self.sliderPanel, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		gSizer2.Add( self.m_slider16, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self.sliderPanel, wx.ID_ANY, u"Google, Inc.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_slider7 = wx.Slider( self.sliderPanel, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		gSizer2.Add( self.m_slider7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.sliderPanel.SetSizer( gSizer2 )
		self.sliderPanel.Layout()
		gSizer2.Fit( self.sliderPanel )
		bSizer16.Add( self.sliderPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self.weightPanel, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self.weightPanel, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();
		bSizer16.Add( m_sdbSizer1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.weightPanel.SetSizer( bSizer16 )
		self.weightPanel.Layout()
		bSizer16.Fit( self.weightPanel )
		bSizer24.Add( self.weightPanel, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer24 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_slider16.Bind( wx.EVT_SCROLL_LINEDOWN, self.sliderScrolling )
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.weightCancelClicked )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.weightOKClicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def sliderScrolling( self, event ):
		event.Skip()
	
	def weightCancelClicked( self, event ):
		event.Skip()
	
	def weightOKClicked( self, event ):
		event.Skip()
	

