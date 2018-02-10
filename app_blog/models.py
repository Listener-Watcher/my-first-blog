from django.db import models
from django.utils import timezone

#models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database
class Post(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)# a link to another model
	title = models.CharField(max_length=200)						# define text with a limited number of char
	text = models.TextField()										# for long text without a limit
	created_date = models.DateTimeField(default=timezone.now)		# date and time(might change based on version)
	published_date = models.DateTimeField(blank=True,null=True)		# date and time again
	
	#publish method
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	#return a string
	def __str__(self):
		return self.title
		
class Comment(models.Model):
	post=models.ForeignKey('app_blog.Post',related_name='comments')
	author=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	approved_comment=models.BooleanField(default=False)
	
	def approve(self):
		self.approved_comment=True;
		self.save()
	
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)
		
	def __str__(self):
		return self.text
