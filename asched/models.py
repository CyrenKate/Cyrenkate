from django.db import models

class clientbasicinfo(models.Model):
	cl_surname = models.CharField(max_length=200, null=True)
	cl_firstname = models.CharField(max_length=200, null=True)
	cl_middlename = models.CharField(max_length=200, null=True)
	cl_email = models.EmailField(max_length=200)
	cl_contact = models.IntegerField(default="")
	

class portraitshot(models.Model):
	shot_choices = {
		('headshot', 'headshot'),
		('bust', 'bust'),
		('halfbody', 'halfbody'),
		('wholebody', 'wholebody'),
	}
	shot = models.CharField(max_length=20, choices=shot_choices)	
	shot_price = models.CharField(max_length=200)

	art_choices = {
		('anime style', 'anime style'),
		('chibi style', 'chibi style'),
		('pixel art', 'pixel art'),
		('vector art', 'vector art'),
	}
	art = models.CharField(max_length=20, choices=art_choices)
	art_price = models.CharField(max_length=200)

	color_choices = {
		('sketch', 'sketch'),
		('black&white', 'black&white'),
		('full color', 'full color'),
	}
	color = models.CharField(max_length=20, choices=color_choices)
	color_price = models.CharField(max_length=200)

	size_choices = {
		('2000 x 2000 px', '2000 x 2000 px'),
		('3300 x 2550 px', '3300 x 2550 px'),
		('4000 x 4000 px', '4000 x 4000 px'),
	}
	sizes = models.CharField(max_length=20, choices=size_choices)
	size_price = models.CharField(max_length=200)
	

class clientattribute(models.Model):
	userid = models.ForeignKey(clientbasicinfo, null=True, on_delete=models.CASCADE)
	currentdatetime = models.DateField(auto_now_add=True)
	# imagereferences = models.ImageField(upload_to='uploads', blank=True)
	background_choices = {
				('transparent', 'transparent'),
				('simple','simple'),
	}
	background = models.CharField(max_length=20, choices=background_choices)
	fileformat_choices = {

				('PNG', 'PNG'),
				('TIFF', 'TIFF'),
				('PDF', 'PDF'),
	
	}
	fileformat = models.CharField(max_length=20, choices=fileformat_choices )	
	# totalpricetopay = models.CharField(max_length=200)

	
