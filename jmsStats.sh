#!/bin/bash
# Purpose: To collect JMS connection stats
# Cron :
#   */5 1-3 * * * cd /prod/ptowdoa1/container/home; sh jmsStats.sh

DATE=`date '+%Y-%m-%d'`
export PATH=$PATH:/prod/binaries/weblogic/WL1036/wlserver_10.3.6/common/bin

logfile="jms_connection_"`hostname`"_$DATE.txt"

echo "********************" `date` "********************" >> $logfile 2<&1
wlst.sh jmsConn.py >> $logfile 2<&1
