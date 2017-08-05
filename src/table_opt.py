#coding=utf-8
from database import Database

class Table_opt(object):
    def insert(self,word,mean):
        mydata = Database()
        mydata.opencnx()
        id = self.findword(word)
        if id<0:
            data_word=(word,1,0,mean)
            add_word = ("INSERT INTO t_vocabulary "
                   "(word, intimes, outtimes, mean) "
                   "VALUES ( %s, %s, %s, %s)")
            mydata.cursor = mydata.cnx.cursor()
            mydata.cursor.execute(add_word, data_word)
            mydata.cnx.commit()
            mydata.closecnx()
        else:
            self.updatain(id)

    def findword(self,word):
        mydata = Database()
        mydata.opencnx()
        query = ("SELECT * FROM t_vocabulary WHERE word =%s ")
        mydata.cursor.execute(query,(word,))
        data =  mydata.cursor.fetchall()
        num = len(data)
        if(num!=0):
            mydata.closecnx()
            return data[0][0]
        else:
            mydata.closecnx()
            return -1

    def updatain(self,id):
        mydata = Database()
        mydata.opencnx()
        query = ("UPDATE t_vocabulary SET intimes=intimes+1 WHERE id =%s")
        mydata.cursor.execute(query,(id,))
        mydata.cnx.commit()
        mydata.closecnx()

    def updataout(self,id):
        mydata = Database()
        mydata.opencnx()
        query = ("UPDATE t_vocabulary SET outtimes=outtimes+1 WHERE id =%s")
        mydata.cursor.execute(query,(id,))
        mydata.cnx.commit()
        mydata.closecnx()

    def randfind(self,maxnum=20):
        mydata = Database()
        mydata.opencnx()
        allnum = self.findallnum()
        if maxnum > allnum:
            maxnum = allnum
        query = ("SELECT * from t_vocabulary order by rand() limit %s")
        mydata.cursor.execute(query,(maxnum,))
        data =  mydata.cursor.fetchall()
        mydata.closecnx()
        return data


    def findallnum(self):
        mydata = Database()
        mydata.opencnx()
        query = ("select count(*) from t_vocabulary;")
        mydata.cursor.execute(query)
        data =  mydata.cursor.fetchall()
        return data[0][0]
