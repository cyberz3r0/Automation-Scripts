# Automation Scripts

This is an automation script to perform several tasks. Punch In and Out for my timesheet (including lunch) as well as post in Discord my status. 



## 🛠 Skills
Selenium(WebDriver), Python, HTML knowledge


## Run Locally

Clone the project

```bash
  git clone https://github.com/cyberz3r0/clockin-out
```

Go to the project directory

```bash
  cd clockin-out-main
```
Create your virtual environment and install dependencies

```bash
  pipenv shell
  pipenv install selenium python-decouple notify-py schedule pytz
```

Start the server

```bash
  py main.py
```


## Environment Variables

To run this project, you will need to add a .env file to `clockin-out-main` and the following environment variables to it: 


`work_user` => CTU email

`work_pw` =>  CTU password

`discord_user` => Discord username

`discord_pw` => Discord Password


## Current Limitations

- Needs direct file manipulation for changes.  
- Needs Third Party or Direct execution of script.
- Discord script can't run in headless as it doesn't find channels. 

## Possible Future Features

- GUI File manipulation
- Installer/self-sustain environment with DB
- Expand on Mac and Windows friendliness
