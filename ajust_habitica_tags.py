#!/usr/bin/python3
# coding=UTF-8
# encoding=UTF-8
import sys
import os
import time
import datetime
import requests
import json
import logging


BASE_URL = "https://habitica.com/api/v3"


class Log:
    def __init__(self, name="ajust"):
        self.looger = logging.getLogger(name)
        self.looger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handlerFile = logging.FileHandler(os.getenv("HABITICA_LOG_AJUST"))
        handlerFile.setFormatter(formatter)
        self.looger.addHandler(handlerFile)

    def info(self, msg):
        self.looger.info(msg)

    def error(self, msg):
        self.looger.error(msg)


log = Log()


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
            return t
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


def addTagToTask(tag, task):
    text = "/tasks/%s/tags/%s" % (task["id"], tag["id"])
    r = requests.post(url=BASE_URL + text, headers=getHeader())
    log.info("add tag %s in task %s" % (tag["name"], task["text"]))
    if tag.get("father", None):
        addTagToTask(tag["father"], task)


def normalizeTasksTags(tags, tasks):
    log.info("------- START NORMALIZE TASKS TAG ---------")
    for task in tasks:
        for tag in tags:
            if (
                tag.get("unicode", None)
                and tag["unicode"] in task["text"]
                and not tag["id"] in task["tags"]
            ):
                addTagToTask(tag, task)
    log.info("------- END NORMALIZE TASKS TAG ---------")


def normalizeTasksText(tags, tasks):
    log.info("------- START NORMALIZE TASKS NAME ---------")
    map_tags = {tag["id"]: tag["unicode"] for tag in tags if tag["unicode"]}
    for task in tasks:
        new_text = task["text"]
        unicodes = [
            map_tags[id_tag] for id_tag in task["tags"] if id_tag and id_tag in map_tags
        ]
        for uni in unicodes:
            new_text = new_text.replace(uni, "")
        new_text = " ".join(["".join(unicodes).strip(), new_text.strip()]).strip()
        if new_text != task["text"]:
            r = requests.put(
                url="%s/tasks/%s" % (BASE_URL, task["id"]),
                headers=getHeader(),
                json={"text": new_text},
            )
            log.info("rename %s to %s" % (task["text"], new_text))

    log.info("------- END NORMALIZE TASKS NAME ---------")


if __name__ == "__main__":
    try:
        log.info("------- START---------")
        normalizeTasksTags(getTags(), getTasks())
        normalizeTasksText(getTags(), getTasks())
        log.info("------- END ---------")
    except Exception as ex:
        log.error("ERROR: %s" % ex)
