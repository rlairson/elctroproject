import os 
import glob
import time

os.system('modprobe w1-gpio') 
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/' 
device_folder1 = glob.glob(base_dir + '28-02131ae0b0aa')[0]
device_folder2 = glob.glob(base_dir + '28-02131ba7bfaa')[0]
device_file1 = device_folder1 + '/w1_slave'
device_file2 = device_folder2 + '/w1_slave'

def read_temp_raw1():
    f = open(device_file1, 'r')
    lines1 = f.readlines()
    f.close()
    return lines1
 

def read_temp1(scale):
     lines1 = read_temp_raw1()
     while lines1[0].strip()[-3:] != 'YES':
          time.sleep(0.2)
          lines1 = read_temp_raw1() 
     equals_pos = lines1[1].find('t=') 
     if equals_pos != -1:
          temp_string = lines1[1][equals_pos+2:] 
          temp_c = float(temp_string) / 1000.0 
          temp_f = temp_c * 9.0 / 5.0 + 32.0 
          if scale == "F":
               return "{:.1f}".format(temp_f)
          if scale =="C":
               return "{:.1f}".format(temp_c)     
          else:
               return temp_c, temp_f

def read_temp_raw2():
    f = open(device_file2, 'r')
    lines2 = f.readlines()
    f.close()
    return lines2
 

def read_temp2(scale):
     lines2 = read_temp_raw2()
     while lines2[0].strip()[-3:] != 'YES':
          time.sleep(0.2)
          lines2 = read_temp_raw2() 
     equals_pos = lines2[1].find('t=') 
     if equals_pos != -1:
          temp_string = lines2[1][equals_pos+2:] 
          temp_c = float(temp_string) / 1000.0 
          temp_f = temp_c * 9.0 / 5.0 + 32.0 
          if scale == "F":
               return "{:.1f}".format(temp_f)
          if scale =="C":
               return "{:.1f}".format(temp_c)     
          else:
               return temp_c, temp_f

while True:
     print("temperature probe #1(C, F):" + str(read_temp1("")))
     print("temperature probe #2(C, F):" + str(read_temp2("")))
     time.sleep(1)
     os.system('clear')
     time.sleep(3)
