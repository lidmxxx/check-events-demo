#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ====#====#====#====
# Author:lidemin
# CreateDate:2020/09/18
# LastUpdate:2020/09/28
# Description:封装一些对 mysql 数据库的操作
# Version:0.1.0
# ====#====#====#====
import pymysql
from pymysql.cursors import DictCursor
import os
import configparser


class DBBase:
    def __init__(self):
        conf = configparser.ConfigParser()
        c_path = os.path.dirname(os.path.abspath(__file__))
        conf.read(c_path + '/event_tracking_test.conf')
        self.conn = pymysql.connect(host=conf.get("mysql", "host"),
                                    port=int(conf.get("mysql", "port")),
                                    user=conf.get("mysql", "user"),
                                    passwd=conf.get("mysql", "password"),
                                    db=conf.get("mysql", "database"),
                                    charset=conf.get("mysql", "charset"))
        self.cursor = self.conn.cursor(cursor=DictCursor)

    def query_one(self, sql):
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            return res
        except Exception as e:
            return e

    def query_all(self, sql):
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            return res
        except Exception as e:
            return f'Error:{e}'

    def insert_data(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            return e

    def update_data(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            return e

    def delete_data(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            return e

    def close_connect(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            return e
