
# scheduler which allows tasks to be run immediately on startup
# if necessary
# https://groups.google.com/forum/?fromgroups#!msg/celery-users/dJfnNpvl-aI/ctx0-3QgdQoJ
 
from djcelery import schedulers
from pihub.packages.models import get_mirror_state, FetchStatus


class ImmediateFirstEntry(schedulers.ModelEntry):

    def is_due(self):
        if self.name == 'pihub.packages.tasks.check_fetch_index':
            return get_mirror_state().index_fetch_status == FetchStatus.NOT_STARTED, 0
        return super(ImmediateFirstEntry, self).is_due()



class Scheduler(schedulers.DatabaseScheduler):
    Entry = ImmediateFirstEntry

