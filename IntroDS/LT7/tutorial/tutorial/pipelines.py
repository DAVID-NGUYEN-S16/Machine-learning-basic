# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class TutorialPipeline:
#     def process_item(self, item, spider):
#         return item
import csv
class TutorialPipeline:
    def open_spider(self, spider):
        self.file = open('TKB.csv', 'w',  encoding='utf-8', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(["Môn học", "Ngày tháng", "Thời gian", "Phòng học"]) # Tên các cột trong file CSV
    
    def close_spider(self, spider):
        self.file.close()
    
    def process_item(self, item, spider):
        # df.loc[id] = [c, Datetime[id_day],time,  class_.text]
        self.writer.writerow([item['course'], item[ 'datetime'], item['time'], item['class']])
        return item