import streamlit as st
st.title("Greenkinator")

#step 1: Greek to Latin or Latin to Greek?

st.header("Welcome, do you wish to Romanize or un-Romanize a Greek word?")
romanizeAnswer = st.selectbox("Choose below:", ["Romanize", "un-Romanize"])
# print("respond as such: 'Romanize'")

#romanizeAnswer = input()

#step 2 (Greek): change the individual letters

def unRomanize():
  word = st.text_input("enter your Romanized Greek word:")
  #print("enter your Romanized Greek word")
  #word = input()

  word = word.replace("th", "θ")
  word = word.replace("kh", "χ")
  word = word.replace("ph", "φ")
  word = word.replace("rh", "ῥ")

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

  st.write(word)

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

#step 5 (Greek): final check for no internal rough breathing marks

  pass
#step 2 (Latin): change the individual letters

def romanize(word):
    pass



if romanizeAnswer == "Romanize":
    romanize()
else:
    unRomanize()
