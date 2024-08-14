# test code for triangle.py
import triangle
import math

print("test_triangle.py is", __name__)  ## When this file is run as the main file __name__ === "__main__"

def test_is_valid_triangle():
    ''' test is_valid_triangle '''
      ## test case 1
    input = (3, 5, 1)
    expected_output = False
    # Automate the test to say either PASS or FAIL
    # Valid triable is that the sum of ANY two sides must be greater than the third side!
    actual_output = triangle.is_valid_triangle(3, 5, 1) # a = 3, b = 5, c = 1 
    # expected output is False because its not the case that  a + c > b
    if actual_output == expected_output:
        print(f"PASSED: {triangle.is_valid_triangle(3, 5, 1) = }")    
    else:
        print(f"FAILED: {triangle.is_valid_triangle(3, 5, 1) = }")  

    ## test case 2 
    input = (5, 3, 1)
    expected_output = False
    # Automate the test to say either PASS or FAIL
    # Valid triable is that the sum of ANY two sides must be greater than the third side!
    actual_output = triangle.is_valid_triangle(5, 3, 1) # a = 5, b = 3, c = 1 
    # expected output is False because its not the case that  b + c > a
    if actual_output == expected_output:
        print(f"PASSED: {triangle.is_valid_triangle(5, 3, 1) = }")    
    else:
        print(f"FAILED: {triangle.is_valid_triangle(5, 3, 1) = }")  
    # We are failing this test case!
    

test_is_valid_triangle()

