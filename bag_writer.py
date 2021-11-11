#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rosbag
from novatel_oem7_msgs.msg import RXSTATUS
import random
import time

class message_rxstatus():

    def __init__(self):

        self.prepare_msg()
        self.seq = 0

    def open_bag(self):

        self.bag = rosbag.Bag("/home/capoom/catkin_ws/src/gnss_error/scripts/deneme.bag","w")

        for topic, msg, t in self.bag.read_messages(topics=["/novatel/oem7/bestpos"]):
            
          self.bag.write("/novatel/oem7/bestpos",msg)
          
          

    def close_bag(self):

        self.bag.close()
        self.seq = 0

    def write(self, list_of_checked):
        
        self.set_msg(list_of_checked)
        self.bag.write("/novatel/oem7/rxstatus", self.msg)
        self.bag.write("/novatel/oem7/bestpos", self.bestposmsg)
        self.seq += 1



    def set_msg(self,list_of_checked):
        
        
        checkbox_names = ['DRAM', 'Invalid FW', 'ROM', 'ESN Access', 'AuthCode', 'Supply Voltage', 'Temperature', 'MINOS', 'PLL RF', 'NVM', 'Software resource limit exceeded', 'Model invalid for this receiver', 'Remote loading has begun', 'Export restriction', 'Safe Mode', 'Component hardware failure', 'Voltage Supply', 'Primary antenna not powered', 'LNA Failure', 'Primary antenna open circuit', 'Primary antenna short circuit', 'COM port tx buffer overrun', 'Jammer detected', 'IMU communication failure', 'Throttled Ethernet Reception', 'Ethernet not connected', 'IMU measurement outlier detected', 'Secondary antenna not powered', 'Secondary antenna open circuit', 'Secondary antenna short circuit', '<60% of available satellites are tracked well', '<15% of available satellites are tracked well', 'No TerraStar Subscription']


        self.msg.error_strs = []
        self.msg.rxstat_strs = []
        self.msg.aux1_stat_strs = []
        self.msg.aux2_stat_strs = []
        self.msg.aux3_stat_strs = []
        self.msg.aux4_stat_strs = []
         
        for check in list_of_checked:
          if(check<=15):
            self.msg.error_strs.append(checkbox_names[check]) 
          elif(check>=16 and check <=23):
            self.msg.rxstat_strs.append(checkbox_names[check])
          elif(check>=24 and check <=26):
            self.msg.aux1_stat_strs.append(checkbox_names[check])
          elif(check>=27 and check <=29):
            self.msg.aux2_stat_strs.append(checkbox_names[check])
          elif(check>=30 and check <=32):
            self.msg.aux4_stat_strs.append(checkbox_names[check])
        
        self.msg.header.seq = self.seq
        self.msg.header.stamp.secs = time.time()

        self.bestposmsg.lat_stdev = random.random()
        self.bestposmsg.lon_stdev = random.random()


    def prepare_msg(self):
        """
        self.msg = RXSTATUS
        
        self.msg.header.seq = 1 
        self.msg.header.stamp.secs = 10 
        self.msg.header.stamp.nsecs = 100 
        self.msg.header.frame_id = "gps"
        self.msg.nov_header.message_name = "RXSTATUS"
        self.msg.nov_header.message_id = 93
        self.msg.nov_header.message_type = 0
        self.msg.nov_header.sequence_number = 0
        self.msg.nov_header.time_status = 180 
        self.msg.nov_header.gps_week_number = 2179 
        self.msg.nov_header.gps_week_milliseconds = 213369057
        self.msg.error = 0 
        self.msg.num_status_codes = 5 

        self.msg.num_status_codes = 5
        self.msg.rxstat = 50331648
        self.msg.rxstat_pri_mask = 0
        self.msg.rxstat_set_mask = 131072
        self.msg.rxstat_clr_mask = 131072
        self.msg.aux1_stat = 128
        self.msg.aux1_stat_pri = 4104
        self.msg.aux1_stat_set = 0
        self.msg.aux1_stat_clr = 0
        self.msg.aux2_stat = 0
        self.msg.aux2_stat_pri = 0
        self.msg.aux2_stat_set = 2147483648
        self.msg.aux2_stat_clr = 0
        self.msg.aux3_stat = 2147483648
        self.msg.aux3_stat_pri = 0
        self.msg.aux3_stat_set = 0
        self.msg.aux3_stat_clr = 0
        self.msg.aux4_stat = 3260416
        self.msg.aux4_stat_pri = 0
        self.msg.aux4_stat_set = 4294967295
        self.msg.aux4_stat_clr = 0
        self.msg.error_bits = []
        self.msg.error_strs = []
        self.msg.rxstat_bits = []
        self.msg.rxstat_strs = []
        self.msg.aux1_stat_bits = []
        self.msg.aux1_stat_strs = []
        self.msg.aux2_stat_bits = []
        self.msg.aux2_stat_strs = []
        self.msg.aux3_stat_bits = []
        self.msg.aux3_stat_strs = []
        self.msg.aux4_stat_bits = []
        self.msg.aux4_stat_strs = []
        """
        #return self.msg
        
        self.bagsss = rosbag.Bag("/home/capoom/catkin_ws/src/gnss_error/scripts/test.bag")
        for topic, msg, t in self.bagsss.read_messages(topics=["/novatel/oem7/rxstatus","/novatel/oem7/bestpos"]):
            if(topic == "/novatel/oem7/rxstatus"):
                self.msg = msg
            elif(topic == "/novatel/oem7/bestpos"):
                self.bestposmsg = msg


    def define_errors(self):

        error_list = ["DRAM", "Invalid FW", "ROM", "", "ESN Access", "AuthCode", "", "Supply Voltage", "", "Temperature", "MINOS", "PLL RF", "", "", "", "NVM", "Software resource limit exceeded",
      "Model invalid for this receiver", "", "", "Remote loading has begun", "Export restriction", "Safe Mode", "", "", "",
      "",
      "",
      "",
      "",
      "",
      "Component hardware failure"]

        status_list = ["","Temperature",
      "Voltage Supply",
      "Primary antenna not powered",
      "LNA Failure",
      "Primary antenna open circuit",
      "Primary antenna short circuit",
      "CPU overload",
      "COM port tx buffer overrun",
      "",
      "",
      "Link overrun",
      "Input overrun",
      "Aux transmit overrun",
      "Antenna gain out of range",
      "Jammer detected",
      "INS reset",
      "IMU communication failure",
      "GPS almanac invalid",
      "Position solution invalid",
      "Position fixed",
      "Clock steering disabled",
      "Clock model invalid",
      "External oscillator locked",
      "Software resource warning",
      "",
      "Interpret Status/Error Bits as Oem7 format",
      "Tracking mode: HDR",
      "Digital filtering enabled",
      "Aux3 event",
      "Aux2 event",
      "Aux1 event"]

        aux1_list = ["Jammer detected on RF1",
    "Jammer detected on RF2",
    "Jammer detected on RF3",
    "Position averaging On",
    "Jammer detected on RF4",
    "Jammer detected on RF5",
    "Jammer detected on RF6",
    "USB not connected",
    "USB1 buffer overrun",
    "USB2 buffer overrun",
    "USB3 buffer overrun",
    "",
    "Profile Activation Error",
    "Throttled Ethernet Reception",
    "",
    "",
    "",
    "",
    "Ethernet not connected",
    "ICOM1 buffer overrun",
    "ICOM2 buffer overrun",
    "ICOM3 buffer overrun",
    "NCOM1 buffer overrun",
    "NCOM2 buffer overrun",
    "NCOM3 buffer overrun",
    "",
    "",
    "",
    "",
    "",
    "",
    "IMU measurement outlier detected"]

        aux2_list = [ "SPI Communication Failure",
    "I2C Communication Failure",
    "COM4 buffer overrun",
    "COM5 buffer overrun",
    "",
    "",
    "",
    "",
    "",
    "COM1 buffer overrun",
    "COM2 buffer overrun",
    "COM3 buffer overrun",
    "PLL RF1 unlock",
    "PLL RF2 unlock",
    "PLL RF3 unlock",
    "PLL RF4 unlock",
    "PLL RF5 unlock",
    "PLL RF6 unlock",
    "CCOM1 buffer overrun",
    "CCOM2 buffer overrun",
    "CCOM3 buffer overrun",
    "CCOM4 buffer overrun",
    "CCOM5 buffer overrun",
    "CCOM6 buffer overrun",
    "ICOM4 buffer overrun",
    "ICOM5 buffer overrun",
    "ICOM6 buffer overrun",
    "ICOM7 buffer overrun",
    "Secondary antenna not powered",
    "Secondary antenna open circuit",
    "Secondary antenna short circuit",
    "Reset loop detected"]

        aux3_list = ["SCOM buffer overrun",
    "WCOM1 buffer overrun",
    "FILE buffer overrun",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "Web content is corrupt or does not exist",
    "RF Calibration Data is present and in error",
    "RF Calibration data exists and has no errors"]

        aux4_list = ["<60% of available satellites are tracked well",
    "<15% of available satellites are tracked well",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "Clock freewheeling due to bad position integrity",
    "",
    "Usable RTK Corrections: < 60%",
    "Usable RTK Corrections: < 15%",
    "Bad RTK Geometry",
    "",
    "",
    "Long RTK Baseline",
    "Poor RTK COM link",
    "Poor ALIGN COM link",
    "GLIDE Not Active",
    "Bad PDP Geometry",
    "No TerraStar Subscription",
    "",
    "",
    "",
    "Bad PPP Geometry",
    "",
    "No INS Alignment",
    "INS not converged"]

        self.words_dict = {"error_list":error_list,"status_list":status_list, "aux1_list":aux1_list, "aux2_list":aux2_list,
                            "aux3_list":aux3_list, "aux4_list":aux4_list}

"""
header: 
  seq: 24
  stamp: 
    secs: 1634037351
    nsecs:  11455450
  frame_id: "gps"
nov_header: 
  message_name: "RXSTATUS"
  message_id: 93
  message_type: 0
  sequence_number: 0
  time_status: 180
  gps_week_number: 2179
  gps_week_milliseconds: 213369057
error: 0
num_status_codes: 5
rxstat: 50331648
rxstat_pri_mask: 0
rxstat_set_mask: 131072
rxstat_clr_mask: 131072
aux1_stat: 128
aux1_stat_pri: 4104
aux1_stat_set: 0
aux1_stat_clr: 0
aux2_stat: 0
aux2_stat_pri: 0
aux2_stat_set: 2147483648
aux2_stat_clr: 0
aux3_stat: 2147483648
aux3_stat_pri: 0
aux3_stat_set: 0
aux3_stat_clr: 0
aux4_stat: 3260416
aux4_stat_pri: 0
aux4_stat_set: 4294967295
aux4_stat_clr: 0
error_bits: []
error_strs: []
rxstat_bits: [24, 25]
rxstat_strs: [Interpret Status/Error Bits as Oem7 format]
aux1_stat_bits: [7]
aux1_stat_strs: [USB not connected]
aux2_stat_bits: []
aux2_stat_strs: []
aux3_stat_bits: [31]
aux3_stat_strs: [RF Calibration data exists and has no errors]
aux4_stat_bits: [14, 15, 16, 20, 21]
aux4_stat_strs: ['Usable RTK Corrections: < 60%', 'Usable RTK Corrections: < 15%', Bad RTK Geometry,
  Poor RTK COM link, Poor ALIGN COM link]
"""