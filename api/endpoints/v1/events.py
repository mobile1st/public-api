from __future__ import absolute_import, division, print_function
from api.app import api
from flask import g, request


@api.list("/events")
@api.doc(""" Get NFT Events """)
def get_axie_events():
    before_date = request.args.get('before')
    after_date = request.args.get("after")
    return g.core.event.get_events(before_date, after_date)
