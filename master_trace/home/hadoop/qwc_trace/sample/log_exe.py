import re
import os
import sys
sys.path.append('..')
from conf.env_conf import *

slaves_name = get_slaves_name()

#rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util


def do_refine_iostat(iostatfile, outfile):
    time_count = []
    rrgm = []
    wrgm = []
    rs = []
    ws = []
    rkb = []
    wkb = []
    avgrq = []
    avgqu = []
    await = []
    rawait = []
    wawait = []
    svctm = []
    util = []

    line = iostatfile.readline()

    count = -1

    while line:

        linedata = re.findall(r'[0-9]+\.?[0-9]*',line)
	if linedata and len(linedata) == 13 :

		count = count + 1
		time_count.append(str(count))
		rrgm.append(linedata[0])
		wrgm.append(linedata[1])
		rs.append(linedata[2])
		ws.append(linedata[3])
		rkb.append(linedata[4])
		wkb.append(linedata[5])
		avgrq.append(linedata[6])
		avgqu.append(linedata[7])
		await.append(linedata[8])
		rawait.append(linedata[9])
		wawait.append(linedata[10])
		svctm.append(linedata[11])
		util.append(linedata[12])
			

	line = iostatfile.readline()	
	
	
    for i in xrange(0,count):
	    outline = [time_count[i],' ',rrgm[i],' ',wrgm[i],' ',rs[i],' ',ws[i],' ',rkb[i],' ',wkb[i],' ',avgrq[i],' ',avgqu[i],' ',await[i],' ',rawait[i],' ',wawait[i],' ',svctm[i],' ',util[i],'\n']
	    outfile.writelines(outline)	


def do_refine_mpstat(mpfile, outfile):
    time_stp_all = []
    user_all = []
    nice_all = []
    sys_all = []
    iowait_all = []
    irq_all = []
    soft_all = []
    steal_all = []
    guest_all = []
    gnice_all = []
    idle_all = []
    line = mpfile.readline()
    line_num = 1
    count = -1
    while line:
        if line_num %7 == 4 and line_num < 10000: # ALL
            line_list = line.split()
            time_stp_all.append(str(count+1))
            user_all.append(line_list[2])
            nice_all.append(line_list[3])
            sys_all.append(line_list[4])
            iowait_all.append(line_list[5])
            irq_all.append(line_list[6])
            soft_all.append(line_list[7])
            steal_all.append(line_list[8])
            guest_all.append(line_list[9])
            gnice_all.append(line_list[10])
            idle_all.append(line_list[11])
            count = count + 1
        line_num = line_num + 1
        line = mpfile.readline()

    for i in xrange(0,count):
        outline = [time_stp_all[i],' ',user_all[i],' ',nice_all[i],' ',sys_all[i],' ',iowait_all[i],' ',irq_all[i],' ',soft_all[i],' ',steal_all[i],' ',guest_all[i],' ',gnice_all[i],' ',idle_all[i],'\n']
        
        outfile.writelines(outline)


def do_refine_sar(sarfile, outfile):
    time_stp_all = []
    rxkb_all = []
    txkb_all = []
    ifutil_all = []
    line = sarfile.readline().split()
    line_num = 1
    count = -1
    for line in sarfile:
        line = line.split()
        if line and line[1] == 'eth1' : # eth0
            time_stp_all.append(str(count+1))
            rxkb_all.append(line[4])
            txkb_all.append(line[5])
            ifutil_all.append(line[9])
            count = count + 1
        line_num = line_num + 1
        #line = sarfile.readline().split()
    for i in xrange(0,count):
        outline = [time_stp_all[i],' ',rxkb_all[i],' ',txkb_all[i],' ',ifutil_all[i],'\n']
        outfile.writelines(outline)

iostatfile = open("iostat_log_master","r")
outfile = open("out_log/iostat_out_master","w")
do_refine_iostat(iostatfile,outfile)
iostatfile.close()
outfile.close()

mpstatfile = open("mpstat_log_master","r")
outfile = open("out_log/mpstat_out_master","w")
do_refine_mpstat(mpstatfile, outfile)
mpstatfile.close()
outfile.close()

sarfile = open("sar_log_master","r")
outfile = open("out_log/sar_out_master","w")
do_refine_sar(sarfile, outfile)
sarfile.close()
outfile.close()

for slave in slaves_name:
    iostatfile = open("iostat_log_"+slave,"r")
    outfile = open("out_log/iostat_out_"+slave,"w")
    do_refine_iostat(iostatfile,outfile)
    iostatfile.close()
    outfile.close()

    mpstatfile = open("mpstat_log_"+slave,"r")
    outfile = open("out_log/mpstat_out_"+slave,"w")
    do_refine_mpstat(mpstatfile,outfile)
    mpstatfile.close()
    outfile.close()

    sarfile = open("sar_log_"+slave,"r")
    outfile = open("out_log/sar_out_"+slave,"w")
    do_refine_sar(sarfile, outfile)
    sarfile.close()
    outfile.close()



