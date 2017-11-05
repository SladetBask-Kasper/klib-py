import socket

# UNCOMMENT "del" IF YOU don't WANNA HAVE VERSION AVAIABLE
SOCK_KLIB_VERSION = "1"
#del SOCK_KLIB_VERSION

class sock:
    class tcp:
        def get():
            return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Send one packet and then close socket. No socket required
        def Send1(ip, port, msg, boolPrint = False):
            if not type(msg) == str:
                print("Send1 INVALID ARGS: (correct) STR INT STR. (your) " + str(type(ip)) + " "  + str(type(port)) + " " + str(type(msg)))
                exit(0)

            if not type(boolPrint) == bool:
                print("WARNING: boolPrint must to be bool (DEFAULTING TO FALSE)")
            elif boolPrint == True:
                print("Sending : " + str(msg))

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            Data = str(msg).encode('utf-8')
            try:
                s.connect((str(ip), int(port)))
            except:
                if boolPrint == True: print("Unable to connect to server...")
                return False

            try:
                s.send(Data)
            except:
                return False

            return True

        def Connect(ip, port, socket):
            try:
                socket.connect((ip, int(port)))
            except:
                return False
            return True

        # Tries To Connect Unitl It Succedes
        def force_connect(ip, port, socket, tries, DEBUGMODE = False):
            x = 0
            while x <= tries:
                try:
                    socket.connect((ip, int(port)))
                    if DEBUGMODE: print(str(x) + " SUCCESS CONNECTING TO SERVER")
                    break
                except:
                    if DEBUGMODE: print(str(x) + " NOT ABLE TO CONNECT. TRYING AGAIN....")
                    x += 1
            if DEBUGMODE: print(str(x) + " Done!")

        def Send(socket, msg, boolPrint = False):

            if not type(boolPrint) == bool:
                print("WARNING: boolPrint must to be bool (DEFAULTING TO FALSE)")
            elif boolPrint == True:
                print("Sending : " + str(msg))

            Data = msg.encode('utf-8')

            try:
                socket.send(msg)
            except:
                return False
            return True

    class udp:

        def get():
            return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        def Send1(ip, port, msg, boolPrint = False):

            if not type(boolPrint) == bool:
                print("WARNING: boolPrint must to be bool (DEFAULTING TO FALSE)")
            elif boolPrint == True:
                print("Sending : " + str(msg))

            Data = msg.encode('utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                s.sendto(Data, (ip, int(port)))
            except:
                print("WARNING: An Error With UDP Socket")
            s.close()

        # Sends without closing socket.
        def Send_no_close(ip, port, msg, socket, boolPrint = False):

            if not type(boolPrint) == bool:
                print("WARNING: boolPrint must to be bool (DEFAULTING TO FALSE)")
            elif boolPrint == True:
                print("Sending : " + str(msg))

            Data = msg.encode('utf-8')
            try:
                socket.sendto(Data, (ip, int(port)))
            except:
                print("WARNING: An Error With UDP Socket")
