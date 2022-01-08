from googletrans import Translator

translator = Translator()

#Text
t = "hi"
 
                                          #from       to
translation = translator.translate(t, src="en", dest="de")

print(f"{translation.origin} -> {translation.text}")

"""
pip install googletrans==3.1.0a0
I'll love the light for it shows me the way, yet I'll endure the darkness because it shows me the stars.
"""
