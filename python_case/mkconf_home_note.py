#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os

#confPaht  = "/data/tools/nagios/etc/servers/"
confPaht  = "/home/sysop/python/nagios_server/"
confGlobal = """
define service{
        name                            u17-service
        active_checks_enabled           1
        passive_checks_enabled          1
        parallelize_check               1
        obsess_over_service             1
        check_freshness                 0
        notifications_enabled           1
        event_handler_enabled           1
        flap_detection_enabled          1
        process_perf_data               1
        retain_status_information       1
        retain_nonstatus_information    1
        is_volatile                     0
        check_period                    24x7
        contact_groups                  admins
        notification_options            w,u,c,r
        notification_interval           60
        notification_period             24x7
        register                        0
        check_interval                  30
        retry_interval                  1
        max_check_attempts              4
        normal_check_interval           1
        retry_check_interval            1
        register                        0
        }

define host{
        name                            u17-host
        notifications_enabled           1
        event_handler_enabled           1
        flap_detection_enabled          1
        process_perf_data               1
        retain_status_information       1
        retain_nonstatus_information    1
        notification_period             24x7
        register                        0
        check_period                    24x7
        check_interval                  5
        retry_interval                  1
        max_check_attempts              10
        check_command                   check-host-alive
        notification_period             workhours
        notification_interval           120
        notification_options            d,u,r
        contact_groups                  admins
        register                        0
        }

define contact{						
        name                            u17-contact        
        service_notification_period     24x7                   
        host_notification_period        24x7                   
        service_notification_options    w,u,c,r,f,s        
        host_notification_options       d,u,r,f,s 
        service_notification_commands   u17-notify-service-by-email,u17-notify-service-by-sms
        host_notification_commands      u17-notify-host-by-email,u17-notify-host-by-sms
        register                        0                      
        }

define contact{
        contact_name                    mzg
        use                             u17-contact     
        alias                           mzg-contact
        email                           muzonggui@u17.com
        pager                           13581670176
        }

define contact{
        contact_name                    wj
        use                             u17-contact
        alias                           wj-contact
        email                           wangjun@u17.com
        pager                           13581557353
        }

define contact{
        contact_name                    gyf
        use                             u17-contact
        alias                           gyf-contact
        email                           gaoyanfei@u17.com
        pager                           13901033841
        }

define contact{
        contact_name                    yxh
        use                             u17-contact
        alias                           yxh-contact
        email                           yuxianghua@u17.com
        pager                           13466686010
        }

define contact{
        contact_name                    sjg
        use                             u17-contact
        alias                           sjg-contact
        email                           shuaijianguo@u17.com
        pager                           15011390610
        }

define contact{
        contact_name                    zjl
        use                             u17-contact
        alias                           zjl-contact
        email                           zhujinlong@u17.com
        pager                           18611626520
        }

define contact{
        contact_name                    xy
        use                             u17-contact
        alias                           xy-contact
        email                           xuyu@u17.com
        pager                           18210118839
        }

define contact{
        contact_name                    qh
        use                             u17-contact
        alias                           qh-contact
        email                           qiaohu@u17.com
        pager                           18310424277
        }

define contact{
        contact_name                    xwh
        use                             u17-contact
        alias                           xwh-contact
        email                           xuweihua@u17.com
        pager                           18668099235
        }

define contact{
        contact_name                    zl
        use                             u17-contact
        alias                           zl-contact
        email                           zhaoliang@u17.com
        pager                           13522209896
        }

define contactgroup{ 
        contactgroup_name               managergroup
        alias                           managergroup
        members                         yxh,gyf
        }

define contactgroup{ 
        contactgroup_name               osgroup
        alias                           osgroup
        members                         mzg,gyf,zl
        }

define contactgroup{ 
        contactgroup_name               osdbgroup
        alias                           osdbgroup
        members                         wj,mzg,gyf,zl
        }

define contactgroup{ 
        contactgroup_name              dbgroup
        alias                          dbgroup
        members                        wj,mzg,gyf,zl
        }

define contactgroup{
        contactgroup_name              phpgroup
        alias                          phpgroup
        members                        sjg,xwh
        }

define contactgroup{
        contactgroup_name              javagroup
        alias                          javagroup
        members                        qh
        }

define contactgroup{
        contactgroup_name              golanggroup
        alias                          golanggroup
        members                        xwh,gyf
        }

define command{
        command_name    u17-notify-host-by-email
        command_line    /usr/bin/printf "%b" "***** 报警 *****\\n\\n通知类型: $NOTIFICATIONTYPE$\\n服务器: $HOSTNAME$\\n状态: $HOSTSTATE$\\n地址: $HOSTADDRESS$\\n信息: $HOSTOUTPUT$\\n\\n日期时间: $LONGDATETIME$\\n" | /bin/mail -s "** $NOTIFICATIONTYPE$ 服务器报警: $HOSTNAME$ is $HOSTSTATE$ **" $CONTACTEMAIL$
        }

define command{
        command_name    u17-notify-service-by-email
        command_line    /usr/bin/printf "%b" "***** 报警 *****\\n\\n通知类型: $NOTIFICATIONTYPE$\\n\\n服务: $SERVICEDESC$\\n服务器: $HOSTALIAS$\\n地址: $HOSTADDRESS$\\n状态: $SERVICESTATE$\\n\\n日期时间: $LONGDATETIME$\\n\\n信息:\\n\\n$SERVICEOUTPUT$\\n" | /bin/mail -s "** $NOTIFICATIONTYPE$ 服务报警: $HOSTALIAS$/$SERVICEDESC$ is $SERVICESTATE$ **" $CONTACTEMAIL$
        }

define command{
        command_name    u17-notify-host-by-sms
        command_line    /usr/bin/curl  -L -G --data-urlencode "to=$CONTACTPAGER$" --data-urlencode "msg=服务器报警: $HOSTNAME$ is $HOSTSTATE$, 信息: $HOSTOUTPUT$, 日期时间: $LONGDATETIME$" --data-urlencode "type=sms" "http://10.18.1.253:8088/monitor"
        }

define command{
        command_name    u17-notify-service-by-sms
        command_line    /usr/bin/curl  -L -G --data-urlencode "to=$CONTACTPAGER$" --data-urlencode "msg=服务报警: $HOSTALIAS$/$SERVICEDESC$ is $SERVICESTATE$, 信息: $SERVICEOUTPUT$, 日期时间: $LONGDATETIME$" --data-urlencode "type=sms" "http://10.18.1.253:8088/monitor"
        }

""".strip()

confGroup = """
define hostgroup{
        hostgroup_name  %(groupName)s
        alias           %(groupName)s
        members         %(groupMemberStr)s
        }
""".strip()

confHost = """
define host{
        use                     u17-host
        host_name               %(hostName)s
        alias                   %(hostName)s
        address                 %(hostIp)s
        contact_groups          %(hostContact)s
        }
""".strip()
confService = """
define service{
       use                      u17-service
       host_name                %(hostName)s
       service_description      %(mt)s
       check_command            check_nrpe!%(mt)s
       contact_groups           %(serviceContact)s
}
""".strip()

osMonitor = [
                "check_load",  "check_disk_sda1",    "check_disk_sda3",
                "check_users", "check_procs_zombie", "check_swap",
                "check_crond", "check_procs_total",  "check_snmpd"
            ]

dbMonitor = []
dbs= {'db1':[3302,3303,3304,3305,3306,3307,3308,3309,3310,3311], 'db2':[3302,3303,3304,3305,3306,3307,3308,3309,3310,3311],'db3':[3302,3303,3304,3305,3306,3307,3308,3309,3310,3311], 'db10':[3302,3303,3304,3305,3306,3307,3308,3309,3310,3311],'db11':[3302,3303,3304,3305,3306,3307,3308,3309,3310,3311],'db12':[3302,3303,3304,3305,3306,3307,3308,3309,3310,3311], 'db4':[3301], 'db8':[3301]}
modes_slave = ["uptime", "slave-lag", "slave-io-running", "slave-sql-running", "threads-connected"]
modes_master = ["uptime", "threads-connected"]
for (mysqlhostname, mysqlports) in dbs.items():
    for mysqlprot in mysqlports:
	modes = modes_slave
        if 'db8'==mysqlhostname:
            modes = modes_master
        for mysqlmode in modes:
            dbMonitor.append("check_mysql_%s_%s_%s" %(mysqlhostname, mysqlprot, mysqlmode))


javaHttpMonitor = []
phpHttpMonitor  = []
golangHttpMonitor   = []

javaHttpMonitorBoss = []
phpHttpMonitorBoss  = []

javaMemcacheMonitor = []
phpMemcacheMonitor  = []

javaRedisMonitor = []

phpPortMonitor = []

for host, port in [("php1", 9000), ("php2", 9000)]:
	phpPortMonitor.append("check_tcp_%s_%s" %(host, port))


for httpHost, httpUri in [("wan.u17.com", ""), ("m.u17.com", "")]:
    javaHttpMonitor.append("check_http_web1_%s%s" %(httpHost, httpUri))
    javaHttpMonitor.append("check_http_web2_%s%s" %(httpHost, httpUri))
    javaHttpMonitorBoss.append("check_httpBoss_Web1_%s%s" %(httpHost, httpUri))
    javaHttpMonitorBoss.append("check_httpBoss_Web2_%s%s" %(httpHost, httpUri))

for httpHost, httpIP, httpUri in [("m.u17.com", "java6", "/index.html"),("m.u17.com", "java1", "/index.html"),("op_backend","php1","/xxadmin/login.php")]:
    javaHttpMonitor.append("check_http_%s_%s%s" %(httpIP, httpHost, httpUri))
    #javaHttpMonitorBoss.append("check_httpBoss_%s_%s%s" %(httpIP, httpHost, httpUri))

for httpHost, httpIP, httpUri in [("op_backend","php1","/xxadmin/login.php")]:
    phpHttpMonitor.append("check_http_%s_%s%s" %(httpIP, httpHost, httpUri))

for httpHost, httpIP, httpUri in [("app.u17.com", "db13", "/v3/app/android/phone/comic/checkUpdate")]:
    golangHttpMonitor.append("check_http_golang_%s_%s%s" %(httpIP, httpHost, httpUri))


for host, port in [("php5", 7001), ("share.bj.u17", 7003)]:
    golangHttpMonitor.append("check_tcp_%s_%s" %(host, port))

for httpHost, httpUri in [("www.u17.com", ""), ("www.u17.com", "/comic/11072.html"), ("xiong.ac", ""), ("xiong.ac", "/hh295591"), ("i.u17.com", "")]:
    phpHttpMonitor.append("check_http_web1_%s%s" %(httpHost, httpUri))
    phpHttpMonitor.append("check_http_web2_%s%s" %(httpHost, httpUri))
    phpHttpMonitorBoss.append("check_httpBoss_Web1_%s%s" %(httpHost, httpUri))
    phpHttpMonitorBoss.append("check_httpBoss_Web2_%s%s" %(httpHost, httpUri))

for httpHost, httpUri in [("bbs.u17.com", "")]:
    phpHttpMonitor.append("check_http_web3_%s%s" %(httpHost, httpUri))
    phpHttpMonitorBoss.append("check_httpBoss_Web3_%s%s" %(httpHost, httpUri))

for memcacheHost, memcachePort in [("cache1", 11211), ("cache1", 11212)]:
    phpMemcacheMonitor.append("check_memcache_%s_%s_size"  %(memcacheHost, memcachePort))
    phpMemcacheMonitor.append("check_memcache_%s_%s_time"  %(memcacheHost, memcachePort))
    phpMemcacheMonitor.append("check_memcache_%s_%s_hit"   %(memcacheHost, memcachePort))

for memcacheHost, memcachePort in [("cache1", 11213), ("cache1", 11214)]:
    javaMemcacheMonitor.append("check_memcache_%s_%s_size" %(memcacheHost, memcachePort))
    javaMemcacheMonitor.append("check_memcache_%s_%s_time" %(memcacheHost, memcachePort))
    javaMemcacheMonitor.append("check_memcache_%s_%s_hit"  %(memcacheHost, memcachePort))

for redisHost, redisPort in [("cache1", 6379), ("cache1", 6380)]:
    javaRedisMonitor.append("check_redis_%s_%s_size" %(redisHost, redisPort))


data = { "os" : [
                    { "name"    : "webs",
                      "contact" : ["osgroup"],
                      "member"  : [							
                                      { "name" : "web1.bj.u17",     "ip" : "web1.bj.u17",     "monitor" : [osMonitor],                   "contact" : ["osgroup"] },
                                      { "name" : "web2.bj.u17",     "ip" : "web2.bj.u17",     "monitor" : [osMonitor],                   "contact" : ["osgroup"] },
                                  ],
                    },
                    { "name"    : "phps",
                      "contact" : ["osgroup"],
                      "member"  : [
                                      { "name" : "php1.bj.u17",     "ip" : "php1.bj.u17",     "monitor" : [osMonitor,"check_sersync2"],  "contact" : ["osgroup"] },
                                      { "name" : "php2.bj.u17",     "ip" : "php2.bj.u17",     "monitor" : [osMonitor,"check_sersync2"],  "contact" : ["osgroup"] },
                                      { "name" : "php3.bj.u17",     "ip" : "php3.bj.u17",     "monitor" : [osMonitor],                   "contact" : ["osgroup"] },
                                      { "name" : "php4.bj.u17",     "ip" : "php4.bj.u17",     "monitor" : [osMonitor],                   "contact" : ["osgroup"] },
                                      { "name" : "php5.bj.u17",     "ip" : "php5.bj.u17",     "monitor" : [osMonitor],                   "contact" : ["osgroup"] },
                                      #{ "name" : "php6.bj.u17",     "ip" : "php6.bj.u17",     "monitor" : [osMonitor],                   "contact" : ["osgroup"] },
                                      { "name" : "php7.bj.u17",     "ip" : "php7.bj.u17",     "monitor" : [osMonitor],                   "contact" : ["osgroup"] },
                                      { "name" : "php8.bj.u17",     "ip" : "php8.bj.u17",     "monitor" : [osMonitor],                   "contact" : ["osgroup"] },
                                  ],
                    },
                    { "name"    : "dbs",
                      "contact" : ["osdbgroup"],
                      "member"  : [
                                      { "name" : "db1.bj.u17",      "ip" : "db1.bj.u17",      "monitor" : [osMonitor], "contact" : ["dbgroup"] },
                                      { "name" : "db2.bj.u17",      "ip" : "db2.bj.u17",      "monitor" : [osMonitor], "contact" : ["dbgroup"] },
                                      { "name" : "db3.bj.u17",      "ip" : "db3.bj.u17",      "monitor" : [osMonitor], "contact" : ["dbgroup"] },
                                      { "name" : "db4.bj.u17",      "ip" : "db4.bj.u17",      "monitor" : [osMonitor], "contact" : ["dbgroup"] },
                                      { "name" : "db5.bj.u17",      "ip" : "db5.bj.u17",      "monitor" : [osMonitor], "contact" : ["dbgroup"] },
                                      { "name" : "db6.bj.u17",      "ip" : "db6.bj.u17",      "monitor" : [osMonitor], "contact" : ["dbgroup"] },
                                      { "name" : "db7.bj.u17",      "ip" : "db7.bj.u17",      "monitor" : [osMonitor], "contact" : ["dbgroup"] },
                                      { "name" : "db8.bj.u17",      "ip" : "db8.bj.u17",      "monitor" : [osMonitor], "contact" : ["dbgroup"] },
                                      { "name" : "db9.bj.u17",      "ip" : "db9.bj.u17",      "monitor" : [osMonitor], "contact" : ["dbgroup"] },
                                      { "name" : "db10.bj.u17",     "ip" : "db10.bj.u17",     "monitor" : [osMonitor], "contact" : ["dbgroup"] },
                                      { "name" : "db11.bj.u17",     "ip" : "db11.bj.u17",     "monitor" : [osMonitor], "contact" : ["dbgroup"] },
                                      { "name" : "db12.bj.u17",     "ip" : "db12.bj.u17",     "monitor" : [osMonitor], "contact" : ["dbgroup"] },
                                      { "name" : "db13.bj.u17",     "ip" : "db13.bj.u17",     "monitor" : [osMonitor], "contact" : ["dbgroup"] },
                                  ],
                    },
                    { "name"    : "javas",
                      "contact" : ["osgroup"],
                      "member"  : [
                                      { "name" : "java1.bj.u17",    "ip" : "java1.bj.u17",    "monitor" : [osMonitor], "contact" : ["osgroup"] },
                                      { "name" : "java2.bj.u17",    "ip" : "java2.bj.u17",    "monitor" : [osMonitor], "contact" : ["osgroup"] },
                                      { "name" : "java3.bj.u17",    "ip" : "java3.bj.u17",    "monitor" : [osMonitor], "contact" : ["osgroup"] },
                                      { "name" : "java4.bj.u17",    "ip" : "java4.bj.u17",    "monitor" : [osMonitor], "contact" : ["osgroup"] },
                                      #{ "name" : "java5.bj.u17",    "ip" : "java5.bj.u17",    "monitor" : [osMonitor], "contact" : ["osgroup"] },
                                      { "name" : "java6.bj.u17",    "ip" : "java6.bj.u17",    "monitor" : [osMonitor], "contact" : ["osgroup"] },
                                  ],
                    },
                    { "name"    : "storages",
                      "contact" : ["osgroup"],
                      "member"  : [
                                      { "name" : "storage1.bj.u17", "ip" : "storage1.bj.u17",      "monitor" : [osMonitor], "contact" : ["osgroup"] },
                                      { "name" : "storage2.bj.u17", "ip" : "storage2.bj.u17",      "monitor" : [osMonitor], "contact" : ["osgroup"] },
                                  ],
                    },
                    { "name"    : "monitors",
                      "contact" : ["osgroup"],
                      "member"  : [
                                      { "name" : "monitor1.bj.u17", "ip" : "monitor1.bj.u17",      "monitor" : [osMonitor], "contact" : ["osgroup"] },
                            #          { "name" : "tokyo01", 	    "ip" : "tokyo01", 	           "monitor" : [osMonitor], "contact" : ["osgroup"] },
                            #          { "name" : "hk01", 	    "ip" : "hk01", 	           "monitor" : [osMonitor], "contact" : ["osgroup"] },
                                  ],
                    },
                    { "name"    : "mysqls",
                      "contact" : ["dbgroup"],
                      "member"  : [
                                      {
                                        "name"    : "mysql",
                                        "ip"      : "monitor1.bj.u17",
                                        "contact" : ["osgroup", "dbgroup"],
                                        "monitor" : [dbMonitor],
                                      },
                                  ],
                    },
                    { "name"    : "app",
                      "contact" : ["osgroup"],
                      "member"  : [
                                      {
                                        "name"    : "httpPhp",
                                        "ip"      : "monitor1.bj.u17",
                                        "contact" : ["phpgroup"],
                                        "monitor" : [phpHttpMonitor],
                                      },
                                      {
                                        "name"    : "httpJava",
                                        "ip"      : "monitor1.bj.u17",
                                        "contact" : ["javagroup"],
                                        "monitor" : [javaHttpMonitor],
                                      },
                                      {
                                        "name"    : "httpPhp2Boss",
                                        "ip"      : "monitor1.bj.u17",
                                        "contact" : ["managergroup"],
                                        "monitor" : [phpHttpMonitorBoss],
                                      },
                                      {
                                        "name"    : "httpJava2Boss",
                                        "ip"      : "monitor1.bj.u17",
                                        "contact" : ["managergroup"],
                                        "monitor" : [javaHttpMonitorBoss],
                                      },
                                      {
                                        "name"    : "memcachePhp",
                                        "ip"      : "monitor1.bj.u17",
                                        "contact" : ["osgroup", "phpgroup"],
                                        "monitor" : [phpMemcacheMonitor],
                                      },
                                      {
                                        "name"    : "memcacheJava",
                                        "ip"      : "monitor1.bj.u17",
                                        "contact" : ["osgroup", "javagroup"],
                                        "monitor" : [javaMemcacheMonitor],
                                      },
                                      {
                                        "name"    : "redisJava",
                                        "ip"      : "monitor1.bj.u17",
                                        "contact" : ["osgroup", "javagroup"],
                                        "monitor" : [javaRedisMonitor],
                                      },
                                      {
                                        "name"    : "dnsOs",
                                        "ip"      : "monitor1.bj.u17",
                                        "contact" : ["osgroup"],
                                        "monitor" : ["check_dns_m", "check_dns_s"],
                                      },
                                      {
                                        "name"    : "golandHttp",
                                        "ip"      : "monitor1.bj.u17",
                                        "contact" : ["golanggroup"],
                                        "monitor" : [golangHttpMonitor],
                                      },

                                      {
                                        "name"    : "phpport",
                                        "ip"      : "monitor1.bj.u17",
                                        "contact" : ["golanggroup"],
                                        "monitor" : [phpPortMonitor],
                                      },
                                      {
                                        "name"    : "opBackendHttp",
                                        "ip"      : "monitor1.bj.u17",
                                        "contact" : ["phpgroup"],
                                        "monitor" : [phpHttpMonitor],
                                      },
                                  ],
                    },
               ],
       }



def toConf():
    with open(confPaht + "global.cfg", "w") as f:	#将f做为打开的global.cfg文件的变量
        f.write(confGlobal)							#将global.cfg中定义的字符串写到变量f既global.cfg文件中
    for key in data.keys():							#定义for循环，获取字典data中的键，定义为变量key,key为os
#	print key

#import sys
#sys.exit(0)

	tmp = data[key]								#定义tmp变量，获取os键的值,tmp值为os下对应的所有值
	#	print tmp
	for group in tmp:							#定义for循环，group为os键对应的值以member为一段的开始，name为一段的结尾,既os中对应的一段值而非整个值,如：{'member': [{'ip': 'web1.bj.u17', 'contact': ['osgroup'], 'name': 'web1.bj.u17', 'monitor': [['check_load', 'check_disk_sda1', 'check_disk_sda3', 'check_users', 'check_procs_zombie', 'check_swap', 'check_crond', 'check_procs_total', 'check_snmpd']]}, {'ip': 'web2.bj.u17', 'contact': ['osgroup'], 'name': 'web2.bj.u17', 'monitor': [['check_load', 'check_disk_sda1', 'check_disk_sda3', 'check_users', 'check_procs_zombie', 'check_swap', 'check_crond', 'check_procs_total', 'check_snmpd']]}], 'contact': ['osgroup'], 'name': 'webs'}
			#print group
		groupName       = group["name"]			#groupName值为上段中的webs,不取嵌套内的name值
		groupMember     = group["member"]		#groupMember值为上段中member内的所有值
		groupMemberStr  = ",".join([tmp["name"] for tmp in group["member"]])	#groupMemberStr值为上段中member内的name键对应值，同时以,号分隔，既web1.bj.u17,web2.bj.u17
		groupPath       = confPaht + groupName + ".cfg"	#groupPath为前几行定义的conf文件存放路径加上webs.cfg,既定义主机组的cfg配置文件
		hostContact     = ",".join(group["contact"])	#定义联系人组，值为上段中的contace，既osgroup
		with open(groupPath, "w") as f:					#将f做为打开文件既定义好的主机组的cfg文件(webs.cfg)的变量
			f.write(confGroup %locals() + "\n")			#将confGroup中定义的字符串加上locals意为局部变量写入到变量f既webs.cfg中,到此步，global.cfg及主机组文件webs|phps|dbs等.cfg生成完毕
		for host in groupMember:						#定义for循环，host对应值为data-os-member键的值
			hostName    = host["name"]						#hostName的值为web1.bj.u17 web2.bj.u17
                	hostIp      = host["ip"]
                	hostPath    = confPaht + hostName + ".cfg"
                	hostMonitor = []
                	for m in host["monitor"]:
                		if type(m) is list:
                        		for l in m: hostMonitor.append(l)
                    		else:
                        		hostMonitor.append(m)
                	hostMonitor = list(set(hostMonitor))
	        	serviceContact = ",".join(host["contact"])
                	with open(hostPath, "w") as f:
                   		f.write(confHost %locals() +"\n")
                   		for mt in hostMonitor:
                   			f.write(confService %locals() + "\n")

if __name__ == "__main__":
    os.system("rm -rf /data/tools/nagios/etc/servers/*.cfg")
    toConf()
