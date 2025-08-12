attempt = 1
max_attempts = 3
success = False

#الفكره فى while انك هتشتغل لحد ما توصل لقيمه معينه 
#while the value of attempts not eqqual to the value of max_attempts  انت شغال و بتطبع  

while attempt <= max_attempts and not success:
    print(f"Attempt {attempt} ..")
    # محاكاة: أول محاولتين فاشلين، الثالثة تنجح
    success = (attempt == 3)
    attempt += 1

print("Result:", "PASS" if success else "FAIL")
