from tkinter import *                #Library om form, button, labels en enries van te krijgen
from tkinter import scrolledtext     #Library om scrolledtext (informatie_panel) van te krijgen
from tkinter import messagebox       #Library om een message te laten zien aan de gebruiker te krijgen
import requests                      #Library om informatie uit een bepalde url te krijgen
import xmltodict                     #Library om xml bestanden te kunnen maken

Main_form_titel_font = ("Algerian", "50" , "bold", "italic")  #Font settings van Main_form
button_font = ("Arial", "12", "bold")                         #Font settings van buttons
plaatsnaam_edit_font = ("Arial", "20", "bold")                #Font settings van plaatsnaam_edit
informatie_panel_font = ("Arial", "14")                       #Font setting van informatie_panel
informatie_panel_font_fout = ("Arial", "50")                  #Font setting van informatie_panel als er een fout melding is

def informatie(station_naam): #fuctie die de station_naam haalt en de informatie ten aan zien van de station_naam haalt vanuit de web url en daarna de informatie netjes weergeven
    auth_details = ('zakaria.bouhaddaoui@student.hu.nl', '6cheH3UXyshPXxDhkjTX9E3VTXWkQ_TNYZLfBmhD7Ug9LldpvWDnnA') #inloggegevens in auth_details zetten
    api_url = 'http://webservices.ns.nl/ns-api-avt?station='+station_naam  #station_naam met de url concatteneren
    response = requests.get(api_url, auth=auth_details)   #Vraag om informatie van de toegevoegde url met inloggegevens in zetten
    vertrekXML = xmltodict.parse(response.text)    #De reis informatie die wij hebben gekregen in vertrekXML zetten
    informatie_panel.configure(state=NORMAL)       #Om informatie_panel te enabellen om te kunnen
    informatie_panel.delete(1.0, END)              #informatie_panel leeg maken
    informatie_panel.configure(fg='white',font=informatie_panel_font)         #informatie_panel fontkleur wit maken,en fontstyle normaal maken, want misschien bij de vorige uitvoering was er geen resultaat en de font kleur rood was
    headders = ['V-tijd','Vertraging','V-plaats','V-spoor','Trein soort','Vervoerder','Ritnum','Eindbestemming']     #De hoofdtitels als en lijst maken
    headder = ('{}{:9}{}{:18}{}{:39}{}{:4}{}{:17}{}{:16}{}{:6}{}'.format(headders[0],'', headders[1],'', headders[2],'',headders[3],'',headders[4],'',headders[5],'',headders[6],'',headders[7])+'\n')
    informatie_panel.insert(INSERT, headder)       #De hoofdtitel in informatie_panel schrijven
    informatie_panel.insert(INSERT, 'ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ'*3+"ــ")
    try:     #Om te proberen de stations naam die de gebruiker ingevoerd heeft of die wij hebben ingevoerd in de code
        for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']: #Lopen voor elke vertrekkende trein van het station die wij hebben gegeven
            vertraging = ''  #Om het resultaat van of er of geen vertraging is erop te slaan
            vertrektijd = vertrek['VertrekTijd']  #De vertrek tijd van de vertrekndetrein te halen
            vertrektijd = vertrektijd[11:16]      #Allen maar de numers(tijd) van de vertrek tijd van de vertrekndetrein te halen
            try:    #Om te proberen of er een vertraging is
                vertraging = vertrek['VertrekVertragingTekst'] #Als er een vertraging is, dan het vertraging op vertraging variable slaan
            except KeyError: #Zorgt om geen rare fout melding aan de gebruiker laten zien als er geen vertraging is, dan geeft de programma geen als een waarde van vertraging
                vertraging = 'geen'  #Als er geen vertraging is, dan sla 'geen' op vertaging op
            #De informatie van de vertrekende trein netjes op informatie_printen schrijven.
            informatie_printen = ('\n' + '{}\t{}\t\t{}\t\t\t{}\t{}\t\t{}\t\t{}\t{}\t\t'.format(vertrektijd, vertraging, station_naam, vertrek['VertrekSpoor']["#text"], vertrek['TreinSoort'], vertrek['Vervoerder'], vertrek['RitNummer'], vertrek['EindBestemming']))
            informatie_panel.insert(INSERT, informatie_printen)  #Alle informatie op informatie_panel schrijven
    except KeyError: #Zorgt om geen rare fout melding aan de gebruiker laten zien als de stationsnaam onjuist is of geen vertrekkende treinen vanuit het station er zijn, dan geeft de programma een netjes bericht met een uitleg over de foutmelding
        informatie_panel.delete(1.0, END) #informatie_panel leeg maken
        informatie_panel.insert(INSERT, ('\n'*3) + (' ' * 23) + 'Geen resultaat') #Geen resultaat printen
        informatie_panel.configure(fg='red',font=informatie_panel_font_fout) #font kleur rood maken, en font maat groter maken
        messagebox.showerror('NS-API', 'U heeft een onjuiste plaatsnaam ingevoerd, of er zijn momenteel geen vertrekkende treinen vanuit '+station_naam) #Een netjes foutbrief weergeven
    informatie_panel.configure(state="disabled") #Informatie_panel disablen om de gebruiker geen informatie kan wijzigen.

def clicked_reis_informtaie_button(): #click functie van reis_informatie_button
    informatie(plaatsnaam_edit.get()) #Hier krijgen wij de station naam uit de plaatsnaam_edit(Endry)

def clicked_Amsterdam_button():    #click functie van Amsterdam_button
    informatie("Amsterdam")        #Stationsnaam als Amsterdam zetten

def clicked_Rotterdam_button():    #click functie van Rotterdam_button
    informatie("Rotterdam")

def clicked_Utrecht_Centraal_button():  #click functie van Utrecht_Centraal_button
    informatie("Utrecht")

def clicked_Schiphol_button():     #click functie van Schiphol_button
    informatie("Schiphol")

def clicked_Den_Bosch_button():    #click functie van Den_Bosch_button
    informatie("'s-Hertogenbosch")

def clicked_Den_Haag_button():     #click functie van Den_Haag_button
    informatie("Den Haag")

Mainform = Tk()                        #Main_form maken
Mainform.title('NS-API')               #Main_form titel zetten
Mainform.geometry('1920x1080')         #Main_form maat
Mainform.configure(bg='blue')  #Main_form achtergrond kleur
Mainform.wm_state('zoomed')            #Main form Maximized starten

Mainform_title = Label(Mainform, font=Main_form_titel_font, bg="blue", text='Welcome bij NS-API', fg="yellow")   #Verwelkomings label maken
Mainform_title.place(relx=0.265, rely=-0.035, relheight=0.2, relwidth=1)  #Verwelkomings label positie en maat maken

Reis_informatie_button = Button(Mainform, text="Reisinformatie over een\n"+" andere plaats tonen", activebackground="blue", activeforeground="yellow", bg="yellow", fg="blue", font= button_font,command=clicked_reis_informtaie_button) #reis_informatie_button maken en configureren
Reis_informatie_button.place(relx=0.01, rely=0.0155, relheight=0.1, relwidth=0.13)  #Reis_informatie_button positie en maat maken
Mainform.bind('<Return>', (lambda e, Reis_informatie_button=Reis_informatie_button: Reis_informatie_button.invoke()))  #Reis_informatie_button default button maken (dus als je op enter drukt, wordt hij uitgevoerd)

plaatsnaam_edit = Entry(Mainform,font=plaatsnaam_edit_font) #plaats_naam entry maken
plaatsnaam_edit.place(relx=0.2, rely=0.035, relheight=0.08, relwidth=0.25)  #plaats naam entry positie en maat maken

plaatsnaam_label = Label(Mainform, font=button_font, text='Type de naam van een andere plaats', fg="yellow", bg="blue")  #plaats_naam titel label maken
plaatsnaam_label.place(relx=0.2, rely=0.01, relheight=0.02, relwidth=0.25)  #plaats_naam titel label positie en maat maken

Amsterdam_button = Button(Mainform, text="Amsterdam", activebackground="blue", activeforeground="yellow", bg="yellow", fg="blue", font= button_font,command=clicked_Amsterdam_button) #Amsterdam_button maken en configureren
Amsterdam_button.place(relx=0.06, rely=0.14, relheight=0.1, relwidth=0.13)  #Amsterdam_button positie en maat maken

Rotterdam_button = Button(Mainform, text="Rotterdam Centraal", activebackground="blue", activeforeground="yellow", bg="yellow", fg="blue", font= button_font,command=clicked_Rotterdam_button) #Rotterdam_button maken en configureren
Rotterdam_button.place(relx=0.21, rely=0.14, relheight=0.1, relwidth=0.13)  #Rotterdam_button positie en maat maken

Utrecht_Centraal_button = Button(Mainform, text="Utrecht Centraal", activebackground="blue", activeforeground="yellow", bg="yellow", fg="blue", font= button_font,command=clicked_Utrecht_Centraal_button) #Utrecht_Centraal_button maken en configureren
Utrecht_Centraal_button.place(relx=0.36, rely=0.14, relheight=0.1, relwidth=0.13)  #Utrecht_Centraal_button positie en maat maken

Schiphol_button = Button(Mainform, text="Schiphol", activebackground="blue", activeforeground="yellow", bg="yellow", fg="blue", font= button_font,command=clicked_Schiphol_button) #Schiphol_button maken en configureren
Schiphol_button.place(relx=0.51, rely=0.14, relheight=0.1, relwidth=0.13)  #Schiphol_button positie en maat maken

Den_Bosch_button = Button(Mainform, text="'s Hertogenbosch", activebackground="blue", activeforeground="yellow", bg="yellow", fg="blue", font= button_font,command=clicked_Den_Bosch_button) #Den_Bosch_button maken en configureren
Den_Bosch_button.place(relx=0.66, rely=0.14, relheight=0.1, relwidth=0.13) #Den_Bosch_button positie en maat maken

Den_Haag_button = Button(Mainform, text="Den Haag", activebackground="blue", activeforeground="yellow", bg="yellow", fg="blue", font= button_font,command=clicked_Den_Haag_button) #Den_Haag_button maken en configureren
Den_Haag_button.place(relx=0.81, rely=0.14, relheight=0.1, relwidth=0.13) #Den_Haag button positie en maat maken

informatie_panel = scrolledtext.ScrolledText(Mainform,bg='blue') #informatie_panel als scrolledtext maken en configureren
informatie_panel.place(relx=0.06, rely=0.26, relwidth= 0.88, relheight= 0.73) #informatie panel positie en maat maken

Mainform.mainloop()