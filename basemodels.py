class User:
    """Représente un utilisateur d'une application.

    Attributes:
        name (str): Le nom de l'utilisateur.
        email (str): L'adresse e-mail de l'utilisateur.
        password (str): Le mot de passe de l'utilisateur.
    """

    def __init__(self, name, email, password):
        self.__name = name   # attribut privé
        self.__email = email   # attribut privé
        self.__password = password   # attribut privé

    def get_name(self):
        """Retourne le nom de l'utilisateur."""
        return self.__name

    def set_name(self, name):
        """Modifie le nom de l'utilisateur."""
        self.__name = name

    def get_email(self):
        """Retourne l'adresse e-mail de l'utilisateur."""
        return self.__email

    def set_email(self, email):
        """Modifie l'adresse e-mail de l'utilisateur."""
        self.__email = email

    def get_password(self):
        """Retourne le mot de passe de l'utilisateur."""
        return self.__password

    def set_password(self, password):
        """Modifie le mot de passe de l'utilisateur."""
        self.__password = password



class Task:
    def __init__(self, description, status, assignee, categories, deadline=None, difficulty=1, priority=1, energy=1):
        self.__description = description   # attribut privé
        self.__status = status   # attribut privé
        self.__assignee = assignee   # attribut privé
        self.__categories = categories   # attribut privé
        self.__deadline = deadline   # attribut privé
        self.__difficulty = difficulty   # attribut privé
        self.__priority = priority   # attribut privé
        self.__energy = energy   # attribut privé

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

    def get_categories(self):   # méthode d'instance publique
        return self.__categories

    def set_categories(self, categories):   # méthode d'instance publique
        self.__categories = categories

    def get_deadline(self):   # méthode d'instance publique
        return self.__deadline

    def set_deadline(self, deadline):   # méthode d'instance publique
        self.__deadline = deadline

    def get_difficulty(self):   # méthode d'instance publique
        return self.__difficulty

    def set_difficulty(self, difficulty):   # méthode d'instance publique
        self.__difficulty = difficulty

    def get_priority(self):   # méthode d'instance publique
        return self.__priority

    def set_priority(self, priority):   # méthode d'instance publique
        self.__priority = priority

    def get_energy(self):   # méthode d'instance publique
        return self.__energy

    def set_energy(self, energy):   # méthode d'instance publique
        self.__energy = energy


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

    def add_task(self, task):   # méthode d'instance publique
        self.__tasks.append(task)

    def remove_task(self, task):   # méthode d'instance publique
        self.__tasks.remove(task)

    def get_tasks(self):   # méthode d'instance publique
        return self.__tasks

    def add_note(self, note):   # méthode d'instance publique
        self.__notes.append(note)

    def remove_note(self, note):   # méthode d'instance publique
        self.__notes.remove(note)

    def get_notes(self):   # méthode d'instance publique
        return self.__notes

    def generate_report(self):  
        print(f"Report for project '{self.__name}':")
        for task in self.get_tasks():
            print(f"- {task.get_description()}: {task.get_status()}")

        print(f"\nNotes for project '{self.__name}':")
        for note in self.get_notes():
            print(f"- {note.get_title()}: {note.get_content()}")
