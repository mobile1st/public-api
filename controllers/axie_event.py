# -*- coding: utf-8 -*-
"""
"""

from __future__ import absolute_import, division, print_function

from flask import request
from core import models as m
from handlers.query_builder import QueryBuilder

from core.core_base import CoreBase


class AxieEvent(CoreBase):
    """Docstring for AxieEvent."""

    def get_events(self, before, after):
        print(before, after)
        query_filter = {"event_date": {"$lte": after, "$gte": before}}
        # events = self.session.query(m.AxieNftEvent).filter(m.AxieNftEvent.event_date <= after).filter(m.AxieNftEvent.event_date >= before).all()
        return QueryBuilder(m.AxieNftEvent).get_result(query_filter=query_filter)
