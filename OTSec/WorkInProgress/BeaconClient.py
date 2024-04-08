from scapy.all import *
import time

# Modbus Header Fields
TID = 310 # random.randrange(1,2000)  # Trransaction ID
PID = 0 # Protocol ID always "zero"
Unit_ID = 1 # ID of the remote terminal unit
len = 4 # Length
Bit_Count = 5
Byte_Count = 1
MBFunction = 2 # Modbus Function "Read Input Registers"
Data = 3
#Data = random.randrange(1,11)

#IP Header Fields
src_ip='192.168.1.5' # Change it to the Source IP
dst_ip='192.168.2.5' # Change it to the Dest IP

#TCP Header Fields
tcp_sport = 502
tcp_dport = random.randrange(2000,40000)
tcp_seq = random.randrange(1,2000)
tcp_ack = random.randrange(1,2000)
tcp_flags = 'PA'
tcp_window = 2048 # random.randrange(500,1000)


Server_IP = '192.168.2.254'
Server_Port = 5001

s = socket.socket()
s.connect((Server_IP,Server_Port))


class ModbusTCP(Packet):
	name='Modbus/TCP'
	fields_desc = [
		ShortField("Transaction_Identifier", TID),
		ShortField("Protocol_Identifier", PID),
		ShortField("Length", len),
		ByteField("Unit_Identifier", Unit_ID)
	]

class Modbus(Packet):
	name='Modbus'
	fields_desc = [
		XByteField("Function_Code", MBFunction),
		#ShortField("Reference_Number", 0),
		#ShortField("Bit_Count", Bit_Count),
		ByteField("Byte_Count", Byte_Count),
		ByteField("Data", Data)
		]

try:
	while True:
		#pkt.sr1(s, Raw(ModbusTCP()/Modbus()))
		#send(pkt, verbose=0, iface='eth0')
		print("Sending Packets to 192.168.2.254. \n Press Ctrl+C to exit")
#		pkt = IP(src=src_ip, dst=dst_ip)/\
#			TCP(sport=tcp_sport, dport=tcp_dport, seq=tcp_seq, ack=tcp_ack, \
#			flags=tcp_flags, window=tcp_window)/\
#			ModbusTCP()/Modbus()

		#send(pkt, verbose=0, iface='eth0')
		#print("Sending Packets to 192.168.2.254. \n Press Ctrl+C to exit")
		#send(pkt, verbose=0, iface='eth0')
		#sr(pkt)
		#data = ModbusTCP()/Modbus()
		pkt= ModbusTCP()/Modbus()
		s.send(bytes(pkt))
		#send(pkt, verbose=0, iface='eth0')
		time.sleep(1)
except KeyboardInterrupt:
	pass
