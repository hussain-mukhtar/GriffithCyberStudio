#!/bin/bash
while true
do
	modbus read 192.168.1.5 %M100 4
	sleep 1
	modbus read 192.168.1.5 %MW100 4
	sleep 1
done
