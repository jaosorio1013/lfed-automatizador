import pymupdf


def generar_planimetria(original_file, unused_pages: int, ciudad, cliente, diseno):
    # original_file = 'planimetria-inicial.pdf'
    final = './planimetria_paginada/' + original_file.name
    doc = pymupdf.open(original_file.path) # open a document


    # unused_pages = 1
    current_page = 1
    number_of_pages = len(doc)
    total_pages_with_number = number_of_pages - unused_pages
    pagination_position = pymupdf.Point(1485, 1145)  # start point of 1st line


    # ciudad = 'El retiro'
    # cliente = 'Camilo y Valentina'
    # diseno = 'Apartamento Wood'

    diseno_position = pymupdf.Point(370, 1145)
    ciudad_position = pymupdf.Point(655, 1145)
    cliente_position = pymupdf.Point(880, 1145)


    def insert_text_on_position(page, text, position, fontsize = 25):
        page.insert_text(
            position,
            text,
            fontname = "helv",
            fontsize = fontsize,
            rotate = 0,
        )


    for page in doc: # iterate the document pages
        if current_page > unused_pages:
            pagination_text = str(current_page - unused_pages) + ' / ' + str(total_pages_with_number)

            insert_text_on_position(page, pagination_text, pagination_position, 35)
            insert_text_on_position(page, cliente, cliente_position)
            insert_text_on_position(page, ciudad, ciudad_position)
            insert_text_on_position(page, diseno, diseno_position)

            print(pagination_text)

        current_page += 1

    doc.save(final)