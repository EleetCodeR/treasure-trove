# TRAFFIC SHAPING : using simple Leaky bucket algorithm, implemented using multi threading concept in python.

import threading
import time
from random import randint, random

buffer = []
condition = threading.Condition()
BUFFER_LEN = 10


def packet_producer(e1):
    global buffer
    while(True):

        # lock acquire
        condition.acquire()
        # buffer should not be full.
        if(buffer.__len__() == BUFFER_LEN):
            new_pkt = randint(100, 1000)
            print(
                f" ======== Buffer is full! ---> waiting for consumer, Buffer :{buffer} \n")
            print(f" ======== Packet Lost :{new_pkt} \n")
            condition.wait()
            print(
                f" ======== Space in buffer! ---> Consumer consumed , Buffer :{buffer} \n")

        if(buffer.__len__() < BUFFER_LEN):
            while(buffer.__len__() < randint(2, 4)):
                new_pkt = randint(100, 1200)
                buffer.append(new_pkt)
                print(f" ======== New Packet added! ---> Buffer :{buffer} \n")

        # Notify consumer and lock release
        condition.notify()
        condition.release()
        if(e1.isSet()):
            break
        time.sleep(random())


def packet_consumer(bandwidth, e2):
    global buffer
    current_bw = bandwidth
    residue = 0
    packet = 0

    while(True):

        # lock acquire
        condition.acquire()
        if(buffer.__len__() == 0):
            print("--------> Empty Buffer! ---> consumer is waiting...\n")
            condition.wait()
            print("--------> consumer resumes. \n")

        if(residue == 0 and buffer.__len__() != 0):
            packet = buffer.pop(0)
        else:
            packet = residue
            residue = 0

        if(packet < current_bw):
            print(
                f" --------> Current BW :{current_bw}, Packet size :{packet}, Packet sent:{packet}, Remaining BW:{current_bw-packet} \n")
            current_bw = current_bw-packet
        else:
            print(
                f" --------> Current BW :{current_bw}, Packet size :{packet}, Packet sent:{current_bw}, Remaining BW:{0} \n")
            residue = packet-current_bw
            current_bw = bandwidth
            continue

        # lock release
        condition.notify()
        condition.release()
        if(e2.isSet()):
            break
        time.sleep(random())


def Leaky_bucket():
    bandwidth = int(
        input("\n Enter Bandwidth : \n"))

    e1 = threading.Event()
    e2 = threading.Event()

    producer_thread = threading.Thread(target=packet_producer, args=(e1,))
    consumer_thread = threading.Thread(
        target=packet_consumer, args=(bandwidth, e2,))

    producer_thread.start()
    consumer_thread.start()

    print("\n Producer executes join ! \n")
    producer_thread.join(1)
    print("\n Consumer executes join ! \n")
    consumer_thread.join(1)

    if producer_thread.is_alive():
        print(" \n Producer will be terminated ! \n")
        e1.set()

    if consumer_thread.is_alive():
        print(" \n Consumer will be terminated ! \n")
        e2.set()


Leaky_bucket()
