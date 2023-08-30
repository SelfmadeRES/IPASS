### In deze test file staat de code nogmaals, maar nu met van te voren aangegeven velden die kunnen worden gekozen door de andere uit te commenten. Ook kan zo iets sneller een extra veld worden toegevoegd om te testen.

field = [[".", "1", ".", ".", ".", "."], ["0", ".", ".", ".", "1", "1"], ["0", "0", ".", ".", "1", "."], [".", ".", "1", ".", ".", "0"], [".", ".", ".", "1", ".", "."], ["1", ".", ".", ".", "0", "0"]]
#field = [[".", ".", ".", ".", "0", "."], ["1", ".", ".", ".", "0", "0"], [".", "0", ".", "1", ".", "."], [".", ".", "0", ".", ".", "."], ["0", ".", ".", ".", ".", "1"], [".", "1", ".", "0", ".", "."]]
#field = [[".", "1", ".", ".", "0", "."], ["0", ".", ".", ".", ".", "1"], ["0", ".", "0", ".", "1", "1"], [".", ".", ".", "0", ".", "."], ["1", ".", "1", ".", ".", "0"], [".", "0", ".", ".", "1", "."]]

### Solving
### Een Binairo kent de volgende regels:
#1. Elke cel moet een nul of een één bevatten.
#2. Er mogen niet meer dan twee dezelfde cijfers direct naast elkaar of direct onder elkaar worden geplaatst.
#3. Elke rij en elke kolom moet evenveel nullen als enen bevatten.
#4. Elke rij is uniek en elke kolom is uniek. Een willekeurige rij mag echter wel hetzelfde ingevuld worden als een willekeurige kolom.
#Regel 1 is vanzelfsprekend en de andere regels worden hieronder in geprogrammeerd. Ook word er een main functie geprogrammeerd die constant door alle regels zal lopen.


# We hebben al een lijst met alle rijen, maar voor het oplossen van de puzzel is een lijst met de kolommen ook handig, dus die maken we hier aan.
def KolomUpdater(field):
    listOfColumns = []
    columnList = []
    for j in range(len(field)):
        for i in range(len(field)):
            columnList.append(field[i][j])
        listOfColumns.append(columnList)
        columnList = []
    return listOfColumns

listOfColumns = KolomUpdater(field)
# Deze functie zal Regel 2 controleren
def Checker2(row):
    for i in range(len(row)):
        if row[i] != ".":
            value = row[i]
            newValue = str(abs(int(row[i])-1))

            #Dubbel cijfer check
            if i != (len(row) -1):
                if row[i+1] == row[i]:
                    if i != 0:  #De volgende regel moet niet gebeuren als het over het eerste teken in de lijst gaat
                        row[i-1] = newValue
                    if i < (len(row) - 2):  #De volgende regel moet niet gebeuren als het over het een na laatste of laatste teken in de lijst gaat.
                        row[i+2] = newValue
        #Poort check 0,.,0
        else:
            if i != 0 and i < (len(row) - 1):   #Het mag niet het eerste of laatste teken van de rij zijn.
                if row[i-1] == row[i + 1] and row[i-1] != ".":
                    row[i] = str(abs(int(row[i-1])-1))
    return(row)

def Rule2Rows(rows):
    for row in rows:
        Checker2(row)

def Rule2Columns(columns):
    for column in columns:
        Checker2(column)

#Nu wordt de lijst met kolommen aangepast en niet het veld zelf. We moeten dus het veld aanpassen op de kolommen
def FieldUpdater(listOfColumns):
    newField = []
    newColumn = []
    for i in range(len(listOfColumns)):
        for j in range(len(listOfColumns)):
            newColumn.append(listOfColumns[j][i])
        newField.append(newColumn)
        newColumn = []
    return newField

# Hier wordt de derde regel toegepast. 
def Checker3(row):
    if (row.count("0") == (len(row)/2)) or (row.count("1") == (len(row)/2)):  
        if row.count("0") == (len(row)/2):
            newchr = "1"
        else: 
            newchr = "0"
        for i in range(len(row)):
            if row[i] == ".":
                row[i] = newchr

def Rule3Rows(rows):
    for row in rows:
        Checker3(row)

def Rule3Columns(columns):
    for column in columns:
        Checker3(column)

#De vierde regel controleerd of alle volle regels aan de laatste eis voldoen
def Checker4(rows, columns):
    rowcount = 0
    columncount = 0
    for row in rows:
        for rijen in rows:
            if row == rijen:
                rowcount += 1
            if rowcount > 1:
                return False
            rowcount = 0
    for column in columns:
        for kolommen in columns:
            if column == kolommen:
                columncount += 1
            if rowcount > 1:
                return False
            rowcount = 0
    return True
            
def RuleCheck():
    spel = field        #Variabelen voor in de functie
    kolommen = listOfColumns
    working = True
    turns = 0
    while working:
        turns += 1

        """for row in spel:
            print(row)
        for kolom in kolommen:
            print(kolom)"""

        Rule2Rows(spel)
        kolommen = KolomUpdater(spel)   #Constant worden zowel de rijen als kolommen veranderd.
        Rule2Columns(kolommen)
        spel = FieldUpdater(kolommen)

        Rule3Rows(spel)
        kolommen = KolomUpdater(spel)
        Rule3Columns(kolommen)
        spel = FieldUpdater(kolommen)


        print("Solving...")
        points = 0
        for row in spel:        #Controle of het speelveld volledig is ingevuld
            points += row.count(".")
        if points == 0:
            working = False
            
    if not Checker4(spel, kolommen):        #Regel 4
        print("Puzzle solved incorrectly")

    print(f"Puzzle Solved!")
    for row in spel:
        print(row)

field = [[".", "1", ".", ".", ".", "."], ["0", ".", ".", ".", "1", "1"], ["0", "0", ".", ".", "1", "."], [".", ".", "1", ".", ".", "0"], [".", ".", ".", "1", ".", "."], ["1", ".", ".", ".", "0", "0"]]
field = [[".", ".", ".", ".", "0", "."], ["1", ".", ".", ".", "0", "0"], [".", "0", ".", "1", ".", "."], [".", ".", "0", ".", ".", "."], ["0", ".", ".", ".", ".", "1"], [".", "1", ".", "0", ".", "."]]
field = [[".", "1", ".", ".", "0", "."], ["0", ".", ".", ".", ".", "1"], ["0", ".", "0", ".", "1", "1"], [".", ".", ".", "0", ".", "."], ["1", ".", "1", ".", ".", "0"], [".", "0", ".", ".", "1", "."]]
RuleCheck()