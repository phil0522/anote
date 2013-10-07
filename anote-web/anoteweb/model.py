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
    description = ndb.StringProperty(indexed=False)
    
class Thing(ndb.Model):
    STATE_THING = 1
    STATE_WAITING = 2
    STATE_ACTIONABLE = 3
    STATE_DELEGATE = 4
    STATE_DEFERRED = 5
    STATE_INCUBATE = 6
    STATE_DONE = 7
    
    STATES = (
        (STATE_THING, _('thing')),
        (STATE_WAITING, _('waiting'))
        (STATE_ACTIONABLE, _('actionable')),
        (STATE_DELEGATE, _('delegated')),
        (STATE_DEFERRED, _('deferred')),
        (STATE_INCUBATE, _('incubate')),
        (STATE_DONE, _('done')),
    )
    
    parent = ndb.KeyProperty()
    description = ndb.TextProperty(required=True)
    status = ndb.IntegerProperty(choices=STATES)
    
    
    
    
    
    
