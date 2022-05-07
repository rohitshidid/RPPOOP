class Time:
    t1_h=0
    t2_h=0
    t1_m=0
    t2_m=0
    def get_time(self):
        print("+++++ Enter the start time ++++++")
        try:
            t1_h=int (input("Enter hours (24 hrs format)"))
            if(t1_h > 23 or t1_h < 00):
                print("Invalid Hour")
                exit(0)
            
        except ValueError:
            print("Enter only Numbers ")
        
        try:
            t1_m = int(input("Enter mins "))
            if(t1_m > 60 or t1_m < 00):
                print("Invalid Minutes")
                exit(0)
        except ValueError:
            print("Enter only Numbers")

        print("+++++ Enter the End time ++++++")
        
        try:
            t2_h=int (input("Enter hours (24 hrs format)"))
            if(t2_h > 23 or t1_h < 00):
                print("Invalid Hour")
                exit(0)
            
        except ValueError:
            print("Enter only Number ")
        
        try:
            t2_m = int(input("Enter mins "))
            if(t1_m > 60 or t1_m < 00):
                print("Invalid Minutes")
                exit(0)
        except ValueError:
            print("Enter only Numbers")

    
        total1 = t1_h * 60 + t1_m
        total2 = t2_h * 60+t2_m
        if(total1 > total2):
            print("End time is before start time ")
            exit(0)
        worked_h = int((total2 - total1)/60)
        worked_m = (total2 - total1)%60
        print("Time difference is {0} hrs {1} mins".format(worked_h,worked_m))
new =Time()
new.get_time()
