def analyze_result(name, roll, marks):
    total=sum(marks)
    average=total/len(marks)
    if average>=90: grade="A"
    elif average>=75: grade="B"
    elif average>=60: grade="C"
    elif average>=40: grade="D"
    else: grade="Fail"
    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total}, Average: {average}")
    print(f"Grade: {grade}")
    below=[]
    for i,m in enumerate(marks,1):
        if m<40: below.append(f"Subject {i}")
    print("Subjects below 40:", ", ".join(below) if below else "None")

name="Aarav"
roll=101
marks=[88.5,35.0,76.0,92.5,48.0]
analyze_result(name,roll,marks)
