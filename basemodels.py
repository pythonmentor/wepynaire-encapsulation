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
    """Représente une tâche à effectuer dans le cadre d'un projet.

    Attributes:
        description (str): La description de la tâche.
        status (str): Le statut actuel de la tâche.
        assignee (User): L'utilisateur assigné à la tâche.
        categories (list): La liste des catégories de la tâche.
        deadline (date): La date limite de la tâche (facultatif).
        difficulty (int): La difficulté de la tâche (1 = facile, 5 = difficile).
        priority (int): Le niveau de priorité de la tâche (1 = basse, 5 = haute).
        energy (int): Le niveau d'énergie requis pour la tâche (1 = faible, 5 = élevé).
    """

    def __init__(self, description, status, assignee, categories, deadline=None, difficulty=1, priority=1, energy=1, project=None):
        self.__description = description   # attribut privé
        self.__status = status   # attribut privé
        self.__assignee = assignee   # attribut privé
        self.__categories = categories   # attribut privé
        self.__deadline = deadline   # attribut privé
        self.__difficulty = difficulty   # attribut privé
        self.__priority = priority   # attribut privé
        self.__energy = energy   # attribut privé
        self.__project = project   # attribut privé pour le projet
        self.__notes = []   # attribut privé pour les notes

    def get_description(self):
        """Retourne la description de la tâche."""
        return self.__description

    def set_description(self, description):
        """Modifie la description de la tâche."""
        self.__description = description

    def get_status(self):
        """Retourne le statut actuel de la tâche."""
        return self.__status

    def set_status(self, status):
        """Modifie le statut actuel de la tâche."""
        self.__status = status

    def get_assignee(self):
        """Retourne l'utilisateur assigné à la tâche."""
        return self.__assignee

    def set_assignee(self, assignee):
        """Modifie l'utilisateur assigné à la tâche."""
        self.__assignee = assignee

    def get_categories(self):
        """Retourne la liste des catégories de la tâche."""
        return self.__categories

    def set_categories(self, categories):
        """Modifie la liste des catégories de la tâche."""
        self.__categories = categories

    def get_deadline(self):
        """Retourne la date limite de la tâche."""
        return self.__deadline

    def set_deadline(self, deadline):
        """Modifie la date limite de la tâche."""
        self.__deadline = deadline

    def get_difficulty(self):
        """Retourne la difficulté de la tâche."""
        return self.__difficulty

    def set_difficulty(self, difficulty):
        """Modifie la difficulté de la tâche."""
        self.__difficulty = difficulty

    def get_priority(self):
        """Retourne le niveau de priorité de la tâche."""
        return self.__priority

    def set_priority(self, priority):
        """Modifie le niveau de priorité de la tâche."""
        self.__priority = priority

    def get_energy(self):
        """Retourne le niveau d'énergie requis pour la tâche"""
        return self.__energy

    def set_energy(self, energy):
        """Modifie le niveau d'énergie requis pour la tâche"""
        self.__energy = energy
        
    def get_project(self):
        return self.__project

    def set_project(self, project):
        self.__project = project

    def add_note(self, note):
        self.__notes.append(note)
        note.set_task(self)


class Note:
    """Représente une note créée par un utilisateur.

    Attributes:
        title (str): Le titre de la note.
        content (str): Le contenu de la note.
        author (User): L'auteur de la note.
    """

    def __init__(self, title, content, author, project=None, task=None):
        self.__title = title   # attribut privé
        self.__content = content   # attribut privé
        self.__author = author   # attribut privé
        self.__project = project   # attribut privé
        self.__task = task   # attribut privé

    def get_title(self):
        """Retourne le titre de la note."""
        return self.__title

    def set_title(self, title):
        """Modifie le titre de la note."""
        self.__title = title

    def get_content(self):
        """Retourne le contenu de la note."""
        return self.__content

    def set_content(self, content):
        """Modifie le contenu de la note."""
        self.__content = content

    def get_author(self):
        """Retourne l'auteur de la note."""
        return self.__author

    def set_author(self, author):
        """Modifie l'auteur de la note."""
        self.__author = author
        
        
class Document:
    def __init__(self, owner, file_type, added_date, is_draft=True):
        """
        Constructeur de la classe Document.

        :param owner: Le propriétaire du document.
        :type owner: str
        :param file_type: Le type de fichier du document.
        :type file_type: str
        :param added_date: La date à laquelle le document a été ajouté.
        :type added_date: datetime.date
        :param is_draft: Le statut de brouillon du document (par défaut True).
        :type is_draft: bool
        """
        self.__owner = owner   # attribut privé
        self.__file_type = file_type   # attribut privé
        self.__added_date = added_date   # attribut privé
        self.__is_draft = is_draft   # attribut privé

    def get_owner(self):
        """
        Retourne le propriétaire du document.

        :return: Le propriétaire du document.
        :rtype: str
        """
        return self.__owner

    def set_owner(self, owner):
        """
        Modifie le propriétaire du document.

        :param owner: Le nouveau propriétaire du document.
        :type owner: str
        """
        self.__owner = owner

    def get_file_type(self):
        """
        Retourne le type de fichier du document.

        :return: Le type de fichier du document.
        :rtype: str
        """
        return self.__file_type

    def set_file_type(self, file_type):
        """
        Modifie le type de fichier du document.

        :param file_type: Le nouveau type de fichier du document.
        :type file_type: str
        """
        self.__file_type = file_type

    def get_added_date(self):
        """
        Retourne la date à laquelle le document a été ajouté.

        :return: La date à laquelle le document a été ajouté.
        :rtype: datetime.date
        """
        return self.__added_date

    def set_added_date(self, added_date):
        """
        Modifie la date à laquelle le document a été ajouté.

        :param added_date: La nouvelle date à laquelle le document a été ajouté.
        :type added_date: datetime.date
        """
        self.__added_date = added_date

    def is_draft(self):
        """
        Retourne le statut de brouillon du document.

        :return: Le statut de brouillon du document.
        :rtype: bool
        """
        return self.__is_draft

    def set_draft(self, is_draft):
        """
        Modifie le statut de brouillon du document.

        :param is_draft: Le nouveau statut de brouillon du document.
        :type is_draft: bool
        """
        self.__is_draft = is_draft



class Project:
    """Représente un projet avec une liste de tâches, de notes et d'utilisateurs.

    Attributes:
        name (str): Le nom du projet.
        tasks (list): La liste des tâches du projet.
        notes (list): La liste des notes du projet.
        users (list): La liste des utilisateurs associés au projet.
        documents (list) la liste des documents associéts au projet.
    """

    def __init__(self, name):
        self.__name = name   # attribut privé
        self.__tasks = []   # attribut privé
        self.__notes = []   # attribut privé
        self.__users = []   # attribut privé
        self.__documents = []   # nouvel attribut privé

    def add_task(self, task):
        """Ajoute une tâche à la liste des tâches du projet."""
        self.__tasks.append(task)

    def remove_task(self, task):
        """Supprime une tâche de la liste des tâches du projet."""
        self.__tasks.remove(task)

    def get_tasks(self):
        """Retourne la liste des tâches du projet."""
        return self.__tasks

    def add_note(self, note):
        """Ajoute une note à la liste des notes du projet."""
        self.__notes.append(note)

    def remove_note(self, note):
        """Supprime une note de la liste des notes du projet."""
        self.__notes.remove(note)

    def get_notes(self):
        """Retourne la liste des notes du projet."""
        return self.__notes
    
    def add_document(self, document):  
        """Ajoute un document au projet."""
        self.__documents.append(document)

    def remove_document(self, document):  
        """Supprime un document du projet."""
        self.__documents.remove(document)

    def get_documents(self):
        """Retourne une liste de documents."""
        return self.__documents

    def generate_report(self):
        """Génère un rapport pour le projet en affichant les tâches et les notes."""
        print(f"Report for project '{self.__name}':")
        for task in self.get_tasks():
            print(f"- {task.get_description()}: {task.get_status()}")

        print(f"\nNotes for project '{self.__name}':")
        for note in self.get_notes():
            print(f"- {note.get_title()}: {note.get_content()}")
  
