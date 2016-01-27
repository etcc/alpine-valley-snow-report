# -*- coding: utf-8 -*-
"""Crawls alpinevalleyresort.com and scrapes snow report.

Copyright 02014 Ben Keating (http://bpk.deepdream.com)

Originally written for the East Troy Area Chamber of Commerce so we could 
display Alpine Valley's current snow report directly on easttroy.org. This 
module greatly depends on the structure of alpinevalleyresort.com/. 
Please don't change it, Alpine! Just keep it updated. <3
"""

import datetime
from lxml import html
import requests

DEBUG = True

def get_snow_report():

    page = requests.get('http://www.alpinevalleyresort.com/the-mountain/snow-report/')
    tree = html.fromstring(page.text)

    status = tree.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/text()')[0]
    hours = tree.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/text()')[0]
    trail_status = tree.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div/text()')[0]
    lift_status = tree.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div/text()')[0]
    snow_base = tree.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/div/text()')[0]
    snow_yesterday = tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/p[2]/text()[3]')[0]
    currently = tree.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[6]/div/text()')[0]
    condition_description = tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/p[3]/text()')[0]
    last_updated = tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/p[1]/text()')[0]
    polled_at = datetime.datetime.now()

    trail_list = {
        '1st Tracks': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[1]/td[2]/text()')[0],
        'Baby Steps': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[2]/td[2]/text()')[0],
        'E-Z-Does-it': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[3]/td[2]/text()')[0],
        'First Adventure': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[4]/td[2]/text()')[0],
        'Snowbank': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[5]/td[2]/text()')[0],
        'Soft Landings': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[6]/td[2]/text()')[0],
        'Valley View': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[7]/td[2]/text()')[0],
        'Cut Throat': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[8]/td[2]/text()')[0],
        'E-Z Pass': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[9]/td[2]/text()')[0],
        'East Pass': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[10]/td[2]/text()')[0],
        'Halfway': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[11]/td[2]/text()')[0],
        'Northwest Pass': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[12]/td[2]/text()')[0],
        'Timber Gulch': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[13]/td[2]/text()')[0],
        'Timber Trail': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[14]/td[2]/text()')[0],
        'Alpine': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[15]/td[2]/text()')[0],
        'Big Thunder': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[16]/td[2]/text()')[0],
        'Broadway': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[17]/td[2]/text()')[0],
        'Lodge': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[18]/td[2]/text()')[0],
        'Mohawk': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[19]/td[2]/text()')[0],
        'Shelter': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[1]/tbody/tr[20]/td[2]/text()')[0],
    }

    lift_list = {
        'Adding chairlifts as needed': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[2]/tbody/tr[1]/td[2]/text()')[0],
        'Conveyer #1': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[2]/tbody/tr[2]/td[2]/text()')[0],
        'Conveyer #2': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[2]/tbody/tr[3]/td[2]/text()')[0],
        'Conveyer #3': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[2]/tbody/tr[4]/td[2]/text()')[0],
        'Conveyer #4': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[2]/tbody/tr[5]/td[2]/text()')[0],
        'Conveyer #5': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[2]/tbody/tr[6]/td[2]/text()')[0],
        'Double - Valley View Chair': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[2]/tbody/tr[7]/td[2]/text()')[0],
        'Quad - E-Z Rider': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[2]/tbody/tr[8]/td[2]/text()')[0],
        'Quad - Valley Flyer': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[2]/tbody/tr[9]/td[2]/text()')[0],
        'Quad- Super Glide': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[2]/tbody/tr[10]/td[2]/text()')[0],
        'Triple - First Adventure Chair': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[2]/tbody/tr[11]/td[2]/text()')[0],
        'Triple - Lodge Chair': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[2]/tbody/tr[12]/td[2]/text()')[0],
        'Triple - Mohawk Chair': tree.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/table[2]/tbody/tr[13]/td[2]/text()')[0],
    }

    if DEBUG == True:

        if status == "Open":

            print "\n###\n# Alpine Valley Ski Report Snow Report\n###" 
            print "Data retrieved at %s" % polled_at           
            print "Status: %s" % status
            print "Hours: %s" % hours
            print "Trail Status: %s of 20" % trail_status
            print "Lift Status: %s of 12" % lift_status
            print "Snow base: %s" % snow_base
            print "Snow yesterday: %s" % snow_yesterday
            print "Currently: %s" % currently
            print "Condition Description: %s" % condition_description
            
            print "\n###\n# Trail Status\n###"
            for key, value in trail_list.iteritems():
                print "%s: %s" % (key, value)

            print "\n###\n# Lift Status\n###"
            for key, value in lift_list.iteritems():
                print "%s: %s" % (key, value)
        
        elif status == "Closed":

            print "Alpine Valley is Closed Today."

    else: 

        return {
            'status': status,
            'status_full': status_full,
            'hours': hours,
            'trail_status': trail_status,
            'lift_status': lift_status,
            'snow_base': snow_base,
            'snow_yesterday': snow_yesterday,
            'currently': currently,
            'condition_description': condition_description,
            'trail_list': trail_list,
            'lift_list': lift_list,
            'polled_at': polled_at,
        }

get_snow_report()
