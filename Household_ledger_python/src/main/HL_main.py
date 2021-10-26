# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from main import HL_CRUD
from main.barChart import Barchart


###########################################################################
## Class MyFrame
###########################################################################
class MyFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"가계부", pos = wx.DefaultPosition, size = wx.Size( 1360,768 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        # self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"거래번호", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont( wx.Font( 11, 70, 90, 92, False, "Consolas" ) )
        
        bSizer23.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.txtSeriaNo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_READONLY|wx.TE_RIGHT )
        self.txtSeriaNo.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer23.Add( self.txtSeriaNo, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        bSizer11.Add( bSizer23, 1, wx.EXPAND, 5 )
        
        bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"거래일자", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_staticText2.Wrap( -1 )
        self.m_staticText2.SetFont( wx.Font( 11, 70, 90, 92, False, "Consolas" ) )
        
        bSizer24.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.txtDate = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_RIGHT )
        self.txtDate.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer24.Add( self.txtDate, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        bSizer11.Add( bSizer24, 1, wx.EXPAND, 5 )
        
        
        gbSizer1.Add( bSizer11, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 5 ), wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"수입 입력부", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )
        self.m_staticText16.SetFont( wx.Font( 11, 70, 90, 92, False, "Consolas" ) )
        
        bSizer3.Add( self.m_staticText16, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.RadioRevenue = wx.RadioButton( self, wx.ID_ANY, u"수입(필수선택)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.RadioRevenue.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer4.Add( self.RadioRevenue, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"수입구분", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        self.m_staticText17.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer13.Add( self.m_staticText17, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        comboRevenueChoices = [ u"상세내역 선택", u"수입.급여", u"수입.상여", u"수입.이자", u"수입.배당", u"수입.사업", u"수입.연금", u"수입.기타" ]
        self.comboRevenue = wx.ComboBox( self, wx.ID_ANY, u"상세내역 선택", wx.DefaultPosition, wx.Size( 120,-1 ), comboRevenueChoices, 0 )
        self.comboRevenue.SetSelection( 0 )
        self.comboRevenue.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer13.Add( self.comboRevenue, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        bSizer3.Add( bSizer13, 1, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"수입금액", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        self.m_staticText9.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer6.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.txtRevenue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), wx.TE_RIGHT )
        self.txtRevenue.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer6.Add( self.txtRevenue, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        bSizer3.Add( bSizer6, 1, wx.EXPAND, 5 )
        
        
        gbSizer1.Add( bSizer3, wx.GBPosition( 3, 1 ), wx.GBSpan( 4, 2 ), wx.EXPAND, 5 )
        
        bSizer7 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"지출 입력부", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        self.m_staticText10.SetFont( wx.Font( 11, 70, 90, 92, False, "Consolas" ) )
        
        bSizer7.Add( self.m_staticText10, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.RadioExpense = wx.RadioButton( self, wx.ID_ANY, u"지출(필수선택)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.RadioExpense.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer8.Add( self.RadioExpense, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )
        
        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"지출구분", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )
        self.m_staticText18.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer15.Add( self.m_staticText18, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        comboExpenseChoices = [ u"상세내역 선택", u"지출.식대", u"지출.간식", u"지출.여가생활", u"지출.소모품", u"지출.패션", u"지출.가전", u"지출.차량", u"지출.공과금", u"지출.보험", u"지출.기타" ]
        self.comboExpense = wx.ComboBox( self, wx.ID_ANY, u"상세내역 선택", wx.DefaultPosition, wx.Size( 120,-1 ), comboExpenseChoices, 0 )
        self.comboExpense.SetSelection( 0 )
        self.comboExpense.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer15.Add( self.comboExpense, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        bSizer7.Add( bSizer15, 1, wx.EXPAND, 5 )
        
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"지출금액", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        self.m_staticText12.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer9.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.txtExpense = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), wx.TE_RIGHT )
        self.txtExpense.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer9.Add( self.txtExpense, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )
        
        
        gbSizer1.Add( bSizer7, wx.GBPosition( 3, 4 ), wx.GBSpan( 5, 2 ), wx.EXPAND, 5 )
        
        bSizer17 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btnInsert = wx.Button( self, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.Size( 108,-1 ), wx.NO_BORDER )
        self.btnInsert.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer16.Add( self.btnInsert, 0, wx.ALL, 5 )
        
        self.btnUpdate = wx.Button( self, wx.ID_ANY, u"수정", wx.DefaultPosition, wx.Size( 108,-1 ), wx.NO_BORDER )
        self.btnUpdate.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer16.Add( self.btnUpdate, 0, wx.ALL, 5 )
        
        self.btnDelete = wx.Button( self, wx.ID_ANY, u"삭제", wx.DefaultPosition, wx.Size( 108,-1 ), wx.NO_BORDER )
        self.btnDelete.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer16.Add( self.btnDelete, 0, wx.ALL, 5 )
        
        self.btnClear = wx.Button( self, wx.ID_ANY, u"초기화", wx.DefaultPosition, wx.Size( 108,-1 ), wx.NO_BORDER )
        self.btnClear.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer16.Add( self.btnClear, 0, wx.ALL, 5 )
        
        
        bSizer17.Add( bSizer16, 1, wx.EXPAND, 5 )
        
        bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btnFind = wx.Button( self, wx.ID_ANY, u"수입내역 조회", wx.DefaultPosition, wx.Size( 226,-1 ), wx.NO_BORDER )
        self.btnFind.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer20.Add( self.btnFind, 0, wx.ALL, 5 )
        
        self.btnSelectAll = wx.Button( self, wx.ID_ANY, u"전체거래 조회", wx.DefaultPosition, wx.Size( 226,-1 ), wx.NO_BORDER )
        self.btnSelectAll.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer20.Add( self.btnSelectAll, 0, wx.ALL, 5 )
        
        
        bSizer17.Add( bSizer20, 1, wx.EXPAND, 5 )
        
        
        gbSizer1.Add( bSizer17, wx.GBPosition( 13, 1 ), wx.GBSpan( 2, 5 ), wx.EXPAND, 5 )
        
        bSizer21 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"작업내역", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        self.m_staticText19.SetFont( wx.Font( 11, 70, 90, 92, False, "Consolas" ) )
        
        bSizer21.Add( self.m_staticText19, 0, wx.ALL, 5 )
        
        self.txtWorkHistory = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1, 280 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
        self.txtWorkHistory.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer21.Add( self.txtWorkHistory, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        gbSizer1.Add( bSizer21, wx.GBPosition( 16, 1 ), wx.GBSpan( 10, 5 ), wx.EXPAND, 5 )
        
        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"데이터 조회", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        self.m_staticText20.SetFont( wx.Font( 11, 70, 90, 92, False, "Consolas" ) )
        
        gbSizer1.Add( self.m_staticText20, wx.GBPosition( 1, 9 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.list = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        self.list.InsertColumn(0, '거래번호', width = 60)
        self.list.InsertColumn(1, '거래일자', width = 100)
        self.list.InsertColumn(2, '수입/지출', width = 100)
        self.list.InsertColumn(3, '상세내역', width = 120)
        self.list.InsertColumn(4, '수입금액', width = 100)
        self.list.InsertColumn(5, '지출금액', width = 100)
        self.list.InsertColumn(6, '적요', width = 240)
        self.list.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        gbSizer1.Add( self.list, wx.GBPosition( 2, 9 ), wx.GBSpan( 10, 5 ), wx.ALL|wx.EXPAND, 5 )
        
        bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"지출 현황", wx.DefaultPosition, wx.Size( 600,-1 ), 0 )
        self.m_staticText22.Wrap( -1 )
        self.m_staticText22.SetFont( wx.Font( 11, 70, 90, 92, False, "Consolas" ) )
        
        bSizer19.Add( self.m_staticText22, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button7 = wx.Button( self, wx.ID_ANY, u"그래프 보기", wx.DefaultPosition, wx.Size( -1,-1 ), wx.NO_BORDER )
        self.m_button7.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer27.Add( self.m_button7, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
        
        self.m_button8 = wx.Button( self, wx.ID_ANY, u"그래프 지우기", wx.DefaultPosition, wx.Size( -1,-1 ), wx.NO_BORDER )
        self.m_button8.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer27.Add( self.m_button8, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer19.Add( bSizer27, 1, wx.SHAPED, 5 )
        
        
        gbSizer1.Add( bSizer19, wx.GBPosition( 13, 9 ), wx.GBSpan( 1, 32 ), wx.ALIGN_LEFT|wx.EXPAND|wx.SHAPED, 5 )
        
        self.graphPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.graphPanel = Barchart(self)
        self.graphPanel.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        self.graphPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gbSizer1.Add( self.graphPanel, wx.GBPosition( 14, 9 ), wx.GBSpan( 13, 5 ), wx.ALL|wx.EXPAND, 5 )
        
        bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"비고", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_staticText14.Wrap( -1 )
        self.m_staticText14.SetFont( wx.Font( 11, 70, 90, 92, False, "Consolas" ) )
        
        bSizer28.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.txtRemark = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 425,-1 ), wx.TE_MULTILINE )
        self.txtRemark.SetFont( wx.Font( 11, 70, 90, 90, False, "Consolas" ) )
        
        bSizer28.Add( self.txtRemark, 0, wx.ALL, 5 )
        
        
        gbSizer1.Add( bSizer28, wx.GBPosition( 9, 1 ), wx.GBSpan( 3, 5 ), wx.EXPAND, 5 )
        
        
        bSizer1.Add( gbSizer1, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnInsert.Bind( wx.EVT_BUTTON, self.OnInsert )
        self.btnUpdate.Bind( wx.EVT_BUTTON, self.OnUpdate )
        self.btnDelete.Bind( wx.EVT_BUTTON, self.OnDelete )
        self.btnClear.Bind( wx.EVT_BUTTON, self.OnClear )
        self.btnFind.Bind( wx.EVT_BUTTON, self.OnFind )
        self.btnSelectAll.Bind( wx.EVT_BUTTON, self.OnSelectAll )
        self.list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnSelected )
        self.m_button8.Bind( wx.EVT_BUTTON, self.OnErase )
        self.m_button7.Bind( wx.EVT_BUTTON, self.OnPaint )
    
    def __del__( self ):
        pass
    
    
    
    # Virtual event handlers, overide them in your derived class
    
    def OnInsert( self, event ):
        date = self.txtDate.GetValue()
        
        section = ""
        if (self.RadioRevenue.GetValue()):
            section = '수입'
            
        elif(self.RadioExpense.GetValue()):
            section = '지출'      
        
        title = ""
        if ('수입' in  self.comboRevenue.GetValue()):
            title = self.comboRevenue.GetValue()
            
        elif('지출' in  self.comboExpense.GetValue()):
            title = self.comboExpense.GetValue()  
        
        expense = 0
        revenue = 0
        if (self.txtRevenue.GetValue() == ""):
            expense = self.txtExpense.GetValue()
            revenue = 0
            pass
        
        elif(self.txtExpense.GetValue() == ""):
            revenue = self.txtRevenue.GetValue()
            expense = 0
            pass

        remark = self.txtRemark.GetValue()
        
        HL_CRUD.insertData(date, section, title, revenue, expense, remark)
        
        self.txtWorkHistory.AppendText(" - 거래 등록완료. <상세정보 - " + "거래일자:" + date + "/" + section+"건>\n")
        
        self.OnSelectAll(event)
        
        event.Skip()
    
    def OnUpdate( self, event ):
        serialNo = self.txtSeriaNo.GetValue()
        date = self.txtDate.GetValue()

        section = ""        
        if (self.RadioRevenue.GetValue()):
            section = '수입'
            
        elif(self.RadioExpense.GetValue()):
            section = '지출' 
            
        title = ""
        if ('수입' in  self.comboRevenue.GetValue()):
            title = self.comboRevenue.GetValue()
            
        elif('지출' in  self.comboExpense.GetValue()):
            title = self.comboExpense.GetValue()            
            
        revenue = self.txtRevenue.GetValue()
        
        expense = self.txtExpense.GetValue()    
        
        remark = self.txtRemark.GetValue()
        
        HL_CRUD.update(((date, section, title, revenue, expense, remark, serialNo)))
        
        self.txtWorkHistory.AppendText(" - 거래내역 수정완료. <상세정보 - " + "수정한 거래번호:" + serialNo + "/" + section +"건>\n")        
        
        self.OnSelectAll(event)
            
        event.Skip()
    
    def OnDelete( self, event ):
        key = self.txtSeriaNo.GetValue()
        
        HL_CRUD.delete(key)
        
        self.txtWorkHistory.AppendText(" - 거래내역 삭제완료. <상세정보 - " + "삭제한 거래번호:" + key + ">\n")  
        
        self.OnSelectAll(event)
        
        event.Skip()
    
    def OnClear( self, event ):
        self.txtSeriaNo.SetValue("")
        self.txtDate.SetValue("")
        
        self.RadioRevenue.SetValue(False)
        self.RadioExpense.SetValue(False)
        
        self.comboRevenue.SetSelection(0)
        self.comboExpense.SetSelection(0)
        
        self.txtRevenue.SetValue("")
        self.txtExpense.SetValue("")
        
        self.txtRemark.SetValue("")
 
        self.txtWorkHistory.AppendText(" - 출력화면 초기화 완료.\n")  
        
        self.list.DeleteAllItems()
        
        event.Skip()
    
    def OnFind( self, event ):
        self.list.DeleteAllItems()
        rows = HL_CRUD.selectAll()
        
        for row in rows:
            if(row[2] == '수입'):
                self.list.InsertItem(0, str(row[0]))
                self.list.SetItem(0, 1, row[1])
                self.list.SetItem(0, 2, row[2])
                self.list.SetItem(0, 3, row[3])
                self.list.SetItem(0, 4, str(row[4]))
                self.list.SetItem(0, 5, str(row[5]))
                self.list.SetItem(0, 6, row[6])
                
        self.txtWorkHistory.AppendText(" - '수입/지출' 항목이 '수입'인 거래 조회완료.\n")                  
        
        event.Skip()
        
    def OnSelectAll( self, event ):
        self.list.DeleteAllItems()
        rows = HL_CRUD.selectAll()
        
        for row in rows:
            self.list.InsertItem(0, str(row[0]))
            self.list.SetItem(0, 1, row[1])
            self.list.SetItem(0, 2, row[2])
            self.list.SetItem(0, 3, row[3])
            self.list.SetItem(0, 4, str(row[4]))
            self.list.SetItem(0, 5, str(row[5]))
            self.list.SetItem(0, 6, row[6])

        self.txtWorkHistory.AppendText(" - 전체거래 조회완료.\n")     
        
        event.Skip()
 
    def OnSelected( self, event ):
        idx = event.GetIndex()
        
        self.txtSeriaNo.SetValue(self.list.GetItem(idx, 0).GetText())
        
        self.txtDate.SetValue(self.list.GetItem(idx, 1).GetText())

        
        if(self.list.GetItem(idx, 2).GetText() == '수입'):
            self.RadioRevenue.SetValue(True)
            self.RadioExpense.SetValue(False)
            
        elif(self.list.GetItem(idx, 2).GetText() == '지출'):
            self.RadioExpense.SetValue(True)
            self.RadioRevenue.SetValue(False)
        
        
        if('수입' in self.list.GetItem(idx, 3).GetText()):
           self.comboRevenue.SetValue(self.list.GetItem(idx, 3).GetText())
           self.comboExpense.SetSelection(0)
            
        elif('지출' in self.list.GetItem(idx, 3).GetText()):
           self.comboExpense.SetValue(self.list.GetItem(idx, 3).GetText())
           self.comboRevenue.SetSelection(0)

            
        self.txtRevenue.SetValue(self.list.GetItem(idx, 4).GetText())
        
        self.txtExpense.SetValue(self.list.GetItem(idx, 5).GetText())
        
        self.txtRemark.SetValue(self.list.GetItem(idx, 6).GetText())
        
        event.Skip()
        
    def OnPaint( self, event ):
        self.OnSelectAll(event)
                
        i = 0
        getTitle = []
        getExpense = []
        # 조회되는 자료 수 만큼 반복되도록 조건설정.
        while i < self.list.GetItemCount():
            # 데이터 목록에서 5번째 컬럼(비용) 값을 불러와 int타입 변환
            x = int(self.list.GetItem(i,5).GetText())
            # getExpense list에 x 요소 추가
                # 패널에 그래프를 온전히 나타내고자 모든 요소를 1000으로 나눔
            getExpense.append(x/1000)
            
            # getExpense list에 값이 0 혹은 0.0인 요소 제거
            for b in getExpense:
                if(b == 0.0 or 0):
                    getExpense.remove(b)

            # 데이터 목록에서 3번째 컬럼(상세내역) 값을 불러옴                  
            y = self.list.GetItem(i, 3).GetText()
            # getTitle list에 y 요소 추가
            getTitle.append(y)
            
            # 수입 계정과목 종류(대조용) list
            revTitle = ["수입.급여", "수입.상여", "수입.이자", "수입.배당", "수입.사업", "수입.연금", "수입.기타"]
            
            # 만약 getTitle list에서 꺼낸 값이 revTitle list 중에 있다면
            for a in getTitle:
                if(a in revTitle):
                    # 해당 요소를 제거 - '지출'값만 추출하기 위해서.
                    getTitle.remove(a)
                    
               
            # 지출계정과목:지출액을 담을 사전 선언         
            getExpDict = {}
            
            # v는 enumerate()를 활용한 인덱스, k는 getTitle list에서 꺼낸 값
            for v, k in enumerate(getTitle):
                # 변수 val에 getExpense list의 0번 ~ 마지막 까지의 값을 순차적으로 저장
                val = getExpense[v]
                
                # 만약 getExpDict dict에 k(지출계정과목)가 있다면,
                if k in getExpDict:
                    # 키가 k인 밸류에 val 값을 합산하고
                    getExpDict[k] += val
                    
                # 만약 getExpDict dict에 k(지출계정과목)가 없다면,    
                else:
                    # 키카 k인 밸류에 val 값을 대입.
                    getExpDict[k] = val
                        
            i = i + 1
            
            self.graphPanel.SetData(getExpDict)

        self.graphPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ))
        event.Skip()
        
        self.txtWorkHistory.AppendText(" - 전체 기간의 지출현황 집계완료. <상세정보 - 막대그래프로 시각화>\n")     
        
    def OnErase( self, event ):
        self.graphPanel.Destroy()
        self.txtWorkHistory.AppendText(" - 지출현황 지우기 완료.\n")           
        event.Skip()
    
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent = None)
    frame.Show()
    
    app.MainLoop()
    
    pass