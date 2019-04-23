total_process_number = 0
while total_process_number <= 10000:
    print("["+"#"*round(total_process_number/500)+"-"*round((10000-total_process_number)/500)+"]"+str(total_process_number/100)+"%",end='\r')
    total_process_number +=1
print("\ncomplete")