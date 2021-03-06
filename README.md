## SocialSesh

### Overview

A full-stack web app where users can connect, create, and contribute, through online virtual events

<img src="https://github.com/senseofsteph/SocialSesh/blob/master/static/img/social_sesh_updated_gif.gif" width="620">

[Click to view demo video](https://youtu.be/X-m9QDGppNY)

### Technologies and Stack
**Backend:**
Python, Flask, SQLAlchemy, PostgreSQL<br>
**Frontend:**
HTML5, CSS3, JavaScript, Bootstrap<br>
**APIs:**
Twilio and FullCalendar

### MVP Features

- User can browse all virtual events
- User can register to attend a virtual event
- User receives an event confirmation text message

### Set-up & Installation

Install a code editor such as [VS code](https://code.visualstudio.com/download) or [Sublime Text](https://www.sublimetext.com/)<br>
Install [Python3](https://www.python.org/downloads/mac-osx/)<br>
Install [pip](https://pip.pypa.io/en/stable/installing/), the package installer for Python <br>
Install [postgreSQL](https://www.postgresql.org/) for the relational database <br>
Make an account to receive [Twilio SMS API](https://www.twilio.com/docs/sms/api) key and token <br>
Visit [FullCalendar](https://fullcalendar.io) to obtain the necessary JavaScript code

### Clone or fork this repository

- Create and activate a virtual environment:
```shell
git clone https://github.com/senseofsteph/SocialSesh
```

- Install dependencies:
```shell
pip3 install virtualenv
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

- Store the API key and token in 'secrets.sh' file <br>
```shell
source secrets.sh
```

- With PostgreSQL, create the SocialSesh database:
```shell
createdb socialsesh
```

- Create all table and relations in the database and seed all data:
```shell
python3 seed.py
```

- Run the app from the command line:
```shell
python3 server.py
```

### Future features

- User profile customization
- Ability to create and save events
- Chat rooms to discuss common interests in events
- Software deployment

### Connect with the developer

- [Github](https://github.com/senseofsteph)
- [LinkedIn](https://www.linkedin.com/in/stephanieogamba)

