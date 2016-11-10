# Επίλυση Δραστηριοτήτων του μαθήματος Προγραμματισμός Υπολογιστών
# Γ' ΕΠΑΛ
# ΤΟΜΕΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ
# worked with Python 2.7.10
# @ Tasos Chatzipapadopoulos

'''

ΚΕΦΑΛΑΙΟ 11ο ΑΝΤΙΚΕΙΜΕΝΟΣΤΡΕΦΗΣ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ
Δραστηριότητα 1 /σελίδα 221
Να ορίσετε κλάση με όνομα Akeraios, η οποία θα έχει την ιδιότητα timi και τις πα-
ρακάτω μεθόδους:
I. Anathese_timi(timi), η οποία θα αναθέτει τιμή στην ιδιότητα του αντικειμένου.
II. Emfanise_timi(), η οποία θα εμφανίζει την τιμή της ιδιότητας του αντικειμένου.
Στη συνέχεια να δημιουργήσετε στιγμιότυπο της κλάσης Akeraios με όνομα Artios
και να χρησιμοποιήσετε τις παραπάνω μεθόδους για να δώσετε την τιμή 14 στην
ιδιότητα του αντικειμένου και να την εμφανίσετε.

'''

# Δημιουργία Κλάσης ακέραιος
class Akeraios:
    def __init__(self,timi):
        self.timi = timi
    def Anathese_timi(self, timi):
        self.timi = timi
    def Emfanise_timi(self):
        print self.timi
    # Επέκταση της κλάσης ώστε να ελέγχει εάν το αντικείμενο είναι περιττός...
    def isOdd(self):
        if self.timi % 2 == 1 :
            return True
        else :
            return False
    # ... ή Άρτιος ακέραιος
    def isEven(self):
        if self.timi % 2 == 0 :
            return True
        else :
            return False


# Δοκιμαστικές κλήσεις της κλάσης
artios = Akeraios(0)
artios.Emfanise_timi()
artios.Anathese_timi(14)
artios.Emfanise_timi()
x,y = artios.isEven(), artios.isOdd()
print x,y
