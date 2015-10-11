#!/usr/bin/env python
# coding=utf-8
from flask import render_template, url_for, redirect
from forms import TestForm
from app import app
import time
import os

refresh_times = 1
old_time      = 0
new_time      = 2

@app.route('/',methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    savefile='./savefile'
    form = TestForm()
    if form.validate_on_submit():
        generator = form.generator.data
        parser    = form.parser.data
        manager   = form.manager.data
        pipe_depth= form.pipe_depth.data
        pktlen    = form.pktlen.data
        exe = "%s -g %d -p %d -m %d --pipe_depth %d --pktlen %d > %s &" % (('./simulator/simulation'),
                                                                           (int(generator)),
                                                                           (int(parser)),
                                                                           (int(manager)),
                                                                           (int(pipe_depth)),
                                                                           (int(pktlen)),
                                                                           (savefile))
        print exe
        os.system(exe)
        return redirect('starttest')

    return render_template('index.html',
                          title = 'Welcome to here',
                          username= 'programmer',
                          refresh_times = refresh_times,
                          form = form)

@app.route('/starttest')
def starttest():
    savefile='./savefile'
    fp = open(savefile,'r')
    results = fp.readlines()
    fp.close()
    return render_template('starttest.html',
                              results = results)

@app.route('/update_result')
def update_result():
    global new_time,old_time
    savefile='./savefile'
    new_time = os.path.getmtime(savefile)
    if new_time != old_time:
        fp = open(savefile,'r')
        results = fp.readlines()
        fp.close()
        old_time = new_time
        return render_template('update_result.html',
                              results = results)
    else:
        time.sleep(1)
        new_time = os.path.getmtime(savefile)
        if new_time != old_time:
            fp = open(savefile,'r')
            results = fp.readlines()
            fp.close()
            old_time = new_time
            return render_template('update_result.html',
                              results = results)
        else:
            stops = "yes"
            fp = open(savefile,'r')
            results = fp.readlines()
            fp.close()
            return render_template('update_result.html',
                               results = results,
                              stops   = stops)
        

