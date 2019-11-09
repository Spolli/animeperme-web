#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify, url_for, redirect
from src.models.animeforce import Enforcer, download_link, Anime
import json

app = Flask(__name__, template_folder='./src/templates')
loading = True

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.get_json()
        anime = Anime(date['name'], date['link'], date['episodeNumber'], date['type'], date['img'])
        video_link = anime._get_last_episode().download_link()
        return redirect(url_for('video.html', video_link=video_link))
    else:
        global loading
        enforcer = Enforcer()
        lastEpisodeList = enforcer.last_episode_list()
        loading = False
        return render_template('index.html', lastEpisodeList=lastEpisodeList)

@app.route("/animelist")
def fullAnimeList():
    enforcer = Enforcer()
    animeList = enforcer.anime_list()
    return render_template('animelist.html', animelist=animeList)

if __name__ == '__main__':
    app.run(debug=True)