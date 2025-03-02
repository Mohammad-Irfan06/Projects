logo = """
  _____                              _____  _       _                 
 / ____|                            /  ___|(_)     | |                
| |     __ _  ___  ___  __ _ _ __  | |      _ _ __ | |__   ___ _ __   
| |    / _` |/ _ \/ __|/ _` |' __| | |     | | '_ \| '_ \ / _ \' __|  
| |___| (_| |  __/\__ \ (_| | |    | |____ | | |_) | | | |  __/ |     
 \_____\__,_|\___||___/\__,_|_|     \_____||_| .__/|_| |_|\___|_|     
                                             | |                      
                                             |_|                      
"""
print(logo)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
            shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {cipher_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt , type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. otherwise type 'no': ").lower()
    if restart == 'no':
         should_continue = False
         print("Good Bye!")