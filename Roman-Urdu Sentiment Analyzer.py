positive_words = [
    # General Praise & Quality
    "zabardast", "zabrdust", "zbrdst", "behtareen", "behtrin", "aala", "ala", "aalaah", "kamaal", "kamal", 
    "lajawab", "lajawb", "laajawab", "shandar", "shaandar", "khoobsurat", "khubsurat", "khubsurt", "pyara", 
    "pyari", "pyare", "pyaara", "pyaari", "pyaare", "mashallah", "mshallah", "mshallah", "subhanallah", 
    "jazakallah", "jazakAllah", "shukriya", "shukria", "fit", "fitt", "outclass", "mazedar", "mazedaar", 
    "mzedar", "top", "super", "solid", "classic", "authentic", "asli", "aslee", "original", "sasta", 
    "sastaa", "munasib", "munaseb", "fast", "tez", "tezz", "saaf", "saf", "pak", "roshan", "aasan", 
    "asan", "sahulat", "sahoolat", "mutmain", "tasalli", "tasali", "mufeed", "fayda", "faida", "munafa", 
    "imaandar", "imandar", "sacha", "sachaa", "khulus", "khuloos", "izzat", "respect", "duayein", "duain", 
    "hamdard", "khushboo", "khushbu", "zaika", "zaiqadar", "zayqadar", "heavy", "set", "crisp", "fresh", 
    "smooth", "easy", "discount", "gift", "muft", "free", "reliable", "numaya", "umdah", "umda", "dilkash", 

    # Social Media Reaction & Value Slang
    "dilchasp", "mast", "pasand", "psnd", "khush", "acha", "achaa", "achaah", "achi", "achii", "achiy", 

    "achay", "ache", "achey", "hit", "rocks", "clean", "taaza", "taza", "maza", "mazza", "zindabad", 

    "zindabadh", "mubarak", "mubark", "bomb", "elite", "recommended", "recomended", "perfect", "superhit", 

    "love", "dil se", "dil sey", "tareef", "paisa vasool", "paisa wasool", "paisavasool", "paisawasool", 

    "dil jeet liya", "meharbani", "mehrbani", "mubarakbaad", "behtar", "khaas", "khas", "aala tareen", 

    # Variations & Expressions
    "mashahoor", "mashhoor", "zabardast quality", "best", "vip", "salute", "khush raho", "100% original", 
    "zbrdsthai", "zabardast hai", "v good", "bohat acha", "bht acha", "bhut acha", "boht pyara", "bht pyari", 
    "achi hai", "acha hy", "zabardast hy", "zabarjast", "khoob", "khub", "shukriyaa", "10/10", "100/100",

    # Added from Comments
    "theek", "masala", "freshness", "premium", "reasonable", "moisturizing", "creamy", "rich"
]
negative_words = [
    # Direct Complaints & Poor Quality
    "bekaar", "bekar", "bkar", "ganda", "gandah", "gandi", "gandey", "faltu", "faltoo", "bakwas", 
    "bakwaas", "bkwas", "kharab", "khrab", "khrabized", "ghatiya", "ghatya", "ghateeya", "nakal", "nakli", 
    "naklee", "dhoka", "dhokha", "fraud", "froud", "frood", "chor", "choor", "loot", "loott", "mehnga", 
    "mehanga", "mahnga", "daag", "fuzool", "fazool", "fzul", "mayoos", "mayos", "kachra", "jhoot", 

    "jhoot", "jhoota", "jhoote", "jhuto", "takleef", "bura", "buri", "bure", "nuqsan", "nuqsaan", 

    "ghalti", "ghalti", "late", "sust", "slow", "badmijaz", "badmijaaj", "battameez", "batameez", 

    "battameezi", "zillat", "zero", "beghairat", "besharam", "bewaqoof", "bewaqof", "jahil", "badzaat", 

    "lootera", "third class", "3rd class", "worst", "raddi", "radi", "farigh", "faregh", "bogus", 

    "scam", "scammer", "dhokebaaz", "dhokeybaaz", "chalbaz", "museebat", "azaab", "azab", "gusse", 

    # Rejections, Negations & Issues
    "damage", "damaged", "broken", "toota", "toota hua", "phata", "purana", "badboo", "bezaikah", 
    "pheeka", "pheka", "jala", "kadwa", "kacha", "ghalat", "ghlt", "wrong", "fake", "duplicate", 
    "copy", "lut", "pareshan", "preshan", "pareshani", "bojh", "mushkil", "mshkil", "tension", 
    "zulum", "dukh", "nakara", "fuzul", "thug", "farabi", "bura haal", "waste", "waste of money", 

    "fraudster", "bura experience", "delay", "scamster", "chori", "dhokeybaaz", "bada ganda", 

    "faltu tareen", "kamino", "disappointed", "mayoosi", "ghatya quality", "chori chakari", "nahi", 

    "nahe", "nai", "nhe", "nh", "nhi", "nahin", "mat", "mutt", "mtt", "bekar hai", "bekar hy", 

    "bakwas hai", "bakwas hy", "bura hai", "ghatiya quality", "paisa zaya", "paisay zaya", "zaya",

    # Added from Comments
    "dard", "dry", "ruki ruki", "pighal", "daane", "chikna", "chikni", "tukde", "mirchein", 
    "chipchipi", "chipchipahat", "ordinary", "drying"
]


with open ("/storage/emulated/0/Download/CodingPython/comments.txt","r") as f:
    comments=f.readlines()
   
new_comment=[]

for c in comments:
    c=c.strip()
    c=c.lower()
    c = c.replace(".", "")
    c = c.replace(",", "")
    c = c.replace("!", "")
    c = c.replace("'", "")
    c = c.replace('"', "")
    c=c.lstrip("0123456789. ")
    c=c.split()
    new_comment.append(c) 
    
pos_count=0
neg_count=0
neu_count=0

for comment in new_comment:
    pos=0
    neg=0
    for word in comment:
        if word in positive_words:
            pos=pos+1
        if word in negative_words:
            neg=neg+1
    if pos>neg:
        pos_count=pos_count+1
    elif neg>pos:
        neg_count=neg_count+1
    else:
        neu_count=neu_count+1     
print("--- ROMAN URDU SENTIMENT ANALYZER ---")                    
print("positive words: ",pos_count) 
print("negative words: ",neg_count) 
print("neutral words: ",neu_count)   
t=len(new_comment)
#print("total comments: ",t)
pos_percent = (pos_count / t) * 100
neg_percent = (neg_count / t) * 100
neu_percent = (neu_count / t) * 100    
    
print("positive percentage ",pos_percent,"%")  
print("negative percentage: ",round(neg_percent,2),"%")
print("neutral percentage: ",neu_percent,"%")                
                