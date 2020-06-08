!#/bin/bash

for URL in $(cat url_list.txt); do
    for YEAR in {2012..2016}; do
        donewayback_machine_downloader $URL/$YEAR --exclude "/\.((gif|jpg|jpeg|png|css|svg|xml|js|ttf|pdf|txt|php|ico)(\?.*)|(html\?.*))?$/i";
    done
done


cat | while read URL; do
    donewayback_machine_downloader $URL --exclude "/\.((gif|jpg|jpeg|png|css|svg|xml|js|ttf|pdf|txt|php|ico)(\?.*)|(html\?.*))?$/i";
done << EOF
http://www.catonmat.net/blog
https://blog.codinghorror.com/
https://davidwalsh.name
https://github.com/blog
https://www.hanselman.com/blog/
http://highscalability.com/blog/2012
http://highscalability.com/blog/2013
http://highscalability.com/blog/2014
http://highscalability.com/blog/2015
http://highscalability.com/blog/2016
http://highscalability.com/blog/2017
http://blog.kaggle.com
https://lemire.me/blog
https://martinfowler.com/articles
https://blogs.technet.microsoft.com/machinelearning
http://blog.wtf.sg
EOF

for SCRIPT in sort_scripts/*.sh; do
    bash $SCRIPT
done
