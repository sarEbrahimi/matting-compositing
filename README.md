# matting-compositing
first lests see the difference between matting and composing
 adding an alpha channel 
 <h3>why fractional alpha?</h3>
![Screenshot from 2023-07-25 07-29-48](https://github.com/sarEbrahimi/matting-compositing/assets/94298181/2c7f1e52-d9ff-44e5-a7e0-d2bafc8220db)
   
1.cause of the thin features  (e.g. hair) it is practical

![Screenshot from 2023-07-25 07-32-17](https://github.com/sarEbrahimi/matting-compositing/assets/94298181/9a02b5cd-0094-4b37-b2d5-61d8c4b721fe)

2.Motion blur “smears” foreground into background

![Screenshot from 2023-07-25 07-38-51](https://github.com/sarEbrahimi/matting-compositing/assets/94298181/c6e77f3a-5d91-444e-b9b9-878829b83032)

<h1>compositing</h1>
Given the foreground color F=(Fr, Fg, Fb), the
background color (Br, Bg, Bb) and  for each pixel
The compositing operation is: C=aF+(1-a)B
![Screenshot from 2023-07-25 07-43-51](https://github.com/sarEbrahimi/matting-compositing/assets/94298181/1775ca06-86c7-4c0c-bd51-96b8bf620283)

<h1>Matting problem</h1>
• Inverse problem:
Assume an image is the composite of a foreground
and a background
• Given an image color C, find F, B and  so that
C=aF+(1-a)B
![Screenshot from 2023-07-25 07-48-56](https://github.com/sarEbrahimi/matting-compositing/assets/94298181/2ea9e0e6-dd92-43f9-8e15-10e2b2f0c2b7)
