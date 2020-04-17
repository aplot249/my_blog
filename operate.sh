#!/usr/bin/env bash
#
if [ $1 = 'start' ];then
    cd /home/my_blog
    service nginx restart && service redis-server restart && uwsgi --ini uwsgi.ini
elif [ $1 = 'stop' ];then
    cd /home/my_blog
    uwsgi --stop uwsgi.pid
    rm -rf uwsgi.pid uwsgi.log
    rm -rf ../*log
    #supervisorctl stop all
    ps aux | grep uwsgi |awk '{print$2}' | xargs kill -9
    ps aux | grep celery |awk '{print$2}' | xargs kill -9
    ps aux | grep python3 |awk '{print$2}' | xargs kill -9
    ps aux|head -1;ps aux|grep -v PID|sort -rn -k +4|head
elif [ $1 = 'restart' ];then
    bash operate.sh stop
    bash operate.sh start
elif [ $1 = 'update' ];then
    cd /home/my_blog
    bash operate.sh stop
    git pull
    bash operate.sh start
else
    echo "请输入正确指令[start|stop|restart|update]"
fi
