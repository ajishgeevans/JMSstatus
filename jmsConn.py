## JMS Connection status
username="system"
password="admin123"
url="t3://ptowdoa1.lit.gxsonline.net:7002"
servernames=['BKNDApp1', 'BKNDApp2']
def conn():

	try:
		connect(username,password,url)
	except:
		traceback.print_exc(file=sys.stdout)
		System.out.println("ERROR:Unable to find admin server...")
		exit (exitcode=2) 
		
def connectionsList():
    domainRuntime()
    for server in servernames:
     HOST=[]
     print server
     jmsRunBean=getMBean('ServerRuntimes/'+server)
     jmsConnBean=getMBean('ServerRuntimes/'+server+'/JMSRuntime/'+jmsRunBean.getJMSRuntime().getName())
     for conn in jmsConnBean.getConnections(): 
      connbean=getMBean('ServerRuntimes/'+server+'/JMSRuntime/'+jmsRunBean.getJMSRuntime().getName()+'/Connections/'+conn.getName()) 
      try:
       hostAddr=connbean.getHostAddress() 
       session=connbean.getSessionsCurrentCount()
       hostnsession= str(hostAddr) +":"+ str(session)
       HOST.append(hostnsession)
      except:
       print "caught exception"
     print HOST
      
 
conn()
connectionsList()
