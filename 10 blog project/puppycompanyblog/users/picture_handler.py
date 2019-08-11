import os
from PIL import Image # Python Imaging Library 
from flask import url_for, current_app

def add_profile_pic(pic_upload, username):
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1] # file extension, file type. [-1] means we are saving the part after the '.'
    storage_filename = str(username)+'.'+ext_type
    filepath = os.path.join(current_app.root_path, 'static/profile_pics', storage_filename) #the entire filepath = grab the current app path, find 'static/profile_pics' within and add the storage_filename 
    
    output_size = (200, 200)
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)
    
    return storage_filename
