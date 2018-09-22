from peewee import *
db = MySQLDatabase("station", host='127.0.0.1', port=3306, user='root', passwd='123456', charset='utf8')


class DomainConf(Model):
    domain = CharField(max_length=255, unique=True)
    Template = CharField(max_length=255, default='CPModel_2')
    index_title = CharField(max_length=255)
    index_keywords = TextField()
    index_description = TextField()

    class Meta:
        database = db
        table_name = 'CPModel_2_domainconf'
