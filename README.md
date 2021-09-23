# VmssLbLinuxpython
VM scale set with Load balancer and python webserver

Browse to the website of vm#0 (port 7000), which shows the current backend VM name.

Access Website PublicIP:7000/

To start doing work on the first VM click Start_work.
After a few minutes the VM Scale Set capacity will increase. Note that the first scale out takes longer than subsequent scale outs while the autoscale pipeline gets initialized. 

You can stop doing work by browsing to publicIP:7000/stop_work.

if not in use please stop the process. The python script used in the webserver will sclae in and out within 10 minutes. So if not im use please click stop_work to stop the process.
