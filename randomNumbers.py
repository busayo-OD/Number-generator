import random

def randomNumbers():
    range_start = eval(input("Enter start: "))
    range_stop = eval(input("Enter stop: "))

    yes = set(['yes','y', 'ye', ''])
    no = set(['no', 'no'])

    while True:
        step = eval(input("Include Step, Enter yes or no: "))
        
        if step == yes:
            range_step = eval(input("Enter step: "))
            
            even = set(['even', 'eve', 'ev'])
            odd = set(['odd', 'od'])
            both = set(['both', 'bot'])

            while True:
                numtype = eval(input("Enter even or odd  or both: "))
                numbers1 = random.sample(range(range_start, range_stop, range_step), 5)
                print(numbers1)

                if numtype == even:
                    even_nos = list(filter(lambda x: (x % 2 == 0), numbers1))
                    return even_nos
                
                elif numtype == odd:
                    odd_nos = list(filter(lambda x: (x % 2 != 0), numbers1))
                    return odd_nos
                elif numtype == both:
                    return numbers1
                else:
                    return "Please enter numtype"
            break
                     
        elif step == no:
            even = set(['even', 'eve', 'ev'])
            odd = set(['odd', 'od'])
            both = set(['both', 'bot'])

            while True:
                numtype = eval(input("Enter even or odd  or both: "))
                numbers2 = random.sample(range(range_start, range_stop), 5)
                print(numbers2)
                
                if numtype == even:
                    even_nos = list(filter(lambda x: (x % 2 == 0), numbers2))
                    return even_nos
                
                elif numtype == odd:
                    odd_nos = list(filter(lambda x: (x % 2 != 0), numbers2))
                    return odd_nos
                elif numtype == both:
                    return numbers2
                else:
                    return "Please enter numtype"
            break   
        else:
            return "Please enter yes or no"

print(randomNumbers())


