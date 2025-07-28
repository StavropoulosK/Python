''' Ομαδική εργασία στο μάθημα της Εισαγωγής στους Υπολογιστές των:

        Γκούσκου Μόλι

        Δεστούνης Παναγιώτης

        Δημητρέλλος Νικόλαος

        Διγενής Νικόλαος

        Κατωπόδης Αλέξανδρος

        Λιακάκος Νικόλαος

        Σταυρόπουλος Κωνσταντίνος   '''



''' Group project of

        Γκούσκου Μόλι

        Δεστούνης Παναγιώτης

        Δημητρέλλος Νικόλαος

        Διγενής Νικόλαος

        Κατωπόδης Αλέξανδρος

        Λιακάκος Νικόλαος

        Σταυρόπουλος Κωνσταντίνος   '''







from itertools import chain, combinations
from pymprog import model
import tkinter as tk
import random
from PIL import Image, ImageTk
import webbrowser

class UserTXT():
    ''' User enters manually the number of cities - Ο ΧΡΗΣΤΗΣ ΒΑΖΕΙ ΧΕΙΡΟΚΙΝΗΤΑ ΣΥΝΤΕΤΑΓΜΕΝΕΣ ΓΙΑ citynumber (int) ΠΟΛΕΙΣ'''
    def __init__(self,w,citynumber):
        self.citynumber=citynumber
        self.clean()

        
        self.entries1 = {}     
        self.entries2 = {}
        self.labels=    {}
        self.w=w
        self.w.geometry=("300x500")
        self.w.title('set coordinates')

        self.f1 = tk.Frame(self.w)
        self.f1.pack(side='bottom', fill='x')
       

        self.f2= tk.Frame(self.w,bg="#ded7b1")
        self.f2.pack(side='top', fill='x')
        
                #ΔΗΜΙΟΥΡΓΙΑ ΚΑΤΑΛΛΗΛΟΥ ΑΡΙΘΜΟΥ entries ΚΑΙ labels
                # ΑΡΙΣΤΕΡΑ ΤΑ Χ 
                # ΔΕΞΙΑ ΤΑ Υ


        for i in range(self.citynumber):
            self.labels[i]=tk.Label(self.f2, text="city "+str(i+1) )
            self.labels[i]['bg']="#ded7b1"  
            self.labels[i]['fg']="#cc7351"
            self.labels[i]['font']='Monaco'
            self.labels[i].grid(row=(2*i),columnspan=2)
            self.entries1[i]=tk.Entry(self.f2)
            self.entries1[i].grid(row=(2*i+1),column=0)
            self.entries2[i]=tk.Entry(self.f2)
            self.entries2[i].grid(row=(2*i+1),column=1)

        #buttom ΓΙΑ ΤΕΡΜΑΤΙΣΜΟ 
        self.b0 = tk.Button(self.f1, command=self.doit, text='save coordinates',
                            font='Monaco',bg="#9dab86",fg="#965d62")
        self.b0.pack(fill='x', expand=1)

        
        #COLOR PALETTE           
        ###   https://colorhunt.co/palette/226372


        #ΜΟΛΙΣ ΠΑΤΗΣΕΙΣ ΤΟ buttom ΚΛΕΙΝΕΙ ΤΟ ΠΡΟΓΡΑΜΜΑ ΚΑΙ ΔΗΜΙΟΥΡΓΕΙ ΤΟ ΑΡΧΕΙΟ

    def doit(self):
        self.m=open("cities.txt", "w")
        self.m.write(str(self.citynumber))
        for i in range(int(self.citynumber)):
            x=self.entries1[i].get()
            y=self.entries2[i].get()
            self.m.write('\n' +"{:<15}".format(str(x))+" "+"{:<15}".format(str(y)))
        self.m.close()
        self.w.destroy()
        Main("cities.txt")
    
        #ΚΑΘΑΡΙΖΕΙ ΤΟ ΑΡΧΕΙΟ ΠΟΥ ΘΑ ΓΡΑΨΕΙ 

    def clean(self):
        try:
            f =open("cities.txt", "r+")
            f.truncate(0)
            f.close()
        except:
            pass    

class RandomTXT():
    '''Δημιουργεί αρχείο με τυχαίες συντεταγμένες πόλεων'''
    def __init__(self,citynumber):
        self.citynumber=citynumber
        self.clean()
        self.create()
        


    def clean(self):     #ΚΑΘΑΡΙΖΕΙ ΤΟ ΑΡΧΕΙΟ 

        try:
            f =open("cities.txt", "r+")
            f.truncate(0)
            f.close()
        except:
            pass


    def create(self):    # ΓΡΑΦΕΙ ΤΥΧΑΙΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ
        w=open("cities.txt", "w")
        w.write(str(self.citynumber))
        for i in range(int(self.citynumber)):
            r1=random.randint(100,700)
            r2=random.randint(100,700)
            w.write('\n' +"{:<15}".format(str(r1))+" "+"{:<15}".format(int(r2)))

class City():
    ''' create cities with the coordinates - Δημιουργεί πόλεις με τις συντεταγμένες'''
    i=1 ###class variable

    def __init__(self,x,y):
        self.x=float(x)    
        self.y=float(y)
        self.number=City.i
        City.i +=1    ### ο δείκτης κάθε πόλης (αυξάνεται κάθε φορά που δημιουργείται μια πόλη)

    def distance(self,p):
        distance=((self.x-p.x)**2+(self.y-p.y)**2)**(1/2)
        return distance

    ### Επιβεβαίωση ότι οι συντεταγμένες είναι σε σωστή θέση
    # def __str__(self):
    #     out=str(self.x)+" "+ str(self.y)
    #     return out

class Main():
    ''' Solves the problem with 2 different methods - Επιλύει το πρόβλημα με δύο διαφορετικές προσεγγίσεις.'''

    def __init__(self,filename,citynumber=0): 
        self.filename=filename
        self.citynumber=citynumber

        ### Χρήση της κλάσης RandomTXT
        if self.filename=="random" or self.filename=="RANDOM":  
            
            RandomTXT(self.citynumber)
            self.filename="cities.txt"


            r=open("cities.txt","r")           #    PRINT RANDOM CITIES COORDINATES
            cities=r.readlines()
            for i in range(1,int(cities[0])+1):
                print("city ",i,":",cities[i])
        
        if self.filename=="input":
            
            w=tk.Tk()
            UserTXT(w,self.citynumber)
            w.mainloop()
            self.filename="cities.txt"

            r=open("cities.txt","r")           #    PRINT RANDOM CITIES COORDINATES
            cities=r.readlines()
            for i in range(1,int(cities[0])+1):
                print("city ",i,":",cities[i])


        self.katalogos=[]   ###container των αντικειμένων City για την μέθοδο επίλυσης με την pymprog.
        self.number_of_cities=-1
        self.read_coordinates()
        self.dictionary={}
        self.create_distances()

        self.solve_problem()

        w=tk.Tk()
        self.katalogos2=[] ###  container  των αντικειμένων city για τη μέθοδο όπου επιλέγεται κάθε φορά η πιο κοντινή πόλη.
        self.sintomoteri_diadromi()
        GUI(w,self.katalogos,self.katalogos2)
        w.mainloop()    

    def read_coordinates(self):
        ###Διαβάζει από το αρχείο τον αριθμό των πόλεων και παίρνει τις συντεταγμένες κάθε πόλης

        file=open(self.filename,"r",encoding="utf-8")
        self.number_of_cities=int(file.readline())
        for line in file:
            x,y=line.split()
            self.katalogos.append(City(int(x),int(y)))
        file.close()

    def create_distances(self):
        ### Δημιουργεί ένα λεξικό με κλειδιά τις διαδρομές και τιμές τις αντίστοιχες αποστάσεις Π.χ. (1,3):20 

        for one_city in self.katalogos:  ###για κάθε  πόλη
             for another_city in self.katalogos: ### παίρνει όλες τις άλλες πόλεις
                if one_city != another_city:     ### και υπολογίζει την μεταξύ τους απόσταση 
                    self.dictionary[one_city.number,another_city.number]=round(one_city.distance(another_city))     

    def sorted(self):
        st=[]
        city=1
        while len(st) < len(self.tour):       ##βαζει τις διαδρομες σε σειρα
            for i in range(len(self.tour)):
                if self.tour[i][0]==city:            
                    st.append(self.tour[i])
                    city=self.tour[i][1] 
           
                                      ##st=[(1,5),(5,6),(6,7),... ]             
                                   #παρουσιαση με ωραίο τρόπο(1==>5==>6 κτλ.)
        # print("Η ΣΥΝΤΟΜΟΤΕΡΗ ΔΙΑΔΡΟΜΗ ΕΙΝΑΙ: ")
        print("The shortest path is: ")

        for i in range(len(st)+1):
            if i < len(st):
                print(st[i][0],"===>",end=" ")
                
            else :
                print(st[0][0], end=" ")


        u=[]
        for i in range(len(st)):
            st[i]=st[i][0]          ### Από κάθε πλειάδα του st κρατάει μόνο το πρώτο στοιχείο π.χ  st=[(1,5),(5,6),(6,7)-->st[1,5,6]

        st.append(1)                ### Και προσθέτει την πρώτη πόλη ώστε να είναι κλειστή η διαδρομή π.χ. [1,5,6,1]
        for number_of_city in st:
                for city in self.katalogos:         ###Ψάχνει στο self.katalogos τις πόλεις με αριθμούς 1,5,6 κτλ. και τις βάζει σε σειρά
                        if city.number==number_of_city:    ### στη λίστα u
                                u.append(city)
        
        self.katalogos=u                            ### Το self.katalogos πλέον περιέχει τις πόλεις στη σειρά.
        
    def subtour(self,V):

        ### Συνάρτηση από το python_docs https://docs.python.org/3/library/itertools.html
        '''subtour([1,2,3,4,5]) --> [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5),
           (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5),(2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]'''
       
        s = list(V)
        return chain.from_iterable(combinations(s, r) for r in range(2,len(s)-1))

    def solve_problem(self):
        
        V = range(1,self.number_of_cities+1)  ### Αριθμός των πόλεων
        keys = self.dictionary.keys()
        p = model("tsp")
        x = p.var('x',keys,bool) 

        #Ο σκοπός του προβλήματος- Να ελλατώσει την συνολική απόσταση.
        p.min(sum(self.dictionary[t]*x[t] for t in keys))


        #Οι συνθήκες που πρέπει να πληρούνται στη λύση:
          

        #   1)Να μπει σε κάθε πόλη ακριβώς μία φορά   
        for k in V:
            sum(x[k,j] for j in V if k!=j)==1  ##list comprehensions

        #   2)Να φύγει από κάθε πόλη ακριβώς μία φορά    
        for k in V:
            sum(x[i,k] for i in V if i!=k)==1  

        #   3)Από κάθε συνδυασμό πόλεων που επιστρέφει η subtour να φεύγει τουλάχιστον μία φορά(subtour elimination).
        #   Πιθανοί συνδυασμοί από 2 μέχρι και ν-2 πόλεις

        for subset in self.subtour(V):
            

                                                          ### subset: Ένας συνδυασμός πόλεων    
            l=[x for x in V if x not in subset]           ### Οι πόλεις που δεν ανήκουν στον συνδυασμό
            for i in subset:
                sum(x[i,k] for i in subset for k in l)>=1 ### Από τις πόλεις του συνδυασμού πήγαινει τουλάχιστον σε μία πόλη που 
                                                          ### δεν ανήκει στον συνδυασμό.

        p.solve(float)                                    #solve as Linear Programming

        p.solve(int)                                      #solve the Integer Problem

        # self.tour = [t for t in keys if x[t].primal==1]   # Αν η τιμή που έχουν τα x[t] (π.χ. χ[1,2] ) είναι 1 σημαίνει ότι η διαδρομή 1-->2
        self.tour = []
        for t in keys:
            try:
                val = x[t].primal
                if val == 1:
                    self.tour.append(t)
            except Exception as e:
                print(f"x[{t}] has no primal value. Error: {e}")


        self.sorted()                                     # είναι έγκυρη και προσθέτει στη λίστα tour την πλειάδα (1,2)

        p.end

    def enalaktikos_tropos(self,current_city):
        # Παίρνει ως όρισμα την αρχική πόλη και βρίσκει την πιο σύντομη διαδρομή πηγαίνοντας στην πιο κοντινή πόλη κάθε φορά.

        shortest_distance=10**10  
        route=[current_city]   #Λίστα με την διαδρομή.
        total_distance=0        
        
        for _a in range(1,self.number_of_cities):    ###Για κάθε μία πόλη
            for i in self.dictionary:                ###Διαπερνά τα κλειδιά  (π.χ. i=(1,3))
            
                if i[0]==current_city and self.dictionary[i]<shortest_distance and i[1] not in route:  ### Βρίσκει την πιο κοντινή πόλη που δεν έχει ξαναπεράσει. 
                    shortest_distance=self.dictionary[i]
                    shortest_city=i[1]

            
            route.append(shortest_city) #Βάζει την πιο κοντινη πολη στην διαδρομη και την θέτει  ως αρχικη πολη για την συνεχιση της επανάληψης
            current_city=shortest_city
            total_distance += shortest_distance
            shortest_distance=10**10 

        route.append(route[0])   ### Προσθέτει την πόλη από την οποία ξεκίνησε
        total_distance += self.dictionary[(route[0],route[-2])]
       

        return route,total_distance

    def sintomoteri_diadromi(self):
        ### Συγκρίνει για κάθε πόλη την απόσταση με τον εναλακτικό τρόπο και επιστρέφει την πιο σύντομη διαδρομή.
        test_distance=10**10
        fastest_way=[]


        for i in range(1,self.number_of_cities+1):
        
            diadromi,total_distance=self.enalaktikos_tropos(i)
            if  total_distance< test_distance:    
                test_distance=total_distance
                fastest_way=diadromi
        
       
       

        for number_of_city in fastest_way:
            for city in self.katalogos[:-1]: ###  Αρχικά ο κατάλογος περιέχει τις πόλεις από μία φορά  αλλά  με τη πρώτη λύση του προβλήματος καλείται η sorted 
                                                   ###  και προστίθεται στο τέλος του καταλόγου η πρώτη πόλη οπότε υπάρχει δύο φορές.
                    if city.number==number_of_city:
                            self.katalogos2.append(city)

class GUI():
    ''' Display graphically the routes - Απεικονίζει γραφικά τις διαδρομές.'''

    def __init__(self,root,katalogos,katalogos2):
        self.root=root
        self.root.title("Travelling salesman")
        self.root.geometry("800x850")
        self.root.resizable(height="False",width="False")
        self.create_canvas()
        self.katalogos=katalogos                ### Όταν καλείται η GUI λαμβάνει δύο λίστες που περιέχουν τα αντικείμενα City ταξηνομημένα
        self.katalogos2=katalogos2              ### σύμφωνα με τον κάθε τρόπο επίλυσης: self.katalogos-->pymprog
        self.draw_city()                        ###                                     self.katalogos2-->enalaktiki lisi
        self.canvas.bind("<Button-1>",self.draw_map)
        self.root.attributes('-topmost', True)
        self.root.update()
        self.canvas.bind("<Button-3>",self.draw_second_map)
        


    def create_canvas(self):
        # Δημιουργία Canva και φόρτωμα εικόνας

        self.canvas=tk.Canvas(self.root)
        self.canvas.pack(fill="both",expand=1)
        try:   ### Αν δεν υπάρχει η εικόνα συνεχίζει το πρόγραμμα.
            # self.image=ImageTk.PhotoImage(Image.open("Background image.png"))  
            self.image=ImageTk.PhotoImage(Image.open("Background image.jpg"))  

            self.canvas.create_image(0,0,image=self.image,anchor="nw")  ## ως  σημείο 0,0 ορίζεται πάνω αριστερά (North West)
        except:
            pass
              
    def draw_city(self):
        ### Απεικόνιση πόλεων με κύκλους

        for city in self.katalogos:
            self.canvas.create_oval(city.x -12, city.y - 12 ,city.x + 12, city.y + 12, width=1,fill="darkorange4",outline="darkorange4")
            self.canvas.create_oval(city.x -6 ,city.y - 6 ,city.x + 6, city.y + 6, width=1,fill="#5aa469",outline="#5aa469")


    def draw_map(self,event):
        ### Ενώνει μεταξύ τους τις πόλεις, εμφανίζει τις αποστάσεις μεταξύ δύο πόλεων και την συνολική απόσταση.
        ### Η GUI Λειτουργεί Μόνο με το self.katalogos, το άλλο απλά το θυμάται  για να δημιουργήσει αντικείμενο 
        ### του εαυτού της στο draw_second_map

        total_distance=-1
        
        city1=self.katalogos[0]
        for city in self.katalogos[1:]:
            
            self.canvas.create_line(city1.x , city1.y , city.x , city.y , fill="red4", width=3)
            distance=int(city1.distance(city))
            total_distance += distance
            self.text=self.canvas.create_text((city1.x + city.x )/2 +25 ,(city1.y + city.y)/2 , text=str(distance),\
                    fill="azure",font="Purisa 20")
            city1=city
            coordinates=str(int(city.x))+" "+str(int(city.y))
            self.text=self.canvas.create_text(city.x -25 , city.y-35 , text=coordinates,\
                    fill="black",font="Purisa 14")
        self.text=self.canvas.create_text(250,40,text="Total distance is:"+" "+str(total_distance),fill="black",font="Purisa 21")
            
    def draw_second_map(self,event):
        ### Δημιουργία του δεύτερου παραθύρου 


        w2=tk.Toplevel()
        sec_window=GUI(w2,self.katalogos2,self.katalogos2)  ### Η κλάση Gui δημιουργεί αντικείμενο του εαυτού της όπου πλέον το self.katalogos2
                                                            ### γίνεται  self.katalogos  και το δεύτερο self.katalogos2  περισεύει και δίνεται μόνο 
                                                            ### γιατί η GUI παίρνει 3 γνωρίσματα.
        sec_window.canvas.unbind("<Button-3>")  ### Σταματάει να ανοίγουν νέα παράθυρα με δεξί click.
        w2.mainloop()           

class Menu(): 
    ''' Graphical interface - ΓΡΑΦΙΚΑ ΜΕΝΟΥ'''                    
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x220')
        self.root.resizable(False, False)
        self.root.title('TSP')
        self.press=0
        try: 
            root.iconbitmap("tsp.ico")
        except: pass

        self.f1 = tk.Frame(self.root)
        self.f1.pack(side='top', fill='x')

        self.b0 = tk.Button(self.f1, command=self.show_info, text='( i )',fg="#aa8976",bg="#c6ebc9",
                            font='Arial 20')
        self.b0.pack(side='left', fil='x', expand=1)

        self.b2 = tk.Button(self.f1, command=self.input,fg="#aa8976",bg="#c6ebc9",
                            text=' input type ', font='Arial 20')
        self.b2.pack(side='left', fill='x', expand=1)

        self.b1 = tk.Button(self.f1, command=self.run, text=' run ',fg="#aa8976",bg="#c6ebc9",
                                         font='Arial 20')
        self.b1.pack(side='left', fill='x', expand=1)

        self.f3 = tk.Frame(self.root,bg="#f0e2d0")
        self.f3.pack(side='bottom', fill='x')
        
    def show_info(self):         #WIKIPEDIA
        webbrowser.open("https://en.wikipedia.org/wiki/Travelling_salesman_problem")


    def input(self):   #ΕΜΦΑΝΗΣΗ INPUT TYPE ΥΠΟ-ΜΕΝΟΥ
        
        if self.press==0:
            self.press=1
            self.r1=tk.Button(self.f3,command=self.r, text='  random  ',bg="#70af85",fg="#f0e2d0",
                                         font='Arial 20')
            self.r1.grid(row = 0, column = 0)
            
            
            self.r2=tk.Button(self.f3,command=self.it, text=' inputTXT ',bg="#70af85",fg="#f0e2d0",
                                         font='Arial 20')
            self.r2.grid(row = 1, column = 0   )

            self.r3=tk.Button(self.f3,command=self.d , text='    user     ',bg="#70af85",fg="#f0e2d0",
                                         font='Arial 20')
            self.r3.grid(row = 2, column = 0)
                


    def r(self):
        try:
            self.l1.destroy()
            self.e1.destroy()
        except:pass
        self.l1=tk.Label(self.f3, text="city number :", font='Arial 20',bg='#f0e2d0')
        self.l1.grid(row = 0, column = 1)    
        self.e1=tk.Entry(self.f3,font='Arial 20' )
        self.e1.grid(row = 0, column = 2)
        try:
            self.l2.destroy()
            self.e2.destroy()
        except:pass
        try:
            self.l3.destroy()
            self.e3.destroy()
        except:pass

    def d(self):
        try:
            self.l3.destroy()
            self.e3.destroy()
        except:pass
        self.l3=tk.Label(self.f3, text="city number :", font='Arial 20',bg='#f0e2d0')
        self.l3.grid(row = 2, column = 1)    
        self.e3=tk.Entry(self.f3,font='Arial 20' )
        self.e3.grid(row = 2, column = 2)
        try:
            self.l2.destroy()
            self.e2.destroy()
        except:pass
        try:
            self.l1.destroy()
            self.e1.destroy()
        except:pass


    
    def it(self):
        try:
            self.l2.destroy()
            self.e2.destroy()
        except:pass
        self.l2=tk.Label(self.f3, text="file name :", font='Arial 20',bg='#f0e2d0')
        self.l2.grid(row = 1, column = 1)    
        self.e2=tk.Entry(self.f3,font='Arial 20' )
        self.e2.grid(row = 1, column = 2)
        try:
            self.l1.destroy()
            self.e1.destroy()
        except:pass
        try:
            self.l3.destroy()
            self.e3.destroy()
        except:pass


    def run(self):   #ΤΡΕΧΕΙ ΤΟ ΠΡΟΓΡΑΜΜΑ
        
        try:
            k=self.e1.get()
            self.l1.destroy()
            self.e1.destroy()
            self.root.destroy()
            Main("random", int(k))
            
        except:pass
            #print("not integer")
      

        try:
            k=self.e3.get()
            self.l3.destroy()
            self.e3.destroy()
            self.root.destroy()
            Main("input",int(k))
            
        except:pass
            #print("not integer")
        

        try:
            k=self.e2.get()
            self.l2.destroy()
            self.e2.destroy()
            self.root.destroy()
            if str(k).endswith(".txt"):
                Main(k)
            else:
                k=str(k)+".txt"
                Main(k)
            
        except:pass
            #print("file not found")

        



        


if __name__ == "__main__":


    root=tk.Tk()
    Menu(root)
    root.mainloop()


