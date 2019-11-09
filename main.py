#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for, redirect
from src.models.animeforce import Enforcer, download_link, Anime

app = Flask(__name__, template_folder='./src/templates')

@app.route('/')
def index():
    enforcer = Enforcer()
    lastEpisodeList = enforcer.last_episode_list()
    return render_template('index.html', lastEpisodeList=lastEpisodeList)

@app.route("/video", methods=['GET', 'POST'])
def video_page():
    if request.method == 'POST':
        date = request.get_json()
        anime = Anime(date['name'], date['link'], date['episodeNumber'], date['type'], date['img'])
        opened_episode = anime._get_last_episode()
        return render_template('video.html', episode=opened_episode, video_link=opened_episode.download_link())

@app.route("/animelist")
def fullAnimeList():
    enforcer = Enforcer()
    animeList = enforcer.anime_list()
    return render_template('animelist.html', animelist=animeList)

if __name__ == '__main__':
    app.run(debug=True)