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


def company_research_sxcx(cid, cname):
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
            sql31 = 'select grouporpeople,processunit,noticeunit,handtime,' \
                    'time,product from sxcx where cid = "' + str(cid) + '"'
            cur.execute(sql31)
            result_21 = cur.fetchone()
            for row in result_21:
                if row is None:

                    resultlist.append("???")
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
            sql32 = 'select grouporpeople,processunit,noticeunit,handtime,' \
                    'time,product from sxcx where cid = "' + str(cid) + '"'
            cur.execute(sql32)
            if cur.execute(sql32):
                result_22 = cur.fetchone()
                for row in result_22:
                    if row is None:

                        resultlist.append("???")
                    else:
                        resultlist.append(row)
                for company_id in result_12:
                    # print(str(row))
                    # return company_id
                    resultlist.append(company_id)
                print(resultlist)
                return resultlist
            else:
                print('?????????cid???????????? ??????????????? ??????!!!!!')

        elif cur.execute(sql13) :
            cur.execute(sql13)
            result_13 = cur.fetchone()
            sql33 = 'select grouporpeople,processunit,noticeunit,handtime,' \
                    'time,product from sxcx where cid = "' + str(cid) + '"'
            cur.execute(sql33)
            if cur.execute(sql33):
                result_33 = cur.fetchone()
                for row in result_33:
                    if row is None:

                        resultlist.append("???")
                    else:
                        resultlist.append(row)
                for company_id in result_13:
                    # print(str(row))
                    # return company_id
                    resultlist.append(company_id)
                print(resultlist)
                return resultlist
            else:
                print('?????????cid???????????? ??????????????? ??????!!!!!')
        else:
            print("No such company in company list!!")


def company_id_insert_sxcx(resultlist):
    cur = db.cursor()
    if resultlist is None:
        print("resultList is None!!!")
    else:
        #print(resultlist)
        #sql1 = "INSERT INTO company_link_sxcx(company_link_sxcx_name,company_id) VALUES (%s,%s); "
        #print(resultlist[0],resultlist[5])
        sql3 = "INSERT INTO company_link_sxcx SET " \
               "company_link_sxcx_grouporpeople = '" + resultlist[0] + \
               "',company_link_sxcx_processunit='" + resultlist[1] + \
               "',company_link_sxcx_noticeunit='" + resultlist[2] + \
               "',company_link_sxcx_handtime='" + resultlist[3] + \
               "',company_link_sxcx_time='" + resultlist[4] + \
               "',company_link_sxcx_product='" + resultlist[5] + \
               "',company_id='" + resultlist[6] + "';"
        #cur.execute(sql1, [str(resultlist[0]), str(resultlist[5])])

        cur.execute(sql3)
        db.commit()
        print("Finished!!")


if __name__ == '__main__':
    ####?????????????????????????????? ??? ??????????????????????????????????????????????????????????????????????????????????????? cid???name??? company?????? company_id
    company_research_sxcx("1", "??????")
    company_research_sxcx("2", "??????")
    # company_research_sxcx("3", "??????")
    ####???????????????????????????????????????????????????company_id,????????????????????????????????? ????????? ??????DB??????
    company_id_insert_sxcx(company_research_sxcx("1", "??????"))
    company_id_insert_sxcx(company_research_sxcx("2", "??????"))
    db.close()
    # company_research_sxcx(2, "??????")
    # company_research_sxcx(3,'')
