# TRAFFIC SHAPING : using simple Leaky bucket algorithm, implemented using multi threading concept in python.

import threading
import time
from random import randint, random

buffer = []
condition = threading.Condition()
BUFFER_LEN = 10


def packet_producer(e):
    global buffer
    while(True):
        if(e.isSet()):
            break
        # lock acquire
        condition.acquire()
        # buffer should not be full.
        if(buffer.__len__() == BUFFER_LEN):
            print(
                f"Buffer is full !!!..waiting for consumer, Buffer :{buffer} \n")
            condition.wait()
            print(
                f"Space in buffer ! Consumer consumed some packets, Buffer :{buffer} \n")

        if(buffer.__len__() < BUFFER_LEN):
            new_pkt = randint(100, 1200)
            buffer.append(new_pkt)
            print(f" New Packet added !!! Buffer :{buffer} \n")
            # Notify consumer and lock release
            condition.notify()
            condition.release()
            time.sleep(random())


def packet_consumer(bandwidth, e):
    global buffer
    current_bw = bandwidth
    residue = 0
    packet = 0

    while(True):
        if(e.isSet()):
            break
        # lock acquire
        condition.acquire()
        if(buffer.__len__() == 0):
            print("Empty Buffer !!! consumer is waiting... \n")
            condition.wait()
            print("Producer added a new packet !!! \n")

        if(residue == 0 and buffer.__len__() != 0):
            packet = buffer.pop(0)
        else:
            packet = residue
            residue = 0

        if(packet < current_bw):
            print(
                f"Current BW :{current_bw} ,Packet size :{packet}, Packet sent:{packet}, Remaining BW:{current_bw-packet}\n")
            current_bw = current_bw-packet
        else:
            print(
                f"Current BW :{current_bw} ,Packet size :{packet}, Packet sent:{current_bw}, Remaining BW:{0} \n")
            residue = packet-current_bw
            current_bw = bandwidth
            continue

        # lock release
        condition.notify()
        condition.release()
        time.sleep(random())


def Leaky_bucket():
    bandwidth = int(input("Enter a Bandwidth for network traffic shaping:"))

    e = threading.Event()

    producer_thread = threading.Thread(target=packet_producer, args=(e,))
    consumer_thread = threading.Thread(
        target=packet_consumer, args=(bandwidth, e,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join(10)
    consumer_thread.join(10)

    if producer_thread.is_alive() or consumer_thread.is_alive():
        e.set()


Leaky_bucket()
