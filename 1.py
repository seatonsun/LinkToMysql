import pymysql


db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="123",
    db="lnulinkdb"
)
if __name__ == '__main__':
    cur = db.cursor()
    sql1 = 'select company_id from company order by company_id DESC limit 1;'
    cur.execute(sql1)
    resultcompany1 = cur.fetchone()


    for i in resultcompany1:
        resultcompanyfina1 = int(str(i).replace('CP','')) + 1
    #print(resultcompanyfina1)
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

    fina = str(fina).replace('1','')
    #print(fina)
    result = "CP" + fina + str(resultcompanyfina1)
    print(result)
    # print(type(result))