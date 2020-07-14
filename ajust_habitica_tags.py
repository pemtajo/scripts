#!/usr/bin/python3
# coding=UTF-8
# encoding=UTF-8
import sys
import os
import time
import datetime
import requests
import json

BASE_URL = "https://habitica.com/api/v3"


def getHeader():
    return {
        "x-api-key": os.getenv("HABITICA_API_KEY"),
        "x-api-user": os.getenv("HABITICA_API_USER"),
    }


def getUnicode(tag):
    sts = tag["name"].split()
    return sts[2] if len(sts) > 2 else None


def getFather(tag, tags):
    sts = tag["name"].split()
    number = ".".join(sts[0].split(".")[:-1])
    for t in tags:
        number_father = t["name"].split()[0]
        if number_father == number:
            return t["id"]
    else:
        return None


def getTags():
    r = requests.get(url=BASE_URL + "/tags", headers=getHeader())
    tags = r.json()["data"]
    return [
        {
            "id": tag["id"],
            "name": tag["name"],
            "unicode": getUnicode(tag),
            "father": getFather(tag, tags),
        }
        for tag in tags
    ]


def getTasks():
    r = requests.get(url=BASE_URL + "/tasks/user", headers=getHeader())
    tasks = r.json()["data"]
    return [
        {"id": task["_id"], "text": task["text"], "tags": task["tags"]}
        for task in tasks
        if task["type"] != "reward" and task["type"] != "completedTodos"
    ]


tasks = getTasks()
tags = getTags()


print(json.dumps(tags, indent=3))
