#/bin/bash

######################  CLEAN WORK ###########################
python ./clean_all.py


##################### Time Alignment ##########################
python get_time_alignment_deviation.py


####################### Start Sample ############################

cd sample
python samp_run.py $2
python instru_run.py

###################### start app ################################
echo 'Starting APP:'
echo $1

if [ $1 == 'pagerank' ]; then

	echo 'pagerank' >> analysis/app_info
	echo `date +%s`
	~/hibench/HiBench-master/bin/workloads/websearch/pagerank/spark/run.sh
	echo `date +%s`
elif [ $1 == 'terasort' ]; then

	echo 'terasort' >> analysis/app_info
	echo `date +%s`
	~/hibench/HiBench-master/bin/workloads/micro/terasort/spark/run.sh	
	echo `date +%s`

elif [ $1 == 'bayes' ]; then

	echo 'bayes' >> analysis/app_info
	echo `date +%s`
	~/hibench/HiBench-master/bin/workloads/ml/bayes/spark/run.sh	
	echo `date +%s`

elif [ $1 == 'als' ]; then

	echo 'als' >> analysis/app_info
        echo `date +%s`	
	~/hibench/HiBench-master/bin/workloads/ml/als/spark/run.sh
	echo `date +%s`



elif [ $1 == 'test0' ]; then

	echo 'test' >> analysis/app_info 
	echo `date +%s`
	spark-submit --master spark://master:7077 --deploy-mode client  WordCount7.jar Norm_test_data
	echo `date +%s`

elif [ $1 == 'test1' ]; then
	
	echo 'test' >> analysis/app_info
	echo `date +%s`
	spark-submit --master spark://master:7077 --deploy-mode client  WordCount7.jar Norm_test_data
	echo `date +%s`

else
	echo "Unknow app"
	exit

fi
####################### Stop Instrumen ##################################

python instru_stop.py
cd ..

####################### Get Logs ##################################

#exit

cp $SPARK_HOME/tsee_log/app* log/app

python get_trace_log.py

cd sample
python get_logs.py

####################### ANALYSIS #################################
python sample/log_exe.py
cd ../analysis
python engine.py
python decode_dot.py
python do_straggler.py
cd ..
python merge.py
#for ((i=1;i<6;i++))
#do
#	ssh -p 22 hadoop@slave$i 'cd ~/qwc_trace;./run_instrument.sh'&
#done&
