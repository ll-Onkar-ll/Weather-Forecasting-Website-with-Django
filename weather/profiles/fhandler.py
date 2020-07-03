from pathlib import Path

def handle_uploaded_file(f, usr):
	path = "E:/Django_Projects/weather/static/submissions/" + usr + "/"
	Path(path).mkdir(parents=True, exist_ok=True)
	fpath = path + f.name
	with open(fpath, 'wb+') as destination:
		for chunk in f.chunks():
		    destination.write(chunk)
		    print(destination)
	return "Success"