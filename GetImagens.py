import fitz
import os

class DownloadImagens:
    def __init__(self):
        self.pdf_path = ["ab.pdf","cj.pdf", "bb.pdf", "bp.pdf", "bt.pdf", "mb.pdf", "gb.pdf", "corrente.pdf", "ibp.pdf"] 
        self.output_folder = "./imagens"

    def GetImagens(self):
        os.makedirs(self.output_folder, exist_ok=True)

        for file in self.pdf_path:
            doc = fitz.open(file)
            for page_num, page in enumerate(doc, start=1):
                
                text_near_image = page.get_text("text").replace(" ", "").split()
                text_list = text_near_image[2:]

                print("Numero da Pagina",page_num)
                print(text_list)

                images = []  

                for img_index, img in enumerate(page.get_images(full=True), start=1):
                    img_name = img[7] 
                    img_index_num = int(img_name.replace("Im", "").replace("age",""))
                    images.append((img_index_num, img))

                images.sort(key=lambda x: x[0])

                count = 0
                for img_index, img in images:
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    ext = base_image["ext"]

                    img_filename = f"image_{text_list[count]}.{ext}"
                    img_filepath = os.path.join(self.output_folder, img_filename)
                   

                    with open(img_filepath, "wb") as img_file:
                        img_file.write(image_bytes)
                        print("Salvando : -> " + img_filepath)

                    count +=1  

                print("-------")

downloadImagens = DownloadImagens()
downloadImagens.GetImagens()