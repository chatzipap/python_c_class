# Επίλυση Δραστηριοτήτων του μαθήματος Προγραμματισμός Υπολογιστών
# Γ' ΕΠΑΛ
# ΤΟΜΕΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ
# worked with Python 2.7.10
# @TasosChatz

'''

ΚΕΦΑΛΑΙΟ 8ο ΔΟΜΕΣ ΔΕΔΟΜΕΝΩΝ ΙΙ
Δραστηριότητα 7 /σελίδα 151
Να γράψετε μια συνάρτηση σε Python η οποία θα δέχεται μια λίστα από λέξεις και
θα επιστρέφει τη λέξη με το μεγαλύτερο μήκος.

'''

# Δεδομένα Δοκιμών ... κείμενο εισόδου
myText = ''' Either the well was very deep or she fell very slowly for she
had plenty of time as she went down to look about her and to
wonder what was going to happen next  First she tried to look
down and make out what she was coming to but it was too dark to
see anything then she looked at the sides of the well and
noticed that they were filled with cupboards and bookshelves
here and there she saw maps and pictures hung upon pegs  She
took down a jar from one of the shelves as she passed it was
labelled ORANGE MARMALADE but to her great disappointment it
was empty she did not like to drop the jar for fear of killing
somebody so managed to put it into one of the cupboards as she
fell past it'''

# Δημιουργία λίστας λέξεων από κείμενο με τη μέθοδο split
# για να αποφύγουμε κοπιαστικό data entry
words = myText.split()

# Εύρεση λέξης μεγαλύτερου μήκους
xmax = 0
xword = ''
for word in words :
    if len(word) > xmax :
        xmax = len(word)
        xword = word

print 'Η λέξη "%s" είναι η μεγαλύτερη με %d γράμματα' % (xword, xmax)

        
