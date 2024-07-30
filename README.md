Purpose of this script is to automatically startup my portfolio projects
everyday, since it takes Render about ~20 minutes to wake up.

This script will ping the URL's listed within `URLS`.

I am managing the ping schedule using a Cronjob.

# Setup

1. Activate venv and install requirements

```shell
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt
```

2. Within the file `startupRithmProjects.py`, update the list of URL's to be your
   own URL's.

3. cd into the directory that this file is saved in

4. Get the absolute file path (type in `pwd`)
   (For me, it is: /Users/alicechang/rithm/personal/startUpRithmProj )

5. Run this in shell:

```shell
cd < YOUR ABSOLUTE FILE PATH >
< YOUR ABSOLUTE FILE PATH >/venv/bin/python startupRithmProjects.py

# for me, it looks like:
# cd /Users/alicechang/rithm/personal/startUpRithmProj
# /Users/alicechang/rithm/personal/startUpRithmProj/venv/bin/python startupRithmProjects.py
```

6. Setup Cronjob

```shell
crontab -e
```

7. Within the crontab editor window:

```
0 4 * * * cd /Users/alicechang/rithm/personal/startUpRithmProj && /Users/alicechang/rithm/personal/startUpRithmProj/venv/bin/python /Users/alicechang/rithm/personal/startUpRithmProj/startupRithmProjects.py

```

8. Save & exit. Check if the cronjob is there: `crontab -l`

9. Done :)
