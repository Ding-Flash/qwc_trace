import os
import sys
sys.path.append('..')
from conf.env_conf import *

slaves_name = get_slaves_name()
user = get_user()

os.system("rm iostat_log_m*&")
os.system("rm iostat_log_s*&")
os.system("rm out_log/iostat_out_*&")
os.system("rm mpstat_log_master&")
os.system("rm mpstat_log_s*&")
os.system("rm out_log/mpstat_out_*&")
os.system("rm sar_log_master&")
os.system("rm sar_log_s*&")
os.system("rm out_log/sar_out_*&")

for slave in slaves_name:
    os.system("ssh "+user+"@"+slave+" \"rm "+slave_path+"/sample/iostat_log_"+slave+"&\"")

for slave in slaves_name:
    os.system("ssh "+user+"@"+slave+" \"rm "+slave_path+"/sample/mpstat_log_"+slave+"&\"")

for slave in slaves_name:
    os.system("ssh "+user+"@"+slave+" \"rm "+slave_path+"/sample/sar_log_"+slave+"&\"")
