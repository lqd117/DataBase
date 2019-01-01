from django.urls import path

from . import views

app_name = 'dorm'
urlpatterns = [
    path('login/',views.user_login,name='user_login'),
    path('confirm/',views.confirm,name='confirm'),
    #学生
    path('student/index.html/',views.student_index,name='student_index'),
    path('student/mark.html/',views.student_mark,name='student_mark'),
    path('student/fee.html/',views.student_fee,name='student_fee'),
    path('student/unsubscribe.html/',views.student_unsubscribe,name='student_unsubscribe'),
    path('student/repair_record.html/',views.student_repair_record,name='student_repair_record'),
    path('student/building_select.html/',views.student_building_select,name='student_building_select'),
    path('student/unsubscribe_result.html/',views.student_unsubscribe_result,name='student_unsubscribe_result'),
    path('student/repair.html/',views.student_repair,name='student_repair'),
    path('student/new_repair.html/',views.student_new_repair,name='student_new_repair'),
    path('student/building.html/',views.student_building, name='student_building'),
    path('student/checkin.html/',views.student_checkin, name='student_checkin'),
    #导员
    path('instructor/index.html/',views.instructor_index,name='instructor_index'),
    path('instructor/class.html/',views.instructor_class,name='instructor_class'),
    path('instructor/lookup.html/',views.instructor_lookup,name='instructor_lookup'),
    path('instructor/checkin.html/',views.instructor_checkin,name='instructor_checkin'),
    path('instructor/unsubscribe.html/',views.instructor_unsubscribe,name='instructor_unsubscribe'),
    path('instructor/member.html/',views.instructor_member,name='instructor_member'),
    path('instructor/lookup_result.html/',views.instructor_lookup_result,name='instructor_lookup_result'),
    path('instructor/checkin_result.html/',views.instructor_checkin_result,name='instructor_checkin_result'),
    path('instructor/unsubscribe_result.html/',views.instructor_unsubscribe_result,name='instructor_unsubscribe_result'),
    #维修人员
    path('maintenance/index.html/',views.maintenance_index,name='maintenance_index'),
    path('maintenance/repair.html/',views.maintenance_repair,name='maintenance_repair'),
    path('maintenance/repair_result.html/',views.maintenance_repair_result,name='maintenance_repair_result'),
    #舍管
    path('housemaster/index.html/',views.housemaster_index,name='housemaster_index'),
    path('housemaster/add_visitor.html/',views.housemaster_add_visitor,name='housemaster_add_visitor'),
    path('housemaster/new_visitor.html/',views.housemaster_new_visitor,name='housemaster_new_visitor'),
    path('housemaster/building.html/',views.housemaster_building,name='housemaster_building'),
    path('housemaster/checkin.html/',views.housemaster_checkin,name='housemaster_checkin'),
    path('housemaster/checkin_result.html/',views.housemaster_checkin_result,name='housemaster_checkin_result'),
    path('housemaster/lookup.html/',views.housemaster_lookup,name='housemaster_lookup'),
    path('housemaster/lookup_result.html/',views.housemaster_lookup_result,name='housemaster_lookup_result'),
    path('housemaster/member.html/',views.housemaster_member,name='housemaster_member'),
    path('housemaster/unsubscribe.html/',views.housemaster_unsubscribe,name='housemaster_unsubscribe'),
    path('housemaster/unsubscribe_result.html/',views.housemaster_unsubscribe_result,name='housemaster_unsubscribe_result'),
    path('housemaster/visitor.html/',views.housemaster_visitor,name='housemaster_visitor'),
    path('housemaster/mark.html/',views.housemaster_mark,name='housemaster_mark'),
    path('housemaster/new_mark.html/',views.housemaster_new_mark,name='housemaster_new_mark'),
    #书记
    path('secretary/building.html/',views.secretary_building,name='secretary_building'),
    path('secretary/checkin.html/',views.secretary_checkin,name='secretary_checkin'),
    path('secretary/checkin_result.html/',views.secretary_checkin_result,name='secretary_checkin_result'),
    path('secretary/class.html/',views.secretary_class,name='secretary_class'),
    path('secretary/index.html/',views.secretary_index,name='secretary_index'),
    path('secretary/lookup.html/',views.secretary_lookup,name='secretary_lookup'),
    path('secretary/lookup_result.html/',views.secretary_lookup_result,name='secretary_lookup_result'),
    path('secretary/member.html/',views.secretary_member,name='secretary_member'),
    path('secretary/unsubscribe.html/',views.secretary_unsubscribe,name='secretary_unsubscribe'),
    path('secretary/unsubscribe_result.html/',views.secretary_unsubscribe_result,name='secretary_unsubscribe_result'),

]