# workserver.py - simple HTTP server with a do_work / stop_work API
# GET /do_work activates a worker thread which uses CPU
# GET /stop_work signals worker thread to stop
import math
import socket
import threading
import time

from bottle import route, run

hostname = socket.gethostname()
hostport = 80
keepworking = False  # boolean to switch worker thread on or off


# thread which maximizes CPU usage while the keepWorking global is True
def workerthread():
    # outer loop to run while waiting
    while (True):
        # main loop to thrash the CPI
        while (keepworking == True):
            for x in range(200, 500):
                math.factorial(x)
        time.sleep(3)


# start the worker thread
worker_thread = threading.Thread(target=workerthread, args=())
worker_thread.start()


def writebody():
   # body = '<html><head><title>Work interface - build</title></head>'
   # body += '<body><h2>Worker interface on ' + hostname + '</h2><ul><h3>'
    body = '<html><head><title>Work interface - build</title></head>'
    body += '<body><h2>Hello World, I am one of the Virtual Machine my name is:' + hostname + '</h2><ul><h3>'

    if keepworking == False:
        body += '<br/>Worker thread is not running. <a href="./start_work">Start work</a><br/>'
    else:
        body += '<br/>Worker thread is running. <a href="./stop_work">Stop work</a><br/>'

    body += '<br/>Usage:<br/><br/>/start_work = start worker thread<br/>/stop_work = stop worker thread<br/>'
    body += '</h3></ul></body></html>'
    return body


@route('/')
def root():
    return writebody()


@route('/start_work')
def start_work():
    global keepworking
    # start worker thread
    keepworking = True
    return writebody()


@route('/stop_work')
def stop_work():
    global keepworking
    # stop worker thread
    keepworking = False
    return writebody()


run(host=hostname, port=hostport)
