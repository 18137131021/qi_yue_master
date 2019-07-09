# -*- coding: utf-8 -*-
"""
用于测试环境的全局配置
"""
from settings import APP_ID


# ===============================================================================
# 数据库设置, 测试环境数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 默认用mysql
        'NAME': 'chenguilin_t',                        # 数据库名 (默认与APP_ID相同)
        'USER': 'chenguilin_t',                            # 你的数据库user
        'PASSWORD': 'chenguilin_t@2018',                        # 你的数据库password
        'HOST': '192.168.51.51',                   		   # 数据库HOST
        'PORT': '3306',                        # 默认3306
    },
}
