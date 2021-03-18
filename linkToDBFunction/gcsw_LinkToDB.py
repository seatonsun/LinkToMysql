import pymysql
import re
from urllib import parse

'''高层人员死亡整个流程是 对于输入的 cid，cname，pname来说： 
其中 先使用cname 来查找 指定的公司在本地数据库中是否存在，并获得其company_id
再使用company_id 来查找 高层人员表中是否有 pname 这个高层
如果有的活，再通过cid 来将 新的事件 存在 新建的本地数据库中

与其他几个方法的差别是 多查了一个 高层人员表
'''

db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="123",
    db="lnulinkdb"
)




def company_research_gcsw(cid, cname, pname):
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
                #print(companyid1)
            sql12 = 'select company_listedCompany_executiveInfor_name from company_listedcompany_executiveinfor' \
                    ' where company_id = "' + str(companyid1) + '";'
            cur.execute(sql12)
            result_12 = cur.fetchall()
            #print(result_12)
            print(type(result_12))
            count = 0
            for executivename in result_12:
                for i in executivename:
                    executivename1 = i
                count += 1
                if str(pname) == str(executivename1):

                    sql2 = 'select name,work,age,time,people from gcsw where cid = "' + str(cid) + '"'
                    cur.execute(sql2)
                    result_2 = cur.fetchone()
                    for row in result_2:
                        if row is None:

                            resultlist.append("无")
                        else:
                            resultlist.append(row)
                    for company_id in result_1:
                        # print(str(row))
                        # return company_id
                        resultlist.append(company_id)
                    print(resultlist)

                    return resultlist
                else:
                    #while count ==
                    pass
        else:
            print("No such company in company list!!")
            #######这要加上添加新公司的代码，添加到company表中
            sqlnew = ''


def company_id_insert_gcsw(resultlist):
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
               "',company_id='" + resultlist[5] + "';"
        #cur.execute(sql1, [str(resultlist[0]), str(resultlist[5])])

        cur.execute(sql2)
        db.commit()
        print("Finished!!")


if __name__ == '__main__':
    company_research_gcsw("1", "淘宝","红红")
    company_id_insert_gcsw(company_research_gcsw("1", "淘宝","红红"))
    db.close()
    # company_research_gcsw(2, "小酒")
    # company_research_gcsw(3,'')
