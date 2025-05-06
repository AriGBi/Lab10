from database.DB_connect import DBConnect
from model.stato import Stato


class DAO():

    @staticmethod
    def getAllCountries():
        conn= DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res=[]

        query=""" Select * from country"""
        cursor.execute(query)
        for row in cursor:
            res.append(Stato(**row))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getCountriesAnno(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []

        query = """ SELECT state1no as s1
                        from contiguity c 
                        where c.`year` <=%s """
        cursor.execute(query, (anno,))
        for row in cursor:
            res.append(row["s1"])

        cursor.close()
        conn.close()
        return res


    @staticmethod
    def getEdges(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []

        query = """ SELECT state1no as s1,state2no as s2
                    from contiguity c 
                    where c.conttype=1 and c.`year` <=%s """
        cursor.execute(query, (anno,))
        for row in cursor:
            res.append((row["s1"], row["s2"]))

        cursor.close()
        conn.close()
        return res

