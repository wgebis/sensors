#!/bin/bash 

SYS_DATE=`date +%d.%m.%Y`
EBUS_DATE=`ebusctl read -f -c 470 Date`

if [ "$SYS_DATE" != "$EBUS_DATE" ] ; then
   ebusctl write -c 470 Date $SYS_DATE
fi

SYS_TIME=`env TZ="Europe/Warsaw" date +%H:%M:%S`
EBUS_TIME=`ebusctl read -f -c 470 Time`

if [ `dateutils.ddiff $EBUS_TIME $SYS_TIME -f %S` -gt 10 ] ; then
   ebusctl write -c 470 Time $SYS_TIME
fi
