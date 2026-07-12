import streamlit as st
import regex
import re
import html

st.markdown("""
<style>
* {
    font-family: 'New Athena Unicode' !important;
}
</style>
""", unsafe_allow_html=True)



# alanur tasks:
# -> result history
# -> parse out strings by space to get individual words 
# filter them to consider the letters only for the INDEXING
# THIS MIGHT NOT BE NEEDED FOR THE REGEX PARTS - check again!!


# vincent (actually Alanur) tasks:
# ōi smooth breathing mark (done)
# ï circumflex
# vowel stem checker (ongoing)
# why do the a's dissapear in hīaa? (done)
# being handsome (done)

st.markdown(
    """
    <style>
    .hero-container {
        position: relative;
        width: 100%;
        height: 250px; 
        overflow: hidden;
    }
    .hero-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }
    .hero-text-1 {
        position: absolute;
        top: 2%;
        left: 5%;
        transform: (-50%, -50%);
        color: white;
        font-size: 3em;
        font-weight: bold;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.7);
        margin: 0;
    }
    .hero-text-2 {
        position: absolute;
        top: 70%;
        left: 5%;
        transform: (-50%, -50%);
        color: white;
        font-size: 3em;
        font-weight: bold;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.7);
        margin: 0;
    }
    </style>

    <div class="hero-container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/b/bc/Byzantine_-_Evangelist_Mark_Seated_in_his_Study_-_Walters_W530A.jpg" alt="Hero Image">
        <div class="hero-text-1">Ancient Greek</div>
        <div class="hero-text-2">Code Tester</div>
    </div>
    """,
    unsafe_allow_html=True
)

tab1, tab2, tab3 = st.tabs(["Word Modifier", "Greekinator", "I_hate_Github"])

if "outputs" not in st.session_state:
    st.session_state.outputs = []

# CONSTANTS
allVows = ["α", "ε", "ι", "ο", "υ", "ᾱ", "η", "ῑ", "ω", "ῡ", "αι", "αυ", "ει", 
             "ευ", "οι", "ου", "υι", "ᾳ", "ᾱυ", "ῃ", "ηυ", "ῳ", "ωυ", "ῡι", "ϊ", 
             "ϋ", "ἀ", "ἐ", "ἰ", "ὀ", "ὐ", "ᾱ̓", "ἠ", "ῑ̓", "ὠ", "ῡ̓", "αἰ", "αὐ", 
             "εἰ", "εὐ", "οἰ", "οὐ", "υἰ", "ᾀ", "ᾱὐ", "ᾐ", "ηὐ", "ᾠ", "ωὐ", "ῡἰ", 
             "ἁ", "ἑ", "ἱ", "ὁ", "ὑ", "ᾱ̔", "ἡ", "ῑ̔", "ὡ", "ῡ̔", "αἱ", "αὑ", "εἱ", 
             "εὑ", "οἱ", "οὑ", "υἱ", "ᾁ", "ᾱὑ", "ᾑ", "ηὑ", "ᾡ", "ωὑ", "ῡἱ"]

allAcuteVows = ["ά", "έ", "ί", "ό", "ύ", "ᾱ́", "ή", "ῑ́", "ώ", "ῡ́", "αί", "αύ", 
                  "εί", "εύ", "οί", "ού", "υί", "ᾴ", "ᾱύ", "ῄ", "ηύ", "ῴ", "ωύ",
                  "ῡί", "ΐ", "ΰ", "ἄ", "ἔ", "ἴ", "ὄ", "ὔ", "ᾱ̓́", "ἤ", "ῑ̓́", "ὤ",
                  "ῡ̓́", "αἴ", "αὔ", "εἴ", "εὔ", "οἴ", "οὔ", "υἴ", "ᾄ", "ᾱὔ", "ᾔ",
                  "ηὔ", "ᾤ", "ωὔ", "ῡἴ", "ἅ", "ἕ", "ἵ", "ὅ", "ὕ", "ᾱ̔́", "ἥ", "ῑ̔́", 
                  "ὥ", "ῡ̔́", "αἵ", "αὕ", "εἵ", "εὕ", "οἵ", "οὕ", "υἵ", "ᾅ", "ᾱὕ",
                  "ᾕ", "ηὕ", "ᾥ", "ωὕ", "ῡἵ"]

allGraveVows = ["ὰ", "ὲ", "ὶ", "ὸ", "ὺ", "ᾱ̀", "ὴ", "ῑ̀", "ὼ", "ῡ̀", "αὶ", "αὺ", 
                  "εὶ", "εὺ", "οὶ", "οὺ", "υὶ", "ᾲ", "ᾱὺ", "ῂ", "ηὺ", "ῲ", "ωὺ", 
                  "ῡὶ", "ῒ", "ῢ", "ἂ", "ἒ", "ἲ", "ὂ", "ὒ", "ᾱ̓̀", "ἢ", "ῑ̓̀", "ὢ", 
                  "ῡ̓̀", "αἲ", "αὒ", "εἲ", "εὒ", "οἲ", "οὒ", "υἲ", "ᾂ", "ᾱὒ", "ᾒ", 
                  "ηὒ", "ᾢ", "ωὒ", "ῡἲ", "ἃ", "ἓ", "ἳ", "ὃ", "ὓ", "ᾱ̔̀", "ἣ", "ῑ̔̀",
                  "ὣ", "ῡ̔̀", "αἳ", "αὓ", "εἳ", "εὓ", "οἳ", "οὓ", "υἳ", "ᾃ", "ᾱὓ", 
                  "ᾓ", "ηὓ", "ᾣ", "ωὓ", "ῡἳ"]

allCircumflexVows = ["", "", "", "", "", "ᾶ", "ῆ", "ῗ", "ῶ", "ῧ", "αῖ", "αῦ", 
                       "εῖ", "εῦ", "οῖ", "οῦ", "υῖ", "ᾷ", "ᾱῦ", "ῇ", "ηῦ", "ῷ", 
                       "ωῦ", "ῡῖ", "", "", "", "", "", "", "", "ἆ", "ἦ", "ἶ", "ὦ",
                       "ὖ", "αἶ", "αὖ", "εἶ", "εὖ", "οἶ", "οὖ", "υἶ", "ᾆ", "ᾱὖ",
                       "ᾖ", "ηὖ", "ᾦ", "ωὖ", "ῡἶ", "", "", "", "", "", "ἇ", "ἧ",
                       "ἷ", "ὧ", "ὗ", "αἷ", "αὗ", "εἷ", "εὗ", "οἷ", "οὗ", "υἷ",
                       "ᾇ", "ᾱὗ", "ᾗ", "ηὗ", "ᾧ", "ωὗ", "ῡἷ"]

allShortVows = ["α", "ε", "ι", "ο", "υ", "ϊ", "ϋ", "ἀ", "ἐ", "ἰ", "ὀ",
                "ὐ", "ἁ", "ἑ", "ἱ", "ὁ", "ὑ"]


allLongVows = ["ᾱ", "η", "ῑ", "ω", "ῡ", "αυ", "ει", "ευ", "ου", "υι", "ᾳ", "ᾱυ", "ῃ", "ηυ", "ῳ", "ωυ", "ῡι", 
             "ᾱ̓", "ἠ", "ῑ̓", "ὠ", "ῡ̓", "αὐ", "εἰ", "εὐ", "οὐ", "υἰ", "ᾀ", "ᾱὐ", "ᾐ", "ηὐ", "ᾠ", "ωὐ", "ῡἰ", 
             "ᾱ̔", "ἡ", "ῑ̔", "ὡ", "ῡ̔", "αὑ", "εἱ", "εὑ", "οὑ", "υἱ", "ᾁ", "ᾱὑ", "ᾑ", "ηὑ", "ᾡ", "ωὑ", "ῡἱ"]

allAnnoyingVows = ["αι", "οι", "αἰ", "οἰ", "αἱ", "οἱ"]

allUnbreathedVows = ["α", "ε", "ι", "ο", "υ", "ᾱ", "η", "ῑ", "ω", "ῡ", "αι", "αυ", "ει", 
             "ευ", "οι", "ου", "υι", "ᾳ", "ᾱυ", "ῃ", "ηυ", "ῳ", "ωυ", "ῡι", "ϊ", 
             "ϋ"]

allRoughBreathedVows = ["ἁ", "ἑ", "ἱ", "ὁ", "ὑ", "ᾱ̔", "ἡ", "ῑ̔", "ὡ", "ῡ̔", "αἱ", "αὑ", "εἱ", 
             "εὑ", "οἱ", "οὑ", "υἱ", "ᾁ", "ᾱὑ", "ᾑ", "ηὑ", "ᾡ", "ωὑ", "ῡἱ"]

allNonContractVows = ["i", "u", "ā", "ē", "ī", "ō", "ū", "ai", "au", "ei", 
             "eu", "oi", "ou", "ui", "āi", "āu", "ēi", "ēu", "ōi", "ōu", "ūi", "ï", 
             "ü"]
            
allLiquidConsonants = ["r", "rh", "l", "m", "n"]
allLabialConsonants = ["p", "ph", "b"]
allDentalConsonants = ["t", "th", "d", "z", "s"]
allPalatalConsonants = ["k", "kh", "g"]
            
allVowsAndConsonants = ["a", "e", "i", "o", "u", "ā", "ē", "ī", "ō", "ū", "ai", "au", "ei", 
             "eu", "oi", "ou", "ui", "āi", "āu", "ēi", "ēu", "ōi", "ōu", "ūi", "ï", 
             "ü", "r", "rh", "t", "th", "p", "ph", "s", "d", "g", "h", "k", "kh", "l", "z", "x", "b", "n", "m"]




#st.title("Ancient Greek Code Tester")

#step 1: Greek to Latin or Latin to Greek?

#st.subheader("Please select how you would like to modify your Greek word")
#romanizeAnswer = st.selectbox("Choose below:", ["Latin (unaccented) -> Greek (unaccented)", "Greek (unaccented) -> Latin (unaccented)", "Greek (unaccented) -> Greek (accented)", "Latin (unaccented) -> Greek (accented)"])

#step 2 (Greek): change the individual letters

def unRomanize(word):
  
  #word = st.text_input("Enter your transliterated Greek word")
 
  #word = word.replace("ch", "kh")

  #word = word.replace("ah", "a")
  #word = word.replace("ih", "i")
  #word = word.replace("eh", "e")
  #word = word.replace("oh", "o")
  #word = word.replace("uh", "u")

  #word = word.replace("sh", "s")
  #word = word.replace("dh", "d")
  #word = word.replace("gh", "kh") #might change
  #word = word.replace("lh", "l")
  #word = word.replace("zh", "z")
  #word = word.replace("xh", "x")
  #word = word.replace("bh", "b")
  #word = word.replace("nh", "n")
  #word = word.replace("mh", "m")

  #if word[0] == "r":
    #if word [1] == "h":
      #word = "@" + word[2:]

  #word = word.replace("rrh", "@")

  #word = word.replace("rh", "r")

  #if word[0] == "@":
    #word = "rh" + word[1:]

  #word = word.replace("@", "rrh")

  #change the individual letters

  word = word.replace("rrh", "ρρ")
  word = word.replace("rh", "ῥ")
  
  word = word.replace("th", "θ")
  word = word.replace("kh", "χ")
  word = word.replace("ph", "φ")

  word = word.replace("ha", "ἁ")
  word = word.replace("he", "ἑ")
  word = word.replace("hi", "ἱ")
  word = word.replace("ho", "ὁ")
  word = word.replace("hu", "ὑ")
  word = word.replace("hā", "ᾱ̔")
  word = word.replace("hē", "ἡ")
  word = word.replace("hī", "ῑ̔")
  word = word.replace("hō", "ὡ")
  word = word.replace("hū", "ῡ̔")

  word = word.replace("ks", "ξ")
  word = word.replace("ps", "ψ")

  word = word.replace("a", "α")
  word = word.replace("e", "ε")
  word = word.replace("i", "ι")
  word = word.replace("o", "ο")
  word = word.replace("u", "υ")
  word = word.replace("ā", "ᾱ")
  word = word.replace("ē", "η")
  word = word.replace("ī", "ῑ")
  word = word.replace("ō", "ω")
  word = word.replace("ū", "ῡ")
  word = word.replace("r", "ρ")
  word = word.replace("t", "τ")
  word = word.replace("p", "π")
  word = word.replace("s", "σ")
  word = word.replace("d", "δ")
  word = word.replace("g", "γ")
  word = word.replace("k", "κ")
  word = word.replace("l", "λ")
  word = word.replace("z", "ζ")
  word = word.replace("b", "ϐ")
  word = word.replace("n", "ν")
  word = word.replace("m", "μ")
  word = word.replace("x", "ξ")

  word = word.replace("ï", "ϊ")
  word = word.replace("ü", "ϋ")

  #fix the rough breathing marks and iota subscript

  word = word.replace("ωι", "ῳ")
  word = word.replace("ηι", "ῃ")
  word = word.replace("ᾱι", "ᾳ")

  word = word.replace("ἁι", "αἱ")
  word = word.replace("ἑι", "εἱ")
  word = word.replace("ὁι", "οἱ")
  word = word.replace("ὑι", "υἱ")
  word = word.replace("ᾱ̔ι", "ᾁ")
  word = word.replace("ἡι", "ᾑ")
  word = word.replace("ὡι", "ᾡ")
  word = word.replace("ῡ̔ι", "ῡἱ")
  word = word.replace("ἁυ", "αὑ")
  word = word.replace("ἑυ", "εὑ")
  word = word.replace("ὁυ", "οὑ")
  word = word.replace("ᾱ̔υ", "ᾱὑ")
  word = word.replace("ἡυ", "ηὑ")
  word = word.replace("ὡυ", "ωὑ")
  #fix the final and initial letters

  word = regex.findall(r'\X', word)



  try: 
    
    if word[-1] == "σ":
      word = word[:-1] + ["ς"]
  
    if word[0] == "ϐ":
      word = ["β"] + word[1:]
        
    if word[0] == "ρ":
      word = ["ῤ"] + word[1:]
    
    if word[0] not in allRoughBreathedVows:
      if word[1] not in allRoughBreathedVows: #just to make sure that the first vowel doesnt get two breathing marks
      
       if word[0] == "α":
         if word[1] == "ι":
           word = regex.findall(r'\X', "αἰ") + word[2:]
         elif word[1] == "υ":
           word = regex.findall(r'\X', "αὐ") + word[2:]
         else:
           word = ["ἀ"] + word[1:]
     
       if word[0] == "ε":
         if word[1] == "ι":
           word = regex.findall(r'\X', "εἰ") + word[2:]
         elif word[1] == "υ":
           word = regex.findall(r'\X', "εὐ") + word[2:]
         else:
           word = ["ἐ"] + word[1:]
     
       if word[0] == "ι":
         word = ["ἰ"] + word[1:]
       
       if word[0] == "ο":
         if word[1] == "ι":
           word = regex.findall(r'\X', "οἰ") + word[2:]
         elif word[1] == "υ":
           word = regex.findall(r'\X', "οὐ") + word[2:]
         else:
           word = ["ὀ"] + word[1:]
     
       if word[0] == "υ":
         if word[1] == "ι":
           word = regex.findall(r'\X', "υἰ") + word[2:]
         else:
           word = ["ὐ"] + word[1:]
     
       if word[0] == "ᾱ":
         if word[1] == "ι":
           word = ["ᾀ"] + word[2:]
         elif word[1] == "υ":
           word = regex.findall(r'\X', "ᾱὐ") + word[2:]
         else:
           word = ["ᾱ̓"] + word[1:]
     
       if word[0] == "η":
         if word[1] == "ι":
           word = ["ᾐ"] + word[2:]
         elif word[1] == "υ":
           word = regex.findall(r'\X', "ηὐ") + word[2:]
         else:
           word = ["ἠ"] + word[1:]
     
       if word[0] == "ῑ":
         word = ["ῑ̓"] + word[1:]
     
       if word[0] == "ω":
         if word[1] == "ι":
           word = ["ᾠ"] + word[2:]
         elif word[1] == "υ":
           word = regex.findall(r'\X', "ωὐ") + word[2:]
         else:
           word = ["ὠ"] + word[1:]
     
       if word[0] == "ῡ":
         if word[1] == "ι":
           word = regex.findall(r'\X', "ῡἰ") + word[2:]
         else:
           word = ["ῡ̓"] + word[1:]

       if word[0] == "ῳ":
           word = ["ᾠ"] + word[1:]
           
       if word[0] == "ῃ":
           word = ["ᾐ"] + word[1:]
          
       if word[0] == "ᾳ":
           word = ["ᾀ"] + word[1:]

  except IndexError:
    if word == ["ῃ"]:
        word = ["ᾐ"]
    if word == ["ᾳ"]:
        word = ["ᾀ"]
    if word == ["ῳ"]:
        word = ["ᾠ"]
    if word == ["α"]:
        word = ["ἀ"]
    if word == ["ε"]:
        word = ["ἐ"]
    if word == ["ι"]:
        word = ["ἰ"]
    if word == ["ο"]:
        word = ["ὀ"]
    if word == ["υ"]:
        word = ["ὐ"]
    if word == ["ᾱ"]:
        word = ["ᾱ̓"]
    if word == ["η"]:
        word = ["ἠ"]
    if word == ["ῑ"]:
        word = ["ῑ̓"]
    if word == ["ω"]:
        word = ["ὠ"]
    if word == ["ῡ"]:
        word = ["ῡ̓"]
    pass
        
  return "".join(word)
    
  if word:
    st.session_state.outputs.insert(0, word)
   
  pass

def romanize(word):

  # word = st.text_input("Enter your Greek word")

  word = word.replace("α","a")
  word = word.replace("ε","e")
  word = word.replace("ι","i")
  word = word.replace("ο","o")
  word = word.replace("υ","u")
  word = word.replace("ᾱ","ā")
  word = word.replace("η","ē")
  word = word.replace("ῑ","ī")
  word = word.replace("ω","ō")
  word = word.replace("ῡ","ū")
  word = word.replace("ᾳ","āi")
  word = word.replace("ῃ","ēi")
  word = word.replace("ῳ","ōi")
  word = word.replace("ϊ","ï")
  word = word.replace("ϋ","ü")
  word = word.replace("ἀ","a")
  word = word.replace("ἐ","e")
  word = word.replace("ἰ","i")
  word = word.replace("ὀ","o")
  word = word.replace("ὐ","u")
  word = word.replace("ᾱ̓","ā")
  word = word.replace("ἠ","ē")
  word = word.replace("ῑ̓","ī")
  word = word.replace("ὠ","ō")
  word = word.replace("ῡ̓","ū")
  word = word.replace("ᾀ","āi")
  word = word.replace("ᾐ","ēi")
  word = word.replace("ᾠ","ōi")
  word = word.replace("ἁ","ha")
  word = word.replace("ἑ","he")
  word = word.replace("ἱ","hi")
  word = word.replace("ὁ","ho")
  word = word.replace("ὑ","hu")
  word = word.replace("ᾱ̔","hā")
  word = word.replace("ἡ","hē")
  word = word.replace("ῑ̔","hī")
  word = word.replace("ὡ","hō")
  word = word.replace("ῡ̔","hū")
  word = word.replace("ᾁ","hāi")
  word = word.replace("ᾑ","hēi")
  word = word.replace("ᾡ","hōi")
  
  word = word.replace("ρρ","rrh")
  word = word.replace("ρ","r")
  word = word.replace("ῥ", "rh")
  word = word.replace("ῤ", "r")
  
  word = word.replace("τ","t")
  word = word.replace("θ","th")
  word = word.replace("π","p")
  word = word.replace("σ","s")
  word = word.replace("ς","s")
  word = word.replace("δ","d")
  word = word.replace("φ","ph")
  word = word.replace("γ","g")
  word = word.replace("ξ","x")
  word = word.replace("κ","k")
  word = word.replace("λ","l")
  word = word.replace("ζ","z")
  word = word.replace("χ","kh")
  word = word.replace("ψ","ps")
  word = word.replace("β","b")
  word = word.replace("ν","n")
  word = word.replace("μ","m")
  
  word = word.replace("ahi", "hai")
  word = word.replace("ahu", "hau")
  word = word.replace("ehi", "hei")
  word = word.replace("ehu", "heu")
  word = word.replace("ohi", "hoi")
  word = word.replace("ohu", "hou")
  word = word.replace("uhi", "hui")
  word = word.replace("āhu", "hāu")
  word = word.replace("ēhu", "hēu")
  word = word.replace("ōhu", "hōu")
  word = word.replace("ūhi", "hūi")
  
  word = word.replace("āhi", "hāi")
  word = word.replace("ēhi", "hēi")
  word = word.replace("ōhi", "hōi")

  return word
 
  pass

def getVowels(word):
  vow_list = []
  idx_list = []

  i = 0
  word = regex.findall(r'\X', word)
  while i < len(word):
    if word[i] in allVows:
      vowel_1 = word[i]
      if i < len(word) - 1:
        vowel_2 = vowel_1 + word[i+1]
        if vowel_2 in allVows:
          vow_list.append(vowel_2)
          idx_list.append(i)
          i += 2
          continue
      vow_list.append(vowel_1)
      idx_list.append(i)
    i += 1

  return vow_list, idx_list

def acuteAccent(word, n): # n from last
  vow_lt, idx_lt = getVowels(word)
  
  vow = vow_lt[-n]
  idx =  idx_lt[-n]

  mapping = dict(zip(allVows, allAcuteVows))
  act_vow = mapping.get(vow, vow)
    
  word = regex.findall(r'\X', word)
  word = word[:idx] + [act_vow] + word[idx + len(regex.findall(r'\X', act_vow)):]  
  return "".join(word)

def graveAccent(word, n): # n from last
  vow_lt, idx_lt = getVowels(word)
  
  vow = vow_lt[-n]
  idx =  idx_lt[-n]

  mapping = dict(zip(allVows, allGraveVows))
  grv_vow = mapping.get(vow, vow)

  word = regex.findall(r'\X', word)
  word = word[:idx] + [grv_vow] + word[idx + len(regex.findall(r'\X', grv_vow)):]  
  return "".join(word)



def circumflexAccent(word, n): # n from last
  vow_lt, idx_lt = getVowels(word)
  
  vow = vow_lt[-n]
  idx =  idx_lt[-n]

  mapping = dict(zip(allVows, allCircumflexVows))
  crcm_vow = mapping.get(vow, vow)

  word = regex.findall(r'\X', word)
  word = word[:idx] + [crcm_vow] + word[idx + len(regex.findall(r'\X', crcm_vow)):]  
  return "".join(word)




def accentuate(word):
    # word = st.text_input("enter your unaccented Greek word:")
    vow_list, idx_list = getVowels(word)
    
    last_vow = vow_list[-1]

    vow_count = len(vow_list)

    if vow_count == 1: # MONOSYLLABIC
      return graveAccent(word, 1)
    elif vow_count == 2: # DISYLLABIC
      if last_vow in allLongVows: # if long
        return acuteAccent(word, 2)
      else: 
          if vow_list[-2] in allShortVows: 
            return acuteAccent(word, 2)
          else: # if long
            return circumflexAccent(word, 2)
    elif vow_count >= 3:
      if last_vow in allLongVows: # if long
        return acuteAccent(word, 2)
      else:
        return acuteAccent(word, 3)

#if ῗ ῧ before cons turns into ῖ ῦ

def unRomanizeAndAccentuate(word):
    #word = st.text_input("Enter your Romanized Greek word")
  
    word = unRomanize(word)
    word = accentuate(word)
  
    return word 
  
    pass

def getVowelsAndConsonants(word):
  try:
    thing_list = []
    idx_list = []
    
    i = 0
    word = regex.findall(r'\X', word)
    st.write(word)
      
    while i < len(word):
      if word[i] in allVowsAndConsonants:
        thing_1 = word[i]
        if i < len(word) - 1:
          thing_2 = thing_1 + word[i+1]
          if thing_2 in allVowsAndConsonants:
            thing_list.append(thing_2)
            idx_list.append(i)
            i += 2
            continue
        thing_list.append(thing_1)
        idx_list.append(i)
      i += 1
  
  except TypeError:
    pass
      
  st.write(thing_list)
  return thing_list, idx_list

def rootsGuesser():

  col1, col2 = st.columns([0.7, 0.3])
  with col2:
    st.write("")
    st.write("")
    if st.button("More information"):
        st.write("Whilst the principle part is created by adding a verb ending to the stem, the stem is created by adding one or multiple affixes to the root. This means that the root is the primary building block when constructing a verb's morphology. Whilst, idealy, the root stays constant between every stem, it is not uncommon for the root to change. Though those changes are sometimes irregular, often they are predictable.")
        
  with col1:
    word_1 = st.text_input("Enter the root of your verb's first principle part")
    word_1 = romanize(word_1)

    # initializing root status
    rootStatus = ""
            
    thing_list, idx_list = getVowelsAndConsonants(word_1)
    st.write(thing_list) #debug

   
        
    last_thing = thing_list[-1]
      
            
    if last_thing in allNonContractVows:
      rootStatus = "vowelStem"
    elif last_thing in allLiquidConsonants:
      rootStatus = "liquidStem"
    elif last_thing in allLabialConsonants:
      rootStatus = "labialStem"
    elif last_thing in allDentalConsonants:
      rootStatus = "dentalStem"
    elif last_thing in allPalatalConsonants:
      rootStatus = "palatalStem"
    else:
      return
        
    rootStatusMessage = rootStatus + "Message"
    st.write(rootStatusMessage)
    st.write("")
    st.write(last_thing)
    
    if rootStatusMessage == "vowelStemMessage":
      st.write("It seems like your verb is what is known as a 'vowel stem verb.' This is great news, because this class of verb usually has a predictable root formation.")

#################################
#################################
#################################
#################################
#START OF AKROOMENOIS DEFINITIONS

def clean_for_matching(text):
    """Normalize text into pure alphabetic lowercase characters for safe alignment matching."""
    cleaned = re.sub(r'[\d\W_]+', '', text.lower())
    return cleaned

def parse_textgrid_intervals(textgrid_content):
    """Parse a standard TextGrid file buffer or raw string into a flat sequence list of timed words."""
    intervals = []
    block_pattern = re.compile(r'intervals\s*\[\d+\]\s*:\s*xmin\s*=\s*([\d.]+)\s*xmax\s*=\s*([\d.]+)\s*text\s*=\s*"([^"]*)"')
    
    for match in block_pattern.finditer(textgrid_content):
        xmin = float(match.group(1))
        xmax = float(match.group(2))
        word_text = match.group(3).strip()
        
        if word_text:
            intervals.append({
                "start": xmin,
                "end": xmax,
                "text": word_text,
                "clean": clean_for_matching(word_text)
            })
    return intervals

def parse_source_text_with_subsections(raw_text, mode="grc"):
    """
    Parses raw text inputs into sections.
    Greek: Splits by ALL punctuation (including commas), tracking sections, sentences, and sub-sentences.
    English: Splits by commas to match the sub-sentence depth structure cleanly.
    """
    lines = raw_text.split('\n')
    sections_dict = {}
    current_section = None
    
    for line in lines:
        line = line.strip()
        if not line or "Event Date:" in line:
            continue
            
        diogenes_match = re.search(r'Section\s+(\d+)\.', line, re.IGNORECASE)
        topos_match = re.search(r'(?:§\s*\d+\.\d+\.(\d+)|\[(\d+)\])', line)
        
        if diogenes_match:
            current_section = int(diogenes_match.group(1))
            continue 
        elif topos_match:
            sec_num = topos_match.group(1) or topos_match.group(2)
            current_section = int(sec_num)
            line = re.sub(r'(?:§\s*\d+\.\d+\.\d+|\[\d+\])\s*(?:Book_\d+)?', '', line).strip()
            
        if current_section is None:
            continue
            
        if current_section not in sections_dict:
            sections_dict[current_section] = []
            
        if mode == "grc":
            # Greek split on everything including commas
            raw_phrases = re.split(r'(?<=[,.,·;:•!?\x27’])\s+', line)
            sentence_counter = 1
            sub_sentence_counter = 1
            
            for p in raw_phrases:
                p_str = p.strip()
                if not p_str:
                    continue
                
                sections_dict[current_section].append({
                    "text": p_str,
                    "sentence_num": sentence_counter,
                    "sub_sentence_num": sub_sentence_counter
                })
                
                # Check how sentences/sub-sentences step forward:
                if re.search(r'[,]$', p_str):
                    # It's a comma: next phrase is a new sub-sentence inside the same main sentence
                    sub_sentence_counter += 1
                elif re.search(r'[.·;:•!?]$', p_str):
                    # Terminal punctuation: move to next main sentence block, reset sub-counter
                    sentence_counter += 1
                    sub_sentence_counter = 1
        else:
            # English splits on both structural markers AND commas to attempt sub-sentence pairing
            raw_phrases = re.split(r'(?<=[,.;:!?])\s+', line)
            sentence_counter = 1
            sub_sentence_counter = 1
            
            for p in raw_phrases:
                p_str = p.strip()
                if not p_str:
                    continue
                
                sections_dict[current_section].append({
                    "text": p_str,
                    "sentence_num": sentence_counter,
                    "sub_sentence_num": sub_sentence_counter
                })
                
                if re.search(r'[,]$', p_str):
                    sub_sentence_counter += 1
                elif re.search(r'[.;:!?]$', p_str):
                    sentence_counter += 1
                    sub_sentence_counter = 1
                
    return sections_dict

def align_and_generate_html(greek_text, english_text, textgrid_text):
    """Run cross-source text matching and generate parallel outputs using 3-tier sub-sentence tags."""
    greek_sections = parse_source_text_with_subsections(greek_text, mode="grc")
    english_sections = parse_source_text_with_subsections(english_text, mode="en")
    tg_intervals = parse_textgrid_intervals(textgrid_text)
    
    tg_idx = 0
    num_intervals = len(tg_intervals)
    
    output_1_lines = []
    output_2_lines = []
    output_3_lines = []
    
    all_sections = sorted(list(set(greek_sections.keys()).intersection(set(english_sections.keys()))))
    if not all_sections:
        all_sections = sorted(list(greek_sections.keys()))
        
    for idx, sec in enumerate(all_sections):
        sub_sentence_timestamps = {}
        section_start_timestamp = None
        
        # --- PROCESS GREEK PHRASES ---
        if sec in greek_sections and greek_sections[sec]:
            is_first_phrase = True
            
            for item in greek_sections[sec]:
                phrase = item["text"]
                s_num = item["sentence_num"]
                ss_num = item["sub_sentence_num"]
                
                words = phrase.split()
                matched_words_data = []
                phrase_start_time = None
                
                for word in words:
                    clean_w = clean_for_matching(word)
                    if not clean_w:
                        matched_words_data.append({"text": word, "start": None, "end": None, "is_punc": True})
                        continue
                    
                    word_start = 0.0
                    word_end = 0.0
                    found_match = False
                    
                    attempts = 0
                    while tg_idx < num_intervals and attempts < 15:
                        tg_clean = tg_intervals[tg_idx]["clean"]
                        if tg_clean == clean_w or clean_w in tg_clean or tg_clean in clean_w:
                            word_start = tg_intervals[tg_idx]["start"]
                            word_end = tg_intervals[tg_idx]["end"]
                            if phrase_start_time is None:
                                phrase_start_time = word_start
                            tg_idx += 1
                            found_match = True
                            break
                        else:
                            tg_idx += 1
                            attempts += 1
                    
                    if not found_match:
                        word_start = tg_intervals[tg_idx-1]["end"] if tg_idx > 0 else 0.0
                        word_end = word_start + 0.5
                        if phrase_start_time is None:
                            phrase_start_time = word_start
                    
                    matched_words_data.append({
                        "text": word,
                        "start": word_start,
                        "end": word_end,
                        "is_punc": False
                    })
                
                if phrase_start_time is None:
                    phrase_start_time = 0.0
                
                if section_start_timestamp is None:
                    section_start_timestamp = phrase_start_time
                
                # Cache via compound keys: (sentence, sub_sentence)
                timestamp_key = (s_num, ss_num)
                if timestamp_key not in sub_sentence_timestamps:
                    sub_sentence_timestamps[timestamp_key] = phrase_start_time
                    
                o1_words_str = ""
                for w_item in matched_words_data:
                    punc_match = re.match(r'^([^\w\s]+)(.*?)$|^([\s\w\W]*?)([.,·;:’\']+)$', w_item["text"])
                    if punc_match:
                        base_txt = re.sub(r'[.,·;:’\']', '', w_item["text"])
                        punc_txt = "".join([g for g in punc_match.groups() if g and g != base_txt])
                        o1_words_str += f'<span class="word">{html.escape(base_txt)}</span><span class="punctuation">{html.escape(punc_txt)}</span> '
                    else:
                        o1_words_str += f'<span class="word">{html.escape(w_item["text"])}</span> '
                
                o2_words_str = ""
                for w_item in matched_words_data:
                    if w_item["is_punc"]:
                        o2_words_str += f'<span class="punctuation">{html.escape(w_item["text"])}</span> '
                    else:
                        base_txt = re.sub(r'[.,·;:’\']', '', w_item["text"])
                        punc_only = w_item["text"].replace(base_txt, "")
                        word_span = f'<span class="word" data-word-start="{w_item["start"]:.2f}" data-word-end="{w_item["end"]:.2f}">{html.escape(base_txt)}</span>'
                        if punc_only:
                            word_span += f'<span class="punctuation">{html.escape(punc_only)}</span>'
                        o2_words_str += word_span + " "
                
                # New 3-Tier Label Configuration
                data_sec_label = f"{sec}.{s_num}.{ss_num}"
                if is_first_phrase:
                    o1_phrase = f"  [{sec}] <span data-start=\"{phrase_start_time:.2f}\" data-section=\"{data_sec_label}\" class=\"phrase\">{o1_words_str.strip()}</span>\n"
                    o2_phrase = f"  [{sec}] <span data-start=\"{phrase_start_time:.2f}\" data-section=\"{data_sec_label}\" class=\"phrase\">{o2_words_str.strip()}</span>\n"
                    is_first_phrase = False
                else:
                    o1_phrase = f"  <span data-start=\"{phrase_start_time:.2f}\" data-section=\"{data_sec_label}\" class=\"phrase\">{o1_words_str.strip()}</span>\n"
                    o2_phrase = f"  <span data-start=\"{phrase_start_time:.2f}\" data-section=\"{data_sec_label}\" class=\"phrase\">{o2_words_str.strip()}</span>\n"
                    
                output_1_lines.append(o1_phrase)
                output_2_lines.append(o2_phrase)
                
        if section_start_timestamp is None:
            section_start_timestamp = tg_intervals[tg_idx-1]["start"] if tg_idx > 0 else 0.0
            
        # --- PROCESS ENGLISH PHRASES ---
        if sec in english_sections and english_sections[sec]:
            for i, eng_item in enumerate(english_sections[sec]):
                eng_phrase_text = eng_item["text"]
                e_s_num = eng_item["sentence_num"]
                e_ss_num = eng_item["sub_sentence_num"]
                
                escaped_eng = html.escape(eng_phrase_text, quote=False)
                
                # Check symmetry match on specific structural keys
                target_key = (e_s_num, e_ss_num)
                if target_key in sub_sentence_timestamps:
                    ts_val = f"{sub_sentence_timestamps[target_key]:.2f}"
                else:
                    ts_val = f"{section_start_timestamp:.2f}" if i == 0 else ""
                
                if i == 0:
                    o3_phrase = f"  [{sec}] <span data-start=\"{ts_val}\" class=\"phrase_en\">{escaped_eng}</span>\n"
                else:
                    o3_phrase = f"  <span data-start=\"{ts_val}\" class=\"phrase_en\">{escaped_eng}</span>\n"
                output_3_lines.append(o3_phrase)
            
        if idx < len(all_sections) - 1:
            output_1_lines.append("  <br><br>\n")
            output_2_lines.append("  <br><br>\n")
            output_3_lines.append("  <br><br>\n")
        
    return "".join(output_1_lines), "".join(output_2_lines), "".join(output_3_lines)


def prepare_readalong_studio_text(raw_text):
    """Extracts pure text content from raw web-scraped outputs, removing structural headers."""
    lines = raw_text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if "Event Date:" in line:
            continue
            
        if re.match(r'^Book\s+\d+,\s*Chapter\s+\d+,\s*Section\s+\d+\.?$', line, re.IGNORECASE):
            continue
        if re.match(r'^Section\s+\d+\.?$', line, re.IGNORECASE):
            continue
            
        line = re.sub(r'^(?:§\s*\d+\.\d+\.\d+|\[\d+\])\s*(?:Book_\d+)?\s*', '', line).strip()
        
        if line:
            cleaned_lines.append(line)
        
    return "\n".join(cleaned_lines)

#END OF AKROOMENOIS DEFINITIONS
###############################
###############################
###############################
###############################

#TABS 2 AND 1
with tab1:
  st.subheader("Please select how you would like to modify your Greek word")
  romanizeAnswer = st.selectbox("Choose below:", ["Latin (unaccented) -> Greek (unaccented)", "Greek (unaccented) -> Latin (unaccented)", "Greek (unaccented) -> Greek (accented)", "Latin (unaccented) -> Greek (accented)"])
  
  word = st.text_input("Enter word:")

  try: 
    if romanizeAnswer == "Greek (unaccented) -> Latin (unaccented)":
        st.write(romanize(word))
    
    if romanizeAnswer == "Greek (unaccented) -> Greek (accented)":
        st.write(accentuate(word))
    
    if romanizeAnswer == "Latin (unaccented) -> Greek (unaccented)":
        st.write(unRomanize(word))
   
    if romanizeAnswer == "Latin (unaccented) -> Greek (accented)":
        st.write(unRomanizeAndAccentuate(word))

    if romanizeAnswer == "Principal part roots guesser (experimental)":
        rootsGuesser()
   
  except IndexError:
    pass

with tab2:
  st.subheader("Principal part roots guesser (experimental)")
    
  try: 
    rootsGuesser()
   
  except IndexError:
    pass

#








# --- STREAMLIT TAB 3: AKROOMENOIS INTERFACE REFACTOR ---
with tab3:
    st.subheader("Akroomenois HTML Alignment Generator")
    st.write("Provide your Greek text, English text, and TextGrid alignments using files OR direct copy-paste.")

    # 1. GREEK INPUT
    st.markdown("### 1. Greek Text Input")
    uploaded_greek = st.file_uploader("Upload Greek Source Text (.txt)", type=["txt"], key="upload_grc")
    pasted_greek = st.text_area("OR Paste Greek text directly here:", height=150, key="paste_grc")

    # 2. ENGLISH INPUT
    st.markdown("### 2. English Text Input")
    uploaded_english = st.file_uploader("Upload English Translation (.txt)", type=["txt"], key="upload_en")
    pasted_english = st.text_area("OR Paste English translation directly here:", height=150, key="paste_en")

    # 3. TEXTGRID INPUT
    st.markdown("### 3. TextGrid Alignment Input")
    uploaded_tg = st.file_uploader("Upload TextGrid File (.txt/.TextGrid)", type=["txt", "textgrid"], key="upload_tg")
    pasted_tg = st.text_area("OR Paste TextGrid content directly here:", height=150, key="paste_tg")

    # Resolve Data Sources (Direct Copy-Paste overrides File Upload)
    greek_content = pasted_greek.strip() if pasted_greek.strip() else (uploaded_greek.read().decode("utf-8") if uploaded_greek else None)
    english_content = pasted_english.strip() if pasted_english.strip() else (uploaded_english.read().decode("utf-8") if uploaded_english else None)
    tg_content = pasted_tg.strip() if pasted_tg.strip() else (uploaded_tg.read().decode("utf-8") if uploaded_tg else None)

    if greek_content and english_content and tg_content:
        try:
            out1, out2, out3 = align_and_generate_html(greek_content, english_content, tg_content)
            
            st.success("HTML Outputs Generated Successfully!")
            
            sub_tab1, sub_tab2, sub_tab3 = st.tabs(["Tab 1: Standard Spans", "Tab 2: Word-by-Word Timings", "Tab 3: English Paragraphs"])
            
            with sub_tab1:
                st.code(out1, language="html")
            with sub_tab2:
                st.code(out2, language="html")
            with sub_tab3:
                st.code(out3, language="html")
                
        except Exception as e:
            st.error(f"Error executing text processing alignment: {str(e)}")


# --- STREAMLIT TAB 4: READALONG STUDIO CLEANER INTERFACE ---
#with tab4 if 'tab4' in locals() else st.tabs(["...","...","...","ReadAlong Studio Preparation"])[-1]:
   # st.subheader("Text Normalizer for Forced-Alignment Audio Sync")
   # st.write("Paste raw text or upload files below to discard headers, metadata tags, and paragraph codes.")

   # uploaded_ra = st.file_uploader("Upload Raw Text File (.txt)", type=["txt"], key="upload_ra")
   # pasted_ra = st.text_area("OR Paste raw source text directly here:", height=200, key="paste_ra")

   # ra_content = pasted_ra.strip() if pasted_ra.strip() else (uploaded_ra.read().decode("utf-8") if uploaded_ra else None)

   # if ra_content:
       # cleaned_studio_text = prepare_readalong_studio_text(ra_content)
        
       # st.success("Text normalized and cleared of structural fluff!")
       # st.text_area("Cleaned output (Ready to copy directly into alignment tools):", value=cleaned_studio_text, height=300, key="readalong_clean_output")
