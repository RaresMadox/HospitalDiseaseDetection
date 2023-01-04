from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB

class MainFrame(Frame):
    def __init__(self, container, controller):
        super().__init__(container)


class FirstPage(Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        label = Label(self, text="Meniu Principal", background='#FFFFCC', font="Times 20 italic bold").grid(column=0,
                                                                                                            row=0)

        button1 = Button(self, text='Adauga Pacient', background='#FFE699', width=20,
                         height=3, command=lambda: controller.show_frame(AddPacient)).grid(column=0, row=1)

        button2 = Button(self, text='Identifica Boala', background='#FFE699', width=20,
                         height=3,command=lambda: controller.show_frame(IdentBoala)).grid(column=0, row=2)
        button3 = Button(self, text='Fisa Medicala', background='#FFE699', width=20,
                         height=3,command=lambda: controller.show_frame(FisaMed)).grid(column=0, row=3)

        button4 = Button(self, text='Inchide', background='#FFE699', width=20,
                         height=3, command=controller.destroy).grid(column=0, row=4)

        self.configure(background='#FFFFCC')


class AddPacient(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Adauga Pacient", background='#FFFFCC', font="Times 20 italic bold")
        label.grid(row=2, column=1, padx=10, pady=10)


        button1 = Button(self, text="Identificare boala",
                         command=lambda: controller.show_frame(IdentBoala))


        button1.grid(row=0, column=0, padx=10, pady=10)


        button2 = Button(self, text="Catre pagina principala",
                         command=lambda: controller.show_frame(FirstPage))

        button2.grid(row=1, column=0, padx=10, pady=10)

        L1 = Label(self, text="Nume", background='#FFFFCC')
        E1 = Entry(self, bd=5, width=50)
        L1.grid(row=4, padx=350, column=1)
        E1.grid(row=5, column=1)

        L2 = Label(self, text="Prenume", background='#FFFFCC')
        E2 = Entry(self, bd=5, width=50)
        L2.grid(row=6, column=1)
        E2.grid(row=7, column=1)

        L3 = Label(self, text="An nastere", background='#FFFFCC')
        E3 = Entry(self, bd=5, width=50)
        L3.grid(row=8, column=1)
        E3.grid(row=9, column=1)

        L4 = Label(self, text="Sex", background='#FFFFCC')
        E4 = Entry(self, bd=5, width=50)
        L4.grid(row=10, column=1)
        E4.grid(row=11, column=1)

        L5 = Label(self, text="Numer Telefon", background='#FFFFCC')
        E5 = Entry(self, bd=5, width=50)
        L5.grid(row=12, column=1)
        E5.grid(row=13, column=1)

        L6 = Label(self, text="E-mail", background='#FFFFCC')
        E6 = Entry(self, bd=5, width=50)
        L6.grid(row=14, column=1)
        E6.grid(row=15, column=1)

        button3 = Button(self, text="Adaugati", background='#00FF00')
        button3.grid(row=1, column=22, padx=10, pady=10)

        self.configure(background='#FFFFCC')


class IdentBoala(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.l1 = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills',
              'joint_pain',
              'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition',
              'spotting_ urination', 'fatigue',
              'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness',
              'lethargy', 'patches_in_throat',
              'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
              'dehydration', 'indigestion',
              'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
              'back_pain', 'constipation',
              'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure',
              'fluid_overload',
              'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm',
              'throat_irritation',
              'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
              'fast_heart_rate',
              'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain',
              'dizziness', 'cramps',
              'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid',
              'brittle_nails',
              'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
              'slurred_speech', 'knee_pain', 'hip_joint_pain',
              'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements',
              'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
              'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine',
              'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
              'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
              'abnormal_menstruation', 'dischromic _patches',
              'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum',
              'lack_of_concentration', 'visual_disturbances',
              'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding',
              'distention_of_abdomen', 'history_of_alcohol_consumption',
              'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking',
              'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
              'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
              'yellow_crust_ooze']

        self.disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
                   'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
                   ' Migraine', 'Cervical spondylosis',
                   'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid',
                   'hepatitis A',
                   'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
                   'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
                   'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
                   'Osteoarthristis',
                   'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection',
                   'Psoriasis',
                   'Impetigo']

        self.l2 = []
        for x in range(0, len(self.l1)):
            self.l2.append(0)

        # TESTING DATA
        self.tr = pd.read_csv("Testing.csv")
        self.tr.replace(
            {'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                           'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                           'Bronchial Asthma': 9, 'Hypertension ': 10,
                           'Migraine': 11, 'Cervical spondylosis': 12,
                           'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                           'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                           'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                           'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                           'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                           'Varicose veins': 30, 'Hypothyroidism': 31,
                           'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                           '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                           'Psoriasis': 39,
                           'Impetigo': 40}}, inplace=True)

        self.X_test = self.tr[self.l1]
        self.y_test = self.tr[["prognosis"]]
        np.ravel(self.y_test)

        # TRAINING DATA
        df = pd.read_csv("Training.csv")

        df.replace(
            {'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                           'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                           'Bronchial Asthma': 9, 'Hypertension ': 10,
                           'Migraine': 11, 'Cervical spondylosis': 12,
                           'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                           'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                           'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                           'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                           'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                           'Varicose veins': 30, 'Hypothyroidism': 31,
                           'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                           '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                           'Psoriasis': 39,
                           'Impetigo': 40}}, inplace=True)

        self.X = df[self.l1]

        self.y = df[["prognosis"]]
        np.ravel(self.y)

        self.Symptom1 = StringVar()
        self.Symptom1.set(None)
        self.Symptom2 = StringVar()
        self.Symptom2.set(None)
        self.Symptom3 = StringVar()
        self.Symptom3.set(None)
        self.Symptom4 = StringVar()
        self.Symptom4.set(None)
        self.Symptom5 = StringVar()
        self.Symptom5.set(None)

        label = Label(self, text="Identificare boala",background='#FFFFCC', font="Times 20 italic bold")
        label.grid(row=2, column=1, padx=10, pady=10)


        button1 = Button(self, text="Catre adaugare pacient",
                             command=lambda: controller.show_frame(AddPacient))


        button1.grid(row=0, column=0, padx=10, pady=10)


        button2 = Button(self, text="Catre pagina principala",
                             command=lambda: controller.show_frame(FirstPage))

        button2.grid(row=1, column=0, padx=10, pady=10)

        OPTIONS = sorted(self.l1)

        L1 = Label(self, text="Nume",background='#FFFFCC')
        E1 = Entry(self, bd=5,width = 50)
        L1.grid(row=4, padx = 350, column=1)
        E1.grid(row=5, column=1)

        L2 = Label(self, text="Prenume",background='#FFFFCC')
        E2 = Entry(self, bd=5,width = 50)
        L2.grid(row=6, column=1)
        E2.grid(row=7, column=1)

        L3 = Label(self, text="CNP",background='#FFFFCC')
        E3 = Entry(self, bd=5,width = 50)
        L3.grid(row=8, column=1)
        E3.grid(row=9, column=1)

        L4 = Label(self, text="Simptom1",background='#FFFFCC')
        S1En = OptionMenu(self, self.Symptom1, *OPTIONS)
        L4.grid(row=10, column=1)
        S1En.grid(row=11, column=1)

        L5 = Label(self, text="Simptom2",background='#FFFFCC')
        S2En = OptionMenu(self,self.Symptom2, *OPTIONS)
        L5.grid(row=12, column=1)
        S2En.grid(row=13, column=1)

        L6 = Label(self, text="Simptom3",background='#FFFFCC')
        S3En= OptionMenu(self, self.Symptom3, *OPTIONS)
        L6.grid(row=14,column=1)
        S3En.grid(row=15, column=1)

        L6 = Label(self, text="Simptom4",background='#FFFFCC')
        S4En = OptionMenu(self, self.Symptom4, *OPTIONS)
        L6.grid(row=16, column=1)
        S4En.grid(row=17, column=1)

        L7 = Label(self, text="Simptom5",background='#FFFFCC')
        S5En = OptionMenu(self, self.Symptom5, *OPTIONS)
        L7.grid(row=18, column=1)
        S5En.grid(row=19, column=1)



        self.t3 = Text(self, height=1, width=30)
        self.t3.config(font=("Elephant", 20))
        self.t3.grid(row=22, column=1)

        button3 = Button(self, text="Identificati", background='#00FF00',height=2, width=20, command=self.message)
        # putting the button in its place by
        # using grid
        button3.grid(row=1, column=1)

        self.configure(background='#FFFFCC')

    def NaiveBayes(self):

        gnb = MultinomialNB()
        gnb = gnb.fit(self.X, np.ravel(self.y))

        self.y_pred = gnb.predict(self.X_test)
        print(accuracy_score(self.y_test, self.y_pred))
        print(accuracy_score(self.y_test, self.y_pred, normalize=False))

        psymptoms = [self.Symptom1.get(), self.Symptom2.get(), self.Symptom3.get(), self.Symptom4.get(), self.Symptom5.get()]

        for k in range(0, len(self.l1)):
            for z in psymptoms:
                if (z == self.l1[k]):
                    self.l2[k] = 1

        self.inputtest = [self.l2]
        self.predict = gnb.predict(self.inputtest)
        self.predicted = self.predict[0]

        h = 'no'
        for a in range(0, len(self.disease)):
            if (self.disease[self.predicted] == self.disease[a]):
                h = 'yes'
                break

        if (h == 'yes'):
            self.t3.delete("1.0", END)
            self.t3.insert(END, self.disease[a])
        else:
            self.t3.delete("1.0", END)
            self.t3.insert(END, "No Disease")

    def message(self):
        if (
                self.Symptom1.get() == "None" and self.Symptom2.get() == "None" and self.Symptom3.get() == "None" and self.Symptom4.get() == "None" and self.Symptom5.get() == "None"):
            messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
        else:
            self.NaiveBayes()




class FisaMed(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Fisa Medicala",background='#FFFFCC', font="Times 20 italic bold")
        label.grid(row=1, column=1, padx=10, pady=10)


        # button to show frame 3 with text
        # layout3
        button2 = Button(self, text="Catre pagina principala",
                             command=lambda: controller.show_frame(FirstPage))
        button3 = Button(self, text="Salveaza Format World",
                         command=lambda: controller.show_frame(FirstPage))
        button4 = Button(self, text="Salveaza Format PDF",
                         command=lambda: controller.show_frame(FirstPage))
        L6 = Label(self, text="Nume", background='#FFFFCC')
        E6 = Entry(self, bd=5, width=50)
        L6.grid(row=2, padx=350, column=1)
        E6.grid(row=3, column=1)

        L7 = Label(self, text="Prenume", background='#FFFFCC')
        E7 = Entry(self, bd=5, width=50)
        L7.grid(row=4, column=1)
        E7.grid(row=5, column=1)

        L7 = Label(self, text="CNP", background='#FFFFCC')
        E7 = Entry(self, bd=5, width=50)
        L7.grid(row=6, column=1)
        E7.grid(row=7, column=1)

        # putting the button in its place by
        # using grid
        button2.grid(row=0, column=0, padx=10, pady=10)

        button3.grid(row=8, column=1, padx=10, pady=10)
        button4.grid(row=9, column=1, padx=10, pady=10)
        self.configure(background='#FFFFCC')


class App(Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('Administrare pacienti')
        self.geometry('1200x800')
        self.configure(background='#FFFFCC')
        self.resizable(0, 0)
        # windows only (remove the minimize/maximize button)
        self.attributes('-toolwindow', True)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}


        for F in (FirstPage, AddPacient, IdentBoala, FisaMed):
            frame = F(container, self)


            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)


        self.columnconfigure(0, weight=1)
        self.columnconfigure(3, weight=1)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
