import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the previous color image:
I = cv2.imread('matting1.jpg')
I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)/255
n_rows = I.shape[0]
n_cols = I.shape[1]
n_pixels = n_rows * n_cols
I = np.reshape(I, (n_pixels, 3))

# Load exact matte:
alpha_ex = cv2.imread('matting2.jpg', cv2.IMREAD_GRAYSCALE)/255
alpha_ex = np.reshape(alpha_ex, (n_pixels, 1))

# Generate a version with a green screen:
G_B = 1
I = alpha_ex * I + (1 - alpha_ex) * [0, G_B, 0]
I = np.reshape(I, (n_rows, n_cols, 3))
plt.imshow(I), plt.axis('off'), plt.show();

# RGB components:
R_I = I[:, :, 0]
G_I = I[:, :, 1]
B_I = I[:, :, 2]

# Coefficients:
a_0 = 0
a_1 = 0.5
a_2 = 0

# Compute alpha with formula:
alpha = (B_I - a_1*(G_I - G_B) - a_2*R_I)/(a_0 + a_1*G_B)
alpha[alpha < 0] = 0
alpha[alpha > 1] = 1
plt.imshow(alpha, cmap='gray'), plt.axis('off'), plt.show();

# Compute relative error with exact alpha:
alpha = np.reshape(alpha, (n_pixels, 1))
error = np.linalg.norm(alpha - alpha_ex)/np.linalg.norm(alpha_ex)
print(f'Error (alpha): {error:.2e}')

# Load background K:
K = cv2.imread('matting5.jpg')
K = cv2.cvtColor(K, cv2.COLOR_BGR2RGB)/255
K = K[:n_rows, :n_cols, :]
K = np.reshape(K, (n_pixels, 3))

# Compute new image J with background K:
alpha = np.reshape(alpha, (n_pixels, 1))
R_I = np.reshape(R_I, (n_pixels, 1))
B_I = np.reshape(B_I, (n_pixels, 1))
G_I = np.reshape(G_I, (n_pixels, 1))
tmp = np.minimum(G_I, (B_I - a_0*alpha - a_2*R_I)/a_1)
J = np.concatenate((R_I, tmp, B_I), axis=1) + (1 - alpha)*K
J[J < 0] = 0
J[J > 1] = 1
J = np.reshape(J, (n_rows, n_cols, 3))
plt.imshow(J), plt.axis('off'), plt.show();




"""
import matplotlib.pyplot as plt
import cv2, os , glob
import numpy as np
from skimage.feature import local_binary_pattern
import scipy
from scipy.stats import chisquare

img = cv2.imread('433.png',cv2.IMREAD_GRAYSCALE)
img_lbp = local_binary_pattern(img, 4, 3, method='uniform')
histogram = cv2.calcHist([ np.float32(img_lbp) ],[0],None,[256],[0,256])
# 1.read images
image = []
lbp_image = []
lbp_hist = []
img_dir = "att/"
data_path = os.path.join(img_dir, '*g')
files = glob.glob(data_path)
for f in files:
    img = cv2.imread(f , cv2.IMREAD_GRAYSCALE)
    image.append(img)
    lbp = local_binary_pattern(img, 4, 3, method='uniform')
    lbp_image.append(lbp)
chi_img = []
for i in range(5,500):
    chi = chisquare(lbp_image[i])
    chi_img.append(chi)
print(chi_img)

sorted_chi = chi_img.sort()
print(len(sorted_chi))


# Calc Histogram
from skimage.feature import multiblock_lbp
from skimage.feature import draw_multiblock_lbp
from skimage.transform import integral_image


test_img = integral_image(img)
#lbp_img = multiblock_lbp(test_img , 0 , 0 , int(len(img)/3) , int(len(img[0])/3))
#imag = draw_multiblock_lbp(img, 0, 0, int(len(img)/3) , int(len(img[0])/3) , lbp_code=lbp_img, alpha=0.5)
#plt.imshow(img)
#plt.show()
"""

"""
img_lbp = local_binary_pattern(img, 4, 3, method='uniform')
histogram = cv2.calcHist([ np.float32(img_lbp) ],[0],None,[256],[0,256])
#histogram = cv2.compareHist(histogram,histogram, cv2.HISTCMP_CORREL)
print('histogram of first image: ',histogram)

# 1.read images
image = []
lbp_image = []
lbp_hist = []
img_dir = "att/"
data_path = os.path.join(img_dir, '*g')
files = glob.glob(data_path)
for f in files:
    img = cv2.imread(f , cv2.IMREAD_GRAYSCALE)
    image.append(img)
    lbp = local_binary_pattern(img, 4, 3, method='uniform')
    lbp_image.append(lbp)

print('length of the images: ',len(lbp_image))

for i in range(5,500):
    hist = cv2.calcHist([ np.float32(lbp_image[i]) ], [0], None, [256], [0, 256])
    hist = cv2.compareHist(histogram, hist, cv2.HISTCMP_CORREL)
    lbp_hist.append(hist)

    #plt.hist(hist)
    #plt.title('LBP histogram')
    #plt.show()

print('histogram of lbp images:', lbp_hist)
sorted_hist = sorted(lbp_hist)
print('sorted histogram of lbp images: ',sorted_hist)

print('size of histogram: ',len(lbp_hist))
print('size of sorted hist: ',len(sorted_hist))
keys_hist = []
for i in range(0,10):
    for j in range(len(lbp_hist)):
        if sorted_hist[i] == lbp_hist[j]:
            keys_hist.append(j)
            print(j)
        else:
            print('it doesnt match')

print('this is the key of matched images: ',keys_hist)


from sklearn import metrics
predicted = [1,2,3,4,5,2,6,7,8,7]
actual = [9,9,9,9,9,9,9,9,9,9]
confusion_matrix = metrics.confusion_matrix(actual, predicted)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])
cm_display.plot()
plt.show()
"""