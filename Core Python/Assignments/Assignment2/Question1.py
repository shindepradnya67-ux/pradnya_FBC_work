## Convert the time entered in hh , min , and sec into seconds .

## input hours , minutes , and seconds
hours = int (input ('Enter hours : '))
minute = int (input ('Enter minute : '))
seconds = int (input('Enter seconds : '))

## Calculate total seconds

total_seconds = (hours * 3600)+(minute*60)+seconds

print("Total Seconds = ",total_seconds)