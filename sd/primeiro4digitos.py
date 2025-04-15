def separa_4_primeiros_bits():# Pede ao usuário uma string de 16 bits e retorna os 4 .
    
    while True:
        entrada = input("Digite uma sequência de exatamente 16 bits: ").replace(" ","")#replece ("termo que deseja trocar", "pelo o que deseja trocar")
        
        # Verifica se tem 16 bits e se todos sao numeros
        if len(entrada) != 16 or not entrada.isdigit():
            print("Erro: A entrada deve ter exatamente 16 bits. Tente novamente.")
        else:
            break  # Sai do loop 
    
    # Pega os 4 primeiros bits (posições 0, 1, 2 e 3)
    quatro_primeiros = entrada[:4]
    
    print(f"Bits digitados: {entrada}")
    print("Os 4 primeiros bits são:", quatro_primeiros)
    return quatro_primeiros

# Executa o programa

separa_4_primeiros_bits()