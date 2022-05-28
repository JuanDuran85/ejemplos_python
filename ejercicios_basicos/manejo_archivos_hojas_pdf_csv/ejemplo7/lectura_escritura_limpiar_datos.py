"""_summary_

    Lectura y escritura de un archivo txt para eliminar espacios en datos del tipo string
    
"""

path_file_txt: str = "/home/juan/Descargas/programacion/ejemplos_python/ejercicios_basicos/manejo_archivos_hojas_pdf_csv/ejemplo7/ej5.txt"

text_in: str = ""
list_text_out: list = []


with open(path_file_txt, 'r', encoding="utf8") as total_file:
    for i,line in enumerate(total_file):
        print(line)
        list_text_out.append(line.split(','))


print(list_text_out)

for i,text_line in enumerate(list_text_out):
    for j,text_in_line in enumerate(text_line):
        list_text_out[i][j] = text_in_line.strip() 

print(list_text_out)

with open(path_file_txt, 'w', encoding="utf8") as total_file:
    for i,text_line in enumerate(list_text_out):
        total_file.write(','.join(text_line))
        total_file.write('\n')