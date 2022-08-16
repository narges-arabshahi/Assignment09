class time:
    def __init__(self,h,m,s):
        self.hour=h
        self.minute=m
        self.second=s
    def show(self):
        print(self.hour,":",self.minute,":",self.second)
    def sum(self,mehman):
        result=time(None,None,None)
        result.hour=self.hour + mehman.hour
        result.minute=self.minute + mehman.minute
        result.second=self.second + mehman.second
        if result.second >=60:
            result.second -=60
            result.minute +=1
        if result.minute >= 60:
            result.minute -=60
            result.hour += 1
        return result
    def sub(self,mehman):
        result=time(None,None,None)
        result.hour=self.hour - mehman.hour
        result.minute=self.minute - mehman.minute
        result.second=self.second - mehman.second
        if result.second < 0:
            result.second +=60
            result.minute -=1
        if result.minute < 0:
            result.minute +=60
            result.hour -= 1
        return result
    def convert_second_time(self):
        while self.second >=60:
            self.minute=self.second // 60
            self.second=self.second % 60
            while self.minute >= 60:
                self.minute -=60
                self.hour +=1
        return self
    def convert_time_second(self):
        seconds=int(self.hour) *3600 + int(self.minute) * 60 + int(self.second)
        print('time is :',seconds,'seconds')



t1=time(2,30,45)
t2=time(3,17,40)
t1.show()
t2.show()
t3=t1.sum(t2)
t3.show()
t4=t1.sub(t2)
t4.show()
t5=time(0,0,int(input("enter seconds: ")))
t5=t5.convert_second_time()
t5.show()
t6=time(int(input("enter hour: ")),int(input("enter minute: ")),int(input("enter seconds: ")))
t6.show()
t6.convert_time_second()

