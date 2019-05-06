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
    created_at = models.DateTimeField(auto_now=True)
    due_on = models.DateTimeField()
    status = models.CharField(max_length=20)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return 'id: {}, name: {}, due_on: {}, status: {}, created_at: {}'.format(self.id, self.name, self.due_on, self.status, self.created_at)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'due_on': self.due_on,
            'status': self.status,
            'created_at': self.created_at
        }
