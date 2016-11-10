# Επίλυση Δραστηριοτήτων του μαθήματος Προγραμματισμός Υπολογιστών
# Γ' ΕΠΑΛ
# ΤΟΜΕΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ
# worked with Python 2.7.10
# @ Tasos Chatzipapadopoulos

'''

ΚΕΦΑΛΑΙΟ 8ο ΔΟΜΕΣ ΔΕΔΟΜΕΝΩΝ ΙΙ
Δραστηριότητα 4 /σελίδα 151
Να γράψετε μια συνάρτηση isSubstring(string, substring) η οποία θα ελέγχει, αν η
συμβολοσειρά substring περιέχεται στην συμβολοσειρά string και αν ναι, θα επι-
στρέφει True. Στη συνέχεια να χρησιμοποιήσετε αυτή τη συνάρτηση, για να βρείτε
πόσες φορές εμφανίζεται μια συμβολοσειρά μέσα σε μια άλλη.

'''

# Η λύση εδώ παρουσιάζεται με μία αλλαγή καθότι η 1η συνάρτηση δεν έχει ιδιαίτερο
# νόημα εφόσον ο τελεστης in (substring in string) δίνει τη λύση
# έτσι υλοποιούμε μία  συνάρτηση η οποία βρίσκει όχι μόνο πόσες φορές
# αλλά και σε ποιες θέσεις εμφανίζεται η substring μέσα στην string
# χρησιμοποιώντας την τεχνική slicing

# Δεδομένα δοκιμής
myText = 'hellotherethisisascriptinpythonlanghellotherethisisascriptinpythonlang'

# Αλγοριθμικός τρόπος
def isSubstring(substring, string):
    n = len(substring)
    N = len(string)
    found = False
    start = 0
    end = n
    position = []   # λίστα θέσεων εμφάνισης της substring
    while end <= N :
        part = string[start:end] # τεμαχιζουμε την string σε φέτες μεγέθους n
        if substring == part :
            position.append(start)
        start, end = start + 1, end + 1
    print
    print 'Η υπο-συμβολοσειρά "%s" βρέθηκε στη συμβολοσειρά "%s" ακριβώς %d φορές στις \
θέσεις %s' % (substring, string, len(position), position)
    # return position

# Pythonic Way μόνο για το πλήθος όχι για τις θέσεις
def isSubstring2(substring, string):
    return string.count(substring)

 # Δοκιμαστική κλήση συνάρτησης
isSubstring('hello', myText) 

