# Identify shapes on gray scale image
=============
# Steps to try 

### 1 Local build
```bash
sudo docker-compose -f local.yml build
```

### 2 run docker with cv2 algorithm (Important, only work with BIN extension)
With this command you can test with the default image with default method 'cv2'. With this version if a pixel has a pixel with the same color in diagonal is part of the same shape

This algorithm maybe throw false positives when the shape evaluated has a different color shape bigger around it, this because of Euclidean distance says that closer color is the other shape.

![Test Image ](https://github.com/SPLAYER-HD/ImageDetect-Colors-Shapes/blob/master/resources/shades-of-grey.png)

The shape by default is 256,256 but if you want to change it, you can use the environment variable called SHAPE how you can see in the example

```bash
sudo docker run -e "SHAPE=255,255"  shapes_local/diego:v1
```

### 3 run docker with other images (Important, only work with "bin" extension)
You have to create a folder called resources, put the images into it and from a previous folder run this command:
(you can change the image name with the environment variable called IMAGE)

```bash
sudo docker run -v $pwd:/resources -e "IMAGE=sample.bin" shapes_local/diego:v1
```

### 4 run docker with my own algorithm (Important, only work with tiny images)
This algorithm use recursion to find in every neighbor if belongs to the same color so for that reason is very heavy and with normal or big images doesn't work for memory. With this version if a pixel has a pixel with the same color in diagonal is part of other shape

![Test small Image ](https://github.com/SPLAYER-HD/ImageDetect-Colors-Shapes/blob/master/resources/small-shades-of-grey.png)

```bash
sudo docker run -e "METHOD=diego" shapes_local/diego:v1
```

# TO DO
improve catch errors
