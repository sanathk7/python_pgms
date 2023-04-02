#SELECTING ONLY WORDS WHICH CONTAINS ALPABET B...


L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings=[]
for group in L:
    for word in group:
        for i in word:
            if 'b'==i:
                b_strings.append(word)
                BREAK;
print(b_strings)

#ANOTHER METHOD :

L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings=[]
for group in L:
    for word in group: 
            if 'b' in word:
                b_strings.append(word)
                
print(b_strings)
