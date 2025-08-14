import datetime
class Task:
    def __init__(self,title):
        self.title=title
        self.creation_date=datetime.datetime.now()
        self.is_completed=False
        self.is_pinned=False
        

    def mark_as_completed(self):
        self.is_completed=True

    def toggle_pin(self):
        self.is_pinned=not self.is_pinned
    
    def __str__(self):
        status_icon="a"
        if self.is_completed==True:
            status_icon="✅"
        else:
            status_icon = "❌"


        return f"{status_icon}-{self.title}"
    
    def to_dict(self):
        return{
            "title":self.title,
            "creation_date":self.creation_date.isoformat(),
            "is_completed":self.is_completed,
            "is_pinned":self.is_pinned
        }



