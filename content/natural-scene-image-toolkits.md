Title: 自然场景实验材料处理工具
Date: 2015-4-23
Category: Psychology
Tags: Golang, Psychology
Slug: natural-scene-image-toolkits
Authors: rainy
Keywords: Natural scene, Golang, 心理学实验工具包
Description:以自然场景图像作为实验材料，通常需要每一试次都采用陌生图片，因此每个类别都需要几百上千张实验图片。从下载收集到筛选再到统一尺寸，这工作量当然是由计算机完成最合适。本来会用 Python+OpenCV 处理，但是最近迷上 Golang，以前觉得 Python 的代码块比 `{}` 干净又便捷，但是用过 `goimports & gofmt` 之后，就再也回不去了，享受闭上眼睛写代码的快感吧 :P
Summary:以自然场景图像作为实验材料，通常需要每一试次都采用陌生图片，因此每个类别都需要几百上千张实验图片。从下载收集到筛选再到统一尺寸，这工作量当然是由计算机完成最合适。本来会用 Python+OpenCV 处理，但是最近迷上 Golang，以前觉得 Python 的代码块比 `{}` 干净又便捷，但是用过 `goimports & gofmt` 之后，就再也回不去了，享受闭上眼睛写代码的快感吧 :P

### 0. About

以自然场景图像作为实验材料，通常需要每一试次都采用陌生图片，因此每个类别都需要几百上千张实验图片。从下载收集到筛选再到统一尺寸，这工作量当然是由计算机完成最合适。本来会用 Python+OpenCV 处理，但是最近迷上 Golang，以前觉得 Python 的代码块比 `{}` 干净又便捷，但是用过 `goimports & gofmt` 之后，就再也回不去了，享受闭上眼睛写代码的快感吧 :P

### 1. 采集

主要有两个图片库：[ImageNet](http://image-net.org/) & [SUN](http://groups.csail.mit.edu/vision/SUN/)，其中ImageNet是Fei-Fei大婶的[TED演讲](http://www.ted.com/talks/fei_fei_li_how_we_re_teaching_computers_to_understand_pictures)中推荐的，膜拜Orz…

SUN 整个下载下载有40G左右，ImageNet 只给想要类别的图片链接，需要自己下载，这个代码就不放了。

### 2. 筛选

ImageNet 大部分图片来自 flickr ，图片内容是否可用只能手动筛选，但可以排除一些下载失败、文件太小、尺寸太小的图片([See filter.go](https://github.com/ZJU-Psy/natural-scene-image-toolkits/blob/master/filter.go?ts=2))。

### 3. 统一尺寸

呈现时必须以相同的尺寸，按照目标尺寸进行缩放时需要先通过裁减得到与目标相同宽高比的图像，否则会变形([See shoes.go](https://github.com/ZJU-Psy/natural-scene-image-toolkits/blob/master/shoes.go?ts=2)):

```go
import  "github.com/oliamb/cutter"
func crop(pathsrc, pathdest string) image.Image {
  file, err := os.Open(pathsrc)
  if err != nil {
    log.Fatal(err)
  }
  // decode jpeg into image.Image
  img, err := jpeg.Decode(file)
  if err != nil {
    log.Fatal(err)
  }
  file.Close()
  ow, oh := img.Bounds().Max.X, img.Bounds().Max.Y
  if ow/oh > *WIDTH / *HEIGHT {
    ow = int(float64(*WIDTH) / float64(*HEIGHT) * float64(oh))
  } else {
    oh = int(float64(*HEIGHT) / float64(*WIDTH) * float64(ow))
  }
  croped, _ := cutter.Crop(img, cutter.Config{
    Width:   ow,
    Height:  oh,
    Options: cutter.Copy,
  })
  if pathdest != "" {
    out, err := os.Create(pathdest)
    if err != nil {
      log.Fatal(err)
    }
    defer out.Close()

    // write new image to file
    jpeg.Encode(out, croped, nil)
  }
  return croped
}
```

然后进行缩放：

```go
func scale(img image.Image, dest string) error {
  m := resize.Resize(uint(*WIDTH), uint(*HEIGHT), img, resize.Lanczos3)
  out, err := os.Create(dest)
  if err != nil {
    log.Fatal(err)
  }
  defer out.Close()

  // write new image to file
  jpeg.Encode(out, m, nil)

  return nil
}
```

### 4. 中文词库

需要（大量）指定类别的中文词汇，如动物名称。首先考虑从搜狗输入法词库中提取，参考[搜狗词库转为txt格式（小小输入法）](http://blog.csdn.net/zhangzhenhu/article/details/7014271)，稍加改动，只保留两个字的词汇([See sougou-dict.py](https://github.com/ZJU-Psy/natural-scene-image-toolkits/blob/master/sougou-dict.py?ts=2))。从[搜狗输入法词库](http://pinyin.sogou.com/dict/)下载需词汇类别，然后：

```shell
$ python sougou-dict.py animal.scel
```

### 5. 待...
