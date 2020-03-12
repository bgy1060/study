while(1):
    n=int(input(""))
    dic={"남성":[],"여성":[]}
    if (n<=1 or n<=1000):
        for i in range(n):
            resident_number = input("")
            if(resident_number[7]=='1' or resident_number[7]=='3'):
                dic["남성"].append(resident_number)
            else:
                dic["여성"].append(resident_number)
        print(dic)    
        break
            
    else:
        print("n은 최소 1개, 최대 1000개 입니다. n을 다시 입력해 주세요.")
        


    