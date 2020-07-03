from django.shortcuts import render
from profiles.forms import ProfilePicForm
from profiles.models import ProfilePic
from django.contrib.auth.models import User
from .fhandler import handle_uploaded_file

def profile(request):
	username = request.user.username
	user = User.objects.get(username=username)
	if request.method == "POST":
		if request.POST.get('submit') == 'upload':
			prof_form = ProfilePicForm(request.POST, request.FILES)
			msg = handle_uploaded_file(request.FILES['file'], username)
			if (msg == "Success") and prof_form.is_valid():
				try:
					pp = ProfilePic.objects.get(user_id=user.id)
					pp.delete()
				except ProfilePic.DoesNotExist:
					pass
				obj = prof_form.save(commit=False)
				obj.user = user
				print(user)
				obj.pic = request.FILES['file'].name
				print(request.FILES['file'].name)
				obj.save()
			else:
				print(prof_form.errors)
	else:
		msg = "ab"
	print(msg)
	try:
		pp = ProfilePic.objects.get(user_id=user.id)
		pic = pp.pic
		pth = "submissions/" + username + "/"
		pth = pth + pic
	except ProfilePic.DoesNotExist:
		pth = "imgs/wet.png"
	return render(request, 'settings.html', {'usr': username, 'fn': pth, 'msg': msg})
