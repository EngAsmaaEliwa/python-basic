#هنا عشان انا كتبت اكتر من شرط استخدمت 
# if,elif
status_code = 503
if status_code in [200, 201, 204]:
    result = "PASS"
elif status_code in [400, 401, 403, 404]:
    result = "FAIL (Client Error)"
elif 500 <= status_code <= 599:
    result = "FAIL (Server Error)"
else:
    result = "UNKNOWN"
print(result)
#هنا انا كتبت شرط واحد فروحت استخدمت 
# if,else 
avg_ms = 650
error_rate = 0.01  # 1%
if avg_ms < 800 and error_rate < 0.02:
    print("Healthy")
else:
    print("Needs attention")

