from django.shortcuts import render
posts = [
	{
		'author': 'Shuttle Client',
		'title': 'Patric Maina Testimonial',
		'content': '"I have been using 2NK for a period of and I salute the drivers, conductors and all the staff for providing efficient transport services."',
		'date_posted': 'February 12, 2019'
	},
	{
		'author': 'Parcel Client',
		'title': 'Esther Testimonial',
		'content': '"I run a Hardware store in Nyeri and all my stoke are transported by 2NK parcel services which reduces hustle hustle of travelling to Nairobi now and then. They are efficient and reliable."',
		'date_posted': 'February 12, 2019'
	},
	{
		'author': 'Matatu Owner',
		'title': 'Titus Mwangi',
		'content': '"I bought a second hand Matatu and then joined 2NK SACCO since then I have benefited greatly from this SACCO. Anyone in the transport business, SACCOs are important. 2NK SACCO is open for all."',
		'date_posted': 'February 12, 2019'
	}


]
# Create your views here.
def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)  

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

def services(request):
	return render(request, 'blog/services.html', {'title': 'Services'})

def membership(request):
	return render(request, 'blog/membership.html', {'title': 'Membership'})

def infocenter(request):
	return render(request, 'blog/infocenter.html', {'title': 'Infocenter'})

def CSR(request):
	return render(request, 'blog/CSR.html', {'title': 'CSR'})

def contact(request):
	return render(request, 'blog/contact.html', {'title': 'Contact'})
