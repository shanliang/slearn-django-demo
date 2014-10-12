import time,os
def handle_uploaded_file(f):
    file_name = ""

    try:
        path = "media/photos" + time.strftime('/%Y%m%d%H%M%S/')
        if not os.path.exists(path):
            os.makedirs(path)
            file_name = path + f.name
            destination = open(file_name, 'wb+')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
    except Exception, e:
        print e

    return file_name