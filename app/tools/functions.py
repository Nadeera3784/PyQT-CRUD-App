#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Дополнительные функции
"""

def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if not instance:
        instance = model(**kwargs)
        session.add(instance)
    return instance
