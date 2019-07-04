import os
import sys
sys.path.append('..')
from conf.env_conf import *

slaves_name = get_slaves_name()
user = get_user()

os.system("rm tracelog_*")
os.system("rm task_tracelog_*")

os.system("rm trace*")

os.system("cd sample")
os.system("python ./clean_sample_log.py")
os.system("cd ..")

os.system("rm log/app*")

os.system("rm $SPARK_HOME/tsee_log/app*")

os.system("rm analysis/app_info")
os.system("rm analysis/app_task")
os.system("rm analysis/app_straggler")

os.system("rm analysis/straggler_stack")
os.system("rm straggler_stack")

os.system("rm analysis/atree.dot")
os.system("rm atree.dot")



for slave in slaves_name:
    os.system("ssh -p 22 "+user+"@"+slave+" \'cd "+slave_path+";rm tracelog; rm task_tracelog\'")