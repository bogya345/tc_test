
import datetime

if __name__ == '__main__':
    
    with open('./logs/test2_res.txt', 'r+') as f:
        print(str(datetime.datetime.now()))
        print(f.readline())
        pass

    print('End test3')

    pass