# This file contains configuration variables that shouldn’t be in version control.
# This includes things like API keys and database URIs containing passwords.
# This also contains variables that are specific to this particular instance of your application.
# For example, you might have DEBUG = False in config.py,
# but set DEBUG = True in instance/config.py on your local machine for development.
# Since this file will be read in after config.py, it will override it and set DEBUG = True.

SQLALCHEMY_DATABASE_URI = "mysql://root:AI@2019@ai@rm-8vbwj6507z6465505ro.mysql.zhangbei.rds.aliyuncs.com/stu_db"
