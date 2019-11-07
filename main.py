#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from src.models.animeforce import Enforcer, download_link

app = Flask(__name__, template_folder='./src/templates')
loading = True

@app.route('/')
def index():
    global loading
    enforcer = Enforcer()
    lastEpisodeList = enforcer.last_episode_list()
    last_ep = []
    for anime in lastEpisodeList:
        last_ep.append(anime._get_last_episode())
    loading = False
    return render_template('index.html', lastEpisodeList=last_ep)

@app.route('/video/<string:link>')
def video_page(link):
    video_link = download_link(link)
    return render_template('video.html', video_link=video_link)

@app.route("/animelist")
def fullAnimeList():
    enforcer = Enforcer()
    animeList = enforcer.anime_list()
    return render_template('animelist.html', animelist=animeList)

if __name__ == '__main__':
    app.run(debug=True)