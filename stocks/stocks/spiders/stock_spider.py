#-*- coding:utf-8 -*-
import scrapy
import MySQLdb
import re
from stocks.items import StocksItem

class StockSpider(scrapy.Spider):
    name = "stock"
    allowed_domains = ["baidu.org"]
    #start_urls = self.get_start_urls("./stock_url.txt")
    #start_urls = ['https://gupiao.baidu.com/stock/sh600054.html']
    def __init__(self):
        super(StockSpider, self).__init__()
        self.start_urls = self.get_start_urls("./stock_url.txt")

    def parse(self, response):
        sitem = StocksItem()
        gpmc_tmp = response.xpath("//a[@class='bets-name']/text()").extract()
        gpmc = gpmc_tmp[0].replace(' ', '')
        length = len(gpmc) - 1
        gpmc = gpmc[0:length]
        sitem['gpmc'] = gpmc.replace('\n', '')
        gpjym = response.xpath("//a[@class='bets-name']/span/text()").extract()
        sitem['gpjym'] = gpjym[0]
        jyr = response.xpath("//span[@class='state f-up']/text()").extract()
        sitem['jyr'] = self.parse_datetime(jyr[0])
        spjg = response.xpath("//strong[@class='_close']/text()").extract()
        spjg = spjg[0]
        if spjg == '--' or spjg == '-' or spjg == '':
           spjg = '0.0'
        sitem['spjg'] = spjg
        zfz = response.xpath("////*[@id='app-wrap']/div[2]/div/div[1]/span[1]/text()").extract()
        sitem['zfz'] = self.convert_none_numeral(zfz[0])
        zfb = response.xpath("//*[@id='app-wrap']/div[2]/div/div[1]/span[2]/text()").extract()
        sitem['zfb'] = self.convert_none_numeral(zfb[0].replace('%', '')) 
        jkjg = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[1]/dl[1]/dd/text()").extract() 
        sitem['jkjg'] = self.convert_none_numeral(jkjg[0])
        zsjg = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[2]/dl[1]/dd/text()").extract()
        if len(zsjg) == 0:
            sitem['zsjg'] = '0.0'
        else:
            sitem['zsjg'] = self.convert_none_numeral(zsjg[0])
        cjl = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[1]/dl[2]/dd/text()").extract()
        if len(cjl) == 0:
            sitem['cjl'] = '0.0'
        else:
            sitem['cjl'] = self.parse_cjl_numeral(cjl[0])
        hsl = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[2]/dl[2]/dd/text()").extract()
        hsl = hsl[0]
        if hsl == '--' or hsl == '-' or hsl == '':
           hsl = '0.00'
        sitem['hsl'] = hsl[:(len(hsl)-1)]
        zgjg = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[1]/dl[3]/dd/text()").extract()
        zgjg = zgjg[0]
        if zgjg == '--' or zgjg == '-' or zgjg == '':
           zgjg = '0.0'
        sitem['zgjg'] = zgjg
        zdjg = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[2]/dl[3]/dd/text()").extract()
        zdjg = zdjg[0]
        if zdjg == '--' or zdjg == '-' or zdjg == '':
           zdjg = '0.0'
        sitem['zdjg'] = zdjg
        ztjg = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[1]/dl[4]/dd/text()").extract()
        ztjg = ztjg[0]
        if ztjg == '--' or ztjg == '-' or ztjg == '':
           ztjg = '0.0'
        sitem['ztjg'] = ztjg
        dtjg = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[2]/dl[4]/dd/text()").extract()
        dtjg = dtjg[0].replace(' ', '')
        if dtjg == '--' or dtjg == '-' or dtjg == '':
           dtjg = '0.0'
        sitem['dtjg'] = dtjg.replace('\n', '')
        np = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[1]/dl[5]/dd/text()").extract()
        sitem['np'] = self.parse_cjl_numeral(np[0])
        wp = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[2]/dl[5]/dd/text()").extract()
        sitem['wp'] = self.parse_cjl_numeral(wp[0])
        cje = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[1]/dl[6]/dd/text()").extract()
        sitem['cje'] = self.parse_cje_numeral(cje[0])
        zf = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[2]/dl[6]/dd/text()").extract()
        zf = zf[0]
        if zf == '--' or zf == '-' or zf == '':
           zf = '0.00'
        sitem['zf'] = zf[:(len(zf)-1)]
        wb = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[1]/dl[7]/dd/text()").extract()
        wb = wb[0]
        if wb== '--' or wb == '-' or wb == '':
           wb = '0.00'
        sitem['wb'] = wb[:(len(wb)-1)]
        lb = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[2]/dl[7]/dd/text()").extract()
        lb = lb[0]
        if lb == '--' or lb == '-' or lb == '':
           lb = '0.0'
        sitem['lb'] = lb
        ltsz = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[1]/dl[8]/dd/text()").extract()
        sitem['ltsz'] = self.parse_cje_numeral(ltsz[0])
        zsz = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[2]/dl[8]/dd/text()").extract()
        sitem['zsz'] = self.parse_cje_numeral(zsz[0])
        syl = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[1]/dl[9]/dd/text()").extract()
        syl = syl[0]
        if syl == '--' or syl == '-' or syl == '':
           syl = '0.0'
        sitem['syl'] = syl
        sjl = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[2]/dl[9]/dd/text()").extract()
        sjl = sjl[0]
        if sjl == '--' or sjl == '-' or sjl == '':
           sjl = '0.0'
        sitem['sjl'] = sjl
        mgsy = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[1]/dl[10]/dd/text()").extract()
        mgsy = mgsy[0]
        if mgsy == '--' or mgsy == '-' or mgsy == '':
           mgsy = '0.0'
        sitem['mgsy'] = mgsy
        mgjzc = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[2]/dl[10]/dd/text()").extract()
        mgjzc = mgjzc[0]
        if mgjzc == '--' or mgjzc == '-' or mgjzc == '':
           mgjzc = '0.0'
        sitem['mgjzc'] = mgjzc
        zgb = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[1]/dl[11]/dd/text()").extract()
        sitem['zgb'] = self.parse_cje_numeral(zgb[0])
        ltgb = response.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[2]/dl[11]/dd/text()").extract()
        sitem['ltgb'] = self.parse_cje_numeral(ltgb[0])
        #zllrl = response.xpath("//div[@class='side-fund-today']/dl[1]/dd[1]/text()").extract()
        #zllrl = zllrl[0]
        #print zllrl
        #sitem['zllrl'] = zllrl[:(len(zllrl)-1)]
        #zllrz = response.xpath("//*[@id='app-wrap']/div[5]/div[2]/div[1]/div[2]/dl[1]/dd[2]/text()").extract()
        #print zllrz[0]
        #sitem['zllrz'] = self.parse_cje_numeral(zllrz[0])
        #print sitem[zllrl]
        #print sitem[zllrz]

        #print sitem['zfz']
        #print sitem['gpmc']
        #print sitem['gpjym']
        #print sitem['jyr']
        #print sitem['zfz']
        #print sitem['zfb']
        #print sitem['jkjg']
        #print sitem['zsjg']
        #print sitem['cjl']
        #print sitem['hsl']
        #print sitem['zgjg']
        #print sitem['zdjg']
        #print sitem['ztjg']
        #print sitem['dtjg']
        #print sitem['np']
        #print sitem['wp']
        #print sitem['cje']
        #print sitem['zf']
        #print sitem['wb']
        #print sitem['lb']
        #print sitem['ltsz']
        #print sitem['zsz']
        #print sitem['syl']
        #print sitem['sjl']
        #print sitem['mgsy']
        #print sitem['mgjzc']
        #print sitem['zgb']
        #print sitem['ltgb']
        stype = self.get_stock_type(gpjym[0])
        sitem['scid'] = stype['scid']
        sitem['stid'] = stype['stid']
        self.insert_data_to_db(stock_item = sitem)

    def get_stock_type(self, stock_num):
        stype = {}
        if re.search(r'60[0|1|3|X]\d{3}', stock_num):
            stype['scid'] = '1'
            stype['stid'] = '1'
        elif re.search(r'00[0|X]\d{3}', stock_num):
            stype['scid'] = '2'
            stype['stid'] = '2'
        elif re.search(r'730\d{3}', stock_num):
            stype['scid'] = '1'
            stype['stid'] = '3'
        elif re.search(r'700\d{3}', stock_num):
            stype['scid'] = '1'
            stype['stid'] = '5'
        elif re.search(r'080\d{3}', stock_num):
            stype['scid'] = '2'
            stype['stid'] = '6'
        elif re.search(r'002\d{3}', stock_num):
            stype['scid'] = '2'
            stype['stid'] = '7'
        elif re.search(r'300\d{3}', stock_num):
            stype['scid'] = '2'
            stype['stid'] = '8'
        else:
            pass
        return stype
            
    def convert_none_numeral(self, none_numeral):
        if none_numeral == '--' or none_numeral == '-' or none_numeral == '':
            return  '0.0'
        else:
            return none_numeral

    def parse_cjl_numeral(self, cjl_str):
        pat1 = r"\d+\.\d{2,4}"
        cjl_numeral = 0.0
        if cjl_str == '--' or cjl_str == '-' or cjl_str == '':
            cjl_str == '0.00'
        m1 = re.search(pat1, cjl_str)
        if m1:
            cjl_numeral = float(m1.group(0)) * 10000
            cjl_numeral = str(int(cjl_numeral))
        else:
            m2 = re.search(r"\d+", cjl_str)
            if m2:
                cjl_numberal = m2.group(0)
        return str(cjl_numeral)
    
    def parse_cje_numeral(self, cje_str):
        cje_numeral = 0.0
        factor = 0
        if cje_str == '--':
            cje_str == '0.00'
        m1 = re.search(r'\d+\.\d{2,4}', cje_str)
        if m1:
            cje_numeral = float(m1.group(0))
            if unicode('千亿', 'utf-8') in cje_str:
                cje_numeral = cje_numeral * 100000000000
            elif unicode('亿', 'utf-8') in cje_str:
                cje_numeral = cje_numeral * 100000000
            elif unicode('万', 'utf-8') in cje_str:
                cje_numeral = cje_numeral * 10000
            else:
                pass
        else:
            m2 = re.search(r"\d+", cje_str)
            if m2:
                cje_numberal = m2.group(0)
        return str(int(cje_numeral))

    def parse_datetime(self, datetime):
        pat1 = r"\d{4}-\d{2}-\d{2}"
        pat2 = r"\d{2}:\d{2}:\d{2}"
        m1 = re.search(pat1, datetime)
        date = m1.group(0)
        m2 = re.search(pat2, datetime)
        time = m2.group(0)
        return date + ' ' + time

    def get_start_urls(self, url_file):
        fd = open(url_file, "r")
        stock_urls = []
        for line in fd.readlines():
            stock_urls.append(line.strip("\r\n"))
        return stock_urls

    def insert_data_to_db(self, stock_item, user="root", password="123456", db_host="localhost", port=3306):
        conn= MySQLdb.connect(host=db_host, port = port, user=user, passwd=password, db="stock_db", use_unicode=True, charset="utf8")
        cur = conn.cursor()
        sql  = "insert into Stock_Info(GPJYM,GPMC,STID,SCID,JYR,SPJG,JKJG,SJJG,CJL,HSL,ZGJG,ZDJG,"
        sql += "ZTJG,DTJG,NP,WP,CJE,ZF,WB,LB,LTSZ,ZSZ,SYL,SJL,MGSY,MGJZC,ZGB,LTGB) value ('"
        sql += stock_item['gpjym'] + "','" + stock_item["gpmc"] + "'," + stock_item['stid'] + "," +  stock_item['scid']
        sql += ",'" + stock_item['jyr'] + "'," + stock_item['spjg'] + "," + stock_item['jkjg'] + "," + stock_item['zsjg'] 
        sql += "," + stock_item['cjl'] + "," + stock_item['hsl'] + "," + stock_item['zgjg'] + "," + stock_item['zdjg'] 
        sql += "," + stock_item['ztjg'] + "," + stock_item['dtjg'] + "," + stock_item['np'] + "," + stock_item['wp'] 
        sql += "," + stock_item['cje'] + "," + stock_item['zf'] + "," + stock_item['wb'] + "," + stock_item['lb'] 
        sql += "," + stock_item['ltsz'] + "," + stock_item['zsz'] + "," + stock_item['syl'] + "," + stock_item['sjl']
        sql += "," + stock_item['mgsy'] + "," + stock_item['mgjzc'] + "," + stock_item['zgb'] + "," + stock_item['ltgb'] + ");"
        #print sql
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
