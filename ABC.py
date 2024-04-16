meme_dict = {
    "CRINGE": "Algo raro",
    "LOL": "Una respuesta a algo grasioso",
    "XD": "una risa",
    ":V": "sarcasmo o gracia",
    "BRO": "amigo, compa",
    "CREEPY": "aterrador, siniestro",
    "AGGRO": "ponerse agresivo/enojado"
}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("no se pudo encontrar la palabra")
