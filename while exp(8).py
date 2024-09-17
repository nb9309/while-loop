word = input('enter value:')

index = 0
while index < len(word):
    print(word[index])
    index+=1
print('len of word = ',len(word))
print('-'*50)

# +ve index , reverse order

index = len(word)-1
while index >= 0:
    print(word[index])
    index-=1
print('len of word = ',len(word))
print('-'*50)

# -ve index forword direction

index = -(len(word))
while index<= -1:
    print(word[index])
    index+=1
else:
    print('len of word = ', len(word))
    print('-' * 50)

# -ve indexing backword direction

index = -1
while index>=-(len(word)):
    print(word[index])
    index-=1
else:
    print('len of word = ', len(word))
    print('-' * 50)