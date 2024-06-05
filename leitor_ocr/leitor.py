from abc import ABC, abstractmethod
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import ( PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError)
import cv2
import pytesseract
import mahotas
from PIL import Image
import numpy

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class ILeitor_ocr(ABC):
    __filename = None
    __images = None

    @abstractmethod
    def converter_pdf_para_imagem(self):
        pass

    @abstractmethod
    def ler_imagem_e_identificar_texto_e_pontos_de_interesse(self):
        pass

    @abstractmethod
    def identificar_caixas(self):
        pass

    @abstractmethod
    def ler_marcacao(self):
        pass

    @abstractmethod
    def contar_dados_das_marcacoes(self):
        pass

    @abstractmethod
    def organizar_dados(self):
        pass

    @abstractmethod
    def apresentar_dados(self):
        pass

    @abstractmethod
    def run(self):
        pass

class Leitor_ocr(ILeitor_ocr):
    def __init__(self, filename:str):
        self.__filename = filename
        print('Leitor OCR iniciado...')
    
    def converter_pdf_para_imagem(self):
        self.__images = convert_from_path(self.__filename, fmt='png', poppler_path='C:/Program Files/poppler-24.02.0/Library/bin')
        for idx, image in enumerate(self.__images):
            set_name = f'imagem{idx}.png'
            image.save(set_name)

    def ler_imagem_e_identificar_texto_e_pontos_de_interesse(self):
        # Carrega o classificador de retângulos
        # classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        caminho_da_imagem = 'imagem0.png'
        imagem = cv2.imread(caminho_da_imagem, 0)
        imagem_com_threshold = cv2.adaptiveThreshold(imagem, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 175, 1)
        imagem_binaria = cv2.medianBlur(imagem_com_threshold, 5)

        # imagem_suave = cv2.blur(imagem, (4, 4))
        # T = mahotas.thresholding.otsu(imagem_suave)
        # binnary = imagem_suave.copy()
        # binnary[binnary > T] = 255
        # binnary[binnary < 255] = 0
        # binnary = cv2.bitwise_not(binnary)

        cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        # imagem = cv2.convertScaleAbs(imagem)
        # bordas = cv2.Canny(imagem, 0, 50)
        contours, hierarquia = cv2.findContours(imagem_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        contour_1 = numpy.array([[[0, 0]],[[100, 0]], [[100,100]], [[5,4]]])
        area = cv2.contourArea(contour_1)
        # (x, y, w, h) = cv2.boundingRect(area)

        # Filtrar componentes por tamanho
        # contornos_filtrados = []
        # for cnt in contours:
        #     print(cnt)
        #     area = cv2.contourArea(cnt)
        #     if 0 < area < 400000:  # Ajustar valores de acordo com a imagem
        #         contornos_filtrados.append(cnt)
        print(area)

        # # Desenha os contornos na imagem
        # cv2.rectangle(binnary, (166, 1100), (196, 810), 120, 3)

        # retangulos = classifier.detectMultiScale(binnary, 1.1, 3)

        # # Desenha os retângulos na imagem
        # for (x, y, w, h) in retangulos:
        #     cv2.rectangle(binnary, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # screen_height = cv2.getWindowProperty("test", cv2.width)
        # print(image_height, image_width, screen_height)
        # new_width = int(screen_height * image_width / image_height)
        # bordas = cv2.Canny(binnary, 70, 150)
        # bin2 = cv2.resize(binnary, (300, 300), interpolation=cv2.INTER_AREA)

        cv2.imshow("test", imagem_binaria)

        # screen_width = cv2.getWindowProperty('test', cv2.WND_PROP_FULLSCREEN_WIDTH)
        # print(screen_width)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def identificar_caixas(self):
        pass

    def ler_marcacao(self):
        pass

    def contar_dados_das_marcacoes(self):
        pass

    def organizar_dados(self):
        pass

    def apresentar_dados(self):
        pass

    def get_filename(self):
        return self.__filename
    
    def run(self):
        self.converter_pdf_para_imagem()
        self.ler_imagem_e_identificar_texto_e_pontos_de_interesse()