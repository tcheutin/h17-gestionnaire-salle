# h17-gestionnaire-salle

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Linux (preferable) or Windows
* Python 3
* Postgresql
  * DB ehall created with these creds:
    * user: ehall
    * password: 4dm1n1str4t0r!
  * postgresql service started

### Installing
All the commands below were run in a Linux's Terminal. For Windows, please adapt the commands to your environment. 

Clone the project
```bash
git clone https://github.com/gti525/h17-gestionnaire-salle.git
```

Change directory to cloned project
```
cd h17-gestionnaire-salle/eHall
```

Make migrations & migrate models
```bash
python manage.py makemigrations
python manage.py migrate
```

Run the server
```bash
python manage.py runserver
```

Test the website in your browser
```
http://127.0.0.1:8000/event
```

#### Optional
To access the admin page, an admin user must be created.

Change directory to cloned project
```
cd h17-gestionnaire-salle/eHall
```

Create admin user
```
python manage.py createsuperuser
```

Login with the new admin user
```
http://127.0.0.1:8000/admin
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Postgresql](https://www.postgresql.org/) - Dependency Management


## Authors

* **Kenzyme Le** - *Initial work* - [noireDen](https://github.com/noireDen)
* **Alain Zakkour**
* **Jean-Pierre Bertrand Dorion** 
* **Thierry Cheutin**
* **Nicolas Nadeau**
* **Raphaël Zumer**


See also the list of [contributors](https://github.com/gti525/h17-gestionnaire-salle/contributors) who participated in this project.
