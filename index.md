---
layout: class
title: "CSCI 467: Introduction to Machine Learning"
semester: Spring 2025
time: Tuesdays and Thursdays at 3:30-4:50pm
location: DMC 100
location_link: "https://maps.usc.edu/?id=1928&reference=DMC"
section_time: Fridays at 3:00-3:50pm
section_location: SOS B4 
section_location_link: "https://maps.usc.edu/?id=1928&reference=SOS"
instructor: Robin Jia
order: 1
---
<div class="row" markdown=1>
<div class="col-pic" markdown=1>
![xkcd Tasks](https://imgs.xkcd.com/comics/tasks.png)
Source: [xkcd](https://xkcd.com/1425/)
</div>
<div class="col-intro" markdown=1>

{% capture hw0 %}{% include hw.html num=0 %}{% endcapture %}
{% capture hw1 %}{% include hw.html num=1 %}{% endcapture %}
{% capture hw2 %}{% include hw.html num=2 %}{% endcapture %}
{% capture hw3 %}{% include hw.html num=3 %}{% endcapture %}
{% capture hw4 %}{% include hw.html num=4 %}{% endcapture %}


**Quick Links:**
* **[Lecture Notes](/assets/notes.pdf)**
* **[OneNote Notebook of Handwritten Lectures](https://1drv.ms/o/c/c7647f7ae642c6ff/EqrGz7KAwT5FmAsI_XOp1kEBE_igRdKcaGZHDPEKGCIIyQ?e=yQGf3Z)**
* **[LaTeX Template for Homework Submissions](https://www.overleaf.com/read/kjvpshdfvwsd#593bd8)**
* **[Final Project information](project)** 

**News:** 
* Homework 4 has been released {{ hw4 | strip_newlines }}. It is due **Thursday, May 1**.
* We have released three practice midterm exams: Midterm 1 ([problems](/assets/exams/midterm_1.pdf), [solutions](/assets/exams/midterm_1_solutions.pdf)), Midterm 2 ([problems](/assets/exams/midterm_2.pdf), [solutions](/assets/exams/midterm_2_solutions.pdf)), and Midterm 3 ([problems](/assets/exams/midterm_3.pdf), [solutions](/assets/exams/midterm_3_solutions.pdf)).
* If you want to review prerequisite material for this class, I have a list of recommended [resources](#resources) below.

Some problems in computer science admit precise algorithmic solutions.
Checking if someone is in a national park is, in some sense, straightforward:
get the user's location,
get the boundaries of all national parks,
and check if the user location lies within any of those boundaries.

Other problems are less straightforward.
Suppose you want your computer to determine if an image contains a bird.
To your computer, an image is just a matrix of red, green, and blue pixels.
How do you even begin to write the function `is_bird(image)`?

For problems like this, we turn to a powerful family of methods known as **machine learning.**
The zen of machine learning is the following:
1. I don't know how to solve my problem.
2. But I can obtain a **dataset** that describes what I want my computer to do.
3. So, I will write a program that **learns the desired behavior from the data.**

This class will provide a broad introduction to machine learning.
We will start with **supervised learning,** where our goal is to learn an input-to-output mapping given a set of correct input-output pairs. 
Next, we will study **unsupervised learning,** which seeks to identify hidden structure in data.
Finally, we will cover **reinforcement learning,** in which an agent (e.g., a robot) learns from observations it makes as it explores the world.

</div>
</div>

## Course Staff
<div class="staff-photo" markdown=1>
![Robin Jia](//robinjia.github.io/assets/images/profile.jpg)  
**Robin Jia**  
Instructor
</div>
<div class="staff-photo" markdown=1>
![Deqing Fu](//deqingfu.github.io/images/profile.jpg)  
**Deqing Fu**  
Teaching Assistant
</div>
<div class="staff-photo" markdown=1>
![Steven Shi](/assets/images/steven.jpg)  
**Steven Shi**  
Course Producer
</div>
<div class="staff-photo" markdown=1>
![Ryan Wang](/assets/images/ryan.jpg)  
**Ryan Wang**  
Course Producer
</div>
<div class="staff-photo" markdown=1>
![Alice Wei](/assets/images/alice.jpg)  
**Alice Wei**  
Course Producer
</div>

## Logistics
* **Office hours and drop-in peer mentoring**: See the calendar below or [here](https://calendar.google.com/calendar/embed?src=c_86e4982ab98a1b157f078d62c4489999c4833f08ae66003b169896dd26cca926%40group.calendar.google.com&ctz=America%2FLos_Angeles).
The instructor and TA's will have regular office hours every week.
Course producers will have drop-in peer mentoring sessions before each assignment is due.
<div class="center">
<iframe src="https://calendar.google.com/calendar/embed?src=c_86e4982ab98a1b157f078d62c4489999c4833f08ae66003b169896dd26cca926%40group.calendar.google.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
</div>
* **Assignments**: Assignments should be submitted through [Gradescope](https://www.gradescope.com/courses/945653). Feedback will also be provided on Gradescope. All enrolled students should be in Gradescope automatically--let me know if you are not!
You should submit both your PDF writeup and your code on Gradescope; there will be separate assignments for each.
* **Discussions**: We will be using Piazza for general course-related questions and announcements. 
All enrolled students were added at the beginning of the semester; you can also use this [sign-up link](https://piazza.com/usc/spring2025/csci467).
If you have an individual matter to discuss, email me directly (please put "CSCI 467" in the subject line) or come to my office hours. For grading questions, go to the office hours of the person who graded the problem in question.

## Prerequisites
* Algorithms: CSCI 270 
* Linear Algebra: MATH 225 
* Probability: EE 364 or MATH 407 or BUAD 310

This class will also use some basic multivariate calculus (taking partial derivatives and gradients).
However, knowledge of single-variable calculus is sufficient as we will introduce the required material during class and section. 

All programming assignments will be in Python.
Basics of Python will be covered in discussion sections.
Students who are not familiar with Python may need to spend some time becoming more familiar with it as needed.

## Schedule
All assignments are due by **11:59pm** on the indicated date.

|Date|Topic|Related Readings|Assignments|
|--|--|--|--|
|Tue Jan 14|Introduction ([slides](/assets/lectures/01_intro.pdf)) |PML 1| Homework 0 released {{ hw0 | strip_newlines }}
|Thu Jan 16|Linear Regression ([demo](https://colab.research.google.com/drive/11hdXd0C7GGrxpJlC-PV6eImcWJ3Bk_Q2)) |PML 7.8, 8.2|
|Fri Jan 17|Section: Review of Probability & Linear Algebra ([notes](https://hackmd.io/@charlotteTYC/prerequisites), [section](/assets/spring2024/sections/section1.pdf)) [](){: .schedule-section} | |
|Tue Jan 21|Featurization, Convexity |PML 2.6.3, 4.2, 8.1 ||
|Thu Jan 23|Maximum Likelihood Estimation, Logistic Regression |PML 10.1-10.3| **Homework 0 due** |
|Fri Jan 24|Section: Python & numpy tutorial ([demo](https://colab.research.google.com/drive/1DTjbgRrAuphcW5l8aw6h00wLuvJDdBFJ?usp=sharing)) [](){: .schedule-section} | | 
|Tue Jan 28|Overfitting, Regularization |PML 4.5, 4.7, 11.3-11.4 |
|Thu Jan 30|Bias and Variance, Normal Equations | PML 11.2| Homework 1 released {{ hw1 | strip_newlines }}
|Fri Jan 31|Section: Softmax Regression [](){: .schedule-section}| |
|Tue Feb 4 | Generative Classifiers, Naive Bayes ([slides](/assets/lectures/07_naivebayes.pdf))  |PML 9.3-9.4 |
|Thu Feb 6 |Nearest Neighbors, start of Kernels; Project discussion |PML 16.1, 16.3 |
|Fri Feb 7 |Section: Calculus and Gradients [](){: .schedule-section} | | 
|Tue Feb 11|Kernel methods continued ([visualization](https://www.youtube.com/watch?v=OdlNM96sHio)) |PML 4.3, 17.1, 17.3| **Homework 1 due** |
|Thu Feb 13|Introduction to Neural Networks ([slides](/assets/lectures/10_neuralnets.pdf)) |PML 13.1-13.2 | Homework 2 released {{ hw2 | strip_newlines }}
|Fri Feb 14|Section: Cross-Validation, Evaluation Metrics ([section](/assets/spring2024/sections/section4.pdf)) [](){: .schedule-section}| | 
|Tue Feb 18|Backpropagation ([lecture](/assets/lectures/11_backprop.pdf), demo [part 1](/assets/backprop/part1_forward_only.py), [part 2](/assets/backprop/part2_trees.py), [part 3](/assets/backprop/part3_dags.py)) |PML 13.3 | **Project Proposal due** |
|Thu Feb 20|Neural Network Optimizers, Dropout, Early Stopping ([slides](/assets/lectures/12_nnoptim.pdf)) | PML 8.4, 13.4-13.5|
|Fri Feb 21|Section: Pytorch tutorial ([colab](https://colab.research.google.com/drive/1BLD1Eic5yw3myxdDSnL6qgBIjawYCw-Y?usp=sharing)) [](){: .schedule-section}| | 
|Tue Feb 25|Convolutional Neural Networks ([slides](/assets/lectures/13_convnets.pdf))  |PML 14.1-14.2 |
|Thu Feb 27|Embedding models, Word Vectors ([slides](/assets/lectures/14_wordvec.pdf))  |PML 20.5|
|Fri Feb 28|Section: Sci-kit Learn tutorial ([colab](https://colab.research.google.com/drive/1WsH_gfVC7dIFtRtXNak0Lr2HR7ty4DPC?usp=sharing)) [](){: .schedule-section}| | 
|Tue Mar 4 |Recurrent Neural Networks ([slides](/assets/lectures/15_rnns.pdf)) |PML 15.1-15.2 |
|Thu Mar 6 |Sequence-to-sequence, Attention ([slides](/assets/lectures/16_attention.pdf)) |PML 15.4 | **Homework 2 due** |
|Fri Mar 7 |Section: Midterm preparation ([slides](https://docs.google.com/presentation/d/1MYLoavX6yNuRPu0QSIq9skEK5ypDdTIlYDddKmouHyE/edit?usp=sharing)) [](){: .schedule-section}| | 
|Tue Mar 11|Decision Trees, ensembles ([slides](/assets/lectures/17_trees.pdf)) |PML 18.1-18.5 | 
|Thu Mar 13|**In-class Midterm Exam** [](){: .schedule-exam} | | 
|Fri Mar 14|Section: Reading AlexNet paper ([link](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)) [](){: .schedule-section}| | 
|Mar 15-21 |No class or section (Spring break) [](){: .schedule-break}| |
|Tue Mar 25|Transformers I ([slides](/assets/lectures/18_transformers.pdf)) |PML 15.5-15.6| Homework 3 released {{ hw3 | strip_newlines }}
|Thu Mar 27|Transformers II, Pretraining ([slides](/assets/lectures/19_transformers2.pdf)) |PML 15.7 |
|Fri Mar 28|Section: RNNs and backpropagation in pytorch [](){: .schedule-section}| | 
|Tue Apr 1 |k-Means Clustering ([visualization](https://www.youtube.com/watch?v=5I3Ei69I40s)) | PML 21.3||
|Thu Apr 3 |Gaussian Mixture Models, Expectation Maximization | PML 21.4, PML2 8.1-8.2|
|Fri Apr 4 |Section: Reading Transformers paper ([link](https://arxiv.org/abs/1706.03762)) [](){: .schedule-section}| | **Project Midterm Report due** 
|Tue Apr 8 |Expectation Maximization for GMMs; Start Dimensionality Reduction |PML 20.1, 20.4 |
|Thu Apr 10|Finish Principal Components Analysis; start Multi-armed Bandits |PML2 34.1-34.4 ||
|Fri Apr 11|Section: Practical guide to pretrained deep learning models [](){: .schedule-section}| | 
|Tue Apr 15|Markov Decision Processes, Reinforcement Learning |PML2 34.5-34.6, 35.1, 35.4 |**Homework 3 due**| 
|Thu Apr 17|Q-Learning |PML2 35.2-35.3 | Homework 4 released {{ hw4 | strip_newlines }}
|Fri Apr 18|Section: Reading CLIP paper ([link](https://arxiv.org/abs/2103.00020))  [](){: .schedule-section}| |
|Tue Apr 22|Finishing RL; Adversarial Examples ([slides](/assets/lectures/26_adversarial.pdf)) |PML2 19.1-19.8 |
|Thu Apr 24|Spurious Correlations, Fairness in Machine Learning | FAML 1-4 | 
|Fri Apr 25|Section: Reading NeRF paper ([link](https://arxiv.org/abs/2003.08934)) [](){: .schedule-section}| 
|Tue Apr 29|How does ChatGPT work? | 
|Thu May 1 |Conclusion | | **Homework 4 due** |
|Fri May 2 |Section: Final Exam preparation [](){: .schedule-section}| | 
|Tue May 13|**Final Exam, 2-4pm** [](){:.schedule-exam} | | **Project Final Report due Thursday, May 8**|
{: .schedule #schedule-table}

## Grading
Grades will be based on homework assignments (40%), a class project (20%), and two exams (40%).

**Homework Assignments (40% total)**:
- Homework 0: 4%
- Homeworks 1-4: 9% each

**Final Project (20% total)**.
The final project will proceed in three stages:
- Project proposal: 2%
- Midterm report: 3%
- Final project report: 15%

**Exams (40% total)**:
- In-class midterm: 15% 
- Final exam (cumulative): 25%

### Late days
You have **6 late days** you may use on any assignment **excluding the Project Final Report.**
Each late day allows you to submit the assignment 24 hours later than the original deadline.
You may use a maximum of **3 late days per assignment.**
If you are working in a group for the project, submitting the project proposal or midterm report one day late means that **each member** of the group spends a late day.
We do not allow use of late days for the final project report because we must grade the projects in time to submit final course grades.

If you have used up all your late days and submit an assignment late, you will lose 10% of your grade on that assignment for each day late.
We will **not accept any assignments more than 3 days late.**


## Final project
The final project can be done individually or in groups of up to 3.
This is your chance to freely explore machine learning methods and how they can be applied to a task of our choice.
You will also learn about best practices for developing machine learning methods---inspecting your data, establishing baselines, and analyzing your errors.
More information about the final project is available [here](project). 
{::comment} More information will be released soon.{:/}

## Resources
I have written **[Lecture Notes](/assets/notes.pdf)** that accompany all the iPad lectures.
I recommend using these notes as reference material for studying.
There is no required textbook for this class.
If you do want to learn from a textbook, the following may be useful:
- [*Probabilistic Machine Learning: An Introduction*](https://probml.github.io/pml-book/book1.html) (PML) and [*Probabilistic Machine Learning: Advanced Topics*](https://probml.github.io/pml-book/book2.html) (PML2) by Kevin Murphy. You may also find PML Chapters 2-3 and 7 useful for reviewing prerequisites.
- [*The Elements of Statistical Learning*](https://hastie.su.domains/Papers/ESLII.pdf) by Trevor Hastie, Robert Tibshirani, and Jerome Friedman.
- [*Patterns, Predictions, and Actions: A Story about Machine Learning*](https://mlstory.org/) by Moritz Hardt and Benjamin Recht
- [*Fairness and Machine Learning: Limitations and Opportunities*](https://fairmlbook.org/) (FAML) by Solon Barocas, Moritz Hardt, and Arvind Narayanan.

To review mathematical background material, you may also find the following useful:
- **Linear Algebra**: You don't need to remember many advanced theorems, but you need to be very comfortable with the basics (dot products, Euclidean distance, matrix multiplication, matrix invertibility, etc.). To review these concepts, I recommend using [3blue1brown's linear algebra videos](https://www.3blue1brown.com/topics/linear-algebra). You can skip chapters 6, 10-12, and 16.
  - If you also want a textbook, my recommendation is [*Introduction to Applied Linear Algebra*](https://web.stanford.edu/~boyd/vmls/vmls.pdf) by Stephen Boyd and Lieven Vandenberghe. Most relevant reading: Chapters 1-3, 5-8, 10-11. (Chapters 4 and 12-14 overlap with content for this class.) 
- **Probability**: I recommend [*Introduction to Probability*](http://probabilitybook.net/) by Joseph Blitzstein and Jessica Hwang. Reading Guide:
  - Chapter 1: Optional but good background, recommended to read briefly.
  - Chapter 2: Important for class, read carefully. (2.7-2.8 are optional but good for building understanding)
  - Chapter 3: Read 3.1-3.3, 3.7-3.8.
  - Chapter 4: Read 4.1-4.2, 4.4-4.6.
  - Chapter 5: Read 5.1 and 5.4.
  - Chapter 7: Read 7.1, 7.3, and 7.5. (Will only be relevant after the midterm exam)
- **Multivariate Calculus**: [Oliver Knill's lecture notes](https://abel.math.harvard.edu/~knill/teaching/math21a2012/21a_fall_2012.pdf). Recommended reading: Lectures 11, 14, 15, 16, 17.

## Other Notes
**Collaboration policy and academic integrity**: Our goal is to maintain an optimal learning environment. You may discuss the homework problems at a high level with other students, but you should not look at another student's solutions. Trying to find solutions online or from any other sources for any homework or project is prohibited, will result in zero grade and will be reported. Using AI tools to automatically generate solutions to written or programming problems is also prohibited. To prevent any future plagiarism, uploading any material from the course (your solutions, quizzes etc.) on the internet is prohibited, and any violations will also be reported. Please be considerate, and help us help everyone get the best out of this course.

Please remember the expectations set forth in the [USC Student Handbook](https://policy.usc.edu/studenthandbook/). General principles of academic honesty include the concept of respect for the intellectual property of others, the expectation that individual work will be submitted unless otherwise allowed by an instructor, and the obligations both to protect one's own academic work from misuse by others as well as to avoid using another's work as one's own. All students are expected to understand and abide by these principles. Suspicion of academic dishonesty may lead to a referral to the [Office of Academic Integrity](https://academicintegrity.usc.edu/) for further review.

**Students with disabilities**: Any student requesting academic accommodations based on a disability is required to register with Disability Services and Programs (DSP) each semester. A letter of verification for approved accommodations can be obtained from DSP. Please be sure the letter is delivered to the instructor as early in the semester as possible.
