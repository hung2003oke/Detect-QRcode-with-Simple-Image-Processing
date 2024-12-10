import qrcode

def create_qrcode(data_qrcode):
    qr = qrcode.QRCode(version=1,
                       box_size=10,
                       border=5)

    # Adding data to the instance 'qr'
    qr.add_data(data_qrcode)

    qr.make(fit=True)
    img = qr.make_image(fill_color='black',
                        back_color='white')

    img.save('MyQRCode2.png')
    return img
h='345678'

create_qrcode(h)

