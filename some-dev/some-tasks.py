"""
def some_reverse(number_of_requests):

    print(f'Enter {number_of_requests} numbers, no more than 5 digits each')

    for i in range(number_of_requests):
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
"""


def number_reverse():

    print('Enter number, no more than 5 digits')
    input_number = int(input())
    try:
        if len(str(input_number)) > 5:
            raise Exception('Incorrect number')
        reverse_number = int(str(input_number)[::-1])
        print(reverse_number)
    except ValueError:
        print('Incorrect data')
    except Exception as e:
        print(e)


number_reverse()
number_reverse()
number_reverse()
