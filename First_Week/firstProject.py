num = int(input("How many tests? "))
passed = failed = warn = 0
times = []

for i in range(1, num + 1):
    sc = int(input(f"[Test {i}] Status code: "))
    rt = float(input(f"[Test {i}] Response time (ms): "))
    times.append(rt)

    if sc in [200, 201, 204] and rt < 800:
        print("=> PASS")
        passed += 1
    elif sc in [200, 201, 204] and rt >= 800:
        print("=> WARN (Slow)")
        warn += 1
    else:
        print("=> FAIL")
        failed += 1

avg_time = sum(times) / len(times)
print("\nSummary:")
print("PASS:", passed, "| WARN:", warn, "| FAIL:", failed)
print(f"Average time: {avg_time:.2f} ms")
