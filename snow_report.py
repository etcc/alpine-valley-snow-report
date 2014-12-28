# -*- coding: utf-8 -*-
"""Crawls alpinevalleyresort.com and scrapes snow report.

Copyright 02014 Ben Keating (http://bpk.deepdream.com)

Originally written for the East Troy Area Chamber of Commerce so we could 
display Alpine Valley's current snow report directly on easttroy.org. This 
module greatly depends on the structure of alpinevalleyresort.com/snow-report.php. 
Please don't change it, Alpine! Just keep it updated. <3
"""

import datetime
from lxml import html
import requests

DEBUG = True

def get_snow_report():

    page = requests.get('http://www.alpinevalleyresort.com/snow-report.php')
    tree = html.fromstring(page.text)

    status = tree.xpath('//*[@id="detail-weather"]/tr[6]/th/table/tr[1]/td[2]/span/text()')[0]
    status_full = tree.xpath('//*[@id="body-copy"]/table[2]/tr[1]/td/text()')[0]
    hours = tree.xpath('//*[@id="detail-weather"]/tr[6]/th/table/tr[2]/td[2]/text()')[0]
    trail_status = tree.xpath('//*[@id="detail-weather"]/tr[6]/th/table/tr[3]/td[2]/text()')[0]
    lift_status = tree.xpath('//*[@id="detail-weather"]/tr[6]/th/table/tr[4]/td[2]/text()')[0]
    snow_base = tree.xpath('//*[@id="detail-weather"]/tr[6]/th/table/tr[5]/td[2]/text()')[0]
    snow_yesterday = tree.xpath('//*[@id="detail-weather"]/tr[6]/th/table/tr[6]/td[2]/text()')[0]
    currently = tree.xpath('//*[@id="detail-weather"]/tr[6]/th/table/tr[7]/td[2]/text()')[0]
    condition_description = tree.xpath('//*[@id="body-copy"]/p[1]/text()')[0]
    polled_at = datetime.datetime.now()

    trail_list = {
        'E-Z-Does-it': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[2]/td[2]/text()')[0],
        'First Adventure': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[3]/td[2]/text()')[0],
        'First Tracks': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[4]/td[2]/text()')[0],
        'Raspberry': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[5]/td[2]/text()')[0],
        'Soft Landings': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[6]/td[2]/text()')[0],
        'Strawberry': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[7]/td[2]/text()')[0],
        'Valley View': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[8]/td[2]/text()')[0],
        'Cut Throat': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[9]/td[2]/text()')[0],
        'E-Z Pass': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[10]/td[2]/text()')[0],
        'East Pass': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[11]/td[2]/text()')[0],
        'Halfway': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[12]/td[2]/text()')[0],
        'Northwest Pass': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[13]/td[2]/text()')[0],
        'Timber Gulch': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[14]/td[2]/text()')[0],
        'Timber Trail': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[15]/td[2]/text()')[0],
        'Alpine': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[16]/td[2]/text()')[0],
        'Big Thunder': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[17]/td[2]/text()')[0],
        'Broadway': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[18]/td[2]/text()')[0],
        'Lodge': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[19]/td[2]/text()')[0],
        'Mohawk': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[20]/td[2]/text()')[0],
        'Shelter': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[1]/tr[21]/td[2]/text()')[0]
    }

    lift_list = {
        'Adding chairlifts as needed': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[2]/tr[2]/td[2]/text()')[0],
        'Conveyer #1': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[2]/tr[3]/td[2]/text()')[0],
        'Conveyer #2': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[2]/tr[4]/td[2]/text()')[0],
        'Conveyer #3': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[2]/tr[5]/td[2]/text()')[0],
        'Conveyer #4': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[2]/tr[6]/td[2]/text()')[0],
        'Double - Valley View Chair': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[2]/tr[6]/td[2]/text()')[0],
        'Quad - E-Z Rider': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[2]/tr[8]/td[2]/text()')[0],
        'Quad - Valley Flyer': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[2]/tr[9]/td[2]/text()')[0],
        'Quad- Super Glide': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[2]/tr[10]/td[2]/text()')[0],
        'Triple - First Adventure Chair': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[2]/tr[11]/td[2]/text()')[0],
        'Triple - Lodge Chair': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[2]/tr[12]/td[2]/text()')[0],
        'Triple - Mohawk Chair': tree.xpath('//*[@id="body-copy"]/table[2]/tr[2]/td/table[2]/tr[13]/td[2]/text()')[0],
    }

    if DEBUG == True:

        if status == "Open":

            print "\n###\n# Alpine Valley Ski Report Snow Report\n###" 
            print "Data retrieved at %s" % polled_at           
            print "Status: %s" % status
            print "Status full: %s" % status_full
            print "Hours: %s" % hours
            print "Trail Status: %s" % trail_status
            print "Lift Status: %s" % lift_status
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
