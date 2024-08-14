def some_reverse(x):

    print(f'Enter {x} numbers, no more than 5 digits each')

    for i in range(x):
        some_number = int(input())
        try:
            if len(str(some_number)) > 5:
                raise Exception('Incorrect number')
            reverse_number = int(str(some_number)[::-1])
            print(reverse_number)
        except ValueError:
            print('Incorrect data')
        except Exception as e:
            print(e)
        print('The code is correct')

some_reverse(3)