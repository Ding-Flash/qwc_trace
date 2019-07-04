############################################
Spark程序插桩分析工具 0.1
祁未晨 2018/03/13
############################################ 

使用前须知：
本工具适用于Spark Standalone集群模式的程序性能分析，包括算子执行轨迹回现以及Straggler任务主因检测
使用前请确保如下配置：
所有脚本和程序中的节点名称、节点ip请自行调整
master_trace文件内容解压于Spark集群主节点任意路径下
slave_trace文件内容解压与Spark集群从节点相同路径下
调整日志采集脚本中的相应路径
参考示例配置Spark-default.conf、spark-evn.sh两个Spark脚本文件
请自行调整run_analysis.sh脚本中你的Spark测试程序路径

主要文件说明：

1、master_trace

根目录下：
run_analysis.sh为spark程序提交脚本，使用后自行进行spark程序的性能分析
get_trace_log.sh为日志收集脚本
merge.py为算子事件处理脚本
路径下有三个WordCount测试程序，具体实现稍有不同
atree.dot为目标程序分析时生成的决策树
master.btm为主节点Driver进程的插桩探针文件
straggler_stack为straggler主因分析中间输出结果
op_data为算子轨迹数据文件
task_data为瓶颈任务分析结果数据文件

analysis目录下：
engine.py为任务事件主要分析程序
decision_tree.py为决策树训练程序
decode.py为决策树解码以及右枝分析算法实现程序
do_straggler.py为straggler主因数据处理程序

sample目录下：
get_logs.sh为日志收集脚本
log_exe.py为日志数据预处理脚本
clean_sample_log.py为日志清理脚本
out_log路径下保存处理过后的日志


2、slave_trace

slave_trace.btm为从节点探针文件
run_instrument.sh为动态插桩脚本（不用）


############################################
祁未晨 2018/03/13
############################################