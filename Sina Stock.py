# -*- coding: cp936 -*-
import urllib2

class Stock(object):
    def __init__(self,code):
        scode=str(code)
        if scode.startswith('60'):
            self.scode='sh'+scode
        elif scode.startswith('00'):
            self.scode='sz'+scode
        elif scode.startswith('51'):
            self.scode='sz'+scode
        elif len(code)==0:
            self.scode='sz399001'
        else:
            self.scode='sh'+scode
            
        name=''
        openPrice=''
        closePrice=''
        current=''
        high=''
        low=''
        self.upgraderate=''

        bPrice=''
        aPrice=''
        tcount=''
        tcost=''   
        
        buy1=''
        buy2=''
        buy3=''
        buy4=''
        buy5=''
        sell1=''
        sell2=''
        sell3=''
        sell4=''
        sell5=''
        curDate=''
        curTime=''
        
        self.main()
        
    def main(self):
        
        try:

            page=urllib2.urlopen('http://hq.sinajs.cn/list='+self.scode,timeout=20)
            data=page.read()
            if len(data)<50:
                self.scode='sh000001'  #出现输入错误返回上海指数
                page=urllib2.urlopen('http://hq.sinajs.cn/list='+self.scode,timeout=20)
                data=page.read()
            #print data
            #print len(data)
                
            ss=data.split(',')

            i=ss[0].find('\"')+1
            self.name=ss[0][i:]
        
            self.name=ss[0][i:]
            self.openPrice=ss[1]
            self.closePrice=ss[2]
            self.current=ss[3]
            self.high=ss[4]
            self.low=ss[5]
            upRate=(float(self.current)-float(self.closePrice))/float(self.closePrice) #计算涨幅

            if float(upRate)>0:
                sign='涨 '
            elif float(upRate)<0:
                sign='跌 '
            else:
                sign='平 '
                
            self.upgraderate=sign + str(round(float(upRate) * 100,2)) + '%'
        
            self.bPrice=ss[6]
            self.aPrice=ss[7]
            self.tcount=str(int(float(ss[8])/100)) +' 手'
            self.tcost=str(int(float(ss[9])/10000)) +' 万元' 
            
            self.buy1=ss[11]+ ', ' +str(int(float(ss[10])/100)) +' 手'
            self.buy2=ss[13]+ ', ' +str(int(float(ss[12])/100)) +' 手'
            self.buy3=ss[15]+ ', ' +str(int(float(ss[14])/100)) +' 手'
            self.buy4=ss[17]+ ', ' +str(int(float(ss[16])/100)) +' 手'
            self.buy5=ss[19]+ ', ' +str(int(float(ss[18])/100)) +' 手'
            self.sell1=ss[21]+ ', ' +str(int(float(ss[20])/100)) +' 手'
            self.sell2=ss[23]+ ', ' +str(int(float(ss[22])/100)) +' 手'
            self.sell3=ss[25]+ ', ' +str(int(float(ss[24])/100)) +' 手'
            self.sell4=ss[27]+ ', ' +str(int(float(ss[26])/100)) +' 手'
            self.sell5=ss[29]+ ', ' +str(int(float(ss[28])/100)) +' 手'
            self.curDate=ss[30]
            self.curTime=ss[31]
            
            print "股票名称:",self.name
            print "今天开盘:",self.openPrice
            print "昨天收盘:",self.closePrice
            print "当前价格:",self.current
            print "今天最高:",self.high
            print "今天最低:",self.low
            print "涨跌幅度:",self.upgraderate
            print "竞买价格:",self.bPrice
            print "竞卖价格:",self.aPrice
            print "已经成交:",self.tcount
            print "成交金额:",self.tcost 
            
            print "   买五:",self.buy5
            print "   买四:",self.buy4
            print "   买三:",self.buy3
            print "   买二:",self.buy2
            print "   买一:",self.buy1
            print "   卖一:",self.sell1
            print "   卖二:",self.sell2
            print "   卖三:",self.sell3
            print "   卖四:",self.sell4
            print "   卖五:",self.sell5
            
            print "   日期:",self.curDate
            print "   时间:",self.curTime
        except:
            print "对不起，你的输入有误,请重新输入..."
        

if __name__=='__main__':
    code=''
    while 1:
        instr=raw_input("请输入股票代码：>>>")
        if (len(instr)!=0):
            code=instr
        print ''
        if code.lower()=='exit':
            print 'exited...'
            break
        me=Stock(code)
        del me
        print ''

