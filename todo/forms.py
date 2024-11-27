from django import forms

from todo.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "done",
            "tags",
        ]
        widgets = {
            "deadline":
                forms.DateTimeInput(
                    attrs={
                        "type": "datetime-local",
                        "class": "form-control"
                    }
                )
        }