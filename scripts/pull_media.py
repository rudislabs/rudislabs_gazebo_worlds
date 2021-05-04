#!/usr/bin/env python3
"""
Generate Worlds
@author: Benjamin Perseghetti
@email: bperseghetti@rudislabs.com
"""
import os
import urllib.request
import zipfile

release="v1.0"
git_repo="rudislabs_gazebo_worlds"
rel_model_path ="../models"
script_path = os.path.realpath(__file__).replace("pull_media.py","")
model_path = os.path.realpath(os.path.relpath(os.path.join(script_path, rel_model_path)))

cities = next(os.walk(model_path))[1]

for city in cities:
    media_path = '{:s}/{:s}/{:s}_media'.format(model_path, city, city)
    unzip_media_path = '{:s}/{:s}'.format(model_path, city)
    if not os.path.isdir(media_path):
        zip_url = 'https://github.com/rudislabs/{:s}/releases/download/{:s}/{:s}_media.zip'.format(git_repo, release, city)
        zip_media = '/tmp/{:s}_media.zip'.format(city)
        print('Downloading: {:s} -> {:s}'.format(zip_url, zip_media))
        with urllib.request.urlopen(zip_url) as dl_zip:
            with open(zip_media, 'wb') as out_zip:
                out_zip.write(dl_zip.read())
        print('Finished Downloading: {:s}'.format(zip_media))
        print('Extracting: {:s} -> {:s}'.format(zip_media, unzip_media_path))
        with zipfile.ZipFile(zip_media, 'r') as zip_ref:
            zip_ref.extractall(unzip_media_path)
        print('Finished Extracting to: {:s}'.format(unzip_media_path))
