---
layout: post
subtitle: pick most used colors
categories: [JavaScript]
header:
    image: header.jpg
    align:
    text: light
---

since the image of foreground color and background color we could not determinate before publish. It might be some dynamic setup by real pictures. So that is a way to read the most frequent color value as the main background color, and we can do some special effect to improve user experiences.

An example of JavaScript code below:

```javascript
function getColorList(pixelData) {
            let colorList = [];
            let rgba = [];
            let rgbaStr = '';
            let arr = [];
            for (let i = 0; i < pixelData.length; i += 4) {
                rgba[0] = pixelData[i];
                rgba[1] = pixelData[i + 1];
                rgba[2] = pixelData[i + 2];
                rgba[3] = pixelData[i + 3];

                if (rgba.indexOf(undefined) !== -1 || pixelData[i + 3] === 0) {
                    continue;
                }

                rgbaStr = rgba.join(',');
                if (rgbaStr in colorList) {
                    ++colorList[rgbaStr];
                } else {
                    colorList[rgbaStr] = 1;
                }
            }

            for (let prop in colorList) {
                arr.push({
                    color: `rgba(${prop})`,
                    count: colorList[prop],
                });
            }

            arr.sort((a, b) => {
                return b.count - a.count;
            })
            return arr;
        }

        function getMainColor(image) {
            return new Promise((resolve, reject) => {
                try {
                    const canvas = document.createElement("canvas");
                    const img = new Image();
                    img.src = image;
                    img.onload = () => {
                        const context = canvas.getContext('2d');
                        context.drawImage(img, 0, 0);
                        let pixelData = context.getImageData(0, 0, canvas.width, canvas.height).data;
                        resolve(pixelData);
                    }
                } catch (error) {
                    reject(error);
                }
            });
        }

        getMainColor('./liting.jpg')
            .then(res => { console.log('The most used color: ', getColorList(res)[0]) })

```

