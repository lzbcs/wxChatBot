bind = '127.0.0.1:8000' #gunicorn监控的接口
workers = 4 #进程数
threads = 4 #每个进程开启的线程数
proc_name = 'app'
pidfile = './app.pid' #gunicorn进程id，kill掉该文件的id，gunicorn就停止
loglevel = 'debug'
logfile = './log/debug.log' #debug日志
errorlog = './log/error.log' #错误信息日志
timeout = 90
daemon = 'true'
keepalive = 75 # needs to be longer than the ELB idle timeout
worker_class = 'gevent'
