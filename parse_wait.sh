#!/bin/bash

last_screen_line=$(screen -ls | tail -1)
while ! [ "${last_screen_line::1}" == "2" ]; do
    last_screen_line=$(screen -ls | tail -1)
    echo "Wait please"
    sleep 60
done

cd ~/Project/data/
python3 ~/Project/News_Crawler/merge_csv.py

mv merged.csv ~/Project/my_django_project/static/

python3 ~/Project/my_django_project/manage.py runscript load

