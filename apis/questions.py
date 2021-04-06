from .models import Questions, Hints

filename = ""

with open(filename) as f:
    for line in f:
        questionName = ""
        answer = ""
        imageLocation = ""
        hint1 = ""
        hint2 = ""
        hint3 = ""
        question = Questions.objects.create(

        )
        hints = Hints.objects.create(

        )
        question.save()
        hints.save()
