import customtkinter as ctk
import funcoes as fun

# Configuração do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry('198x307')
root.title('Calculadora')
root.resizable(width=False, height=False)

### Mostrador ###
# O CTkEntry substitui o tk.Entry. Adicionei width e height em pixels.
fonte_tela = ctk.CTkFont(family='Arial', size=20)
etr_result = ctk.CTkEntry(root, width=188, height=40, font=fonte_tela, justify='right', state='readonly')
etr_result.place(x=5, y=5)

### Botões do teclado ###
root.bind('<Key>', lambda event: fun.key_press(event, etr_result))
root.bind('<Return>', lambda event: fun.enter_press(event, etr_result))
root.bind('<BackSpace>', lambda event: fun.back_press(event, etr_result))
root.bind('<Escape>', lambda event: fun.esc_press(event, etr_result))

# Dimensões e fonte padronizadas para os botões (em pixels)
w = 42
h = 38
w_zero = 89 # Largura especial para o botão 0
fnt = ctk.CTkFont(family='Arial', size=16)

# Cores para diferenciar operadores dos números
cor_op = "#4A4D50"
cor_op_hover = "#5C6064"

### Números ###
btn_7 = ctk.CTkButton(root, text='7', width=w, height=h, font=fnt, command=lambda: fun.press('7', etr_result))
btn_7.place(x=5, y=134)

btn_8 = ctk.CTkButton(root, text='8', width=w, height=h, font=fnt, command=lambda: fun.press('8', etr_result))
btn_8.place(x=52, y=134)

btn_9 = ctk.CTkButton(root, text='9', width=w, height=h, font=fnt, command=lambda: fun.press('9', etr_result))
btn_9.place(x=99, y=134)

btn_4 = ctk.CTkButton(root, text='4', width=w, height=h, font=fnt, command=lambda: fun.press('4', etr_result))
btn_4.place(x=5, y=176)

btn_5 = ctk.CTkButton(root, text='5', width=w, height=h, font=fnt, command=lambda: fun.press('5', etr_result))
btn_5.place(x=52, y=176)

btn_6 = ctk.CTkButton(root, text='6', width=w, height=h, font=fnt, command=lambda: fun.press('6', etr_result))
btn_6.place(x=99, y=176)

btn_1 = ctk.CTkButton(root, text='1', width=w, height=h, font=fnt, command=lambda: fun.press('1', etr_result))
btn_1.place(x=5, y=218)

btn_2 = ctk.CTkButton(root, text='2', width=w, height=h, font=fnt, command=lambda: fun.press('2', etr_result))
btn_2.place(x=52, y=218)

btn_3 = ctk.CTkButton(root, text='3', width=w, height=h, font=fnt, command=lambda: fun.press('3', etr_result))
btn_3.place(x=99, y=218)

# Botão zero usa a largura estendida (w_zero)
btn_0 = ctk.CTkButton(root, text='0', width=w_zero, height=h, font=fnt, command=lambda: fun.press('0', etr_result))
btn_0.place(x=5, y=260)

### Operadores e Funções ###
btn_som = ctk.CTkButton(root, text='+', width=w, height=h, font=fnt, fg_color=cor_op, hover_color=cor_op_hover, command=lambda: fun.press('+', etr_result))
btn_som.place(x=146, y=92)

btn_sub = ctk.CTkButton(root, text='-', width=w, height=h, font=fnt, fg_color=cor_op, hover_color=cor_op_hover, command=lambda: fun.press('-', etr_result))
btn_sub.place(x=146, y=134)

btn_div = ctk.CTkButton(root, text='/', width=w, height=h, font=fnt, fg_color=cor_op, hover_color=cor_op_hover, command=lambda: fun.press('/', etr_result))
btn_div.place(x=146, y=176)

btn_mul = ctk.CTkButton(root, text='x', width=w, height=h, font=fnt, fg_color=cor_op, hover_color=cor_op_hover, command=lambda: fun.press('x', etr_result))
btn_mul.place(x=146, y=218)

btn_igu = ctk.CTkButton(root, text='=', width=w, height=h, font=fnt, fg_color="#F38015", hover_color="#9C520D", command=lambda: fun.calcular(etr_result))
btn_igu.place(x=146, y=260)

btn_c = ctk.CTkButton(root, text='C', width=w, height=h, font=fnt, fg_color=cor_op, hover_color=cor_op_hover, command=lambda: fun.press('c', etr_result))
btn_c.place(x=5, y=50)

btn_dot = ctk.CTkButton(root, text='.', width=w, height=h, font=fnt, command=lambda: fun.press('.', etr_result))
btn_dot.place(x=99, y=260)

btn_del = ctk.CTkButton(root, text='\u232B', width=w, height=h, font=fnt, fg_color=cor_op, hover_color=cor_op_hover, command=lambda: fun.delete(etr_result))
btn_del.place(x=52, y=50)

btn_powy = ctk.CTkButton(root, text='x^y', width=w, height=h, font=fnt, fg_color=cor_op, hover_color=cor_op_hover, command=lambda: fun.press('^', etr_result))
btn_powy.place(x=5, y=92)

btn_pow = ctk.CTkButton(root, text='x^2', width=w, height=h, font=fnt, fg_color=cor_op, hover_color=cor_op_hover, command=lambda: fun.pow(etr_result))
btn_pow.place(x=52, y=92)

btn_sqrt = ctk.CTkButton(root, text='\u221Ax', width=w, height=h, font=fnt, fg_color=cor_op, hover_color=cor_op_hover, command=lambda: fun.raiz(etr_result))
btn_sqrt.place(x=99, y=92)

btn_bracel = ctk.CTkButton(root, text='(', width=w, height=h, font=fnt, fg_color=cor_op, hover_color=cor_op_hover, command=lambda: fun.press('(', etr_result))
btn_bracel.place(x=99, y=50)

btn_bracer = ctk.CTkButton(root, text=')', width=w, height=h, font=fnt, fg_color=cor_op, hover_color=cor_op_hover, command=lambda: fun.press(')', etr_result))
btn_bracer.place(x=146, y=50)

root.mainloop()