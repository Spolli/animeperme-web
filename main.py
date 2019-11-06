#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from src.models.animeforce import Enforcer

app = Flask(__name__)

@app.route("/")
def main():
    enforcer = Enforcer()
    lastEpisodeList = enforcer.last_episode_list()
    return render_template('./src/pages/index.html', lastEpisodeList=lastEpisodeList)

@app.route("/animelist")
def fullAnimeList():
    enforcer = Enforcer()
    animeList = enforcer.anime_list()
    return render_template('./src/pages/animelist.html', animelist=animeList)

if __name__ == '__main__':
    app.run()