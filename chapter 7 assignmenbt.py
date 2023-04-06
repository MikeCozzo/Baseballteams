def main():
    attempt()


def attempt():
    with open('WorldSeriesWinners.txt', 'r') as f:
        teams = [line.strip() for line in f]
    l = teams

    Checker = False
    while Checker == False:
        inpt = input('Enter name of a team or quit')
        if inpt == 'Quit':
            Checker = True
            print('ending now')
        else:
            counter = 0
            for i in l:
                if inpt in i:
                    counter = counter + 1
            print('The', inpt, 'won the world series', counter, 'times between 1903 and 2009')
        


main()
