def get_age():
    age=int(input())
    if age<18 or age>75:
        #raising ValueError with message: 'Invalid age.'
        raise ValueError('Invalid age.')
    return age

def fat_burning_heart_rate(age):
    heart_rate=(220-age)*.70
    return heart_rate

if __name__ == '__main__':
    try:
        #reading age
        age=get_age()
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age,fat_burning_heart_rate(age)))
    except ValueError as ve:
        print(ve)
        print('Could not calculate heart rate info.\n')