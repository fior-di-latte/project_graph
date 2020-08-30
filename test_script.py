import argparse
import time
from tests.goodnight import sleep_five_seconds

def sleep_one_seconds():
    time.sleep(1)

def sleep_two_seconds():
    time.sleep(2)

for i in range(3):
    sleep_one_seconds()

sleep_two_seconds()

sleep_five_seconds()
