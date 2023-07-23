import gdown                                                                 # Libreria para bajar un archivo de google drive

# Install gdown in Arch

# git clone https://aur.archlinux.org/gdown.git
# cd gdown
# makepkg -si

# Direccion donde se encuentra
url = "https://drive.google.com/uc?id=1l_5RK28JRL19wpT22B-DY9We3TVXnnQQ"
output = "fcn8s_from_caffe.npz"
gdown.download(url, output, quiet=False)
