from django.db import models


class TaskList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name

        }

class Task(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    due_on = models.DateTimeField()
    task_list = models.ForeignKey(TaskList,on_delete=models.CASCADE,related_name='tasks')
    status = models.CharField(max_length=10)
    def __str__(self):
        return "{}: {},{},{},{}".format(self.name, self.created_at,self.task_list, self.due_on,self.status)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at':self.created_at,
            'due_on':self.due_on,
            'task_list':self.task_list.to_json(),
            'status':self.status
        }
