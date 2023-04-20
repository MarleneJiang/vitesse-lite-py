#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Description: 操作数据库类
usage:
    from core.db.orm import ORM

    orm = ORM()    # 操作数据库类
    author = self.orm.getStorageVar('author')    # 获取储存变量
    print('author', author)
'''

from core.db.models import StorageVar
from core.db.db import DB
from sqlalchemy import select, update, insert


class ORM:
    '''操作数据库类'''

    def getStorageVar(self, key):
        '''获取储存变量'''
        resVal = ''
        dbSession = DB.session()
        with dbSession.begin():
            stmt = select(StorageVar.value).where(StorageVar.key == key)
            result = dbSession.execute(stmt)
            result = result.one_or_none()
            if result is None:
                # 新建
                stmt = insert(StorageVar).values(key=key)
                dbSession.execute(stmt)
            else:
                resVal = result[0]
        dbSession.close()
        return resVal

    def setStorageVar(self, key, val):
        '''更新储存变量'''
        dbSession = DB.session()
        with dbSession.begin():
            stmt = update(StorageVar).where(StorageVar.key == key).values(value=val)
            dbSession.execute(stmt)
        dbSession.close()
