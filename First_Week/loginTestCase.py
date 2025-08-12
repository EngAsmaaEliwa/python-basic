# خطوات اختبار (اسم الخطوة، النتيجة المتوقعة، النتيجة الفعلية)
steps = [
    {"name": "Open login page", "expected": True, "actual": True},
    {"name": "Enter username", "expected": True, "actual": True},
    {"name": "Enter password", "expected": True, "actual": True},
    {"name": "Click login", "expected": True, "actual": True},
    {"name": "Redirect to dashboard", "expected": True, "actual": False},  # فشل
]

all_pass = True
failed_steps = []

for s in steps:
    step_pass = (s["expected"] == s["actual"])
    print(f"- {s['name']}: {'PASS' if step_pass else 'FAIL'}")
    if not step_pass:
        all_pass = False
        failed_steps.append(s["name"])

print("\nTest Case Result:", "PASS" if all_pass else "FAIL")
if failed_steps:
    print("Failed steps:", ", ".join(failed_steps))
