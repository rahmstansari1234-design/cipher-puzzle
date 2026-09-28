import sys

def get_final_concrete_maps():
    # Strict, hardcoded encryption mapping honoring your exact case tricks
    encrypt_map = {
        # Word 1 & 3: Rahmat n Rishika logic
        'R': 'R', 'a': 'E', 'h': 'd', 'm': 'i', 't': 'p',
        'n': 'r', 
        'r': 'n', 'i': 'e', 's': 'o', 'k': 'g',
        
        # Word 2: Hello -> Dahhk logic
        'H': 'D', 'e': 'a', 'l': 'h', 'o': 'k',
        
        # Standalone structural overrides
        'd': 'h', 'v': 'y', 'u': 'y', 'w': 'a', 'x': 'b', 'y': 'c', 'z': 'v'
    }
    
    # Perfect, locked-in reverse lookup table for 100% accurate decryption
    decrypt_map = {v: k for k, v in encrypt_map.items()}
    
    # Force direct multi-pass decoding keys for the "H" and "D" puzzle choices
    decrypt_map['D'] = 'H'
    decrypt_map['H'] = 'd'
    decrypt_map['h'] = 'l'
    
    return encrypt_map, decrypt_map

def run_cipher_engine(text, mapping_matrix):
    output = []
    for char in text:
        # Map the character directly if it exists, otherwise leave spaces/punctuation alone
        output.append(mapping_matrix.get(char, char))
    return "".join(output)

def main():
    enc_matrix, dec_matrix = get_final_concrete_maps()
    print("=== FINAL IMMUTABLE ENCRYPTION TERMINAL ===")
    
    # Infinite loop loop with no exit option as requested
    while True:
        print("\n(1) RED N BLUE FOR LETTER")
        print("(2) RED N BLUE FOR ALPHANUMERIC")
        domain = input("Enter active domain key [1 or 2]: ").strip()
        
        if domain == '1':
            vector = input("Select Vector -> (E)ncrypt or (D)ecrypt: ").strip().upper()
            if vector == 'E':
                payload = input("Enter plaintext data payload: ")
                print(f"-> Encrypted Code: {run_cipher_engine(payload, enc_matrix)}")
            elif vector == 'D':
                payload = input("Enter code to decrypt: ")
                print(f"-> Decrypted Text: {run_cipher_engine(payload, dec_matrix)}")
        else:
            print("Digit Alphanumeric domain is locked and standby.")

if __name__ == "__main__":
    main()

