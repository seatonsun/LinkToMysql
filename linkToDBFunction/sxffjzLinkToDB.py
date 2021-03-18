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


def company_research_sxffjz(cid, cname):
    cur = db.cursor()
    resultlist = []
    if cname is None:
        print("No cname")
    else:
        sql11 = 'select company_id from company where company_name = "' + str(cname) + '"'

        sql12 = 'select company_id from company_listedCompany_keyperson where ' \
               'company_listedCompany_keyperson_generalManager ="' + str(cname) + \
               '" or company_listedCompany_keyperson_legalRepresentative ="' + str(cname) + \
               '" or company_listedCompany_keyperson_topSecretaries ="' + str(cname) + \
               '" or company_listedCompany_keyperson_chairman ="' + str(cname) + \
               '" or company_listedCompany_keyperson_securitiesRepresentative="' + str(cname) + \
               '" or company_listedCompany_keyperson_independentDirector ="' + str(cname) + '";'

        sql13 = 'select company_id from company_companybackground_keyperson where ' \
                'company_companybackground_keyperson_chairman ="' + str(cname) + \
                '" or company_companybackground_keyperson_generalManager ="' + str(cname) + \
                '" or company_companybackground_keyperson_cfo ="' + str(cname) + \
                '" or company_companybackground_keyperson_chairmanSecretary ="' + str(cname) + \
                '" or company_companybackground_keyperson_boardmember ="' + str(cname) + \
                '" or company_companybackground_keyperson_manager ="' + str(cname) + \
                '" or company_companybackground_keyperson_supervisor ="' + str(cname) + '";'

        if cur.execute(sql11):
            cur.execute(sql11)
            result_11 = cur.fetchone()
            sql31 = 'select grouporpeople,processunit,noticeunit,money,' \
                    'handresult,handtime,time,product,noticetime ' \
                    'from sxffjz where cid = "' + str(cid) + '"'
            cur.execute(sql31)
            result_21 = cur.fetchone()
            for row in result_21:
                if row is None:

                    resultlist.append("无")
                else:
                    resultlist.append(row)
            for company_id in result_11:
                # print(str(row))
                # return company_id
                resultlist.append(company_id)
            print(resultlist)
            return resultlist
        elif cur.execute(sql12):
            cur.execute(sql12)
            result_12 = cur.fetchone()
            sql32 = 'select grouporpeople,processunit,noticeunit,money,' \
                    'handresult,handtime,time,product,noticetime ' \
                    'from sxffjz where cid = "' + str(cid) + '"'
            cur.execute(sql32)
            if cur.execute(sql32):
                result_22 = cur.fetchone()
                for row in result_22:
                    if row is None:

                        resultlist.append("无")
                    else:
                        resultlist.append(row)
                for company_id in result_12:
                    # print(str(row))
                    # return company_id
                    resultlist.append(company_id)
                print(resultlist)
                return resultlist
            else:
                print('对应的cid 没有相应的 人员名!!!!!')

        elif cur.execute(sql13) :
            cur.execute(sql13)
            result_13 = cur.fetchone()
            sql33 = 'select grouporpeople,processunit,noticeunit,money,' \
                    'handresult,handtime,time,product,noticetime ' \
                    'from sxffjz where cid = "' + str(cid) + '"'
            cur.execute(sql33)
            if cur.execute(sql33):
                result_33 = cur.fetchone()
                for row in result_33:
                    if row is None:

                        resultlist.append("无")
                    else:
                        resultlist.append(row)
                for company_id in result_13:
                    # print(str(row))
                    # return company_id
                    resultlist.append(company_id)
                print(resultlist)
                return resultlist


            else:
                print('对应的cid所在公司 没有相应的 人员!!!!!')
        else:
            print("No such company in company list!!")


def company_id_insert_sxffjz(resultlist):
    cur = db.cursor()
    if resultlist is None:
        print("resultList is None!!!")
    else:
        #print(resultlist)
        #sql1 = "INSERT INTO company_link_sxffjz(company_link_sxffjz_name,company_id) VALUES (%s,%s); "
        #print(resultlist[0],resultlist[5])
        sql3 = "INSERT INTO company_link_sxffjz SET " \
               "company_link_sxffjz_grouporpeople = '" + resultlist[0] + \
               "',company_link_sxffjz_processunit='" + resultlist[1] + \
               "',company_link_sxffjz_noticeunit='" + resultlist[2] + \
               "',company_link_sxffjz_money='" + resultlist[3] + \
               "',company_link_sxffjz_handresult='" + resultlist[4] + \
               "',company_link_sxffjz_handtime='" + resultlist[5] + \
               "',company_link_sxffjz_time='" + resultlist[6] + \
               "',company_link_sxffjz_product='" + resultlist[7] + \
               "',company_link_sxffjz_noticetime='" + resultlist[8] + \
               "',company_id='" + resultlist[9] + "';"
        #cur.execute(sql1, [str(resultlist[0]), str(resultlist[5])])

        cur.execute(sql3)
        db.commit()
        print("Finished!!")


if __name__ == '__main__':
    ####下面这个函数接受的是 齐 那里的相应事件的实践论元表，我直接导过来用的，返回的是相应 cid与name的 company表的 company_id
    company_research_sxffjz("1", "京东")
    company_research_sxffjz("2", "小红")
    company_research_sxffjz("3","大红")
    # company_research_sxffjz("3", "小红")
    ####下面的函数接收的是上面函数穿下来的company_id,并将对应的事件属性存到 新建的 本地DB表中
    # company_id_insert_sxffjz(company_research_sxffjz("1", "京东"))
    # company_id_insert_sxffjz(company_research_sxffjz("2", "小红"))
    company_id_insert_sxffjz(company_research_sxffjz("3", "大红"))
    db.close()
    # company_research_sxffjz(2, "小酒")
    # company_research_sxffjz(3,'')
