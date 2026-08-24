---
layout: class
title: "CSCI 467: Foundations of Machine Learning"
semester: Fall 2026
time: Mondays and Wednesdays at 2:00-3:20pm
location: THH 210
location_link: "https://maps.usc.edu/?id=1928&reference=THH"
section_time: Fridays at 2:00-2:50pm
section_location: THH 210
section_location_link: "https://maps.usc.edu/?id=1928&reference=THH"
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
* **[LaTeX Template for Homework Submissions](https://www.overleaf.com/read/kjvpshdfvwsd#593bd8)**
{::comment} * **[OneNote Notebook of Handwritten Lectures](https://1drv.ms/o/c/c7647f7ae642c6ff/EqrGz7KAwT5FmAsI_XOp1kEBE_igRdKcaGZHDPEKGCIIyQ?e=yQGf3Z)**{:/}
{::comment} * **[Final Project information](project)** {:/}

**News:** 
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
![Yuqng Yang](/assets/images/yuqing.jpg)  
**Yuqing Yang**  
Teaching Assistant
</div>
<div class="staff-photo" markdown=1>
![Course Producer](/assets/images/person_placeholder.jpg)  
**TBD**  
Course Producer
</div>

## Logistics
* **Office hours and drop-in peer mentoring**: See the calendar below or [here](https://calendar.google.com/calendar/embed?src=c_86e4982ab98a1b157f078d62c4489999c4833f08ae66003b169896dd26cca926%40group.calendar.google.com&ctz=America%2FLos_Angeles).
The instructor and TA's will have regular office hours every week.
Course producers will have drop-in peer mentoring sessions before each assignment is due.
<div class="center">
<iframe src="https://calendar.google.com/calendar/embed?src=c_86e4982ab98a1b157f078d62c4489999c4833f08ae66003b169896dd26cca926%40group.calendar.google.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
</div>
* **Assignments**: Assignments should be submitted through [Gradescope](https://www.gradescope.com/courses/1366005). Feedback will also be provided on Gradescope. All enrolled students should be in Gradescope automatically--let me know if you are not!
You should submit both your PDF writeup and your code on Gradescope; there will be separate assignments for each.
* **Discussions**: We will be using Piazza for general course-related questions and announcements. 
All enrolled students were added at the beginning of the semester; you can also use this [sign-up link](https://piazza.com/usc/fall2026/csci467).
If you have an individual matter to discuss, email me directly (please put "CSCI 467" in the subject line) or come to my office hours. For grading questions, go to the office hours of the person who graded the problem in question.

## Prerequisites

* Discrete math: CSCI 170
* Programming: CSCI 104 or CSCI 114
* Linear Algebra: MATH 225 or EE 141
* Probability: EE 364 or MATH 407 or BUAD 310 or BUAD 312 or ISE 225
* Familiarity with single-variable calculus

This class will also use some basic multivariate calculus (taking partial derivatives and gradients).
However, knowledge of single-variable calculus is sufficient as we will introduce the required material during class and section. 

All programming assignments will be in Python.
Basics of Python will be covered in discussion sections.
Students who are not familiar with Python may need to spend some time becoming more familiar with it as needed.

## Schedule
All assignments are due by **11:59pm** on the indicated date.

|Date|Topic|Related Readings|Assignments|
|--|--|--|--|
|Mon Aug 24|Introduction |PML 1| 
|Wed Aug 26|Linear Regression |PML 7.8, 8.2|
|Fri Aug 28|Section: Python & numpy, Linear Regression in numpy [](){: .schedule-section} | |
|Mon Aug 31|Featurization, Convexity |PML 2.6.3, 4.2, 8.1 ||
|Wed Sep 2|Maximum Likelihood Estimation, Logistic Regression |PML 10.1-10.3|
|Fri Sep 4|Section: Review of Probability & Linear Algebra ([notes](https://hackmd.io/@charlotteTYC/prerequisites)) [](){: .schedule-section} | | 
|Mon Sep 7|No class (Labor Day) [](){: .schedule-break}| | **Homework 0 due Tuesday Sep 8**|
|Wed Sep 9| Overfitting, Regularization |PML 4.5, 4.7, 11.3-11.4 |
|Fri Sep 11|Section: Review of Calculus, Gradients [](){: .schedule-section}| |
|Mon Sep 14|Bias and Variance, Normal Equations | PML 11.2| 
|Wed Sep 16 | Generative Classifiers, Naive Bayes |PML 9.3-9.4 |
|Fri Sep 18|Section: Cross-Validation, Evaluation Metrics [](){: .schedule-section}| | 
|Mon Sep 21|Introduction to Neural Networks |PML 13.1-13.2 |
|Wed Sep 23|Backpropagation |PML 13.3 | **Homework 1 due** |
|Fri Sep 25|Section: Sci-kit Learn tutorial [](){: .schedule-section}| | 
|Mon Sep 28|Neural Network Optimizers, Dropout, Early Stopping | PML 8.4, 13.4-13.5|**Oral exams this week**
|Wed Sep 30|Convolutional Neural Networks |PML 14.1-14.2 |
|Fri Oct 2|Section: Pytorch tutorial ([colab](https://colab.research.google.com/drive/1BLD1Eic5yw3myxdDSnL6qgBIjawYCw-Y?usp=sharing)) [](){: .schedule-section}| | 
|Mon Oct 5|Embedding models, Word Vectors |PML 20.5| **Project Proposal due**
|Wed Oct 7 |Recurrent Neural Networks |PML 15.1-15.2 |
|Fri Oct 9 |No Section (Fall Break) [](){: .schedule-break}| | 
|Mon Oct 12 |Sequence-to-sequence, Attention |PML 15.4 | **Homework 2 due** |
|Wed Oct 14|Decision Trees, ensembles |PML 18.1-18.5 | 
|Fri Oct 16 |Section: Midterm preparation [](){: .schedule-section}| | 
|Mon Oct 19|**In-class Midterm Exam** [](){: .schedule-exam} | | 
|Wed Oct 21|Transformers I |PML 15.5-15.6| 
|Fri Oct 23|Section: Reading AlexNet paper ([link](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)) [](){: .schedule-section}| | 
|Mon Oct 26|Transformers II, Pretraining |PML 15.7 |
|Wed Oct 28 |k-Means Clustering ([visualization](https://www.youtube.com/watch?v=5I3Ei69I40s)) | PML 21.3||
|Fri Oct 30|Section: RNNs and backpropagation in pytorch [](){: .schedule-section}| | 
|Mon Nov 2 | Dimensionality Reduction, Principal Component Analysis |PML 20.1, 20.4 | **Project Midterm Report due**
|Wed Nov 4|Markov Decision Processes, Reinforcement Learning |PML2 34.5-34.6, 35.1, 35.4 |
|Fri Nov 6 |Section: Reading Transformers paper ([link](https://arxiv.org/abs/1706.03762)) [](){: .schedule-section}| | 
|Mon Nov 9|Q-Learning |PML2 35.2 | **Homework 3 due**
|Wed Nov 11|No class (Veteran's Day) [](){: .schedule-break}|
|Fri Nov 13|Section: Practical guide to pretrained deep learning models [](){: .schedule-section}| | 
|Mon Nov 16|Policy Gradient| PML2 35.3 |
|Wed Nov 18|Adversarial Examples, Privacy |PML2 19.1-19.8 |
|Fri Nov 20|Section: Reading CLIP paper ([link](https://arxiv.org/abs/2103.00020))  [](){: .schedule-section}| |
|Mon Nov 23|Spurious Correlations, Fairness in Machine Learning ([slides](/assets/lectures/27_fairness.pdf)) | FAML 1-4 | 
|Nov 25-27|No class or section (Thanksgiving Break) [](){: .schedule-break}|
|Mon Nov 30|Large Language Models | **Homework 4 due**
|Wed Dec 2 |Conclusion ([slides](/assets/lectures/29_conclusion.pdf)) |
|Fri May 6 |Section: Final Exam preparation [](){: .schedule-section}| | 
|Fri Dec 11|**Final Exam, 2-4pm** [](){:.schedule-exam} | | **Project Final Report due Monday, May 7**|
{: .schedule #schedule-table}

## Grading
Grades will be based on homework assignments (31%), a class project (18%), an oral exam (6%), and two written exams (45%).

**Homework Assignments (31% total)**:
- Homework 0: 3%
- Homeworks 1-4: 7% each

**Final Project (18% total)**.
The final project will proceed in three stages:
- Project proposal: 3%
- Midterm report: 5%
- Final project report: 10%

**Oral Exam (6%)**

**Written Exams (45% total)**:
- In-class midterm: 20% 
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
{::comment}More information about the final project is available [here](project). {:/}
More information will be released soon.

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
**Collaboration policy and academic integrity**: Our goal is to maintain an optimal learning environment. You may discuss the homework problems at a high level with other students, but you should not look at another student's solutions. Trying to find solutions online or from any other sources for any homework or project is prohibited, will result in zero grade and will be reported. To prevent any future plagiarism, uploading any material from the course (your solutions, quizzes etc.) on the internet is prohibited, and any violations will also be reported. Please be considerate, and help us help everyone get the best out of this course.

Please remember the expectations set forth in the [USC Student Handbook](https://policy.usc.edu/studenthandbook/). General principles of academic honesty include the concept of respect for the intellectual property of others, the expectation that individual work will be submitted unless otherwise allowed by an instructor, and the obligations both to protect one's own academic work from misuse by others as well as to avoid using another's work as one's own. All students are expected to understand and abide by these principles. Suspicion of academic dishonesty may lead to a referral to the [Office of Academic Integrity](https://academicintegrity.usc.edu/) for further review.

**AI usage guidelines**: The homework assignments in this class are designed to help you develop a deep understanding of the material if you spend the time to do the work yourself. 
Therefore, you are strongly encouraged to do all of the homework assignments yourself, without getting direct help from an AI system.
More appropriate uses of AI include getting general help understanding the class material and asking AI to help check and provide feedback on your write-ups after you have written them.
Regardless of how you use AI, you will be required to disclose the manner in which you used AI on each homework submission.

For the final project, you are encouraged to explore how AI tools can help you make progress. 
However, at the end of the day it is your responsibility to ensure that you understand and agree with everything the AI writes, including any code as well as your final write-ups.


**Students with disabilities**: Any student requesting academic accommodations based on a disability is required to register with Disability Services and Programs (DSP) each semester. A letter of verification for approved accommodations can be obtained from DSP. Please be sure the letter is delivered to the instructor as early in the semester as possible.
