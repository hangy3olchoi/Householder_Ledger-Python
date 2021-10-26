'''
Created on 2021. 8. 2.

@author: pc356
'''
from random import randint

import wx
import wx.xrc


class Barchart(wx.Panel):

    def __init__( self, parent ):
        wx.Panel.__init__(self,parent)
        
    def SetData(self, data):
        self.data = data
        self.Bind(wx.EVT_PAINT,self.OnPaint)
        # 중요 - 새로이 그린 내용으로 갱신 
        self.Refresh() #중요 
                
    def OnPaint(self,e):
        dc = wx.PaintDC(self)
        brush = wx.Brush("white")
        dc.SetBackground(brush)
        dc.Clear()
        
        # '지출' 총액 구하기
        total = 0
        for key in self.data:
            total += self.data[key]
            
        x = 0
        percent = 0
        #############################
        for key in self.data:
            # 그래프 색상 랜덤 변경을 위한 randint()사용
            r = randint(1, 255)
            g = randint(1, 255)
            g = randint(1, 255)
            # 반복 시 마다 r, g, b값이 명확히 달라지게 소수를 곱함
            dc.SetBrush(wx.Brush(wx.Colour(r*3,g*5,g*7)))
            
            # '지출' 총액 표시
            dc.DrawText("지출 총 금액: "+str(total)+"천원", 660, 20)
            
            # 그래프의 구분 표시
            dc.DrawText("계정과목:", 10, 270)                            
            dc.DrawText("지출금액:", 10, 300)
            dc.DrawText("비  율:", 10, 330)              
            
            # (좌측상단x, 좌측상단y, 사각형의가로, 사각형의세로)
            dc.DrawRectangle((80+(x*85)),260-self.data[key], 30, self.data[key])
            
            # 키(지출계정과목) 텍스트로 나타 냄 - (텍스트, 좌측상단x, 좌측상단y)    
            dc.DrawText(key, (70+(x*85)), 270)             
            
            # 데이터의 값을 텍스트로 나타 냄 - (텍스트, 좌측상단x, 좌측상단y)
            dc.DrawText(str(self.data[key])+"천원", (70+(x*85)), 300)        
            
            # '지출' 총액 대비 비율 표시
            percent = int((self.data[key]/total)*100)
            dc.DrawText("약 "+str(percent)+"%", (70+(x*85)), 330)               
            
            # 반복 시 마다 그래프 간격설정을 위한 변수
            x += 1
            
            
        #############################
        # dc.DrawText(str(total),0, 0)
                  
        pass
    
    def __del__( self ):
        pass  