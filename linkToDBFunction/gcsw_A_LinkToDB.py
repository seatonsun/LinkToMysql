import pymysql
import re
from urllib import parse

'''高层人员死亡整个流程是 对于输入的 cid，cname，pname来说： 
其中 先使用cname 来查找 指定的公司在本地数据库中是否存在，并获得其company_id
再使用company_id 来查找 高层人员表中是否有 pname 这个高层
如果有的活，再通过cid 来将 新的事件 存在 新建的本地数据库中

与其他几个方法的差别是 多查了一个 高层人员表
'''

'''update comapny_link_gcsw set docid = "0"'''

db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="123",
    db="lnulinkdb"
)

'''对于一开始的公司，和第二次的高层人员来说，都靠cid来进行 一一对应'''
'''这个处理的是cid和 传来的公司predict实体'''
def company_research_gcswA(cid, cname):
    cur = db.cursor()

    resultlist = []
    if cname is None:
        print("No cname")
    else:
        sql1 = 'select company_id from company where company_name = "' + str(cname) + '"'
        cur.execute(sql1)
        if cur.execute(sql1):
            result_1 = cur.fetchone()
            for companyid in result_1:
                companyid1 = companyid
                #print(companyid1

            sql2 = 'select work,age,time from gcsw where cid = "' + str(cid) + '"'
            cur.execute(sql2)
            result_2 = cur.fetchone()
            resultlist.append(str(cname))
            for row in result_2:
                if row is None:

                    resultlist.append("无")
                else:
                    resultlist.append(row)
            resultlist.append("无")
            for company_id in result_1:
                resultlist.append(company_id)

            resultlist.append(cid)
            resultlist.append("1")
            print(resultlist)

            return resultlist

        else:

            '''查询company表中最后一条数据的id'''
            sql1111 = 'select company_id from company order by company_id DESC limit 1;'
            cur.execute(sql1111)
            resultcompany1 = cur.fetchone()
            for i in resultcompany1:
                resultcompanyfina1 = int(str(i).replace('CP', '')) + 1
            # print(resultcompanyfina1)
            num = 10
            numlist = []
            resultcompanyfina = resultcompanyfina1
            while int(resultcompanyfina / 10) != 0:
                num -= 1
                resultcompanyfina /= 10
            fina = 1
            num -= 1
            while num != 0:
                fina *= 10
                num -= 1
            fina = str(fina).replace('1', '')
            # print(fina)
            company_new_id = "CP" + fina + str(resultcompanyfina1)
            '''上面就是将comapny_id从company表中取出，并完成 +1 动作的代码'''

            '''将对应的新id存到company表中'''
            sqlnew = 'insert into company set company_name = "' + str(cname) + '",company_id ="' + str(
                company_new_id) + '" ;'
            cur.execute(sqlnew)
            db.commit()
            ####上面是完成新公司的存储


            '''下面是完成将新事件论元取出，并和新公司id与新公司名一起传回resultlist'''
            sql2 = 'select work,age,time from gcsw where cid = "' + str(cid) + '"'
            cur.execute(sql2)
            result_2 = cur.fetchone()
            resultlist.append(str(cname))
            for row in result_2:
                if row is None:

                    resultlist.append("无")
                else:
                    resultlist.append(row)

            '''将死亡高层的名字先置为 无 '''
            resultlist.append("无")

            resultlist.append(company_new_id)

            resultlist.append(cid)
            resultlist.append("0")
            print(resultlist)

            return resultlist


def company_id_insert_gcswA(resultlist):
    cur = db.cursor()
    if resultlist is None:
        print("resultList is None!!!")
    else:
        #print(resultlist)
        #sql1 = "INSERT INTO company_link_gcsw(company_link_gcsw_name,company_id) VALUES (%s,%s); "
        #print(resultlist[0],resultlist[5])

        sql2 = "INSERT INTO company_link_gcsw SET " \
               "company_link_gcsw_companyname = '" + resultlist[0] + \
               "',company_link_gcsw_highduty='" + resultlist[1] + \
               "',company_link_gcsw_deathage='" + resultlist[2] + \
               "',company_link_gcsw_deathtime='" + resultlist[3] + \
               "',company_link_gcsw_seniorstaff='" + resultlist[4] + \
               "',company_id='" + resultlist[5] + \
               "',docid='" + resultlist[6] + \
               "',nosuchcompany='" + resultlist[7] + \
               "';"

        #cur.execute(sql1, [str(resultlist[0]), str(resultlist[5])])

        cur.execute(sql2)
        db.commit()
        print("FinishedA!!")



#########下面是对于 高层人员 的方法！！！！！！！###########################


def company_research_gcswB(cid, gname):
    cur = db.cursor()

    resultlist = []
    if gname is None:
        print("没有传给函数高层人员名字！！！！！！")
    else:

        sql1 = 'select company_id from company_link_gcsw where docid = "' + str(cid) + '"'

        cur.execute(sql1)
        if cur.execute(sql1):
            result_1 = cur.fetchone()
            for companyid in result_1:
                companyid1 = companyid
            sql11 = 'select nosuchcompany from company_link_gcsw where docid = "' + str(cid) + '"'
            cur.execute(sql11)
            result11 = cur.fetchone()
            for i in result11:
                nosuchcompany = i
            if str(nosuchcompany) == str(1):

                sql2 = 'select company_companybackground_keyperson_chairman,company_companybackground_keyperson_generalManager,' \
                   'company_companybackground_keyperson_cfo, company_companybackground_keyperson_chairmanSecretary, company_companybackground_keyperson_boardmember,' \
                   'company_companybackground_keyperson_supervisor,company_companybackground_keyperson_manager from company_companybackground_keyperson where ' \
                   'company_id ="' + str(companyid1) + '"'

                sql3 = 'select company_listedCompany_executiveInfor_name from company_listedcompany_executiveinfor where company_id ="' + str(companyid1) + '"'
                cur.execute(sql2)
                result2 = cur.fetchone()
                for i in result2:
                    if str(i) == str(gname):
                        sql21 = 'insert into company_link_gcsw set company_link_gcsw_seniorstaff = "' + str(gname) + '" where docid = "' + str(cid) + '"'
                        cur.execute(sql21)
                        return 0
                cur.execute(sql3)
                result3 = cur.fetchall()
                for i in result3:
                    if str(i) == str(gname):
                        sql21 = 'insert into company_link_gcsw set company_link_gcsw_seniorstaff = "' + str(
                            gname) + '" where docid = "' + str(cid) + '"'
                        cur.execute(sql21)
                        return 0
                '''这下面的代码应该是 将 在本地LNU表中存在的公司，但死亡高管 在LNU中不存在时 的 将 gname 新增进 相应公司的 高管表中 的代码'''


            else:
                '''这加如果没有相应公司在 本地的LNU表中的处理代码 ： 是直接将 人员 新增进 高管表中 不需要查找 ！！！！！！！！'''











if __name__ == '__main__':
    company_id_insert_gcswA(company_research_gcswA("2","天天公司"))
    company_id_insert_gcswA(company_research_gcswA("3", "大大公司"))
    db.close()
    # company_research_gcsw(2, "小酒")
    # company_research_gcsw(3,'')
