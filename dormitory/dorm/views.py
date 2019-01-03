from django.contrib.auth import authenticate, login

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import *


# Create your views here.
def user_login(request):
    return render(request, 'dorm/login.html')

def confirm(request):
    if request.method == 'GET':
        return render(request, 'dorm/login.html')
    userid = request.POST.get('userAccount', '')
    password = request.POST.get('userPwd', '')
    db_info = Owner.objects.filter(user_id=int(userid))
    if db_info.__len__() == 0:
        return render(request, 'dorm/login.html', {'error_message': '用户名或密码错误！'})
    elif db_info[0].user_password == password:
        tab = {'舍管': 'housemaster',
               '导员': 'instructor',
               '学生': 'student',
               '书记': 'secretary',
               '维修人员': 'maintenance'}
        user = db_info[0]
        return render(request, 'dorm/confirm.html',
                      {'user_id': user.user_id, 'user_type': user.user_type, 'dir': tab[user.user_type]})
    else:
        return render(request, 'dorm/index.html', {'error_message': '用户名或密码错误！'})


def student_index(request):
    user_id = request.GET['user_id']
    student = Student.objects.get(pk=user_id)
    fee,mark,housemaster_set = None, None, None
    if student.roomid != None:
        fee = Fee.objects.get(pk=student.roomid)
        mark = Mark.objects.filter(roomid=student.roomid).order_by('-dt')[0]
        housemaster_set = Housemaster.objects.filter(buildingid=student.roomid.buildingid)
    secretary_set = Secretary.objects.filter(collegeid=student.classid.collegeid)
    content = {'student': student,
               'user_id': user_id,
               'fee': fee,
               'mark': mark,
               'secretary_set': secretary_set,
               'housemaster_set': housemaster_set}
    return render(request, 'dorm/student/index.html', content)

def student_mark(request):
    user_id = request.GET['user_id']
    student = Student.objects.get(pk=user_id)
    mark_set = Mark.objects.filter(roomid=student.roomid).order_by('dt')
    return render(request, 'dorm/student/mark.html', {'user_id': user_id, 'student': student, 'mark_set': mark_set})

def student_fee(request):
    user_id = request.GET['user_id']
    student = Student.objects.get(pk=user_id)
    fee_record_set = FeeRecord.objects.filter(roomid=student.roomid).order_by('dt')
    return render(request, 'dorm/student/fee.html',
                  {'user_id': user_id, 'student': student, 'fee_record_set': fee_record_set})

def student_unsubscribe(request):
    user_id = request.GET['user_id']
    return render(request, 'dorm/student/unsubscribe.html', {'user_id': user_id})

def student_repair_record(request):
    user_id = request.GET['user_id']
    student = Student.objects.get(pk=user_id)
    repair_set = Repair.objects.filter(roomid=student.roomid).order_by('book_dt')
    return render(request, 'dorm/student/repair_record.html',
                  {'user_id': user_id, 'student': student, 'repair_set': repair_set})

def student_building_select(request):
    user_id = request.GET['user_id']
    building_set = Building.objects.all()
    return render(request, 'dorm/student/building_select.html', {'user_id': user_id, 'building_set': building_set})

def student_unsubscribe_result(request):
    user_id = request.GET['user_id']
    student = Student.objects.get(pk=user_id)
    rec = QuitApply(sno=student, roomid=student.roomid, dt=timezone.now(), reason=request.POST['reason'])
    rec.save()
    return render(request, 'dorm/student/unsubscribe_result.html', {'user_id': user_id})

def student_repair(request):
    user_id = request.GET['user_id']
    return render(request, 'dorm/student/repair.html', {'user_id': user_id})

def student_new_repair(request):
    user_id = request.GET['user_id']
    student = Student.objects.get(pk=user_id)
    rep = Repair(item=request.POST['item'], roomid=student.roomid, book_dt=timezone.now(),
                 reason=request.POST['reason'])
    rep.save()
    return render(request, 'dorm/student/new_repair.html', {'user_id': user_id})

def student_building(request):
    user_id = request.GET['user_id']
    buildingid = request.GET['buildingid']

    class RoomItem(object):
        pass

    building = Building.objects.get(pk=buildingid)
    housemaster_set = Housemaster.objects.filter(buildingid=building)
    room_set = Room.objects.filter(buildingid=building)
    empty = building.amount - len(room_set)
    full = 0
    room_tab = []
    for room in room_set:
        tmp = RoomItem()
        tmp.name = room.name
        tmp.room_type = room.room_type
        tmp.capacity = room.capacity
        tmp.occupant = 0
        tmp.class_set = set()
        for student in Student.objects.filter(roomid=room):
            tmp.occupant += 1
            tmp.class_set.add(student.classid)
        if room.capacity == len(Student.objects.filter(roomid=room)):
            full += 1
            tmp.is_full = True
        room_tab.append(tmp)
    return render(request, 'dorm/student/building.html',
                  {'user_id': user_id, 'building': building, 'housemaster_set': housemaster_set, 'empty': empty,
                   'full': full, 'not_full': building.amount - empty - full, 'room_tab': room_tab})

def student_checkin(request):
    roomid = request.GET['roomid']
    room = Room.objects.get(pk=roomid)
    user_id = request.GET['user_id']
    student = Student.objects.get(pk=user_id)
    rec = EnterApply(sno=student, roomid=room, dt=timezone.now())
    rec.save()
    return render(request, 'dorm/student/checkin.html', {'user_id': user_id, 'roomid': roomid})


def instructor_index(request):
    user_id = request.GET['user_id']
    instructor = Instructor.objects.get(pk=user_id)
    class_set = Class.objects.filter(instructorid=instructor)
    return render(request, 'dorm/instructor/index.html',
                  {'user_id': user_id, 'instructor': instructor, 'class_set': class_set})

def instructor_class(request):
    user_id = request.GET['user_id']
    classid = request.GET['classid']
    student_set = Student.objects.filter(classid=classid)
    building_set = set()
    room_set = set()
    for student in student_set:
        if student.roomid != None:
            room_set.add(student.roomid)
            building_set.add(student.roomid.buildingid)
    return render(request, 'dorm/instructor/class.html',
                  {'user_id': user_id, 'classname': classid, 'student_set': student_set,
                   'student_amount': len(student_set),
                   'building_amount': len(building_set), 'room_amount': len(room_set)})

def instructor_lookup(request):
    user_id = request.GET['user_id']
    return render(request, 'dorm/instructor/lookup.html', {'user_id': user_id})

def instructor_checkin(request):
    user_id = request.GET['user_id']
    instructor = Instructor.objects.get(pk=user_id)
    rec_set = set()
    for rec in EnterApply.objects.all():
        if rec.sno.classid.instructorid == instructor:
            rec.occupant = 0
            for student in Student.objects.filter(roomid=rec.roomid):
                rec.occupant += 1
            rec_set.add(rec)
    return render(request, 'dorm/instructor/checkin.html', {'user_id': user_id, 'rec_set': rec_set})

def instructor_unsubscribe(request):
    user_id = request.GET['user_id']
    instructor = Instructor.objects.get(pk=user_id)
    rec_set = set()
    for rec in QuitApply.objects.all():
        if rec.sno.classid.instructorid == instructor:
            rec.occupant = 0
            for student in Student.objects.filter(roomid=rec.roomid):
                rec.occupant += 1
            rec_set.add(rec)
    return render(request, 'dorm/instructor/unsubscribe.html', {'user_id': user_id, 'rec_set': rec_set})

def instructor_member(request):
    user_id = request.GET['user_id']
    sno = request.GET['sno']
    student = Student.objects.get(pk=sno)
    student_set = Student.objects.filter(roomid=student.roomid)
    return render(request, 'dorm/instructor/member.html',
                  {'user_id': user_id, 'room': student.roomid, 'student_set': student_set, 'classid': student.classid})

def instructor_lookup_result(request):
    user_id = request.GET['user_id']
    student_set = Student.objects.filter(name=request.POST['name'])
    return render(request, 'dorm/instructor/lookup_result.html', {'user_id': user_id, 'student_set': student_set})

def instructor_checkin_result(request):
    user_id = request.GET['user_id']
    for id in request.POST.getlist('checked'):
        rec = EnterApply.objects.get(pk=id)
        rec.instructor_check = True
        rec.save()
        if rec.housemaster_check and rec.secretary_check:
            live_record = LiveRecord(sno=rec.sno, roomid=rec.roomid, enter_time=timezone.now(), quit_time=None)
            live_record.save()
            rec.delete()
    return render(request, 'dorm/instructor/checkin_result.html', {'user_id': user_id})

def instructor_unsubscribe_result(request):
    user_id = request.GET['user_id']
    for id in request.POST.getlist('checked'):
        rec = QuitApply.objects.get(pk=id)
        rec.instructor_check = True
        rec.save()
        if rec.housemaster_check and rec.secretary_check:
            live_record = LiveRecord.objects.filter(sno=rec.sno_id, roomid=rec.roomid).order_by('-enter_time')[0]
            live_record.quit_time = timezone.now()
            live_record.save()
            rec.delete()
    return render(request, 'dorm/instructor/unsubscribe_result.html', {'user_id': user_id})


def maintenance_index(request):
    user_id = request.GET['user_id']
    fixed_list = []
    unfixed_list = []
    for repair in Repair.objects.all():
        if repair.fix_dt is None and repair.maintenanceid is None:
            unfixed_list.append(repair)
        else:
            fixed_list.append(repair)
    return render(request, 'dorm/maintenance/index.html',
                  {'user_id': user_id, 'fixed_list': fixed_list, 'unfixed_list': unfixed_list})

def maintenance_repair(request):
    user_id = request.GET['user_id']
    repairid = request.GET['repairid']
    repair = Repair.objects.get(pk=repairid)
    return render(request, 'dorm/maintenance/repair.html', {'user_id': user_id, 'repair': repair})

def maintenance_repair_result(request):
    user_id = request.GET['user_id']
    repairid = request.GET['repairid']
    repair = Repair.objects.get(pk=repairid)
    repair.fix_dt = timezone.now()
    maintenance = Maintenance.objects.get(pk=user_id)
    repair.maintenanceid = maintenance
    repair.remark = request.POST['remark']
    repair.save()
    return render(request, 'dorm/maintenance/repair_result.html', {'user_id': user_id})


def housemaster_add_visitor(request):
    user_id = request.GET['user_id']
    return render(request, 'dorm/housemaster/add_visitor.html', {'user_id': user_id})

def housemaster_new_visitor(request):
    user_id = request.GET['user_id']
    housemaster = Housemaster.objects.get(pk=user_id)
    visitor = Visitor(name=request.POST['name'], sex=request.POST['sex'], document_type=request.POST['type'],
                      documentno=request.POST['id'], contact=request.POST['contact'], dt=timezone.now(),
                      housemasterid=housemaster)
    visitor.save()
    return render(request, 'dorm/housemaster/new_visitor.html', {'user_id': user_id})

def housemaster_building(request):
    class RoomItem(object):
        pass

    user_id = request.GET['user_id']
    housemaster = Housemaster.objects.get(pk=user_id)
    building = housemaster.buildingid
    housemaster_set = Housemaster.objects.filter(buildingid=building)
    room_set = Room.objects.filter(buildingid=building)
    empty = building.amount - len(room_set)
    full = 0
    room_tab = []
    for room in room_set:
        tmp = RoomItem()
        tmp.name = room.name
        tmp.room_type = room.room_type
        tmp.capacity = room.capacity
        tmp.occupant = 0
        tmp.class_set = set()
        for student in Student.objects.filter(roomid=room):
            tmp.occupant += 1
            tmp.class_set.add(student.classid)
        if room.capacity == len(Student.objects.filter(roomid=room)):
            full += 1
            tmp.is_full = True
        room_tab.append(tmp)
    return render(request, 'dorm/housemaster/building.html',
                  {'user_id': user_id, 'building': building, 'housemaster_set': housemaster_set, 'empty': empty,
                   'full': full,
                   'not_full': building.amount - empty - full, 'room_tab': room_tab})

def housemaster_checkin(request):
    user_id = request.GET['user_id']
    housemaster = Housemaster.objects.get(pk=user_id)
    building = housemaster.buildingid
    rec_set = set()
    for rec in EnterApply.objects.all():
        if rec.roomid.buildingid == building:
            rec.occupant = 0
            for student in Student.objects.filter(roomid=rec.roomid):
                rec.occupant += 1
            rec_set.add(rec)
    return render(request, 'dorm/housemaster/checkin.html', {'user_id': user_id, 'rec_set': rec_set})

def housemaster_checkin_result(request):
    user_id = request.GET['user_id']
    for id in request.POST.getlist('checked'):
        rec = EnterApply.objects.get(pk=id)
        rec.housemaster_check = True
        rec.save()
        if rec.instructor_check and rec.secretary_check:
            live_record = LiveRecord(sno=rec.sno, roomid=rec.roomid, enter_time=timezone.now(), quit_time=None)
            live_record.save()
            rec.delete()
    return render(request, 'dorm/housemaster/checkin_result.html', {'user_id': user_id})

def housemaster_index(request):
    user_id = request.GET['user_id']
    housemaster = Housemaster.objects.get(pk=user_id)
    building = housemaster.buildingid
    housemaster_set = Housemaster.objects.filter(buildingid=building)
    room_set = Room.objects.filter(buildingid=building)
    empty = building.amount - len(room_set)
    full = 0
    for room in room_set:
        if room.capacity == len(Student.objects.filter(roomid=room)):
            full += 1
    return render(request, 'dorm/housemaster/index.html',
                  {'user_id': user_id, 'housemaster': housemaster, 'building': building,
                   'housemaster_set': housemaster_set, 'empty': empty,
                   'full': full, 'not_full': building.amount - empty - full})

def housemaster_lookup(request):
    user_id = request.GET['user_id']
    return render(request, 'dorm/housemaster/lookup.html', {'user_id': user_id})

def housemaster_lookup_result(request):
    user_id = request.GET['user_id']
    student_set = Student.objects.filter(name=request.POST['name'])
    return render(request, 'dorm/housemaster/lookup_result.html', {'user_id': user_id, 'student_set': student_set})

def housemaster_member(request):
    user_id = request.GET['user_id']
    roomid = request.GET['roomid']
    room = Room.objects.get(pk=roomid)
    student_set = Student.objects.filter(roomid=room)
    return render(request, 'dorm/housemaster/member.html',
                  {'user_id': user_id, 'room': room, 'student_set': student_set})

def housemaster_unsubscribe(request):
    user_id = request.GET['user_id']
    housemaster = Housemaster.objects.get(pk=user_id)
    building = housemaster.buildingid
    rec_set = set()
    for rec in QuitApply.objects.all():
        if rec.roomid.buildingid == building:
            rec.occupant = 0
            for student in Student.objects.filter(roomid=rec.roomid):
                rec.occupant += 1
            rec_set.add(rec)
    return render(request, 'dorm/housemaster/unsubscribe.html', {'user_id': user_id, 'rec_set': rec_set})

def housemaster_unsubscribe_result(request):
    user_id = request.GET['user_id']
    for id in request.POST.getlist('checked'):
        rec = QuitApply.objects.get(pk=id)
        rec.housemaster_check = True
        rec.save()
        if rec.instructor_check and rec.secretary_check:
            live_record = LiveRecord.objects.filter(sno=rec.sno, roomid=rec.roomid).order_by('-enter_time')[0]
            live_record.quit_time = timezone.now()
            live_record.save()
            rec.delete()
    return render(request, 'dorm/housemaster/unsubscribe_result.html', {'user_id': user_id})

def housemaster_visitor(request):
    user_id = request.GET['user_id']
    housemaster = Housemaster.objects.get(pk=user_id)
    building = housemaster.buildingid
    visitor_set = Visitor.objects.filter(housemasterid=housemaster)
    return render(request, 'dorm/housemaster/visitor.html',
                  {'user_id': user_id, 'building': building, 'visitor_set': visitor_set})

def housemaster_mark(request):
    user_id = request.GET['user_id']
    return render(request, 'dorm/housemaster/mark.html', {'user_id': user_id})

def housemaster_new_mark(request):
    user_id = request.GET['user_id']
    housemaster = Housemaster.objects.get(pk=user_id)
    room = Room.objects.get(name=request.POST['room'], buildingid=housemaster.buildingid)
    mark = Mark(roomid=room, dt=timezone.now(), score=request.POST['score'], housemasterid=housemaster,
                remark=request.POST['remark'])
    mark.save()
    return render(request, 'dorm/housemaster/new_mark.html', {'user_id': user_id})


def secretary_building(request):
    user_id = request.GET['user_id']
    return render(request, 'dorm/secretary/building.html', {'user_id': user_id})

def secretary_checkin(request):
    user_id = request.GET['user_id']
    secretary = Secretary.objects.get(pk=user_id)
    rec_set = set()
    for rec in EnterApply.objects.all():
        if rec.sno.classid.collegeid == secretary.collegeid:
            rec.occupant = 0
            for student in Student.objects.filter(roomid=rec.roomid):
                rec.occupant += 1
            rec_set.add(rec)
    return render(request, 'dorm/secretary/checkin.html', {'user_id': user_id, 'rec_set': rec_set})

def secretary_checkin_result(request):
    user_id = request.GET['user_id']
    for id in request.POST.getlist('checked'):
        rec = EnterApply.objects.get(pk=id)
        rec.secretary_check = True
        rec.save()
        if rec.housemaster_check and rec.instructor_check:
            live_record = LiveRecord(sno=rec.sno, roomid=rec.roomid, enter_time=timezone.now(), quit_time=None)
            live_record.save()
            Student.objects.filter(pk=rec.sno).update(roomid=rec.roomid,buildingid=rec.roomid.buildingid)
            Room.objects.filter(pk=rec.roomid).update(capacity=rec.roomid.capacity - 1)
            rec.delete()
    return render(request, 'dorm/secretary/checkin_result.html', {'user_id': user_id})

def secretary_class(request):
    user_id = request.GET['user_id']
    classid = request.GET['classid']
    cls = Class.objects.get(pk=classid)
    student_set = Student.objects.filter(classid=cls)
    building_set = set()
    room_set = set()
    for student in student_set:
        if student.roomid != None:
            room_set.add(student.roomid)
            building_set.add(student.roomid.buildingid)
    return render(request, 'dorm/secretary/class.html',
                  {'user_id':user_id,'cls': cls, 'student_set': student_set, 'student_amount': len(student_set),
                   'building_amount': len(building_set), 'room_amount': len(room_set)})

def secretary_index(request):
    user_id = request.GET['user_id']
    secretary = Secretary.objects.get(pk=user_id)
    class_set = Class.objects.filter(collegeid=secretary.collegeid)
    student_amount = 0
    for cls in class_set:
        student_amount += len(Student.objects.filter(classid=cls))
    return render(request, 'dorm/secretary/index.html',
                  {'user_id':user_id,'secretary': secretary, 'class_set': class_set, 'class_amount': len(class_set),
                   'student_amount': student_amount})

def secretary_lookup(request):
    user_id = request.GET['user_id']
    return render(request, 'dorm/secretary/lookup.html',{'user_id':user_id})

def secretary_lookup_result(request):
    user_id = request.GET['user_id']
    student_set = Student.objects.filter(name=request.POST['name'])
    return render(request, 'dorm/secretary/lookup_result.html', {'user_id':user_id,'student_set': student_set})

def secretary_member(request):
    user_id = request.GET['user_id']
    sno = request.GET['sno']
    student = Student.objects.get(pk=sno)
    student_set = Student.objects.filter(roomid=student.roomid)
    return render(request, 'dorm/secretary/member.html',
                  {'user_id':user_id,'room': student.roomid, 'student_set': student_set, 'classid': student.classid.name})

def secretary_student(request):
    user_id = request.GET['user_id']
    return render(request, 'dorm/secretary/student.html',{'user_id':user_id})

def secretary_unsubscribe(request):
    user_id = request.GET['user_id']
    secretary = Secretary.objects.get(pk=user_id)
    rec_set = set()
    for rec in QuitApply.objects.all():
        if rec.sno.classid.collegeid == secretary.collegeid:
            rec.occupant = 0
            for student in Student.objects.filter(roomid=rec.roomid):
                rec.occupant += 1
            rec_set.add(rec)
    return render(request, 'dorm/secretary/unsubscribe.html', {'user_id':user_id,'rec_set': rec_set})

def secretary_unsubscribe_result(request):
    user_id = request.GET['user_id']
    for id in request.POST.getlist('checked'):
        rec = QuitApply.objects.get(pk=id)
        rec.secretary_check = True
        rec.save()
        if rec.housemaster_check and rec.instructor_check:
            live_record = LiveRecord.objects.filter(sno=rec.sno, roomid=rec.roomid).order_by('-enter_time')[0]
            live_record.quit_time = timezone.now()
            live_record.save()
            Student.objects.filter(pk=rec.sno_id).update(roomid=None, buildingid=None)
            Room.objects.filter(pk=rec.roomid).update(capacity=rec.roomid.capacity + 1)
            rec.delete()
    return render(request, 'dorm/secretary/unsubscribe_result.html', {'user_id': user_id})

def secretary_distribute(request):
    user_id = request.GET['user_id']
    secretary = Secretary.objects.get(pk=user_id)
    student_set = set()
    for temp in Student.objects.all():
        if temp.collegeid == secretary.collegeid:
            student_set.add(temp)
    return render(request, 'dorm/secretary/distribute.html',{'user_id':user_id,'student_set':student_set})

def secretary_distribute_clear(request):
    user_id = request.GET['user_id']
    secretary = Secretary.objects.get(pk=user_id)
    for temp in Student.objects.all():
        if temp.collegeid == secretary.collegeid:
            print(temp.sno_id,temp.buildingid,temp.roomid)
            if temp.roomid != None:
                Room.objects.filter(pk=temp.roomid).update(capacity= temp.roomid.capacity + 1)
            Student.objects.filter(pk=temp.sno_id).update(buildingid = None,roomid = None)
            print(temp.sno_id,temp.buildingid,temp.roomid)
    return render(request, 'dorm/secretary/distribute_clear.html',{'user_id':user_id})

def secretary_distribute_result(request):
    user_id = request.GET['user_id']
    secretary = Secretary.objects.get(pk=user_id)
    buildingid = request.POST['building']
    sex = request.POST['sex']
    sex = True if sex == '1' else False
    temp_arr = []
    for temp in Student.objects.all():
        if temp.collegeid == secretary.collegeid and temp.sex == sex:
            temp_arr.append(temp.sno_id)
    id = 0
    for temp in Room.objects.all():
        if id >= temp_arr.__len__():
            break
        if str(temp.buildingid) == str(buildingid):
            cnt = temp.capacity
            while cnt != 0:
                if id < temp_arr.__len__():
                    Student.objects.filter(pk=temp_arr[id]).update(buildingid_id = buildingid,roomid = temp)
                    cnt -= 1
                    id += 1
                    print(cnt)
            Room.objects.filter(pk=temp.name).update(capacity = cnt)

    return render(request, 'dorm/secretary/distribute_result.html',{'user_id':user_id})