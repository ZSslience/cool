from django.db import models
from db.base_model import BaseModel # 导入抽象模型基类
# Create your models here.

class PassportManager(models.Manager):
    '''
    用户账户模型管理器类
    '''
    def add_one_passport(self, username, password, email):
        '''
        添加一个用户注册信息
        '''
        # 获取模型管理器对象所在的模型类
        model_class = self.model
        # 创建模型类对象
        passport = model_class()
        passport.username = username
        passport.password = password
        passport.email = email
        # 调用save方法保存进数据库
        passport.save()
        # 返回passport对象
        return passport

    def get_one_passport(self, username, password=None):
        '''
        根据用户名和密码查询用户信息
        '''
        try:
            if password is None:
                # 根据用户名查询账户信息
                passport = self.get(username=username)
            else:
                # 根据用户名和密码查询账户信息
                passport = self.get(username=username, password=password)
        except self.model.DoesNotExist:
            passport = None
        return passport


class Passport(BaseModel):
    '''
    用户账户类
    '''
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱')

    objects = PassportManager() # 自定义模型管理器对象

    class Meta:
        db_table = 's_user_account' # 指定表名

