def number_reverse():

    print('Enter number, no more than 5 digits')
    input_number = int(input())
    str_number = str(input_number)
    try:
        if len(str_number) > 5:
            raise Exception('Incorrect number')
        reverse_number = int(str_number[::-1])
        return reverse_number
    except ValueError:
        return 'Incorrect data'
    except Exception as e:
        return e


print(number_reverse())
print(number_reverse())
print(number_reverse())
