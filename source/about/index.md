---
title: Introduction
date: 2023-04-17 18:48:35
---

# Introduction

<img src="/images/Subject.png" width="25%" align=left>


During my undergrad years,I participated in the ACM algorithm training camp in my freshman year. However, influenced by the movie Iron Man, I became deeply interested in developing an advanced HCI system. I first delved into gesture recognition technology and, with the help of a sensor, completed a national-level college student innovation and entrepreneurship project, winning a series of awards. In my junior year, I began leading a research group of ten people, expanding our research areas to include [VR](https://v.youku.com/v_show/id_XMjY5MjU1OTY1Ng==.html), [AR](https://v.youku.com/v_show/id_XMTUwNDM2ODk0OA==.html), HoloLens (MR), and 3D engines (CG). Eventually, the research group received national funding to establish an HCI lab, which continues to produce project results annually. At the end of my undergrad studies, I received a recommendation from [Andreas Butz](http://www.medien.ifi.lmu.de/team/andreas.butz/), the Dean of the CS Department at the University of Munich, to pursue a master's degree at [TUM](https://www.tum.de/en/). However, I declined for personal reasons.

****
In the first few years of my career, I focused on the application of computational geometry, deep neural networks, and CV in the field of remote sensing, and gained extensive experience in GIS system integration and development. In my spare time, I developed an open-source project called [Darth(PyPI Package)](https://pypi.org/project/d-arth/) that supports global data sampling. This project helped my first company train one of the best remote sensing building recognition models in China.
****
In recent years, I realized the intrinsic logic of CV development and shifted my focus to autonomous driving, accumulating a wealth of experience in L2-level perception fusion. The publication of GPT-related papers made me aware of the immense potential of large models in command orchestration, so I began adapting to this change and switched to the field of robotics. In practice, I learned about relevant architectural design and eventually explored a prototype of a natural language-based robot control framework. Thus, after years of technical accumulation, I have gained substantial experience in CV algorithms, GIS algorithm development, and autonomous driving perception fusion. I am extremely passionate about foundational technologies related to perception, multimodality, and large models, and I am enthusiastic about the fields of autonomous driving and robotics.

****

# Contact information
* Tel：+8613146420628
* E-mail: tanwenxuan@live.com
* E-mail: tomwinshare@gmail.com





# LANGUAGE 

* ENGLISH : IELTS 6.0

# SKILLS

* Programming Languages : C++/Python

* Deep Learning Frameworks : PyTorch / (TensorRt ONNX Deployment)
  
* Robotics Perception and Computer Vision Algorithms

* GPU Programming : CUDA

* Max Team Management Experience : 10 people in collage / 3 people in work.

 
 
 
 
 
 
# EXPERIENCE 

### AgiBot (ZHIYUAN) | Senior Perception Algorithm Engineering 2023.Feb - ｜Shanghai

At this stage, I am focusing on developing a foundational perception scheme and a natural language-based command framework for humanoid robots. First, I have completed validation work based on the GPT-3.5 API and a series of distilled models similar to BELLE-7B, LORA, etc., demonstrating the potential of large models in basic task orchestration. Second, I have developed a basic demo in Unity3D that can convert basic natural language instructions into robotic arm movements, such as using natural language commands to control a robotic arm to grab specific obstacles in a simulated environment. Next, I have validated the perception models required for the entire basic instruction set, such as a VIT+Multi Head multitask network that can leverage Imagenet pre-trained models + MLP/MAP structures to simultaneously perform graspable area segmentation and referential expression tasks. Building on this work, I have designed an instruction architecture system that decomposes commands at different levels, combining IK inverse kinematics hard coding, reinforcement learning, MLP direct output, and large-scale model multi-level instruction sequence fusion to achieve a universal foundational framework for controlling mechanical devices using natural language.

****
### DIDI TECHNOLOGY Autopilot Team | Image Algorithm Expert 2021.Jul - 2023.Feb | Beijing 
 

### Autonomous Driving Perception Fusion System 

During autopilot team time, my primary focus is on implementing a Level 2 perception fusion system. The key submodules encompass multi-object tracking, appearance feature extraction networks, obstacle feature fusion, deterministic matching algorithms, and Kalman filtering. In the initial phase, I independently developed the PerceptionHub Python scheduling framework, which streamlines the integration of each module. Ultimately, using configurable scheduling, I successfully connected the entire perception fusion decision-making process, demonstrating the technical viability of the complete chain. In subsequent stages, my primary tasks revolved around employing the Bazel framework for the C++ implementation of the perception fusion components, conducting appearance feature ONNX/TensorRT model inference using C++, and optimizing relevant corner cases.
 


### DIDI TECHNOLOGY | Computer Vision Engineer 2020.Dec - 2021.Jul | Beijing 

#### Automatic Clipping Service 

Using a saliency detection network, I segmented the main semantic region of images from the background semantic region. I re-implement SOD100k and u2Net networks and ultimately achieved 89% accuracy with the annotated dataset Fineturn. By using a series of post-processing algorithms with edge optimization, the service was integrated into the e-commerce image processing workflow, significantly improving design work efficiency.


#### Universal OCR Service 

As a single developer, I implemented an end-to-end general online OCR service based on detection+classification+recognition using CRNN. The service was developed using public pre-trained models. Due to the application scenarios, I improved the sliding window strategy and adopted a unified coordinate conversion+NMS algorithm. In business scenarios, testing found that the final error rate was half that of Baidu's competing interface, and the inference time increased by 30%. To date, the service has been accessed billions of times.

****
 
### TerraQuanta | Computer Vision Engineer | 2020.Feb - 2020.Jul ｜ Beijing
 
#### Remote Sensing Image Data Set Component
 
Remote sensing image data is vast, and improving the performance of remote sensing image neural network models requires increasing the annotation volume, which is extremely costly. Map surveying and mapping providers have a large amount of vector geo-object data. This component can obtain more than 20 types of global data products and rasterize local vector data into ground truth. Combining this component with remote sensing image processing models enables global data sampling training, significantly reducing the cost of model expansion and generalization capabilities.

****

### GAGO LTD | Computer Vision Engineer | 2018.Jan - 2020.Jan | Beijing

#### Target Object Tracking and Analysis System

Detection and tracking of specified target objects in video stream frames, recording the motion curve, activity range, and position distribution of the target. Regression analysis is performed based on these data, and traditional machine learning algorithms are used to analyze related data to derive the possibility of target object lesions and changes in physical conditions. This system serves the smart breeding industry.

#### Field Partition Algorithm 

The boundary division of TB-level remote sensing images has always relied on manual labor, which results in low efficiency and high cost. The automated target vectorization algorithm for remote sensing images has been an urgent problem to be solved. In the special case of field boundary division, the performance of machine learning solutions is greatly reduced. After eight months of continuous attempts, I completed the real-time field boundary vectorization algorithm independently. With qualified quality images, the accuracy rate is slightly lower than the manual level, but the efficiency has increased by 300%.


#### Disaster Relief Center Disaster Relief Resource Deployment System 

Faced with sudden earthquake information, once the intensity is sufficient to cause damage, the system automatically loads satellite images, DEM information, and intensity information before and after the earthquake for the corresponding latitude and longitude. Landslide detection and building detection are performed. Based on the population/building density and landslide-prone areas as weights, rescue forces are deployed in corresponding regions, and different types of rescues are planned according to professional knowledge to reach suitable locations. EfficientNet was used as the backbone network, and the feature vectors were recombined, enabling the combination of DEM feature vectors and other feature vectors to fit the probability of a single-point earthquake outbreak. OpenSource Info : https://github.com/OOXXXXOO/Efficient-landslide
# PAGE&PROJECTS 
### Git:
https://github.com/OOXXXXOO

### Neural Network Research Toolkit WSNets: 
https://github.com/OOXXXXOO/WSNet

### The Satellite Imagery DataSet Toolkit:
 https://github.com/OOXXXXOO/DARTH (Pip Package: https://pypi.org/project/d-arth/)

### LandSlide Prediction Algorithm

https://github.com/OOXXXXOO/Efficient-landslide

# EDUCATION 
* Bachelor of Software Engineering | 2013 - 2017 Southwest Minzu University | China-Chengdu

# PATENTS
* "A Space Scanning System and Its Working Method Based on Unmanned Aerial Vehicle and Structured Light Scanning Technology" (Granted) 

* "Array-based Structured Light Large Space Motion Recognition System" (Under Review)
* "A Method and Device for Counting the Number of Target Objects in a Region" (Granted) 
* "An Image Vectorization Method, Device, Electronic Device, and Medium" (Granted)

# AWARDS

* LeapMition Development Competition, Outstanding Award 
* Excellent National College Students Innovation and Entrepreneurship Projects x4 
* Sichuan Province Computer Works Competition - First Prize x3, Special Prize x1 
* 3D Model Display System Based on Binocular Sensors - Second Prize, China Computer Works Competition (Macau) 
* Home Design System Based on Virtual Reality and Gesture Recognition MSRA MPC Hackathon (Beijing) - 7th Place 
* Projection Touch System Based on TOF Sensor 2016, 2017 China College Students Innovation and Entrepreneurship Annual Conference (Xiamen, Dalian) 
* "Implementation of Fluid Simulator Based on CUDA Parallel Computing" - Outstanding Graduation Thesis
* Microsoft Hackthon-Cargil (Shanghai) - First Place
