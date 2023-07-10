import socket
import pyttsx3
import smtplib
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import cv2
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests
import pywhatkit
import ipaddress

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! CASPER HERE")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

        speak("Ready To Comply. What can I do for you ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # if 'wikipedia' in query:
        #     speak('Searching Wikipedia...')
        #     query = query.replace("wikipedia", "")
        #     results = wikipedia.summary(query, sentences=2)
        #     speak("According to Wikipedia")
        #     print(results)
        #     speak(results)
            
        if 'How can tickets be booked for train travel?' in query:
            speak("Answer is:Indian rail currently provides following ways to book tickets. Reservation a trailwaycounters Online reservation from  https://irctc.co.in Reservation through registered agents and agencies")

        elif 'How many passengers can be booked in a single ticket/transaction?' in query:
            speak("A maximum of 6 passenger for general and upto 4 passenger for tatkal.")

        elif 'Can bulk booking be done through IRCTC?' in query:
            speak("No. Bulk booking cannott be done on the internet.")
        
        elif 'I would like to transfer my ticket to a friend. What is the process?' in query:
            speak("The rail ticket can’t be transferred to a friend. It can be transferred to blood relations (including father, mother, brother, sister, son, daughter, husband or wife) only. For transfer of ticket, an application must be submitted at least 48 hrs to 24 hours in advance of the scheduled departure of the train to the division  office Assistant Commercial Manager  or Area officer.")

        elif 'The name on the ticket is incorrect. How do I get it corrected?' in query:
            speak("It can’t be done once the ticket is reserved. You need to manually cancel the ticket and rebook again.")
        
        elif 'How many days before can a reservation be done?' in query:
            speak("Both the online and offline mode of reservation starts 120 days before the date of journey.")
            
        elif 'How are payment made for online reservation?' in query:
            speak("The following modes are available: Credit card Debit card Mobile/Net banking EMI/cash card")

        elif 'My e-ticket got accidentally deleted from my mail account. How can I get another copy to be sent to me?' in query:
            speak("There is no facility to resend the ticket as mail but you can take the print of you ticket anytime. Just visit https://irctc.co.in and login to your account. There you go to the booked history section and select the ticket and print. You can also enter the PNR number and print the ticket")
        
        elif 'What is Tatkal? How can I get a Tatkal ticket?' in query:
            speak("The Tatkal is a scheme launched by The Indian Railway for passengers who plan their journey at short notice. The Tatkal ticket can be booked one day in advance to the train journey, with booking starting at 10 a.m for AC classes and 11 a.m for sleeper class.")

        elif 'What is the cancellation policy?' in query:
            speak("A reserved ticket can be cancelled up to the charting of the train. The ticket can be cancelled from the reservation counter or by online cancellation section of the IRCTC page after login. A suitable charge will be deducted for the same.")

        elif 'What is the cancellation charge?' in query:
            speak("CANCELLATION TIME	CANCELLATION CHARGE 24 hrs before the departure of the train	Rs.120/- for AC First Class/Executive Class, Rs.100/- for AC 2 Tier/First Class, Rs. 90 for AC 3 Tier/AC Chair car/ AC 3 Economy, Rs.60/- for Sleeper Class and Rs.30/- for Second Class. Within 24 hrs and up to 4 hours before the scheduled departure of the train	25% of the fare Less than 4 hours before the schedule departure of the train up to chart preparation of the train	50% of the fare")

        elif 'I cancelled a ticket, but have not been refunded for the amount. How do I proceed?' in query:
            speak("Generally it takes about 3-7 working days for the refund of the amount. If no refund is made even after 7 working days, you should contact IRCTC 24×7 Helpline: 011 39340000 or send a mail with the ticketing details to care@irctc.co.in")
        
        elif 'Is it mandatory to carry a “Proof of Identity” while travelling?' in query:
            speak("Yes it is mandatory to carry a “Proof of Identity” while travelling in reserved class.")
        
        elif 'What documents can be used as “proof of identity”? Will a photocopy be sufficient?' in query:
            speak("The following shall be accepted as proof of identity: Voter Photo identity card issued by Election Commission of India. Passport. PAN Card issued by Income Tax Department Driving Licence issued by RTO Photo identity card having serial number issued by Central/State Government Student Identity Card with photograph issued by recognized School/College for their students Nationalized Bank Passbook with photograph Credit cards issued by banks with laminated photograph Unique Identification Card “Aadhaar”. Photo identity cards having serial number issued by Public Sector Undertaking of State/Central Government, District Administration, Municipal bodies and Penchant Administration Only attested photocopy of ration card with photograph and nationalized bank passbook with photographs. No other Photocopy will be accepted.")

        elif 'Does Indian Railway offer any discount for group booking?' in query:
            speak("No")

        elif 'How can I reschedule an existing reservation?' in query:
            speak("No, you cannot reschedule any existing reservation. You need to cancel them manually and reserve ticket for the other day or for other train.")
        
        elif 'Can a waitlisted e-ticket holder travel in an unreserved coach?' in query:
            speak("No, ticket holder has to buy another unreserved ticket to do so.")

        elif 'Can I take a pet along with me on the train?' in query:
            speak("Yes, A passenger can take pet along with him in AC First Class or First Class only, provided he/she reserves either a two berth or a four berth compartment exclusively for his/her use, paying the due charges depending upon the type of train. Passengers travelling in other classes are not permitted to carry the pet along with them. But the pet can be booked and carried in the Luggage/Brake Van paying the charges depending upon the type of train. Specially designed Boxes are available in the Brake Van for this purpose. Passengers may contact the Parcel Office to book their pet.")
        
        elif 'Can a tatkal ticket holder who booked tis ticket at the reservation counter travel with out his original ticket?' in query:
            speak("No, He will be treated as travelling without ticket and charged accordingly.")

        elif 'Can I cancelled my PRS counter tickets through IRCTC website/139' in query:
            speak("yes")

        elif 'Are bedrolls given free to passengers travelling in AC Coaches?' in query:
            speak("Yes bedrolls are provided free of cost to passengers travelling in AC 3, AC2 tier and AC first class.")

        elif 'Are catering facilities available in train onboard?' in query:
            speak("Yes. Most of the trains have pantry car facilities. Catering is also arranged in trains where this facility is not available through Train side vending (TSV).")
        
        elif 'Is medical assistance available on trains?' in query:
            speak("A FIRST AID BOX is available with the Train Guards/Superintendents or Pantry Car Managers. They are also trained to provide first aid to passengers. In case of emergency the TTE should be approached so that a message is passed to the Next station. In case hospitalization is required, the passenger may have to discontinue his journey.")

        elif 'Is there any charge for using the Waiting Room at a station?' in query:
            speak("Waiting rooms are available at all major stations. They can be used free of cost upon the production of the Ticket. At few major stations waiting room/dormitory and retiring rooms have outsourced,")
        
        elif 'How can the boarding station be changed?' in query:
            speak("Yes. You need to visit the nearest PRS centers and submit a request to the station master/Chief reservation supervisor.")

        elif 'Will I get a refund on TDR?' in query:
            speak("The TDR refunds are processed as per Extant Railway Rules by concerned railway zones. In most of the cases, TDR must be filed before or within 1 hour of the Departure of Train. The TDR refund process will take at-least 60 days and more. User can always check the status of TDR online.")
        
        elif 'What is the Reservation charges for a class?' in query:
            speak("Reservation Charge :- 1A AC 1 Tier) = 60.00/- Rs. Only 2A AC 2 Tier) = 50.00/- Rs. Only 3A AC 3 Tier) = 40.00/- Rs. Only SL Sleeper) = 20.00/- Rs. Only 2S 2nd Seating) = 15.00/- Rs. Only")

        elif 'What is Super fast charges for a class?' in query:
            speak("Super fast charge :- 1A (AC 1 Tier) = 75.00/- Rs. Only 2A (AC 2 Tier) = 45.00/- Rs. Only 3A (AC 3 Tier) = 45.00/- Rs. Only SL (Sleeper) = 30.00/- Rs. Only 2S (2nd Seating) = 15.00/- Rs. Only General Ticket = 15.00/- Rs. Only.")

        elif 'What is the minimum and maximum Tatkal charges for class?' in query:
            speak("Tatkal Fare – Minimum 30% Fare of Base Fare. Class of Travel Minimum Tatkal Charges (INR) Maximum Tatkal Charges (INR) Second Sitting 10 15 Sleeper 100 200 AC Chair Car 125 225 AC 3 Tier 300 400 AC 2 Tier 400 500 Executive 400 500")

        elif 'Whether I have to pay GST charges?' in query:
            speak("A: Yes, 5% GST charged on AC Classes. Base Fare + Reservation Charge + Superfast Charge + Dynamic fare (if available) * 5% = GST")
        
        elif 'What Fine will be Charged if found Travelling without a pass or ticket?' in query:
            speak("Fare from the station which he has travelled or from the station which the train originally started or from the checking point with equal amount of excess charge subject to a minimum of Rs. 500/- upto the point of detection.")

        elif 'Which is the train for  Bangaluru from Rayabag?' in query:
            speak("16590 RANI CHENNAMMA EXP.")

        elif 'I want to go Dadar. Which train is available from Rayabag?' in query:
            speak("Train No 17317 Hubballi Dadar EXP.")

        elif 'What is the Goa Exp train No. towards Vasco-de-gama?' in query:
            speak("Train No for Goa Exp towards Vasco-De Gama is 12780.")

        elif 'What is the Goa Exp train No, towards  Hazart Nizzamuddin ?' in query:
            speak("Train No. towards Hazart Nizzamuddin is 12779.")