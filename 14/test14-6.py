import socket, select

s = socket.socket()
#host = socket.gethostname()
#print host
port = 1234
host="127.0.0.1"
s.bind((host,port))

s.listen(5)
inputs = [s]
while True:
    rs,ws,es = select.select(inputs,[],[])
    for w in ws:
        print w
    for w in es:
        print e
    
    for r in rs:
        print r
        print s
        if r is s:
            c,addr = s.accept()
            print "Got connection from ",addr
            c.send("thank you for your connecting")
            inputs.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True

            if disconnected:
               print r.getpeername(),'disconnected'
               inputs.remove(r)
            else:
                print r.getpeername(),':',data
                #print data
