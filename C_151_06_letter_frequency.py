# Επίλυση Δραστηριοτήτων του μαθήματος Προγραμματισμός Υπολογιστών
# Γ' ΕΠΑΛ
# ΤΟΜΕΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ
# worked with Python 2.7.10
# @ Tasos Chatzipapadopoulos

'''

ΚΕΦΑΛΑΙΟ 8ο ΔΟΜΕΣ ΔΕΔΟΜΕΝΩΝ ΙΙ
Δραστηριότητα 6 /σελίδα 151
Να γράψετε πρόγραμμα στη γλώσσα Python το οποίο θα δέχεται ως είσοδο ένα
κείμενο και θα εμφανίζει πόσες φορές εμφανίζεται κάθε γράμμα του αγγλικού αλφα-
βήτου σε αυτό. Να χρησιμοποιήσετε ένα λεξικό.

'''

# Δεδομένα Δοκιμών ... κείμενο εισόδου
myText ='''
 Alice was beginning to get very tired of sitting by her sister
on the bank, and of having nothing to do:  once or twice she had
peeped into the book her sister was reading, but it had no
pictures or conversations in it, `and what is the use of a book,'
thought Alice `without pictures or conversation?'
  So she was considering in her own mind (as well as she could,
for the hot day made her feel very sleepy and stupid), whether
the pleasure of making a daisy-chain would be worth the trouble
of getting up and picking the daisies, when suddenly a White
Rabbit with pink eyes ran close by her.
  There was nothing so VERY remarkable in that; nor did Alice
think it so VERY much out of the way to hear the Rabbit say to
itself, `Oh dear!  Oh dear!  I shall be late!'  (when she thought
it over afterwards, it occurred to her that she ought to have
wondered at this, but at the time it all seemed quite natural);
but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-
POCKET, and looked at it, and then hurried on, Alice started to
her feet, for it flashed across her mind that she had never
before seen a rabbit with either a waistcoat-pocket, or a watch to
take out of it, and burning with curiosity, she ran across the
field after it, and fortunately was just in time to see it pop
down a large rabbit-hole under the hedge.
'''

# Εισαγωγή βιβλιοθήκης για αλφάβητο λατινικών χαρακτήρων
import string
letters = string.ascii_lowercase

# Επίλυση Με χρήση λεξικού
dic = {}
for letter in letters:
    dic[letter] = 0

for char in myText:
    if dic.get(char.lower()) != None :
        dic[char.lower()] += 1

# Εκτύπωση λεξικού συχνότητας εμφάνισης χαρακτήρων
print dic

# Επίλυση και εκτύπωση συχνοτήτων χωρίς χρήση λεξικού
for letter in letters :
    f = 0  # Συχνότητα εμφάνισης γράμματος
    for char in myText :
        if letter == char.lower():
            f += 1
    print letter, f


