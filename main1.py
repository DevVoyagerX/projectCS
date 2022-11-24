import csv



fixtures = open('fixtures.csv')
csv_reader = csv.reader(fixtures)

def menu():

    country = input('Enter the country you want to know the fixtures:')
    return country

def Engine(country):
    listofcountries = ['Qatar','France','Portugal','Senegal','Saudi Arabia']
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


run = menu()


Engine(run)
