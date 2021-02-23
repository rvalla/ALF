from char_draw import CharDraw
from txt_draw import TxtDraw
from jpg_draw import JpgDraw

#A code to trigger char art...
#cd = CharDraw(100, 0, 5, 70, "+", "8") #CharDraw dibuja en la terminal
#txt = TxtDraw("test", 100, 5, 3, 40, "-", "@") #Dibuja y guarda en archivos .txt
jpg = JpgDraw("mask_c", 1200, 1800, (0,0,0), (255,255,255), 185, 6, 3, 50, ":", "8") #Dibuja y guarda en .jpg

#Probamos CharDraw()
#cd.random_draw(100)
#cd.triangular_draw(100)
#cd.zigzag_draw(100)
#cd.sin_draw(100)
#cd.harmonic_draw(100, [1,2,3,5])

#Probamos TxtDraw()
#txt.random_draw(200)
#txt.triangular_draw(200)
#txt.zigzag_draw(200)
#txt.sin_draw(200)
#txt.harmonic_draw(200, [1,4,3,2])

#Probamos JpgDraw()
#jpg.random_draw(20)
#jpg.triangular_draw(20)
#jpg.zigzag_draw(20)
#jpg.sin_draw(20)
jpg.harmonic_draw(114, [1,3,2,6])
