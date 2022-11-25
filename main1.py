import csv
import sys
from tabulate import tabulate


fixtures = open('fixtures.csv')
csv_reader = csv.reader(fixtures)

def options():
    print('1.Teams')
    print('2.Fixtures')
    print('3.Squad List')
    print('4.Quit')
    option=int(input('Select your option number:'))
    if option == 1:
        teams()
    elif option ==2:
        FixturesFunc()
    elif option ==3:
        c = input('Enter the country you want to know the squad:')
        SquadFiles(c)
    else:
        print('Goodbye')
        sys.exit()

#Country should be the variable from the option
def SquadFiles(country):
    filename = country+'.csv'
    with open(filename) as Squad:
        SquadObject = csv.reader(Squad)
        listofSquad=[]
        listofSquad.append(['Number','Name','Position'])
        for row in SquadObject:
            listofSquad.append(row,)
        print(tabulate(listofSquad,tablefmt='grid'))

        print()
def teams():
    team=open('teams.csv')
    csv_reader=csv.reader(team)
    for i in csv_reader:
        print('{:<20} {:<10}'.format(i[0],i[1]))
def FixturesFunc():
    country = input('Enter the country you want to know the fixtures:')
    listofcountries = ['Qatar','France','Portugal','Senegal','Saudi Arabia']
    #Here also change into tabulate format
    print("{:<13} {:<14} {:<20} {:<25} {:<15} {:<15} {:<9} {:<5}".format('Match Number','Round Number','Date&Time','Location','Home Team','Away Team','Group','Result'))
    for check_country in listofcountries:
        if country == check_country:
            for row in csv_reader:
                if row[0] == 'Match Number':
                    continue
                elif country == check_country:
                    if row[4] == check_country or row[5] == check_country:
                        MatchNum,Round,Date,Location,Home,Away,Group,Result = row
                        print("{:<13} {:<14} {:<20} {:<25} {:<15} {:<15} {:<9} {:<5}".format(MatchNum,Round,Date,Location,Home,Away,Group,Result))
    print('-'*150)


while True:
    options()
    answer = input('Do you want to continue "y or n"?')
    if answer == 'n':
        break
else:
    print('-'*100)
