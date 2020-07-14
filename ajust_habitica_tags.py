#!/usr/bin/python3
# coding=UTF-8
# encoding=UTF-8
import sys
import os
import time
import datetime
import requests

BASE_URL = "https://habitica.com/api/v3"


def getHeader():
    return {
        "x-api-key": os.getenv("HABITICA_API_KEY"),
        "x-api-user": os.getenv("HABITICA_API_USER"),
    }


r = requests.get(url=BASE_URL + "/tags", headers=getHeader())


print(r.json()["data"])
