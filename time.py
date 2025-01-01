class Time:
    def __init__(self,hour,minute,seconds):
        self.__hour =hour
        self.__minute=minute
        self.__seconds=seconds
    def __add__(self,other):
        s=self.__seconds+other.__seconds
        m=self.__minute+other.__minute
        h=(self.__hour+other.__hour)%24
        if(s>=60):
            s%=60
            m=m+1
        if(m>=60):
            m%=60
            h=h+1
        return Time(h,m,s)
    def __str__(self):
        return f"{self.__hour:02d}: {self.__minute:02d}: {self.__seconds:02d}"
t1 = Time(3, 42, 37)
t2 = Time(2, 22, 59)
T=t1+t2
print(T)

    

        
    
    




