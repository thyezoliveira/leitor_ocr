from abc import ABC, abstractmethod
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import ( PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError)
import cv2
import pytesseract
from PIL import Image

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
        caminho_da_imagem = 'imagem0.png'
        imagem = cv2.imread(caminho_da_imagem)
        
        cv2.imshow("test", imagem)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
            # try:
            #     texto = cv2.Ocr(cv2.ORB_FEATURE_MATCHER, cv2.ORB_EXTRACTOR).readText(image)
            #     print(texto)
            # except Exception as e:
            #     print(e)
            #     texto = pytesseract.image_to_string(image, config='--psm 10')
            #     print(texto)
            # text = pytesseract.image_to_string(image, config='--psm 10')
            # _, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
            # print(text)
        #     print(gray_image)
            # if palavra_chave in text:
            #     print(f"Palavra-chave '{palavra_chave}' encontrada na página {self.__images.index(image) + 1}")
            # else:
            #     print("Palavra não encontrada.")

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