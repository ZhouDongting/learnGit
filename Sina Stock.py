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
                self.scode='sh000001'  #����������󷵻��Ϻ�ָ��
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
            upRate=(float(self.current)-float(self.closePrice))/float(self.closePrice) #�����Ƿ�

            if float(upRate)>0:
                sign='�� '
            elif float(upRate)<0:
                sign='�� '
            else:
                sign='ƽ '
                
            self.upgraderate=sign + str(round(float(upRate) * 100,2)) + '%'
        
            self.bPrice=ss[6]
            self.aPrice=ss[7]
            self.tcount=str(int(float(ss[8])/100)) +' ��'
            self.tcost=str(int(float(ss[9])/10000)) +' ��Ԫ' 
            
            self.buy1=ss[11]+ ', ' +str(int(float(ss[10])/100)) +' ��'
            self.buy2=ss[13]+ ', ' +str(int(float(ss[12])/100)) +' ��'
            self.buy3=ss[15]+ ', ' +str(int(float(ss[14])/100)) +' ��'
            self.buy4=ss[17]+ ', ' +str(int(float(ss[16])/100)) +' ��'
            self.buy5=ss[19]+ ', ' +str(int(float(ss[18])/100)) +' ��'
            self.sell1=ss[21]+ ', ' +str(int(float(ss[20])/100)) +' ��'
            self.sell2=ss[23]+ ', ' +str(int(float(ss[22])/100)) +' ��'
            self.sell3=ss[25]+ ', ' +str(int(float(ss[24])/100)) +' ��'
            self.sell4=ss[27]+ ', ' +str(int(float(ss[26])/100)) +' ��'
            self.sell5=ss[29]+ ', ' +str(int(float(ss[28])/100)) +' ��'
            self.curDate=ss[30]
            self.curTime=ss[31]
            
            print "��Ʊ����:",self.name
            print "���쿪��:",self.openPrice
            print "��������:",self.closePrice
            print "��ǰ�۸�:",self.current
            print "�������:",self.high
            print "�������:",self.low
            print "�ǵ�����:",self.upgraderate
            print "����۸�:",self.bPrice
            print "�����۸�:",self.aPrice
            print "�Ѿ��ɽ�:",self.tcount
            print "�ɽ����:",self.tcost 
            
            print "   ����:",self.buy5
            print "   ����:",self.buy4
            print "   ����:",self.buy3
            print "   ���:",self.buy2
            print "   ��һ:",self.buy1
            print "   ��һ:",self.sell1
            print "   ����:",self.sell2
            print "   ����:",self.sell3
            print "   ����:",self.sell4
            print "   ����:",self.sell5
            
            print "   ����:",self.curDate
            print "   ʱ��:",self.curTime
        except:
            print "�Բ��������������,����������..."
        

if __name__=='__main__':
    code=''
    while 1:
        instr=raw_input("�������Ʊ���룺>>>")
        if (len(instr)!=0):
            code=instr
        print ''
        if code.lower()=='exit':
            print 'exited...'
            break
        me=Stock(code)
        del me
        print ''

