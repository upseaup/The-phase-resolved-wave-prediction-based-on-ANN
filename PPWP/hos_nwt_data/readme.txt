here is data obtained by HOS-NWT. 
We obtain the npy file through the probe file.
It should be noted that the data dt here is 0.01 s (scale model).
We apply the subsampled to make dt = 0.05s in npy file.
The specific settings can be referred to in the paper.
Considering that the scaling ratio is 64, in the npy file, dt=0.05 * 8=0.4 (full model)


# 具体设置可以见论文。需要注意的是 这里的数据的dt = 0.01(scale model) 我们需要每5个点采集一次，这是dt=0.05(scale model), 考虑到缩尺比是64，
# npy文件中dt=0.05*8=0.4(full model)
# 处理了什么给出来 如何处理的给出来 主要是处理不同的采样频率 以及如何去掉头部的数据的 想下其实不用说为啥去点后面的一部分吧，只说去了前一部分就行。
# 以及需要给出prob文件 这样别人好设置你的参数 。论文中是给出了的 
# 给出高阶谱的网站 

# 最后文章发表后 应该在readme中 提出一如果使用本程序 应该引用oe哪片论文
