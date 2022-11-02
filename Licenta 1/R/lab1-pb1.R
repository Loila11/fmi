#Sã presupunem cã am înregistrat în fiecare zi, pe parcursul a 4 
#sãptãmâni (de Luni pânã Duminicã), numãrul de minute petrecute la 
#telefonul mobil (convorbiri + utilizare) si am obtinut urmãtoarele
#valori: 106, 123, 123, 111, 125, 113, 130, 113, 114, 100, 120, 130, 
#118, 114, 127, 112, 121, 114, 120, 119, 127, 114, 108, 127, 131, 
#157, 102, 133. Ne întrebãm: care sunt zilele din sãptãmânã în care 
#am vorbit cel mai mult? dar cel mai putin? dar zilele în care am 
#vorbit mai mult de 120 de minute?
  
v = c(106, 123, 123, 111, 125, 113, 130, 113, 114, 100, 120, 130, 118,
      114, 127, 112, 121, 114, 120, 119, 127, 114, 108, 127, 131, 157, 
      102, 157)

w = rep(c("Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", 
          "Duminica"), 4)

(w[v == (max(v))])  #zilele in care am vorbit cel mai mult
(w[v == (min(v))])  #zilele in care am vorbit cel mai putin
(w[v>120])  #zilele in care am vorbit mai mult de 120 de minute