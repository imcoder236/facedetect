from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse, HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import connection
from django.http.response import HttpResponseServerError
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.core.files.storage import FileSystemStorage
from PIL import Image, ImageDraw
from django.core.mail import send_mail
from django.conf import settings
import cv2
import os
import numpy as np
import threading
from django.views.decorators import gzip
from .models import *
from .forms import *
import face_recognition.api as face_recognition
import base64
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import datetime
from django.core.mail import EmailMessage
vc="";

import random
import string

def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

def email(request):
    reset1=request.POST.get('reset_mail')
    userdetails = User.objects.filter(username=request.POST.get('Username'))[0]
    reset_email = userdetails.email
    uid = userdetails.id
    if reset1 == reset_email:
        random_pass=get_random_alphaNumeric_string(12)
        user_acc =User.objects.get(username=request.POST.get('Username'))
        user_acc.set_password(random_pass)
        user_acc.save()
        mail='<h3>Hello {},</h3>&emsp;&emsp;&emsp;Your new password is <b>{}</b> . <br><br> ThankYou'.format(userdetails.first_name,random_pass);
        email = EmailMessage('New Password', mail, to=[reset1])
        email.content_subtype = "html"
        email.send()
        change_passwd = passwd()
        change_passwd.user_id = uid
        change_passwd.username = request.POST.get('Username')
        change_passwd.umail = reset1
        change_passwd.date = datetime.datetime.now()
        change_passwd.save()
    else:
         return HttpResponse("<script>alert('Email ID mismatched. Enter correct email address to request new password'); windows.location.href('/');</script>")
    return redirect('/')

def success(request):
    return HttpResponse('successfully uploaded')

def admin_login(request):
    return render(request,'admin/a_login.html')

def users_data(request):
    user_detail = User.objects.all()
    return render(request,'include/user_data.html',{'user_detail':user_detail})

def users_repo(request):
    cursor = connection.cursor()
    cursor.execute("select auth_user.first_name,auth_user.email,face_app_users_report.in_time,face_app_users_report.out_time FROM auth_user INNER JOIN face_app_users_report on auth_user.id=face_app_users_report.user_id_id ")
    row = cursor.fetchall()
    return render(request,'include/user_repo.html',{'user_report':row})

def admin_home(request):
    cursor = connection.cursor()
    cursor.execute("select auth_user.first_name,auth_user.email,face_app_users_report.in_time,face_app_users_report.out_time FROM auth_user INNER JOIN face_app_users_report on auth_user.id=face_app_users_report.user_id_id ")
    row = cursor.fetchall()
    user_count=User.objects.count()
    user_detail = User.objects.all()
    change_pass = passwd.objects.all()
    return render(request,'admin/a_home.html',{'sidebar':'true','user_count':user_count,'user_report':row,'user_detail':user_detail,'change_pass':change_pass})

def admin_request(request):
    if request.method == 'POST':
        username = request.POST.get('admin_id')
        password = request.POST.get('admin_pass')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active :
                if user.is_superuser :
                    user = User.objects.filter(username=username)[0]
                    request.session['id'] = user.id
                    request.session['name'] = user.first_name
                    request.session['surname'] = user.last_name
                    userreport=users_report()
                    userreport.in_time = datetime.datetime.now()
                    userreport.user_id=user
                    userreport.save()
                    request.session['user_login_id'] =userreport.id
                    return redirect('/ad66cc5f7daad7a9c5b53d3a04cc3308/')
                else:
                    return render(request,'admin/a_login.html',{'superuser':'false'})
            else:
                return render(request,'admin/a_login.html',{'inactive':'false'})
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request,'admin/a_login.html',{'fail':'false'})
    else:
        return render(request, 'index.html', {})

def adduser(request):
    uid = request.POST.get('id_user')
    uname = request.POST.get('uname')
    umail = request.POST.get('umail')
    pas = request.POST.get('upass')
    user_acc = User()
    user_acc.username = uid
    user_acc.first_name = uname
    user_acc.email = umail
    user_acc.set_password(pas)
    user_acc.save()
    user_count=User.objects.count()
    return redirect('/ad66cc5f7daad7a9c5b53d3a04cc3308/')

def update_profile(request):
    uid = request.POST.get('uid')
    updatepro = User.objects.get(id=uid)
    upname = request.POST.get('name')
    upmail = request.POST.get('uemail')
    updatepro.first_name = upname
    updatepro.email = upmail
    updatepro.save()
    return redirect('/ad66cc5f7daad7a9c5b53d3a04cc3308/')

def update_password(request):
    up_pass=User.objects.get(id=request.session['id'])
    old_pass=request.POST.get('cupass')
    cu_user=up_pass.username
    new_pass=request.POST.get('confpass')
    user= authenticate(username=cu_user,password=old_pass)
    if user:
        up_pass.set_password(new_pass)
        up_pass.save()
    return HttpResponse("done")

def dashboard(request):
    count_face=uploadImage.objects.count()
    count_cam=ip_address.objects.count()
    count_rec=live_track_record.objects.count()
    count_area=location.objects.count()
    return render(request, 'dashboard.html',{'face_count':count_face,'count_cam':count_cam,'count_rec':count_rec,'count_area':count_area})

def record_table(request):
    records = live_track_record.objects.all()
    return render(request, 'include/report_tb.html',{'records': records})

def ip_record_table(request):
    ip_records = ip_address.objects.all()
    return render(request, 'include/ipstatus.html',{'ip_add': ip_records})

def facial_database(request):
    retrive_facial_db = uploadImage.objects.all()
    face_name = uploadImage.objects.all()
    svalue = request.POST.get('f_search')
    if svalue != '' and svalue is not None:
        retrive_facial_db = retrive_facial_db.filter(name = svalue)
    return render(request,"facial_db.html", { 'retrive_facial_db': retrive_facial_db , 'face_name': face_name})

def track(request):
    retrive_name = uploadImage.objects.all()
    retrive_area = location.objects.all()
    return render(request,'track.html',  { 'retrive_name': retrive_name , 'retrive_area': retrive_area})

def load_ip(request):
    retrive_ip = ip_address.objects.all()
    area11 = request.GET.get('area1')
    retrive_ip = retrive_ip.filter(area = area11)
    return render(request, 'include/ipadd.html', {'retrive_ip': retrive_ip})

def web_upload(request):
    name = request.GET.get('id_webcam')
    webpic = request.FILES.get('imgBase64')
    return render(request,'dashboard.html')

def settings(request):
    retrive_area = location.objects.all()
    area12 = request.POST.get('area')
    if area12 != '' and area12 is not None:
        add_area = location()
        add_area.area = area12
        add_area.save()
    cam_add = request.POST.get('cam_add')
    ip = request.POST.get('ip')
    if cam_add != '' and cam_add is not None and ip != '' and ip is not None:
        add_cam = ip_address()
        add_cam.area = cam_add
        add_cam.ip = ip
        add_cam.save()
    records = ip_address.objects.all()
    return render(request,'setting.html',{ 'retrive_area': retrive_area,'records': records})

def report(request):
    retrive_track_record=live_track_record.objects.all()
    return render(request,'report.html',{ 'retrive_track_record': retrive_track_record})

def  user_login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                user = User.objects.filter(username=request.POST['Username'])[0]
                request.session['id'] = user.id
                request.session['name'] = user.first_name
                request.session['username'] = user.username
                request.session['email'] = user.email
                userreport=users_report()
                userreport.in_time = datetime.datetime.now()
                userreport.user_id=user
                userreport.save()
                request.session['user_login_id'] =userreport.id
                return redirect('../f90453ec712ce4505cc425e7e881e1d58ea274c3/')
            else:
                return render(request,'index.html',{'inactive':'false'})
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request,'index.html',{'fail':'false'})
    else:
        return render(request, 'index.html', {})

def logout(request):
    users_report.objects.filter(id=request.session['user_login_id']).update(out_time= datetime.datetime.now())
    request.session.flush()
    return render(request,'index.html')

def image_upload(request):
    if request.method=="POST":
        name = request.POST.get('id_name')
        pic = request.FILES.get('id_picture')
        if name != '' and name is not None and pic != '' and pic is not None:
            uploadPic = uploadImage()
            uploadPic.name = name
            uploadPic.picture = pic
            uploadPic.save()
            return redirect('dashboard')
        else:
            return redirect('dashboard')

def web_image_upload(request):
    if request.method=="GET":
        name = request.GET.get('name1')
        pic = request.GET.get('person_img')
        _format, _img_str = pic.split(';base64,')
        _name, ext = _format.split('/')
        if not name:
            name = _name.split(":")[-1]
        data = ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))
        uploadPic = uploadImage()
        uploadPic.name = name
        uploadPic.picture=data
        uploadPic.save()
        return HttpResponse("Done")

def delete_image(request, pk):
    if request.method == 'POST':
        uploadImage1 = uploadImage.objects.get(pk=pk)
        uploadImage1.delete()
    return redirect('facial_database')

def delete_user(request,pk):
    if request.method == 'POST':
        user_db = users.objects.get(id=pk)
        user_db.delete()
        return redirect('/ad66cc5f7daad7a9c5b53d3a04cc3308/')

def disable_user(request,pid):
    if request.method == 'GET':
        user_db = User.objects.get(id = pid)
        user_db.is_active =0
        user_db.save()
        return redirect('/ad66cc5f7daad7a9c5b53d3a04cc3308/')

def enable_user(request,eid):
    if request.method == 'GET':
        user_db = User.objects.get(id = eid)
        user_db.is_active =1
        user_db.save()
        return redirect('/ad66cc5f7daad7a9c5b53d3a04cc3308/')

def p_details(request, pid):
    p_detail1 = uploadImage.objects.filter(id = pid)
    state1 = state.objects.all()
    city2 = city.objects.all()
    retrive_track_record=live_track_record.objects.raw('SELECT * FROM face_app_live_track_record WHERE user_id_id = %s', [pid])
    return render(request,'details.html',{'p_detail1':p_detail1,'state1':state1,'city2':city2,'retrive_track_record': retrive_track_record})

def webcam(request):
    cap = cv2.VideoCapture(0)
    k = cv2.waitKey(0)
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if k == 27:
            cv2.destroyAllWindows()
        elif k == ord('s'):
            cv2.imwrite('messigray.png',gray)
            cv2.destroyAllWindows()

def edit_pofile(request):
    uid =  request.POST.get('uid')
    email1 = request.POST.get('emailid')
    gender1 = request.POST.get('inlineRadioOptions')
    dob1 = request.POST.get('dob')
    add1 = request.POST.get('add')
    pin1 = request.POST.get('pin')
    aadhar1 = request.POST.get('aadhar')
    phone1 = request.POST.get('phone')

    u_profile = uploadImage.objects.get(id=uid)
    if dob1 != '' and dob1 is not None:
        u_profile.email = email1
        u_profile.gender = gender1
        u_profile.dob = dob1
        u_profile.address = add1
        u_profile.pincode = pin1
        u_profile.aadharno = aadhar1
        u_profile.phone = phone1
        u_profile.save()
    else:
        u_profile.email = email1
        u_profile.gender = gender1
        u_profile.address = add1
        u_profile.pincode = pin1
        u_profile.aadharno = aadhar1
        u_profile.phone = phone1
        u_profile.save()
    return redirect('/c29aea40b84e04595f2fec3e5918530f71f31a7f/'+str(uid))

def edit_photo(request):
    uid =  request.POST.get('edit_pic')
    u_image = request.FILES.get('eidt_pro')
    u_profile = uploadImage.objects.get(id=uid)
    u_profile.picture = u_image
    u_profile.save()
    return redirect('c29aea40b84e04595f2fec3e5918530f71f31a7f/'+str(uid))

class trace_face(object):
    def __init__(self):
        self.vcc=vc
        if self.vcc=='http://0:/' or self.vcc=='0':
            self.vcc=0
        self.video = cv2.VideoCapture(self.vcc)
    def __del__(self):
        self.video.release()
    def get_frame(self):
        return self.video.read()

def gen(camera):
    images=[]
    encodings=[]
    names=[]
    files=[]
    prsn=uploadImage.objects.all()
    for p in prsn:
        images.append(p.name+'_image')
        encodings.append(p.name+'_face_encoding')
        files.append(p.picture)
        names.append(p.name)
    for i in range(0,len(images)):
        images[i]=face_recognition.load_image_file(files[i])
        encodings[i]=face_recognition.face_encodings(images[i])[0]
    known_face_encodings = encodings
    known_face_names = names
    try:
        while True:
            ret,frame = camera.get_frame()
            if ret:
                rgb_frame = frame[:, :, ::-1]
                face_locations = face_recognition.face_locations(rgb_frame)
                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
                for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                ret,jpeg = cv2.imencode('.jpg',frame)
                frame=jpeg.tobytes()
                yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        camera.__del__()
        cv2.destroyAllWindows()
    except(cv2.error):
        return HttpResponse('error')
    finally:
        camera.__del__()
        cv2.destroyAllWindows()

@gzip.gzip_page
def home1(request):
    try:
        global vc
        vc =  request.POST.get('ip_address11')
        ipstatus=ip_status_report()
        ipstatus.ipadd = vc
        ipstatus.save()
        return StreamingHttpResponse(gen(trace_face()),content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        print("aborted")

def photo_detect(request):
    try:
        uploaded_file_url=''
        if request.method == 'POST' and request.FILES['load_img']:
            myfile = request.FILES['load_img']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
        else:
            return HttpResponse('<script>alert("Image Uploading Failed"); window.close();</script>')
        images=[]
        encodings=[]
        names=[]
        files=[]
        prsn=uploadImage.objects.all()
        for p in prsn:
            images.append(p.name+'_image')
            encodings.append(p.name+'_face_encoding')
            files.append(p.picture)
            names.append(p.name)
        for i in range(0,len(images)):
            images[i]=face_recognition.load_image_file(files[i])
            encodings[i]=face_recognition.face_encodings(images[i])[0]
        known_face_encodings = encodings
        known_face_names = names
        unknown_image = face_recognition.load_image_file(uploaded_file_url[1:])
        face_locations = face_recognition.face_locations(unknown_image)
        face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
        pil_image = Image.fromarray(unknown_image)
        draw = ImageDraw.Draw(pil_image)
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
            text_width, text_height = draw.textsize(name)
            draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
            draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
        del draw
        pil_image.show()
        return HttpResponse('<script>window.close();</script>')
    except:
        print("aborted")
        return HttpResponse('<script>alert("Image Rendering Failed"); window.close();</script>')

# def video_detect(request):
#     try:
#         if request.method == 'POST' and request.FILES['load_video']:
#             myfile = request.FILES['load_video']
#             fs = FileSystemStorage()
#             filename = fs.save(myfile.name, myfile)
#             uploaded_file_url = fs.url(filename)
#         vc=uploaded_file_url[1:]
#         video_capture = cv2.VideoCapture(vc)
#         images=[]
#         encodings=[]
#         names=[]
#         files=[]
#         prsn=uploadImage.objects.all()
#         for p in prsn:
#             images.append(p.name+'_image')
#             encodings.append(p.name+'_face_encoding')
#             files.append(p.picture)
#             names.append(p.name)
#         for i in range(0,len(images)):
#             images[i]=face_recognition.load_image_file(files[i])
#             encodings[i]=face_recognition.face_encodings(images[i])[0]
#         known_face_encodings = encodings
#         known_face_names = names
#         while True:
#             ret, frame = video_capture.read()
#             rgb_frame = frame[:, :, ::-1]
#             face_locations = face_recognition.face_locations(rgb_frame)
#             face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
#             for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#                 matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#                 name = "Unknown"
#                 face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#                 best_match_index = np.argmin(face_distances)
#                 if matches[best_match_index]:
#                     name = known_face_names[best_match_index]
#                 cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#                 cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#                 font = cv2.FONT_HERSHEY_DUPLEX
#                 cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
#
#             resized = cv2.resize(frame, (600, 400), interpolation = cv2.INTER_AREA)
#             cv2.imshow('Camera '+str(vc), resized)
#             key = cv2.waitKey(20)
#             if cv2.waitKey(1) & 0xFF == ord('q') or key == 27:
#                 break
#         video_capture.release()
#         cv2.destroyAllWindows()
#         BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         os.remove(os.path.join(BASE_DIR,vc))
#     except:
#         return render(request,'dashboard.html',{'video_err_msg':'Video Error '})
#     return HttpResponse('<script>window.close();</script>')

@gzip.gzip_page
def video_detect(request):
    try:
        global vc
        if request.method == 'POST' and request.FILES['load_video']:
            myfile = request.FILES['load_video']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
        vc=uploaded_file_url[1:]
        return StreamingHttpResponse(gen(trace_face()),content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        return render(request,'dashboard.html',{'video_err_msg':'Video Error '})
