#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy

import wx
import wx.xrc
import wx.adv
from bag_writer import message_rxstatus

class MyFrame(wx.Frame):
    
    def __init__(self, parent):

        super(MyFrame, self).__init__ ( parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 813,712 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.bag_writer = message_rxstatus()

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        gSizer1 = wx.GridSizer( 0, 4, 0, 0 )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button1, 0, wx.ALL, 5 )


        self.checkbox_dict = {}
        checkbox_names = ['DRAM', 'Invalid FW', 'ROM', 'ESN Access', 'AuthCode', 'Supply Voltage', 'Temperature', 'MINOS', 'PLL RF', 'NVM', 'Software resource limit exceeded', 'Model invalid for this receiver', 'Remote loading has begun', 'Export restriction', 'Safe Mode', 'Component hardware failure', 'Voltage Supply', 'Primary antenna not powered', 'LNA Failure', 'Primary antenna open circuit', 'Primary antenna short circuit', 'COM port tx buffer overrun', 'Jammer detected', 'IMU communication failure', 'Throttled Ethernet Reception', 'Ethernet not connected', 'IMU measurement outlier detected', 'Secondary antenna not powered', 'Secondary antenna open circuit', 'Secondary antenna short circuit', '<60% of available satellites are tracked well', '<15% of available satellites are tracked well', 'No TerraStar Subscription']
        i = 0
        for checkbox_name in checkbox_names:
            
            self.checkbox_dict[i] = wx.CheckBox(self, wx.ID_ANY, checkbox_name, wx.DefaultPosition, wx.DefaultSize, 0)
            gSizer1.Add(self.checkbox_dict[i], 0, wx.ALL, 5)
            i += 1
       

        self.SetSizer(gSizer1)
        self.Layout()
        
        self.Centre( wx.BOTH )

        self.Show()

        self.Bind(wx.EVT_BUTTON, self.clicked)
        self.Bind(wx.EVT_CHECKBOX, self.check)

        self.button_status = False



    def clicked(self, event):
        self.button_status = not self.button_status
        if(self.button_status == True):
            self.bag_writer.open_bag()
        elif(self.button_status == False):
            self.bag_writer.close_bag()




    def check(self, event):
        list_of_true = []
        for checkbox_name in self.checkbox_dict.keys():
            if(self.checkbox_dict[checkbox_name].GetValue() == True):
                list_of_true.append(checkbox_name)

        print(list_of_true)
        self.bag_writer.write(list_of_true)



if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None)
    app.MainLoop()