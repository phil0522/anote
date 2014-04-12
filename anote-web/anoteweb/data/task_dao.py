from google.appengine.ext import db

class TaskDao:
  def __init__(self):
    pass

  def save_task(self, task):
    key = task.put()
    return key

  def create_task_notes(self, task, note):
    task.notes.append(note)
    return self.save_task(task)

  def remove_task_notes(self, task, note):
    task.notes.remove(note)
    self.save_task(task)


