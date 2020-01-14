def trans_kor_eng(word_num,lang_num):
    word_text={1:'안녕하세요',2:'감사합니다',3:'실례합니다',4:'이화여자대학교'}
    if lang_num==1:
        if word_num==1:
            print("사용자 입력 내용         영어 출력 내용")
            print("-"*40)
            print("  ",word_text[word_num],"              Hello")
        elif word_num==2:
            print("사용자 입력 내용         영어 출력 내용")
            print("-"*40)
            print(" ",word_text[word_num],"             Thank You")
        elif word_num==3:
            print("사용자 입력 내용         영어 출력 내용")
            print("-"*40)
            print(" ",word_text[word_num],"             Excuse Me ")
        elif word_num==4:
            print("사용자 입력 내용         영어 출력 내용")
            print("-"*40)
            print("",word_text[word_num],"        Ehwa Womans Univ. ") 
    
    
    elif lang_num==2:
        if word_num==1:
            print("사용자 입력 내용         중국어 출력 내용")
            print("-"*40)
            print(" ",word_text[word_num],"                 你好")
        elif word_num==2:
            print("사용자 입력 내용         중국어 출력 내용")
            print("-"*40)
            print(" ",word_text[word_num],"               谢谢啦 ")
        elif word_num==3:
            print("사용자 입력 내용         중국어 출력 내용")
            print("-"*40)
            print(" ",word_text[word_num],"               不好意思")
        elif word_num==4:
            print("사용자 입력 내용         중국 출력 내용")
            print("-"*40)
            print("",word_text[word_num],"          梨花女子大学 ")
        
        
word_list={1:'안녕하세요',2:'감사합니다',3:'실례합니다',4:'이화여자대학교'}
lang_list={1:'Korean to English translation',2:'Korean to Chinese translation'}
lang_choice=int(input("Enter 1 for English and 2 for Chinese:"))

print("You have chosen", lang_list[lang_choice])
word_choice=int(input("Enter word number 1 to 4:"))
trans_kor_eng(word_choice,lang_choice)