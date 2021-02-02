from django.db import models

# Create your models here.
class Photo(models.Model):
    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.FileField(upload_to="room_photos")
    board = models.ForeignKey(
        "Board", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption



class Board(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=80)
    description = models.TextField()

    host = models.ForeignKey('users.User', related_name='boards', on_delete=models.CASCADE)

    def first_photo(self):
        photo, = self.photos.all()[:1]
        return photo.file.url