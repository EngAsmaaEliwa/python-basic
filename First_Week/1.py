# انا عايزه احسب نسبة النجاح 
passed = 37
failed = 3
total = passed + failed
pass_rate = (passed / total) * 100
print(f"Pass rate = {pass_rate}%")  # السطر ده معناه ايه 
# (f"")--> و ده عشان اعرف احط متغيير بين الاقواس {}الى هو
# pass rate متغيير 

# شروط على أزمنة الاستجابة عشان اتمم ان الرد بيكون خلال وقت معين حته زياده ممكن تعديها دلوقتى 
avg_ms = 820
sla_ms = 1000
print("OK under SLA?", avg_ms <= sla_ms)

#   كود حالة HTTP حته زياده ممكن تعديها دلوقتى 
status_code = 201
is_success = status_code in [200, 201, 204]
print("API success?", is_success)
