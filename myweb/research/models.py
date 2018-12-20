from django.db import models

# Create your models here.

# 用户
class User(models.Model):
    # 用户id，主键，自增列
    user_id = models.AutoField(primary_key=True)
    # 用户名，最大长度为20
    user_name = models.CharField(max_length=20)
    # 用户真实姓名，最大长度为20
    user_real_name = models.CharField(max_length=20)
    # 用户密码，最大长度为18，明文记录
    user_password = models.CharField(max_length=18)
    # 用户权限，最大长度20
    user_permission = models.CharField(max_length=20)
    # 用户单位，最大长度为20
    user_unit = models.CharField(max_length=20)

# 系统日志
class System_log(models.Model):
    # 编号，主键，自增列
    log_numbering = models.AutoField(primary_key=True)
    # 记录时间
    log_time = models.DateTimeField(auto_now_add=True)
    # 操作员id，这里不能用外键，因为系统日志不可删减
    log_operator_id = models.ImageField()
    # 操作内容，最大长度100
    log_content = models.CharField(max_length=100)
    # IP地址
    log_ip = models.IPAddressField()

# 申报人信息
class Reporter_information(models.Model):
    # 申报人序号，主键，自增列
    reporter_serial_number = models.AutoField(primary_key=True)
    # 申报人id，外键，级联删除
    reporter_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # 申报人真实姓名，最大长度为20
    reporter_real_name = models.CharField(max_length=20)
    # 申报人性别，最大长度为2
    reporter_gender = models.CharField(max_length=2)
    # 申报人出生日期
    reporter_date_of_birth = models.DateField()
    # 申报人身份证号，固定长度为18位，在models判断
    reporter_identity_number = models.CharField(max_length=18)
    # 申报人单位，最大长度为20
    reporter_unit = models.CharField(max_length=20)

# 科研课题信息
class Research_projects(models.Model):
    # 该元组所属人id，外键，级联删除
    project_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # 课题序号，主键，自增列
    project_number = models.AutoField(primary_key=True)
    # 课题类别，最大长度为20
    project_category = models.CharField(max_length=20)
    # 课题名称，最大长度为20
    project_name = models.CharField(max_length=20)
    # 合同号，最大长度为20
    contract_no = models.CharField(max_length=20)
    # 参加人数
    participants_number = models.IntegerField()
    # 本人排名，最大长度为20
    my_ranking = models.CharField(max_length=20)
    # 课题负责人，最大长度为20
    project_leader = models.CharField(max_length=20)
    # 课题经费
    project_funding = models.IntegerField()
    # 课题得分
    project_score = models.IntegerField()
    # 经费分值
    funding_score = models.IntegerField()

# 获奖信息
class Award_information(models.Model):
    # 该元组所属人，外键，级联删除
    award_id = models.ForeignKey(User,on_delete=models.CASCADE)
    # 获奖序号，主键，自增列
    award_serial_number = models.AutoField(primary_key=True)
    # 获奖代码，最大长度为20
    award_code = models.CharField(max_length=20)
    # 获奖名称，最大长度为20
    award_name = models.CharField(max_length=20)
    # 获奖等级，最大长度为20
    award_grade = models.CharField(max_length=20)
    # 获奖人数
    award_number = models.IntegerField()
    # 本人排名，最大长度为20
    my_ranking = models.CharField(max_length=20)
    # 获奖得分
    awarding_score = models.IntegerField()
    # 计分标准，最大长度为20
    scoring_standard = models.CharField(max_length=20)

# 课题鉴定
class Question_identification(models.Model):
    # 该元组所属人，外键，级联删除
    identification_id = models.ForeignKey(User,on_delete=models.CASCADE)
    # 鉴定序号，主键，自增列
    identification_serial_number = models.AutoField(primary_key=True)
    # 鉴定类别，最大长度为20
    identification_category = models.CharField(max_length=20)
    # 鉴定名称，最大长度为20
    identification_name = models.CharField(max_length=20)
    # 鉴定单位，最大长度为20
    identification_unit = models.CharField(max_length=20)
    # 完成人数，
    number_of_completions = models.IntegerField()
    # 本人排名，最大长度为20
    my_ranking = models.CharField(max_length=20)
    # 鉴定时间，
    identification_time = models.DateField()
    # 鉴定得分，
    identification_score = models.IntegerField()
    # 计分标准，最大长度为20
    scoring_standard = models.CharField(max_length=20)

# 学术活动
class Academic_events(models.Model):
    # 该元组所属人，外键，级联删除
    event_id = models.ForeignKey(User,on_delete=models.CASCADE)
    # 活动序号，主键，自增列
    event_serial_number = models.AutoField(primary_key=True)
    # 活动类别，最大长度为20
    event_category = models.CharField(max_length=20)
    # 活动名称，最大长度为20
    event_name = models.CharField(max_length=20)
    # 报告题目，最大长度为20
    headline = models.CharField(max_length=20)
    # 举办国家，最大长度为20
    host_country = models.CharField(max_length=20)
    # 举办单位，最大长度为20
    organizer = models.CharField(max_length=20)
    # 举办地点，最大长度为20
    venue = models.CharField(max_length=20)
    # 活动得分，
    event_score = models.IntegerField()
    # 计分标准，最大长度为20
    scoring_standard = models.CharField(max_length=20)

# 科技论文
class Scientific_Papers(models.Model):
    # 该元组所属人，外键，级联删除
    paper_id = models.ForeignKey(User,on_delete=models.CASCADE)
    # 论文序号，主键，自增列
    paper_serial_number = models.AutoField(primary_key=True)
    # 论文类别，最大长度为20
    paper_category = models.CharField(max_length=20)
    # 论文名称，最大长度为20
    paper_name = models.CharField(max_length=20)
    # 期刊名称，最大长度为20
    journal_title = models.CharField(max_length=20)
    # 期刊编号，最大长度为20
    journal_number = models.CharField(max_length=20)
    # 收录因子，
    inclusion_factor = models.IntegerField()
    # 作者人数，
    number_of_authors = models.IntegerField()
    # 本人排名，最大长度为20
    my_ranking = models.CharField(max_length=20)
    # 论文分数，
    paper_score = models.IntegerField()
    # 计分标准，最大长度为20
    scoring_standard = models.CharField(max_length=20)

# 著作
class Book(models.Model):
    # 该元组所属人，外键，级联删除
    book_id = models.ForeignKey(User,on_delete=models.CASCADE)
    # 著作序号，主键，自增列
    book_serial_number = models.AutoField(primary_key=True)
    # 著作类别，最大长度为20
    book_category = models.CharField(max_length=20)
    # 著作名称，最大长度为20
    book_name = models.CharField(max_length=20)
    # 出版社名称，最大长度为20
    publisher_name = models.CharField(max_length=20)
    # 字数，
    word_count = models.IntegerField()
    # 作者人数，
    number_of_authors = models.IntegerField()
    # 本人排名，最大长度为20
    my_ranking = models.CharField(max_length=20)
    # 著作分数，
    book_score = models.IntegerField()
    # 字数分标准，最大长度为20
    word_count_standard = models.CharField(max_length=20)

# 专利
class Patent(models.Model):
    # 该元组所属人，外键，级联删除
    patent_id = models.ForeignKey(User,on_delete=models.CASCADE)
    # 专利序号，主键，自增列
    patent_serial_number = models.AutoField(primary_key=True)
    # 专利类别，最大长度为20
    patent_category = models.CharField(max_length=20)
    # 专利号，最大长度为20
    patent_no = models.CharField(max_length=20)
    # 专利名称，最大长度为20
    patent_name = models.CharField(max_length=20)
    # 持有人数，
    patent_number = models.IntegerField()
    # 本人排名，最大长度为20
    my_ranking = models.CharField(max_length=20)
    # 专利得分
    patent_score = models.IntegerField()
    # 计分标准，最大长度为20
    scoring_standard = models.CharField(max_length=20)
