import streamlit as st
import regex



st.markdown("""
<style>
* {
    font-family: 'New Athena Unicode' !important;
}
</style>
""", unsafe_allow_html=True)



# alanur tasks:
# result history
# being cute (done)

# vincent (actually Alanur) tasks:
# ōi smooth breathing mark (done)
# ï circumflex
# vowel stem checker
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

# https://upload.wikimedia.org/wikipedia/commons/b/bc/Byzantine_-_Evangelist_Mark_Seated_in_his_Study_-_Walters_W530A.jpg

# UI
#st.sidebar.write("sidebar check")
# check whether it works wout the sidebar

#st.markdown(
# """
# <style>
# .stApp {
#        background-color: #FFFFFF;
#    }
# </style>
# """,
# unsafe_allow_html=True
#)

#st.markdown(
#    """
#    <style>
#    section[data-testid="stSidebar"] > div:first-child {
#        background-image: url("https://upload.wikimedia.org/wikipedia/commons/b/bc/Byzantine_-_Evangelist_Mark_Seated_in_his_Study_-_Walters_W530A.jpg");
#        background-size: cover;
#        background-position: 20% center; /* SHIFT */
#        background-repeat: no-repeat;;
#    }
#    </style>
#    """,
#    unsafe_allow_html=True
#)



if "outputs" not in st.session_state:
    st.session_state.outputs = []

# CONSTANTS
allVows = ["α", "ε", "ι", "ο", "υ", "ᾱ", "η", "ῑ", "ω", "ῡ", "αι", "αυ", "ει", 
             "ευ", "οι", "ου", "υι", "ᾳ", "ᾱυ", "ῃ", "ηυ", "ῳ", "ωυ", "ῡι", "ϊ", 
             "ϋ", "ἀ", "ἐ", "ἰ", "ὀ", "ὐ", "ᾱ̓", "ἠ", "ῑ̓", "ὠ", "ῡ̓", "αἰ", "αὐ", 
             "εἰ", "εὐ", "οἰ", "οὐ", "υἰ", "ᾀ", "ᾱὐ", "ᾐ", "ηὐ", "ᾠ", "ωὐ", "ῡἰ", 
             "ἁ", "ἑ", "ἱ", "ὁ", "ὑ", "ᾱ̔", "ἡ", "ῑ̔", "ὡ", "ῡ̔", "αἱ", "αὑ", "εἱ", 
             "εὑ", "οἱ", "οὑ", "υἱ", "ᾁ", "ᾱὑ", "ᾑ", "ηὑ", "ᾡ", "ωὑ", "ῡἱ"]


#allVows = [clustered(v) for v in allVows]

allAcuteVows = ["ά", "έ", "ί", "ό", "ύ", "ᾱ́", "ή", "ῑ́", "ώ", "ῡ́", "αί", "αύ", 
                  "εί", "εύ", "οί", "ού", "υί", "ᾴ", "ᾱύ", "ῄ", "ηύ", "ῴ", "ωύ",
                  "ῡί", "ΐ", "ΰ", "ἄ", "ἔ", "ἴ", "ὄ", "ὔ", "ᾱ̓́", "ἤ", "ῑ̓́", "ὤ",
                  "ῡ̓́", "αἴ", "αὔ", "εἴ", "εὔ", "οἴ", "οὔ", "υἴ", "ᾄ", "ᾱὔ", "ᾔ",
                  "ηὔ", "ᾤ", "ωὔ", "ῡἴ", "ἅ", "ἕ", "ἵ", "ὅ", "ὕ", "ᾱ̔́", "ἥ", "ῑ̔́", 
                  "ὥ", "ῡ̔́", "αἵ", "αὕ", "εἵ", "εὕ", "οἵ", "οὕ", "υἵ", "ᾅ", "ᾱὕ",
                  "ᾕ", "ηὕ", "ᾥ", "ωὕ", "ῡἵ"]

#allAcuteVows = [clustered(v) for v in allAcuteVows]

allGraveVows = ["ὰ", "ὲ", "ὶ", "ὸ", "ὺ", "ᾱ̀", "ὴ", "ῑ̀", "ὼ", "ῡ̀", "αὶ", "αὺ", 
                  "εὶ", "εὺ", "οὶ", "οὺ", "υὶ", "ᾲ", "ᾱὺ", "ῂ", "ηὺ", "ῲ", "ωὺ", 
                  "ῡὶ", "ῒ", "ῢ", "ἂ", "ἒ", "ἲ", "ὂ", "ὒ", "ᾱ̓̀", "ἢ", "ῑ̓̀", "ὢ", 
                  "ῡ̓̀", "αἲ", "αὒ", "εἲ", "εὒ", "οἲ", "οὒ", "υἲ", "ᾂ", "ᾱὒ", "ᾒ", 
                  "ηὒ", "ᾢ", "ωὒ", "ῡἲ", "ἃ", "ἓ", "ἳ", "ὃ", "ὓ", "ᾱ̔̀", "ἣ", "ῑ̔̀",
                  "ὣ", "ῡ̔̀", "αἳ", "αὓ", "εἳ", "εὓ", "οἳ", "οὓ", "υἳ", "ᾃ", "ᾱὓ", 
                  "ᾓ", "ηὓ", "ᾣ", "ωὓ", "ῡἳ"]

#allGraveVows = [clustered(v) for v in allGraveVows]

allCircumflexVows = ["", "", "", "", "", "ᾶ", "ῆ", "ῗ", "ῶ", "ῧ", "αῖ", "αῦ", 
                       "εῖ", "εῦ", "οῖ", "οῦ", "υῖ", "ᾷ", "ᾱῦ", "ῇ", "ηῦ", "ῷ", 
                       "ωῦ", "ῡῖ", "", "", "", "", "", "", "", "ἆ", "ἦ", "ἶ", "ὦ",
                       "ὖ", "αἶ", "αὖ", "εἶ", "εὖ", "οἶ", "οὖ", "υἶ", "ᾆ", "ᾱὖ",
                       "ᾖ", "ηὖ", "ᾦ", "ωὖ", "ῡἶ", "", "", "", "", "", "ἇ", "ἧ",
                       "ἷ", "ὧ", "ὗ", "αἷ", "αὗ", "εἷ", "εὗ", "οἷ", "οὗ", "υἷ",
                       "ᾇ", "ᾱὗ", "ᾗ", "ηὗ", "ᾧ", "ωὗ", "ῡἷ"]

#allCircumflexVows = [clustered(v) for v in allCircumflexVows]

allShortVows = ["α", "ε", "ι", "ο", "υ", "ϊ", "ϋ", "ἀ", "ἐ", "ἰ", "ὀ",
                "ὐ", "ἁ", "ἑ", "ἱ", "ὁ", "ὑ"]

#allShortVows = [clustered(v) for v in allShortVows]

allLongVows = ["ᾱ", "η", "ῑ", "ω", "ῡ", "αυ", "ει", "ευ", "ου", "υι", "ᾳ", "ᾱυ", "ῃ", "ηυ", "ῳ", "ωυ", "ῡι", 
             "ᾱ̓", "ἠ", "ῑ̓", "ὠ", "ῡ̓", "αὐ", "εἰ", "εὐ", "οὐ", "υἰ", "ᾀ", "ᾱὐ", "ᾐ", "ηὐ", "ᾠ", "ωὐ", "ῡἰ", 
             "ᾱ̔", "ἡ", "ῑ̔", "ὡ", "ῡ̔", "αὑ", "εἱ", "εὑ", "οὑ", "υἱ", "ᾁ", "ᾱὑ", "ᾑ", "ηὑ", "ᾡ", "ωὑ", "ῡἱ"]

allAnnoyingVows = ["αι", "οι", "αἰ", "οἰ", "αἱ", "οἱ"]

allUnbreathedVows = ["α", "ε", "ι", "ο", "υ", "ᾱ", "η", "ῑ", "ω", "ῡ", "αι", "αυ", "ει", 
             "ευ", "οι", "ου", "υι", "ᾳ", "ᾱυ", "ῃ", "ηυ", "ῳ", "ωυ", "ῡι", "ϊ", 
             "ϋ"]

#allUnbreathedVows = [clustered(v) for v in allUnbreathedVows]

allRoughBreathedVows = ["ἁ", "ἑ", "ἱ", "ὁ", "ὑ", "ᾱ̔", "ἡ", "ῑ̔", "ὡ", "ῡ̔", "αἱ", "αὑ", "εἱ", 
             "εὑ", "οἱ", "οὑ", "υἱ", "ᾁ", "ᾱὑ", "ᾑ", "ηὑ", "ᾡ", "ωὑ", "ῡἱ"]

#allRoughBreathedVows = [clustered(v) for v in allRoughBreathedVows]
            
allNonContractVows = ["i", "u", "ā", "ē", "ī", "ō", "ū", "ai", "au", "ei", 
             "eu", "oi", "ou", "ui", "āi", "āu", "ēi", "ēu", "ōi", "ōu", "ūi", "ï", 
             "ü"]

#allNonContractVows = [clustered(v) for v in allNonContractVows]
            
allVowsAndConsonants = ["a", "e", "i", "o", "u", "ā", "ē", "ī", "ō", "ū", "ai", "au", "ei", 
             "eu", "oi", "ou", "ui", "āi", "āu", "ēi", "ēu", "ōi", "ōu", "ūi", "ï", 
             "ü", "r", "rh", "t", "th", "p", "ph", "s", "d", "g", "h", "k", "kh", "l", "z", "x", "b", "n", "m"]

#allVowsAndConsonants = [clustered(v) for v in allVowsAndConsonants]



#st.title("Ancient Greek Code Tester")

#st.image("https://upload.wikimedia.org/wikipedia/commons/b/bc/Byzantine_-_Evangelist_Mark_Seated_in_his_Study_-_Walters_W530A.jpg", caption="Evangelist Mark Seated in his Study", use_container_width=True)


#step 1: Greek to Latin or Latin to Greek?

st.subheader("Please select how you would like to modify your Greek word")
romanizeAnswer = st.selectbox("Choose below:", ["Latin (unaccented) -> Greek (unaccented)", "Greek (unaccented) -> Latin (unaccented)", "Greek (unaccented) -> Greek (accented)", "Latin (unaccented) -> Greek (accented)", "Principal part roots guesser (experimental)"])


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
  thing_list = []
  idx_list = []

  i = 0
  word = regex.findall(r'\X', word)
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
    
    return thing_list, idx_list

def rootsGuesser(word):

    # initializing root status
    rootStatus = ""
    
    thing_list, idx_list = getVowelsAndConsonants(word)
    st.write(thing_list)
    last_thing = thing_list[-1]
    
    if last_thing in allNonContractVows:
        rootStatus = "vowelStem"
    
    st.write("Enter the first principal part root of your verb")
    st.write(last_thing)
    st.write(rootStatus)
    

#word = clustered(st.text_input("Enter word:") or "")
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
      st.write(rootsGuesser(word))
   
except IndexError:
  pass

#st.write("")
#st.write("Past results:")
#for output in st.session_state.outputs:
    #st.write(output)
