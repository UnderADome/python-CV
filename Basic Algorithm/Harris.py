from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters

#角点响应器，返回反馈值R
def compute_harris_response(im, sigma=3):
    #计算导数
    imx = zeros(im.shape)
    filters.gaussian_filter(im, (sigma, sigma), (0, 1), imx)
    imy = zeros(im.shape)
    filters.gaussian_filter(im, (sigma, sigma), (1, 0), imy)

    #计算Harris矩阵的分量
    Wxx = filters.gaussian_filter(imx*imx, sigma)
    Wxy = filters.gaussian_filter(imx*imy, sigma)
    Wyy = filters.gaussian_filter(imy*imy, sigma)

    #计算特征值和矩阵的迹
    Wdet = Wxx*Wyy - Wxy**2
    Wtr = Wxx + Wyy

    return Wdet/Wtr

#返回角点
#threshold预设的阈值
#min_dist分割焦点和图像边界的最少像素数目
def get_harris_points(harrisim, min_dist=10, threshold=0.1):
    #寻找高于阈值的候选角点
    corner_threshold = harrisim.max() * threshold
    harrisim_t = (harrisim > corner_threshold) * 1
    
    #得到候选点的坐标
    coords = array(harrisim_t.nonzero()).T

    #候选点的Harris响应值
    candidate_values = [harrisim[c[0], c[1]] for c in coords]

    #对候选点按照Harris响应值进行排序
    index = argsort(candidate_values)

    #将可行点的位置保存到数组中
    allowed_locations = zeros(harrisim.shape)
    allowed_locations[min_dist:-min_dist, min_dist:-min_dist] = 1

    #按照min_distance原则，选择最佳Harris点
    filtered_coords = []
    for i in index:
        if allowed_locations[coords[i, 0], coords[i, 1]] == 1:
            filtered_coords.append(coords[i])
            allowed_locations[(coords[i,0] - min_dist) : (coords[i,0] + min_dist), 
                (coords[i,1] - min_dist) : (coords[i,1] + min_dist)] = 0
    
    return filtered_coords

#绘制图像中检测到的角点
def plot_harris_points(image, filtered_coords):
    figure()
    gray()
    imshow(image)
    plot([p[1] for p in filtered_coords], [p[0] for p in filtered_coords], "+")
    axis('off')
    show()


im = array(Image.open('test.jpg').convert('L'))
harrism = compute_harris_response(im)
filtered_coords = get_harris_points(harrism, 6)
plot_harris_points(im, filtered_coords)

