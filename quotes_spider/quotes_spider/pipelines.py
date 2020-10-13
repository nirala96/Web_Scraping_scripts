# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector
#database already created
# a table already created






class QuotesSpiderPipeline:

    def create_connection(self):
    # creates connection with the database(host_name,user_name,password,database_name)
        mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'quotes_scrape')  
        
        mycursor = mydb.cursor()
        
        return mydb,mycursor


    def insert_data(self,item):
        #sql = 
        author = item['author']
        quote = item['quote'] 
        tags = item['tags']
        
        #val = []
        try:
            mydb,mycursor = self.create_connection()
            mycursor.execute('INSERT INTO quotes_data VALUES (%s,%s,%s)',(author,quote,tags))
            mydb.commit()
        except Exception as e:
            print("Some exception occured in fetching data from databse {}".format(e))
        finally:
            try:
                mydb.close()
                mycursor.close()
            except Exception as e:
                print("Database connection already closed.")
        


    def process_item(self, item, spider):
        print("++++++++++++++++++++++++++++++++ i am in pipelines.py ++++++++++++++++++++++++++++++++++++++++++++++")
        self.insert_data(item)
        print("+++++++++++++++++++++++++++++++++++")

