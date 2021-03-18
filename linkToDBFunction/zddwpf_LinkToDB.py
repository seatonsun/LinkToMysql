import pymysql
import re
from urllib import parse


db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="123",
    db="lnulinkdb"
)


def company_research_zddwpf(cid, cname):
    cur = db.cursor()
    resultlist = []
    if cname is None:
        print("No cname")
    else:
        sql1 = 'select company_id from company where company_name = "' + str(cname) + '"'
        cur.execute(sql1)
        if cur.execute(sql1):
            result_1 = cur.fetchone()
            sql2 = 'select time,money,paypeople,name from zddwpf where cid = "' + str(cid) + '"'
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
            print("No such company in company list!!")


def company_id_insert_zddwpf(resultlist):
    cur = db.cursor()
    if resultlist is None:
        print("resultList is None!!!")
    else:
        #print(resultlist)
        #sql1 = "INSERT INTO company_link_zddwpf(company_link_zddwpf_name,company_id) VALUES (%s,%s); "
        #print(resultlist[0],resultlist[5])
        sql2 = "INSERT INTO company_link_zddwpf SET " \
               "company_link_zddwpf_noticetime = '" + resultlist[0] + \
               "',company_link_zddwpf_lossmoney='" + resultlist[1] + \
               "',company_link_zddwpf_lossobject='" + resultlist[2] + \
               "',company_link_zddwpf_companyname='" + resultlist[3] + \
               "',company_id='" + resultlist[4] + "';"
        #cur.execute(sql1, [str(resultlist[0]), str(resultlist[5])])

        cur.execute(sql2)
        db.commit()
        print("Finished!!")


if __name__ == '__main__':
    #company_research_zddwpf("4", "淘宝")
    company_id_insert_zddwpf(company_research_zddwpf("4", "淘宝"))
    db.close()
    # company_research_zddwpf(2, "小酒")
    # company_research_zddwpf(3,'')
