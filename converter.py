import streamlit as st

# UI
st.sidebar.write("sidebar check")
# check whether it works wout the sidebar

st.markdown(
 """
 <style>
 .stApp {
        background-color: #F8DE7E;
    }
 </style>
 """,
 unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] > div:first-child {
        background-image: url("https://cdn.discordapp.com/attachments/1245387818327347241/1405968152784928910/IMG_8713.jpeg?ex=68a0c161&is=689f6fe1&hm=c48537a411f380d820e1ff5838644f02d99cbca7ee06c91bf4190dd37190fdab");
        background-size: cover;
        background-position: 20% center; /* SHIFT */
        background-repeat: no-repeat;;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>
.bubble {
    background-color: 	#EADDCA; /* SECONDARY COLOR */
    padding: 10px 15px;
    border-radius: 15px;
    margin-bottom: 10px;
    color: black; /* TEXT COLOR */
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="bubble">This is a bubble</div>', unsafe_allow_html=True)


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

allShortVows = ["α", "ε", "ι", "ο", "υ", "αι", "οι", "ϊ", "ϋ", "ἀ", "ἐ", "ἰ", "ὀ",
                "ὐ", "αἰ", "οἰ", "ἁ", "ἑ", "ἱ", "ὁ", "ὑ", "αἱ", "οἱ"]

st.title("Ancient Greek Code Tester")

#step 1: Greek to Latin or Latin to Greek?

st.header("Please select how you would like to modify your Greek word?")
romanizeAnswer = st.selectbox("Choose below:", ["Latin (unaccented) -> Greek (unaccented)", "Greek (unaccented) -> Latin (unaccented)", "Greek (unaccented) -> Greek (accented)"])


#step 2 (Greek): change the individual letters

def unRomanize():
  word = st.text_input("enter your Romanized Greek word:")
 
  
  #print("enter your Romanized Greek word")
  #word = input()

  #debug
  
  word = word.replace("ch", "kh")

  word = word.replace("ah", "a")
  word = word.replace("eh", "e")
  word = word.replace("ih", "i")
  word = word.replace("oh", "o")
  word = word.replace("uh", "u")

  word = word.replace("sh", "s")
  word = word.replace("dh", "d")
  word = word.replace("gh", "kh") #might change
  word = word.replace("lh", "l")
  word = word.replace("zh", "z")
  word = word.replace("xh", "x")
  word = word.replace("bh", "b")
  word = word.replace("nh", "n")
  word = word.replace("mh", "m")

  if word[0] == "r":
    if word [1] == "h":
      word = "@" + word[2:]

  word = word.replace("rrh", "@")

  word = word.replace("rh", "r")

  if word[0] == "@":
    word = "rh" + word[1:]

  word = word.replace("@", "rrh")

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

  #st.write(word)

#step 3 (Greek): fix the rough breathing marks and iota subscript

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

#step 4 (Greek): fix the final and initial letters

  if word[-1] == "σ":
    word = word[:-1] + "ς"

  if word[0] == "ϐ":
    word = "β" + word[1:]
  if word[0] == "ρ":
    word = "ῤ" + word[1:]

  if word[0] == "α":
    if word[1] == "ι":
      word = "αἰ" + word[2:]
    elif word[1] == "υ":
      word = "αὐ" + word[2:]
    else:
      word = "ἀ" + word[1:]

  if word[0] == "ε":
    if word[1] == "ι":
      word = "εἰ" + word[2:]
    elif word[1] == "υ":
      word = "εὐ" + word[2:]
    else:
      word = "ἐ" + word[1:]

  if word[0] == "ι":
    word = "ἰ" + word[1:]

  if word[0] == "ο":
    if word[1] == "ι":
      word = "οἰ" + word[2:]
    elif word[1] == "υ":
      word = "οὐ" + word[2:]
    else:
      word = "ὀ" + word[1:]

  if word[0] == "υ":
    if word[1] == "ι":
      word = "υἰ" + word[2:]
    else:
      word = "ὐ" + word[1:]

  if word[0] == "ᾱ":
    if word[1] == "ι":
      word = "ᾀ" + word[2:]
    elif word[1] == "υ":
      word = "ᾱὐ" + word[2:]
    else:
      word = "ᾱ̓" + word[1:]

  if word[0] == "η":
    if word[1] == "ι":
      word = "ᾐ" + word[2:]
    elif word[1] == "υ":
      word = "ηὐ" + word[2:]
    else:
      word = "ἠ" + word[1:]

  if word[0] == "ῑ":
    word = "ῑ̓" + word[1:]

  if word[0] == "ω":
    if word[1] == "ι":
      word = "ᾠ" + word[2:]
    elif word[1] == "υ":
      word = "ωὐ" + word[2:]
    else:
      word = "ὠ" + word[1:]

  if word[0] == "ῡ":
    if word[1] == "ι":
      word = "ῡἰ" + word[2:]
    else:
      word = "ῡ̓" + word[1:]

 
    
  st.write(word)
    
  if word:
    st.session_state.outputs.insert(0, word)

#step 5 (Greek): final check for no internal rough breathing marks

  pass
#step 2 (Latin): change the individual letters

def romanize():

  st.write("I didnt write code for this yet")
  
  pass

def getVowels(word):
  vow_list = []
  idx_list = []

  i = 0
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

  return word[:idx] + act_vow + word[idx + len(act_vow):]

def graveAccent(word, n): # n from last
  vow_lt, idx_lt = getVowels(word)
  
  vow = vow_lt[-n]
  idx =  idx_lt[-n]

  mapping = dict(zip(allVows, allGraveVows))
  grv_vow = mapping.get(vow, vow)

  return word[:idx] + grv_vow + word[idx + len(grv_vow):]

def circumflexAccent(word, n): # n from last
  vow_lt, idx_lt = getVowels(word)
  
  vow = vow_lt[-n]
  idx =  idx_lt[-n]

  mapping = dict(zip(allVows, allCircumflexVows))
  crcm_vow = mapping.get(vow, vow)

  return word[:idx] + crcm_vow + word[idx + len(crcm_vow):]


def accentuate():
    word = st.text_input("enter your unaccented Greek word:")
    vow_list, idx_list = getVowels(word)
    last_vow = vow_list[-1]

    vow_count = len(vow_list)

    if vow_count == 1: # MONOSYLLABIC
      st.write(graveAccent(word, 1))

    elif vow_count == 2: # DISYLLABIC
      if last_vow in allShortVows: 
          if vow_list[-2] in allShortVows: 
            st.write(acuteAccent(word, 2))
          else: # if long
            st.write(circumflexAccent(word, 2))
      
      else: # if long
        st.write(acuteAccent(word, 2))

    elif vow_count >= 3:
      if last_vow in allShortVows:
        st.write(acuteAccent(word, 3))
      else: # if long
        st.write(acuteAccent(word, 2))

    

try: 
  if romanizeAnswer == "Greek (unaccented) -> Latin (unaccented)":
      romanize()
    
  if romanizeAnswer == "Greek (unaccented) -> Greek (accented)":
      accentuate()
    
  if romanizeAnswer == "Latin (unaccented) -> Greek (unaccented)":
      unRomanize()
except IndexError:
  pass

for output in st.session_state.outputs:
    st.write(output)
