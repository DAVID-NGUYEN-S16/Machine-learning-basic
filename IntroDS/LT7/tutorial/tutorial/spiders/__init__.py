import scrapy
import re
class MySpider(scrapy.Spider):
  import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ["https://sv.iuh.edu.vn/SinhVienTraCuu/GetDanhSachLichTheoTuan"]
    headers = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'ASP.NET_SessionId=s24w4sqrmanmpupmxwm4j0yi',
        'Origin': 'https://sv.iuh.edu.vn',
        'Referer': 'https://sv.iuh.edu.vn/tra-cuu/lich-hoc-theo-tuan.html?k=JJKCYq3ZGwh66sI2wLLxzrYsplZE08si-6NqTXZEMTE',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    payload = {
        'k': 'JJKCYq3ZGwh66sI2wLLxzrYsplZE08si-6NqTXZEMTE',
        'pNgayHienTai': '1680614547452',
        'pLoaiLich': '0'
    }

    def start_requests(self):
        yield scrapy.FormRequest(
            url=self.start_urls[0],
            headers=self.headers,
            formdata=self.payload,
            callback=self.parse
        )

    def parse(self, response):
        # Handle the response here
        print("++++++++++++++++++++++++++++++++++")
        # print(response.text)

    # def parse(self, response):
        time = response.xpath("//th")[1:]
        datetimes = []
        # datetimes = [i.xpath('.//text()').get().split('\n')[1] for i in time]
        for row in time:
            date_selector = row.xpath('//th')
            date_text = date_selector.re(r'\d{2}/\d{2}/\d{4}')[0]
            datetimes.append(date_text)
        # print(response.xpath("//tbody//tr"))
        # lesson = response.xpath("//tbody//tr")[1]
        # print(lesson.xpath('.//td'))
        # print("++++++++++++++++++++++++++++++++++")
        for lesson in response.xpath("//tbody//tr"):
            id_day = -1
            b = 0
            for study in lesson.xpath('.//td')[1:]:
                id_day += 1
                if study.xpath('//text()').get() != "":
                    for mon in study.xpath('.//div'):
                
                        class_ = mon.xpath('.//span/text()').get()
                        course_ = mon.xpath('.//b//a/text()').get()
                        p_tags = mon.xpath('.//p')[1]
                        pattern = r'Tiết:\s*\d+\s*-\s*\d+'
                        time = re.search(pattern, p_tags.xpath('.//text()').get()).group(0)
                        # print(class_, course_, time)
                        # print(datetimes[id_day])
                        print("++++++++++++++++++++++++++++++++++")
                        print(class_,course_, time, datetimes[id_day] )
                        print("++++++++++++++++++++++++++++++++++")
                        yield {
                            'class': class_,
                            'course': course_,
                            'time': time,
                            'datetime': datetimes[id_day]
                        }