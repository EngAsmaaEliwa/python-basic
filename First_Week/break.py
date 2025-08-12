# نوقف أول ما نلاقي فشل
results = ["PASS", "PASS", "FAIL", "PASS"]
for r in results:
    if r == "FAIL":
        print("Stop at first FAIL")
        break # وقف الوايل
    #output --> هيمر على كل الى موجود و اول ما يلاقى ال fail 
    #يروح طابع الجمله ديه 

# تخطّي اختبارات Low priority
for prio in ["High", "Low", "High" , "asmaa"]:
    if prio == "Low":
        continue
    print("Run:", prio)
    # هنا هيمر على كل القييم و يطبعها عادى و لما تيجى كلمه 
    #continue يعنى عديها و متطبعهاش 
    # output --> 
    #Stop at first FAIL 
    #Run: High
    #Run: High
    #Run: asmaa