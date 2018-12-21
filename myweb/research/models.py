from django.db import models

# Create your models here.

# 用户
class User(models.Model):
    class Meta:
        verbose_name_plural = "用户"
    # 用户id，主键，自增列
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20,verbose_name="用户名")
    user_real_name = models.CharField(max_length=20,verbose_name="姓名")
    user_password = models.CharField(max_length=18,verbose_name="密码")
    user_permission = models.CharField(max_length=20,verbose_name="权限")
    user_unit = models.CharField(max_length=20,verbose_name="单位")

# 系统日志
class System_log(models.Model):
    class Meta:
        verbose_name_plural = "系统日志"
    # 编号，主键，自增列
    log_numbering = models.AutoField(primary_key=True)
    log_time = models.DateTimeField(auto_now_add=True,verbose_name="记录时间")
    log_operator_id = models.ImageField(verbose_name="id")
    log_content = models.CharField(max_length=100,verbose_name="操作内容")
    log_ip = models.GenericIPAddressField(verbose_name="IP地址")

# 申报人信息
class Reporter_information(models.Model):
    class Meta:
        verbose_name_plural = "申报人信息"
    # 申报人序号，主键，自增列
    reporter_serial_number = models.AutoField(primary_key=True)
    # 申报人id，外键，级联删除
    reporter_id = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="id")
    reporter_real_name = models.CharField(max_length=20,verbose_name="姓名")
    reporter_gender = models.CharField(max_length=2,verbose_name="性别")
    reporter_date_of_birth = models.DateField(verbose_name="出生日期")
    # 申报人身份证号，固定长度为18位，在models判断
    reporter_identity_number = models.CharField(max_length=18,verbose_name="身份证号")
    reporter_unit = models.CharField(max_length=20,verbose_name="单位")

# 科研课题信息
class Research_projects(models.Model):
    class Meta:
        verbose_name_plural = "科研课题信息"
    # 课题序号，主键，自增列
    project_number = models.AutoField(primary_key=True)
    # 该元组所属人id，外键，级联删除
    project_id = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="id")
    project_category = models.CharField(max_length=20,verbose_name="课题类别")
    project_name = models.CharField(max_length=20,verbose_name="课题名称")
    contract_no = models.CharField(max_length=20,verbose_name="合同号")
    participants_number = models.IntegerField(verbose_name="参加人数")
    my_ranking = models.CharField(max_length=20,verbose_name="本人排名")
    project_leader = models.CharField(max_length=20,verbose_name="课题负责人")
    project_funding = models.IntegerField(verbose_name="课题经费")
    project_score = models.IntegerField(verbose_name="课题得分")
    funding_score = models.IntegerField(verbose_name="经费分值")

# 获奖信息
class Award_information(models.Model):
    class Meta:
        verbose_name_plural = "获奖信息"
    # 获奖序号，主键，自增列
    award_serial_number = models.AutoField(primary_key=True)
    # 该元组所属人，外键，级联删除
    award_id = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="id")
    award_code = models.CharField(max_length=20,verbose_name="获奖代码")
    award_name = models.CharField(max_length=20,verbose_name="获奖名称")
    award_grade = models.CharField(max_length=20,verbose_name="获奖等级")
    award_number = models.IntegerField(verbose_name="获奖人数")
    my_ranking = models.CharField(max_length=20,verbose_name="本人排名")
    awarding_score = models.IntegerField(verbose_name="获奖得分")
    scoring_standard = models.CharField(max_length=20,verbose_name="计分标准")

# 课题鉴定
class Question_identification(models.Model):
    class Meta:
        verbose_name_plural = "课题鉴定"
    # 鉴定序号，主键，自增列
    identification_serial_number = models.AutoField(primary_key=True)
    # 该元组所属人，外键，级联删除
    identification_id = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="id")
    identification_category = models.CharField(max_length=20,verbose_name="鉴定类别")
    identification_name = models.CharField(max_length=20,verbose_name="鉴定名称")
    identification_unit = models.CharField(max_length=20,verbose_name="鉴定单位")
    number_of_completions = models.IntegerField(verbose_name="完成人数")
    my_ranking = models.CharField(max_length=20,verbose_name="本人排名")
    identification_time = models.DateField(verbose_name="鉴定时间")
    identification_score = models.IntegerField(verbose_name="鉴定得分")
    scoring_standard = models.CharField(max_length=20,verbose_name="计分标准")

# 学术活动
class Academic_events(models.Model):
    class Meta:
        verbose_name_plural = "学术活动"
    # 活动序号，主键，自增列
    event_serial_number = models.AutoField(primary_key=True)
    # 该元组所属人，外键，级联删除
    event_id = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="id")
    event_category = models.CharField(max_length=20,verbose_name="活动类别")
    event_name = models.CharField(max_length=20,verbose_name="活动名称")
    headline = models.CharField(max_length=20,verbose_name="报告题目")
    host_country = models.CharField(max_length=20,verbose_name="举办国家")
    organizer = models.CharField(max_length=20,verbose_name="举办单位")
    venue = models.CharField(max_length=20,verbose_name="举办地点")
    event_score = models.IntegerField(verbose_name="活动得分")
    scoring_standard = models.CharField(max_length=20,verbose_name="计分标准")

# 科技论文
class Scientific_Papers(models.Model):
    class Meta:
        verbose_name_plural = "科技论文"
    # 论文序号，主键，自增列
    paper_serial_number = models.AutoField(primary_key=True)
    # 该元组所属人，外键，级联删除
    paper_id = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="id")
    paper_category = models.CharField(max_length=20,verbose_name="论文类别")
    paper_name = models.CharField(max_length=20,verbose_name="论文名称")
    journal_title = models.CharField(max_length=20,verbose_name="期刊名称")
    journal_number = models.CharField(max_length=20,verbose_name="期刊编号")
    inclusion_factor = models.IntegerField(verbose_name="收录因子")
    number_of_authors = models.IntegerField(verbose_name="作者人数")
    my_ranking = models.CharField(max_length=20,verbose_name="本人排名")
    paper_score = models.IntegerField(verbose_name="论文分数")
    scoring_standard = models.CharField(max_length=20,verbose_name="计分标准")

# 著作
class Book(models.Model):
    class Meta:
        verbose_name_plural = "著作"
    # 著作序号，主键，自增列
    book_serial_number = models.AutoField(primary_key=True)
    # 该元组所属人，外键，级联删除
    book_id = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="id")
    book_category = models.CharField(max_length=20,verbose_name="著作类别")
    book_name = models.CharField(max_length=20,verbose_name="著作名称")
    publisher_name = models.CharField(max_length=20,verbose_name="出版社名称")
    word_count = models.IntegerField(verbose_name="字数")
    number_of_authors = models.IntegerField(verbose_name="作者人数")
    my_ranking = models.CharField(max_length=20,verbose_name="本人排名")
    book_score = models.IntegerField(verbose_name="著作分数")
    word_count_standard = models.CharField(max_length=20,verbose_name="字数分标准")

# 专利
class Patent(models.Model):
    class Meta:
        verbose_name_plural = "专利"
    # 专利序号，主键，自增列
    patent_serial_number = models.AutoField(primary_key=True)
    # 该元组所属人，外键，级联删除
    patent_id = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="id")
    patent_category = models.CharField(max_length=20,verbose_name="专利类别")
    patent_no = models.CharField(max_length=20,verbose_name="专利号")
    patent_name = models.CharField(max_length=20,verbose_name="专利名称")
    patent_number = models.IntegerField(verbose_name="持有人数")
    my_ranking = models.CharField(max_length=20,verbose_name="本人排名")
    patent_score = models.IntegerField(verbose_name="专利得分")
    scoring_standard = models.CharField(max_length=20,verbose_name="计分标准")
