
import statistics

i = 0
lowest = 1000
lowestYear = ''
lowestCountry = ''
highest = 10000
yearHigh = ''
countryHigh = ''
choiceYear = int(input('Enter a year of interest: '))
choice = []
with open('life-expectancy.csv') as lifeFile:
    for line in lifeFile:
        i += 1
        cleanLine = line.strip()
        words = cleanLine.split(',')
        if i > 1:
            country = words[0]
            code = words[1]
            year = int(words[2])
            lifeExp = float(words[3])
            if lowest > lifeExp:
                lowest = lifeExp
                lowestYear = year
                lowestCountry = country
                
            if highest < lifeExp:
                highest = lifeExp
                countryHigh = country
                yearHigh = year
                
            if choiceYear == year:
                choice.append(lifeExp)
                
                if lowest > lifeExp:
                    lowest = lifeExp
                    lowestYear = year
                    lowestCountry = country
                
                if highest < lifeExp:
                    highest = lifeExp
                    countryHigh = country
                    yearHigh = year

average2 = statistics.mean(choice)
print(f'The overall lowest life expectancy is:{lowest} from {lowestCountry} in {lowestYear}')
print(f'The overall highest life expectancy is:{highest} from {countryHigh} in {yearHigh}')
print()
print(f'The average life expectancy across all countries was {average2}.')
print(f'The highest life expectancy was in {countryHigh} with {lifeExp}')
print(f'The lowest life expectancy was in {lowestCountry} with {lifeExp}')
