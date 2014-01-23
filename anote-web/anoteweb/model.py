from google.appengine.ext import ndb
    
def _progress_validator(x):
    if x < 0 or x > 100:
        raise "progress should range in [0,100]"
    return None

class Project(ndb.Model):
    """Projects associated with a task"""
    parent = ndb.KeyProperty()
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(indexed=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    modified = ndb.DateTimeProperty(auto_now=True)
    progress = ndb.IntegerProperty(default=0, validator=_progress_validator)

class Context(ndb.Model):
    parent = ndb.KeyProperty()
    name = ndb.StringProperty(required=True)
    full_name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(indexed=False)



class Task(ndb.Model):
    parent_task = ndb.KeyProperty()
    sub_tasks = ndb.StringListProperty(repeated=True)

    STATUS_PENDING = 'pending'
    STATUS_DONE = 'done'
    STATUS_ABORTED = 'aborted'
    ALL_TASK_STATUS = (STATUS_ABORTED, STATUS_DONE, STATUS_PENDING)

    status = ndb.StringProperty(choices=ALL_TASK_STATUS)
    contexts = ndb.StringProperty(repeated=True)






    
    
