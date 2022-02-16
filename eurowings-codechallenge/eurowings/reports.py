"""reports.py:
    Provide queries of any required report
"""
__author__      = "Adel Ramezani <adramazany@gmail.com>"

from eurowings.helper import spark

class Reports:

    def searchCountByCountryRegion(self):
        df = spark.sql("select date_format(s.date,'yyyy-MM-dd') date"
                              ",v.country"
                              ",v.region"
                              ",count(*) count"
                              " from parquet.searches s"
                              " left join (select visitor_id,date"
                              ",min(country) as country"
                              ",min(region) as region"
                              " from parquet.visitors"
                              " group by date,visitor_id"
                              ")v on (v.visitor_id=s.visitor_id and v.date=s.date)"
                              " group by s.date,v.country,v.region")
        # return df.collect()
        return df
