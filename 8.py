# find 13 digits with the greatest product in the 1000 digit number

number = """73167176531330624919225119674426574742355349194934969835203127745063262395783180169848018694788518431254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"""

def get_string_from_index(start_index, end_index):
    return (number[start_index:end_index])

def get_array_from_string(string):
    array = []
    for i in range(0, 13):
        array.append(string[i])
    return array

def mult_nums_in_array(array):
    result = 1
    for item in array:
        result *= int(item)
    return result



curr_start_index = 0
curr_end_index = 13
curr_highest_start = 0
curr_highest_end = 13
curr_highest = 0
while curr_end_index < len(number):
    string = get_string_from_index(curr_start_index, curr_end_index)
    array = get_array_from_string(string)
    result = mult_nums_in_array(array)
    if result > curr_highest:
        curr_highest_start = curr_start_index
        curr_highest_end = curr_end_index
        curr_highest = result
        print("Overall stats: indexes: {0}-{1}; highest: %{2}".format(curr_highest_start, curr_highest_end, curr_highest))
    print("Loop stats: indexes = {0}-{1}; array = {2}; result = {3}".format(curr_start_index, curr_end_index, array, result))
    curr_start_index += 1
    curr_end_index += 1

print("Overall stats: indexes: {0}-{1}; highest: {2}".format(curr_highest_start, curr_highest_end, curr_highest))