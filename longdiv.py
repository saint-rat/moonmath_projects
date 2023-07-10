import random

def long_div(a, b):
    """Computes the euclidian long division of a divided by b. returns a
    tuple in the form (answer, remainder)
    inputs: a -> int
            b -> int
    returns (ans,r) -> (int, int)"""

    assert isinstance(a, int)
    assert isinstance(b, int)
    if(a == 0):
        return (0,0)
    elif(b == 0):
        return (0,a)
    
    ans_str = ''
    r = 0
    ans = 0

    a_abs = abs(a)
    b_abs = abs(b)
    is_neg = False

    # if it's negative add to the ans_str now so it's dealt with
    if((a < 0 and b > 0) or
            (b < 0 and a > 0)):
        ans_str += '-'  # even if it's '-0' it will be fine
        is_neg = True
    
    str_a = str(a_abs)
    for digit_num in range(len(str_a)):

        digit = str_a[digit_num]
        div_num = r*10 + int(digit)
        
        # do normal division
        if ((digit_num+1) != len(str_a)):
            div_ans = int(div_num / b_abs)
            ans_str += str(div_ans)
            
        # need to round last digit properly
        else:
            if(a > 0):
                div_ans = int(div_num/b_abs)
            else:
                if(((div_num/b_abs) - int(div_num/b_abs)) > 0):
                    div_ans = int(div_num/b_abs) + 1
                else:
                    div_ans = int(div_num/b_abs)
            
            # if not 10 we can just add the digit to the string
            if(div_ans != 10):
                ans_str += str(div_ans)

            # other previous digits need to change if div_ans is 10
            # so we just turn the str back to int and add or subtract
            else:
                if(is_neg):
                    ans_str = str(int(ans_str + '0') - div_ans)
                else:
                    ans_str = str(int(ans_str + '0') + div_ans)                
        
        # calc the remainder
        r = abs(div_num - div_ans*b_abs)
    
    ans = int(ans_str)
    return ans, r

def test():

    num_tests = 1000000
    correct = 0
    
    for _ in range(num_tests):
        a = random.randint(-10,10)
        b = random.randint(-10,10)
        ans, r = long_div(a,b)

        # check each answer is correct, if not, print it.
        if(b != 0 and ((r >= abs(b)) or (b*ans+r != a) or (r < 0))):
            print(f"a: {a}, b: {b} = ans: {ans}, r: {r}, b*ans+r = {b*ans+r}")
        else:
            correct += 1
    
    if (correct == num_tests):
        print("all correct")

if __name__ == "__main__":
    test()
