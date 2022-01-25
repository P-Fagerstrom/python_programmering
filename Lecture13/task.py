class Task:
    """A To-Do API handling Tasks. A task have a title, can be assigned to someone, 
    is either done or not and can have a description. 
    We will be hosting the tasks in a list of dictionaries directly on the server 
    so they will not persist between executions of the application
    """
    def __init__(self, id, title, assigned_to = "", completed = False, description = ""):
        self.__id = id
        self.title = title
        self.completed = completed
        self.assigned_to = assigned_to
        self.description = description
        
    @property
    def id(self):
        return self.__id
    
    def update(self, task_dict):
        if "title" in task_dict:
            self.title = task_dict["title"]
        if "description" in task_dict:
            self.description = task_dict["description"]
        if "completed" in task_dict:
            self.completed = task_dict["completed"]
        if "assigned_to" in task_dict:
            self.assigned_to = task_dict["assigned_to"]
            
    def to_json(self):
        return {"id":self.__id, "title": self.title, "assigned_to": self.assigned_to, 
                "completed": self.completed, "description": self.description}