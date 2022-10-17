PLACEHOLDER="[name]"

with open("./Input/Names/invited") as data:
    names=data.readlines()
    print (names)
with open("./Input/Letters/starting") as letters:
    letter = letters.read()

for i in names:
    i = i.strip()
    with open(f"./Output/ReadyToSend/{i}",mode='w') as files:

        files.write(letter.replace(PLACEHOLDER,i))






