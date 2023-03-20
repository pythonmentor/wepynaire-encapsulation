class User:
    def __init__(self, name, email, password):
        self.__name = name   # attribut privé
        self.__email = email   # attribut privé
        self.__password = password   # attribut privé

    def get_name(self):   # méthode d'instance publique
        return self.__name

    def set_name(self, name):   # méthode d'instance publique
        self.__name = name

    def get_email(self):   # méthode d'instance publique
        return self.__email

    def set_email(self, email):   # méthode d'instance publique
        self.__email = email

    def get_password(self):   # méthode d'instance publique
        return self.__password

    def set_password(self, password):   # méthode d'instance publique
        self.__password = password


class Task:
    def __init__(self, description, status, assignee):
        self.__description = description   # attribut privé
        self.__status = status   # attribut privé
        self.__assignee = assignee   # attribut privé

    def get_description(self):   # méthode d'instance publique
        return self.__description

    def set_description(self, description):   # méthode d'instance publique
        self.__description = description

    def get_status(self):   # méthode d'instance publique
        return self.__status

    def set_status(self, status):   # méthode d'instance publique
        self.__status = status

    def get_assignee(self):   # méthode d'instance publique
        return self.__assignee

    def set_assignee(self, assignee):   # méthode d'instance publique
        self.__assignee = assignee


class Note:
    def __init__(self, title, content, author):
        self.__title = title   # attribut privé
        self.__content = content   # attribut privé
        self.__author = author   # attribut privé

    def get_title(self):   # méthode d'instance publique
        return self.__title

    def set_title(self, title):   # méthode d'instance publique
        self.__title = title

    def get_content(self):   # méthode d'instance publique
        return self.__content

    def set_content(self, content):   # méthode d'instance publique
        self.__content = content

    def get_author(self):   # méthode d'instance publique
        return self.__author

    def set_author(self, author):   # méthode d'instance publique
        self.__author = author


class Project:
    def __init__(self, name):
        self.__name = name   # attribut privé
        self.__tasks = []   # attribut privé
        self.__notes = []   # attribut privé
        self.__users = []   # attribut privé

    def add_user(self, user):   # méthode d'instance publique
        self.__users.append(user)

    def remove_user(self, user):   # méthode d'instance publique
        self.__users.remove(user)

    def get_users(self):   # méthode d'instance publique
        return self.__users

    def add_task(self, task):   # méthode d'instance publique
