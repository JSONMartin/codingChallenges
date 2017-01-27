# Read through array of arrays iteratively and build hash table with lengths (N)
# Read through hash table with a for loop, and return first missing value

def get_length_of_missing_array(array_of_arrays):
    try:
        LENGTH = len(array_of_arrays)
        if LENGTH <= 0: return 0
        MIN_LENGTH, MAX_LENGTH  = len(array_of_arrays[0]), len(array_of_arrays[0])

        array_lengths = {}

        for arr in array_of_arrays:
            if len(arr) <= 0: return 0
            else:
                array_lengths[len(arr)] = True
                MIN_LENGTH = min(MIN_LENGTH, len(arr))
                MAX_LENGTH = max(MAX_LENGTH, len(arr))

        for i in range(MIN_LENGTH, MAX_LENGTH):
            if i in array_lengths: pass
            else: return i

    except: # Input is invalid
        return 0

#########
# TESTS #
#########
