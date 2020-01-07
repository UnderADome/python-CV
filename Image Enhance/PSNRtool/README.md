# PSNR(峰值信噪比)
一种评价图像的客观标准，一般是用最大值信号和背景噪音做对比；原始图像的峰值信噪比为0。
PSNR是最普遍、最广泛使用的评价画质的客观测量方法，但是PSNR的分数无法和人眼看到的视觉品质完全一致。有可能PSNR分数较高但是视觉效果反而差于PSNR分数低的图像。
这种现象也是因为人眼对于误差的敏感度并不是绝对的而造成的，人感知的结果会受到许多因素的影响而产生变化（eg：人眼对空间频率较低的对比差异敏感度较高，人眼对亮度对比差异的敏感度较色度高，人眼对一个区域的感知结果会受到其周围邻近区域的影响）

>参考：<br/>
https://github.com/magonzalezc/PSNRtool    <br/>
https://baike.baidu.com/item/psnr#2


>PSNR和SNR：<br/>
https://www.cnblogs.com/qrlozte/p/5340216.html     <br/>
https://blog.csdn.net/Aoulun/article/details/79007902         <br/>
https://blog.csdn.net/lien0906/article/details/30059747      

<br/>

# PSNRtool

This is a python PSNR calculator tool

## How to install (Linux)

1. Install Python 3.5 if you dont have it in your computer.

2. Open a new terminal and type:

  ```
  # apt-get install python3-pip
  # pip3 install numpy
  # pip3 install pillow
  ```

3. Go to the path where example.py is and execute it with the command:

  ```
  python3 main.py path_original_image path_encoded_image
  ```


## Example

  python3 main.py ./lena.bmp ./lenadec.bmp
