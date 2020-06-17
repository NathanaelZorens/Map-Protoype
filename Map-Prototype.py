from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.title("Map-Prototype")

#THis is a part of the GUI Stuff...  
CrDes_fr=LabelFrame(root,padx=40,pady=40,text="Location")
CrDes_fr.grid(row=0,column=0)

Map_fr=LabelFrame(root,padx=40,pady=40,text="Map")
Map_fr.grid(row=0,column=1)

Lbl1=Label(CrDes_fr,text="Silahkan Masukkan Lokasi").grid(row=0,column=0) 
Lbl2=Label(Map_fr,text="Peta Kampus Tembalang").pack()

Map_img=Image.open("Map-00.png")
Rz=Map_img.resize((650,400), Image.ANTIALIAS)

Canvas1=Canvas(Map_fr,width=650,height=400,bg="orange")
Canvas1.pack()
MapRz_img=ImageTk.PhotoImage(Rz)
Canvas1.create_image(0, 0 , anchor=NW, image=MapRz_img)



#Graph... All of the vetexes/nodes
global graph

graph = {
    'n1':{'n10':4,'n7':9,'n2':5},
    'n2':{'n5':1,'n1':5,'n3':5},
    'n3':{'n23':5,'n2':5},
    'n4':{'n5':1,'n22':3},
    'n5':{'n4':1,'n14':2,'n6':2,'n2':1},
    'n6':{'n5':2,'n12':2},
    'n7':{'n8':2,'n1':9},
    'n8':{'n7':2},
    'n9':{'n18':3,'n10':2},
    'n10':{'n15':1,'n11':2,'n9':2,'n1':4},
    'n11':{'n12':2,'n10':2,'n26':4},
    'n12':{'n13':1,'n11':2,'n6':2},
    'n13':{'n14':1,'n12':1},
    'n14':{'n5':2,'n20':1,'n13':1},
    'n15':{'n19':2,'n10':1},
    'n16':{'n51':7,'n17':1},
    'n17':{'n18':1,'n16':1},
    'n18':{'n32':2,'n9':3},
    'n19':{'n15':2,'n31':3},
    'n20':{'n14':1,'n21':1,'n25':1},
    
    'n21':{'n22':1,'n24':1,'n28':2,'n20':1},
    'n22':{'n21':1,'n4':3},
    'n23':{'n3':5,'n42':6,'n24':1},
    'n24':{'n23':1,'n21':1},
    'n25':{'n27':1,'n20':1},
    'n26':{'n27':1,'n11':4},
    'n27':{'n25':1,'n26':1,'n28':2,'n29':1},
    'n28':{'n41':3,'n21':2,'n27':2},
    'n29':{'n27':1,'n40':2},
    'n30':{'n38':1,'n31':1,'n39':1},
    'n31':{'n30':1,'n38':1,'n19':3},
    'n32':{'n36':1,'n33':1,'n18':2},
    'n33':{'n34':1,'n32':1},
    'n34':{'n35':2,'n33':1},
    'n35':{'n34':2,'n50':2},
    'n36':{'n32':1,'n48':2},
    'n37':{'n45':2,'n38':1},
    'n38':{'n37':1,'n39':1,'n30':1,'n31':1},
    'n39':{'n40':1,'n38':1,'n30':1},
    'n40':{'n41':2,'n29':2,'n39':1},
    
    'n41':{'n40':2,'n43':2,'n42':2,'n28':3},
    'n42':{'n41':2,'n23':6},
    'n43':{'n44':2,'n41':2},
    'n44':{'n55':4,'n46':2,'n43':2},
    'n45':{'n46':1,'n37':2},
    'n46':{'n45':1,'n47':2,'n44':2},
    'n47':{'n48':2,'n46':2},
    'n48':{'n47':2,'n53':3,'n49':1,'n36':2},
    'n49':{'n48':1,'n50':1},
    'n50':{'n35':2,'n49':1},
    'n51':{'n16':7,'n52':2},
    'n52':{'n51':2,'n54':2,'n53':2},
    'n53':{'n52':2,'n54':1},
    'n54':{'n55':2,'n52':2,'n53':1},
    'n55':{'n54':2,'n44':4}
    }
#An array to contain the coordinates and a function to Draw the line(s)
global coor
coor = []
def MkLn():
    def no1():
     coor.append(361)
     coor.append(366)
    def no2():
     coor.append(219)
     coor.append(328)
    def no3():
     coor.append(99)
     coor.append(295)
    def no4():
     coor.append(196)
     coor.append(292)
    def no5():
     coor.append(223)
     coor.append(314)
    def no6():
     coor.append(291)
     coor.append(328)
    def no7():
     coor.append(547)
     coor.append(310)
    def no8():
     coor.append(594)
     coor.append(295)
    def no9():
     coor.append(418)
     coor.append(287)
    def no10():
     coor.append(378)
     coor.append(281)
    def no11():
     coor.append(335)
     coor.append(275)
    def no12():
     coor.append(291)
     coor.append(268)
    def no13():
     coor.append(270)
     coor.append(265)
    def no14():
     coor.append(237)
     coor.append(260)
    def no15():
     coor.append(378)
     coor.append(267)
    def no16():
     coor.append(493)
     coor.append(242)
    def no17():
     coor.append(467)
     coor.append(230)
    def no18():
     coor.append(443)
     coor.append(218)
    def no19():
     coor.append(386)
     coor.append(230)
    def no20():
     coor.append(247)
     coor.append(225)
    def no21():
     coor.append(229)
     coor.append(216)
    def no22():
     coor.append(191)
     coor.append(221)
    def no23():
     coor.append(153)
     coor.append(184)
    def no24():
     coor.append(192)
     coor.append(201)
    def no25():
     coor.append(264)
     coor.append(207)
    def no26():
     coor.append(302)
     coor.append(197)
    def no27():
     coor.append(281)
     coor.append(190)
    def no28():
     coor.append(240)
     coor.append(176)
    def no29():
     coor.append(288)
     coor.append(165)
    def no30():
     coor.append(322)
     coor.append(168)
    def no31():
     coor.append(345)
     coor.append(176)
    def no32():
     coor.append(461)
     coor.append(168)
    def no33():
     coor.append(485)
     coor.append(175)
    def no34():
     coor.append(507)
     coor.append(181)
    def no35():
     coor.append(534)
     coor.append(149)
    def no36():
     coor.append(468)
     coor.append(147)
    def no37():
     coor.append(383)
     coor.append(148)
    def no38():
     coor.append(353)
     coor.append(144)
    def no39():
     coor.append(313)
     coor.append(142)
    def no40():
     coor.append(299)
     coor.append(131)
    def no41():
     coor.append(264)
     coor.append(102)
    def no42():
     coor.append(213)
     coor.append(61)
    def no43():
     coor.append(313)
     coor.append(61)
    def no44():
     coor.append(357)
     coor.append(72)
    def no45():
     coor.append(396)
     coor.append(113)
    def no46():
     coor.append(407)
     coor.append(85)
    def no47():
     coor.append(444)
     coor.append(94)
    def no48():
     coor.append(483)
     coor.append(105)
    def no49():
     coor.append(500)
     coor.append(115)
    def no50():
     coor.append(524)
     coor.append(120)
    def no51():
     coor.append(596)
     coor.append(109)
    def no52():
     coor.append(552)
     coor.append(81)
    def no53():
     coor.append(504)
     coor.append(71)
    def no54():
     coor.append(513)
     coor.append(58)
    def no55():
     coor.append(462)
     coor.append(28)
     
    coordinates = {
     'n1':no1,'n2':no2,'n3':no3,'n4':no4,'n5':no5,
     'n6':no6,'n7':no7,'n8':no8,'n9':no9,'n10':no10,
     'n11':no11,'n12':no12,'n13':no13,'n14':no14,'n15':no15,
     'n16':no16,'n17':no17,'n18':no18,'n19':no19,'n20':no20,
     'n21':no21,'n22':no22,'n23':no23,'n24':no24,'n25':no25,
     'n26':no26,'n27':no27,'n28':no28,'n29':no29,'n30':no30,
     'n31':no31,'n32':no32,'n33':no33,'n34':no34,'n35':no35,
     'n36':no36,'n37':no37,'n38':no38,'n39':no39,'n40':no40,
     'n41':no41,'n42':no42,'n43':no43,'n44':no44,'n45':no45,
     'n46':no46,'n47':no47,'n48':no48,'n49':no49,'n50':no50,
     'n51':no51,'n52':no52,'n53':no53,'n54':no54,'n55':no55
     }
    ag=0
    sm=0
    l=0
    for ag in range(len(path)):
     l=sm+ag      
     coordinates[path[l]]()
    ag+=1 
    Canvas1.create_line(*coor, fill="red",width=2)
#========================================================================
#This is where the Algorithm is. We use it as a function
path = []
def dijkstra(graph,start,goal):
    graph = {
        'n1':{'n10':4,'n7':9,'n2':5},
        'n2':{'n5':1,'n1':5,'n3':5},
        'n3':{'n23':5,'n2':5},
        'n4':{'n5':1,'n22':3},
        'n5':{'n4':1,'n14':2,'n6':2,'n2':1},
        'n6':{'n5':2,'n12':2},
        'n7':{'n8':2,'n1':9},
        'n8':{'n7':2},
        'n9':{'n18':3,'n10':2},
        'n10':{'n15':1,'n11':2,'n9':2,'n1':4},
        'n11':{'n12':2,'n10':2,'n26':4},
        'n12':{'n13':1,'n11':2,'n6':2},
        'n13':{'n14':1,'n12':1},
        'n14':{'n5':2,'n20':1,'n13':1},
        'n15':{'n19':2,'n10':1},
        'n16':{'n51':7,'n17':1},
        'n17':{'n18':1,'n16':1},
        'n18':{'n32':2,'n9':3},
        'n19':{'n15':2,'n31':3},
        'n20':{'n14':1,'n21':1,'n25':1},
        'n21':{'n22':1,'n24':1,'n28':2,'n20':1},
        'n22':{'n21':1,'n4':3},
        'n23':{'n3':5,'n42':6,'n24':1},
        'n24':{'n23':1,'n21':1},
        'n25':{'n27':1,'n20':1},
        'n26':{'n27':1,'n11':4},
        'n27':{'n25':1,'n26':1,'n28':2,'n29':1},
        'n28':{'n41':3,'n21':2,'n27':2},
        'n29':{'n27':1,'n40':2},
        'n30':{'n38':1,'n31':1,'n39':1},
        'n31':{'n30':1,'n38':1,'n19':3},
        'n32':{'n36':1,'n33':1,'n18':2},
        'n33':{'n34':1,'n32':1},
        'n34':{'n35':2,'n33':1},
        'n35':{'n34':2,'n50':2},
        'n36':{'n32':1,'n48':2},
        'n37':{'n45':2,'n38':1},
        'n38':{'n37':1,'n39':1,'n30':1,'n31':1},
        'n39':{'n40':1,'n38':1,'n30':1},
        'n40':{'n41':2,'n29':2,'n39':1},
        'n41':{'n40':2,'n43':2,'n42':2,'n28':3},
        'n42':{'n41':2,'n23':6},
        'n43':{'n44':2,'n41':2},
        'n44':{'n55':4,'n46':2,'n43':2},
        'n45':{'n46':1,'n37':2},
        'n46':{'n45':1,'n47':2,'n44':2},
        'n47':{'n48':2,'n46':2},
        'n48':{'n47':2,'n53':3,'n49':1,'n36':2},
        'n49':{'n48':1,'n50':1},
        'n50':{'n35':2,'n49':1},
        'n51':{'n16':7,'n52':2},
        'n52':{'n51':2,'n54':2,'n53':2},
        'n53':{'n52':2,'n54':1},
        'n54':{'n55':2,'n52':2,'n53':1},
        'n55':{'n54':2,'n44':4}
        }
    unseenNodes = graph
    shortest_distance = {}
    predecessor = {}
    infinity=9999999    
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
 
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
 
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
 
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            print(start)
            print(path)
            print(shortest_distance)
            print(goal)
            print(shortest_distance[goal])
            print(unseenNodes)
            print(graph)
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))
        print(start)
        print(path)
        print(shortest_distance)
        print(goal)
        print(shortest_distance[goal])
        print(unseenNodes)
        print(graph)
#===========================================================================
#This is... uuuh... Idk.. where the main function i guess?
nw=StringVar()
des=StringVar()
Places=['1.Widya Puraya','2.Gedung Serbaguna','3.ICT Center','4.Lab Terpadu','5.Stadion','6.Waduk Pendidikan','7.Sekolah Vokasi','8.Fakultas Hukum',
        '9.Fakultas Ilmu Budaya','10.Fakultas Ilmu Sosial','11.Fakultas Teknik','12. Fakultas Peternakan dan Pertanian','13.Fakultas Perikanan dan Ilmu Kelautan',
        '14.Fakultas Psikologi','15.Fakultas Kedokteran','16.Fakultas Kesehatan Masyarakat','17.Fakultas Ekonomika dan Bisnis','18.Fakultas Sains dan Matematika','19.Gedung Prof. Soedarto']     
Now=OptionMenu(CrDes_fr, nw, *Places).grid(row=1,column=0,columnspan=2)
Dest=OptionMenu(CrDes_fr, des,*Places).grid(row=2,column=0,columnspan=2)        
nw.set("Pilih Lokasi anda")
des.set("Pilih Tujuan")

global Choice
Choice=[]
def Reset():
    path.clear()
    coor.clear()
    Choice.clear()
    Canvas1.delete("all")
    Canvas1.create_image(0, 0 , anchor=NW, image=MapRz_img)
    
# This function is self explanatory. Males jelasin di comment aja sih wkwk    
def TranslatePlace(x):
 def N1():
  Choice.append('n40')
 def N2():
  Choice.append('n4')
 def N3():
  Choice.append('n11') 
 def N4():
  Choice.append('n9')
 def N5():
  Choice.append('n7')
 def N6():
  Choice.append('n8')
 def N7():
  Choice.append('n24')
 def N8():
  Choice.append('n25')
 def N9():
  Choice.append('n29') 
 def N10():
  Choice.append('n13')
 def N11():
  Choice.append('n31')
 def N12():
  Choice.append('n17') 
 def N13():
  Choice.append('n33') 
 def N14():
  Choice.append('n49')
 def N15():
  Choice.append('n50')
 def N16():
  Choice.append('n36')
 def N17():
  Choice.append('n47')
 def N18():
  Choice.append('n45')
 def N19():
  Choice.append('n15')  
 PlcCh={'1.Widya Puraya':N1,'2.Gedung Serbaguna':N2,'3.ICT Center':N3,'4.Lab Terpadu':N4,'5.Stadion':N5,'6.Waduk Pendidikan':N6,'7.Sekolah Vokasi':N7,'8.Fakultas Hukum':N8,'9.Fakultas Ilmu Budaya':N9,'10.Fakultas Ilmu Sosial':N10,
        '11.Fakultas Teknik':N11,'12. Fakultas Peternakan dan Pertanian':N12,'13.Fakultas Perikanan dan Ilmu Kelautan':N13,'14.Fakultas Psikologi':N14,'15.Fakultas Kedokteran':N15,
        '16.Fakultas Kesehatan Masyarakat':N16,'17.Fakultas Ekonomika dan Bisnis':N17,'18.Fakultas Sains dan Matematika':N18,'19.Gedung Prof. Soedarto':N19}
        
 PlcCh[x]()


# OK Button and the function that triggered by the OK Button
def OK():
    Reset()
    yl=nw.get()
    yd=des.get()
    if (yl=="Pilih Lokasi anda" or yd=="Pilih Tujuan"):
     messagebox.showinfo("Kosong", "Harap isi Lokasi dan Tujuan.")
    elif (yl==yd):
     messagebox.showinfo("Warning", "Posisi dan Tujuan sama. Harap memilih yang berbeda.")
    else:    
     TranslatePlace(yl)
     TranslatePlace(yd)
     Crnt=Choice[0]
     WtG=Choice[1]
     dijkstra(graph, Crnt, WtG)
     MkLn()
     print (path)
    
Enter_B=Button(CrDes_fr,text="Go",command=OK).grid(row=3,column=0) 






root.mainloop()
