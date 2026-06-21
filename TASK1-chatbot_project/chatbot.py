import datetime
import random

print("🤖 ChatBot: Hey Khushboo! Main aa gaya. Baat karte hain?")
print("Commands: hi, name, how are you, time, date, weather, joke, exit\n")

while True:
    x = input("You: ").lower().strip()
    
    # 1. EXIT
    if x == "exit" or x == "bye" or x == "ttyl":
        print("Bot: Bye Khushboo! Apna khayal rakhna ❤️")
        input("Press Enter to close...")
        break
    
    # 2. GREETING
    elif x in ["hi", "hii", "hello", "hey"]:
        print("Bot: Hello Khushboo! Aaj mood kaisa hai?")
    
    # 3. NAME
    elif "name" in x or "naam" in x:
        print("Bot: Main ChatBot hu. Aur tum Khushboo ho na? Sahi bola?")
    
    # 4. HOW ARE YOU
    elif "how are you" in x or "kaise ho" in x:
        print("Bot: Main toh mast hu! Tum sunao, din kaisa gaya?")
    
    # 5. MOOD REPLY - YAHAN `print` sahi kar diya
    elif "good" in x or "accha" in x or "maza" in x:
        print("Bot: Wah! Ye sunke accha laga 😊 Chai peeyogi?")  # prints ❌  print ✅
    elif "thak" in x or "tired" in x:
        print("Bot: Arre thak gayi? 5 min rest kar le. Main yahin hu")
    elif "bored" in x:
        print("Bot: Bore ho rahi? 'joke' likh ke dekh")
    
    # 6. TIME - YE MISSING THA
    elif "time" in x:
        now = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Bot: Abhi {now} ho raha hai ⏰")
    
    # 7. DATE - YE BHI MISSING THA
    elif "date" in x or "aaj" in x:
        today = datetime.datetime.now().strftime("%d %B %Y")
        print(f"Bot: Aaj {today} hai 📅")
    
    # 8. WEATHER - YE BHI MISSING THA
    elif "weather" in x or "mausam" in x:
        print("Bot: Kankhal me abhi 28°C, Thoda cloudy hai ⛅")
        print("Bot: Aaj baarish ka chance 20% hai. Chhatri le jana!")
    
    # 9. JOKE
    elif "joke" in x or "hasao" in x:
        jokes = [
            "Teacher: Beta 2+2? Student: Sir 22 😂",
            "WiFi slow hai toh brain fast kar lete hain?"
        ]
        print("Bot:", random.choice(jokes))
    
    # 10. HELP
    else:
        print("Bot: 'help' likh ke dekh ki main kya samajhta hu")