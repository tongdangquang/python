import qrcode
from PIL import Image
qr = qrcode.QRCode(version = 5, error_correction = qrcode.ERROR_CORRECT_M, box_size = 5, border = 3)
qr.add_data("Tống Đăng Quang")
qr.add_data("https://www.facebook.com/profile.php?id=100045553913440-and")
qr.add_data("-https://github.com/tongdangquang")
# lưu ý: chỉ có thể đưa link vào trong add_data()
qr.make(fit = True)
img = qr.make_image(fill_color = "black", back_color = 'white')
img.save("name qrcode.png")