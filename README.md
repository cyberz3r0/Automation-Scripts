# Automation Scripts

This is an automation script to perform several tasks. Punch In and Out for my timesheet (including lunch) as well as post in Discord my status. 



## 🛠 Skills
Selenium(WebDriver), Python, HTML knowledge


## Run Locally
Note: If you're Windows 11 Pro x64 please install using Python 3.11 as Notify-Py has a known issue with Python 3.12.[Issue](https://github.com/ms7m/notify-py/pull/55)

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

To run this project, you will need to add a .env file to the same directory as `main.py` and the following environment variables to it: 


`work_user` => CTU email

`work_pw` =>  CTU password

`discord_user` => Discord username

`discord_pw` => Discord Password

`gmail_user` => gmail email

`gmail_password` => gmail app password (Note: This is not your gmail password. See [here](https://support.google.com/accounts/answer/185833?hl=en) to configure)

`recipient` => recipient's email. (Note: For multiple recipients, input a list of strings)


## Current Limitations

- Needs direct file manipulation for changes.  
- Needs Third Party or Direct execution of script.
- Discord script can't run in headless as it doesn't find channels. 

## Possible Future Features

- GUI File manipulation
- Installer/self-sustain environment with DB
- Expand on Mac and Windows friendliness
