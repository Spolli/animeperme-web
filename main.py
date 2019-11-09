#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for, redirect
from src.models.animeforce import Enforcer, download_link, Anime

app = Flask(__name__, template_folder='./src/templates')
video_link = None

@app.route('/', methods = ['GET', 'POST'])
def index():
    loading = True
    if request.method == 'POST':
        global video_link
        date = request.get_json()
        anime = Anime(date['name'], date['link'], date['episodeNumber'], date['type'], date['img'])
        video_link = anime._get_last_episode().download_link()
    else:
        enforcer = Enforcer()
        lastEpisodeList = enforcer.last_episode_list()
        loading = False
    return render_template('index.html', lastEpisodeList=lastEpisodeList, loading=loading)

@app.route("/video/")
def video_page():
    return render_template('video.html', video_link=video_link)

@app.route("/animelist")
def fullAnimeList():
    enforcer = Enforcer()
    animeList = enforcer.anime_list()
    return render_template('animelist.html', animelist=animeList)

if __name__ == '__main__':
    app.run(debug=True)