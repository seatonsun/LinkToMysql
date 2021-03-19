import pymysql
import re
from urllib import parse

'''破产清算模块'''

db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="123",
    db="lnulinkdb"
)


def company_research_pcqs(cid,cname):
        cur = db.cursor()
        resultlist = []
        resultlistfina = []

    # for cid in entitydoc:
    #     mention = mentionlist[cid]
    #     cname = predict[mention]

        if cname is None:
            print("No cname")
        elif cid is None:
            print("cid is None")
        else:
            sql1 = 'select company_id from company where company_name = "' + str(cname) + '"'
            cur.execute(sql1)
            if cur.execute(sql1):
                result_1 = cur.fetchone()
                sql2 = 'select name,cindustry,court,rulingtime,announcementtime from pcqs where cid = "' + str(cid) + '"'
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
                '''将对应的新comapnyname存到company表中'''
                sql2 = 'select name,cindustry,court,rulingtime,announcementtime from pcqs where cid = "' + str(cid) + '"'
                cur.execute(sql2)
                result_2 = cur.fetchone()
                for row in result_2:
                    if row is None:

                        resultlist.append("无")
                    else:
                        resultlist.append(row)

                resultlist.append(company_new_id)
                print(resultlist)
                return resultlist
                #resultlistfina.append(resultlist)

    #return resultlistfina


def company_id_insert_pcqs(resultlist):
        cur = db.cursor()
    # for resultlist in resultlistfina:
        if resultlist is None:
            print("resultList is None!!!")
        else:
            #print(resultlist)
            #sql1 = "INSERT INTO company_link_pcqs(company_link_pcqs_name,company_id) VALUES (%s,%s); "
            #print(resultlist[0],resultlist[5])
            sql2 = "INSERT INTO company_link_pcqs SET " \
                   "company_link_pcqs_name = '" + resultlist[0] + \
                   "',company_link_pcqs_industry='" + resultlist[1] + \
                   "',company_link_pcqs_court='" + resultlist[2] + \
                   "',company_link_pcqs_rulingtime='" + resultlist[3] + \
                   "',company_link_pcqs_announcementtime='" + resultlist[4] + \
                   "',company_id='" + resultlist[5] + "';"
            #cur.execute(sql1, [str(resultlist[0]), str(resultlist[5])])

            cur.execute(sql2)
            db.commit()
            print("Finished!!")


if __name__ == '__main__':
    #company_research_pcqs("4", "淘宝")
    company_id_insert_pcqs(company_research_pcqs("4", "淘宝"))
    db.close()
    # company_research_pcqs(2, "小酒")
    # company_research_pcqs(3,'')
