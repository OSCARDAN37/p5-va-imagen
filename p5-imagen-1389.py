import cv2
#leer la imagen con cv2 = computer vision
img = cv2.imread('lambo.jpg')
#determinar el tipo de imagennumpy.ndrray
print(type(img))
#mostrar pixeles
print(img.shape)
#mostrando imagen en ventana barra de titulo
cv2.imshow('auto 1389', img)
##tiempos de espera
cv2.waitKey(0)
# destruir todas las ventanas
cv2.destroyAllWindows()