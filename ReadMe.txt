############################################
Spark�����׮�������� 0.1
��δ�� 2018/03/13
############################################ 

ʹ��ǰ��֪��
������������Spark Standalone��Ⱥģʽ�ĳ������ܷ�������������ִ�й켣�����Լ�Straggler����������
ʹ��ǰ��ȷ���������ã�
���нű��ͳ����еĽڵ����ơ��ڵ�ip�����е���
master_trace�ļ����ݽ�ѹ��Spark��Ⱥ���ڵ�����·����
slave_trace�ļ����ݽ�ѹ��Spark��Ⱥ�ӽڵ���ͬ·����
������־�ɼ��ű��е���Ӧ·��
�ο�ʾ������Spark-default.conf��spark-evn.sh����Spark�ű��ļ�
�����е���run_analysis.sh�ű������Spark���Գ���·��

��Ҫ�ļ�˵����

1��master_trace

��Ŀ¼�£�
run_analysis.shΪspark�����ύ�ű���ʹ�ú����н���spark��������ܷ���
get_trace_log.shΪ��־�ռ��ű�
merge.pyΪ�����¼�����ű�
·����������WordCount���Գ��򣬾���ʵ�����в�ͬ
atree.dotΪĿ��������ʱ���ɵľ�����
master.btmΪ���ڵ�Driver���̵Ĳ�׮̽���ļ�
straggler_stackΪstraggler��������м�������
op_dataΪ���ӹ켣�����ļ�
task_dataΪƿ�����������������ļ�

analysisĿ¼�£�
engine.pyΪ�����¼���Ҫ��������
decision_tree.pyΪ������ѵ������
decode.pyΪ�����������Լ���֦�����㷨ʵ�ֳ���
do_straggler.pyΪstraggler�������ݴ������

sampleĿ¼�£�
get_logs.shΪ��־�ռ��ű�
log_exe.pyΪ��־����Ԥ����ű�
clean_sample_log.pyΪ��־����ű�
out_log·���±��洦��������־


2��slave_trace

slave_trace.btmΪ�ӽڵ�̽���ļ�
run_instrument.shΪ��̬��׮�ű������ã�


############################################
��δ�� 2018/03/13
############################################