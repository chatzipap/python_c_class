# Επίλυση Δραστηριοτήτων του μαθήματος Προγραμματισμός Υπολογιστών
# Γ' ΕΠΑΛ
# ΤΟΜΕΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ
# worked with Python 2.7.10
# @ Tasos Chatzipapadopoulos

'''

ΚΕΦΑΛΑΙΟ 8ο ΔΟΜΕΣ ΔΕΔΟΜΕΝΩΝ ΙΙ
Δραστηριότητα 2 /σελίδα 151
Να γράψετε ένα πρόγραμμα το οποίο θα διαβάζει μία λέξη και θα εμφανίζει πόσα
κεφαλαία αγγλικά γράμματα περιέχει η λέξη.

'''

# Κλήση βιβλιοθήκης string για πρόσβαση σε συμβολοσειρές αλφάβητων
import string
englishCaps = string.ascii_uppercase

# Αντί διάβασμα λέξης χρησιμοποιούμε το παρακάτω κείμενο για εύρεση κεφαλαίων λατινικών χαρακτήρων
myText = '''
Python is a widely used high-level, general-purpose, Interpreted, dynamic programming Language.[24][25] 
Its design philosophy emphasizes code readability, and its SYNTAX allows programmers to Express concepts 
in Fewer LINES of code than POSSIBLE in Languages such as C++ or Java.[26][27] The language provides constructs 
INTENDED to enable WRITING clear programs on both a small and large SCALE.[28]
Η Python είναι μια υψηλού επιπέδου γλώσσα προγραμματισμού[1][2] η οποία δημιουργήθηκε από τον Ολλανδό 
Γκβίντο βαν Ρόσσουμ (Guido van Rossum) το 1990. Ο κύριος στόχος της είναι η αναγνωσιμότητα του κώδικά της 
και η ευκολία ΧΡΗΣΗΣ της και το συντακτικό της επιτρέπει στους Προγραμματιστές να εκφράσουν έννοιες σε λιγότερες 
γραμμές κώδικα απ'ότι θα ήταν δυνατόν σε Γλώσσες όπως η C++ ή η Java.[3][4] Διακρίνεται λόγω του ότι έχει πολλές 
βιβλιοθήκες που διευκολύνουν ΙΔΙΑΙΤΕΡΑ αρκετές συνηθισμένες εργασίες και για την ταχύτητα εκμάθησης της.
'''

# Εύρεση κεφαλαίων Με τη χρήση του τελεστή in & με διάσχιση
countCaps = 0

for letter in myText:
    if letter in englishCaps :
        countCaps += 1
		
print 'Found %d English Capital letters' % countCaps


# Εύρεση κεφαλαίων Χωρίς τον τελεστή in & με slicing
countCaps = 0

for i in range(len(myText)):
    for j in range(len(englishCaps)):
        if myText[i] == englishCaps[j] :
            countCaps += 1
			
print 'Found %d English Capital letters' % countCaps
