---
layout: class
title: "CSCI 467: Introduction to Machine Learning"
semester: Spring 2024
time: Tuesdays and Thursdays at 3:30-4:50pm
location: DMC 100
location_link: "https://maps.usc.edu/?id=1928&reference=DMC"
section_time: Fridays at 3:00-3:50pm
section_location: DMC 102
section_location_link: "https://maps.usc.edu/?id=1928&reference=DMC"
instructor: Robin Jia
order: 1
---
<div class="row" markdown=1>
<div class="col-pic" markdown=1>
![xkcd Tasks](https://imgs.xkcd.com/comics/tasks.png)
Source: [xkcd](https://xkcd.com/1425/)
</div>
<div class="col-intro" markdown=1>

{% capture hw0 %}{% include hw.html sem="spring2024" num=0 %}{% endcapture %}
{% capture hw1 %}{% include hw.html sem="spring2024" num=1 %}{% endcapture %}
{% capture hw2 %}{% include hw.html sem="spring2024" num=2 %}{% endcapture %}
{% capture hw3 %}{% include hw.html sem="spring2024" num=3 %}{% endcapture %}
{% capture hw4 %}{% include hw.html sem="spring2024" num=4 %}{% endcapture %}


**Quick Links:**
* **[Lecture Notes](/assets/spring2024/notes.pdf)**
* **[Final Project information](project)**

**News:** 
* We have released two practice final exams: Final 1 ([problems](/assets/spring2024/exams/final_1.pdf), [solutions](/assets/spring2024/exams/final_1_solutions.pdf)) and Final 2 ([problems](/assets/spring2024/exams/final_2.pdf), [solutions](/assets/spring2024/exams/final_2_solutions.pdf)). 
* We have released two practice midterm exams: Midterm 1 ([problems](/assets/spring2024/exams/midterm_1.pdf), [solutions](/assets/spring2024/exams/midterm_1_solutions.pdf)) and Midterm 2 ([problems](/assets/spring2024/exams/midterm_2.pdf), [solutions](/assets/spring2024/exams/midterm_2_solutions.pdf)).
* Homework 4 has been released {{ hw4 | strip_newlines }}. It is due **Thursday, April 25**.
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
![Ameya Godbole](//ameyagodbole.github.io/assets/img/avatar-480.webp)  
**Ameya Godbole**  
Teaching Assistant
</div>
<div class="staff-photo" markdown=1>
![Soumya Sanyal](/assets/spring2024/images/soumya.jpg)  
**Soumya Sanyal**  
Teaching Assistant
</div>
<div class="staff-photo" markdown=1>
![Vishesh Agrawal](/assets/spring2024/images/vishesh.jpg)  
**Vishesh Agrawal**  
Course Producer
</div>
<div class="staff-photo" markdown=1>
![Ryan Wang](/assets/spring2024/images/ryan.jpg)  
**Ryan Wang**  
Course Producer
</div>
<div class="staff-photo" markdown=1>
![Lorena Yan](/assets/spring2024/images/lorena.jpg)  
**Lorena Yan**  
Course Producer
</div>
<div class="staff-photo" markdown=1>
![Wenyang Zhang](/assets/spring2024/images/wenyang.jpg)  
**Wenyang Zhang**  
Course Producer
</div>

## Logistics
* **Office hours and drop-in peer mentoring**: See the calendar below or [here](https://calendar.google.com/calendar/embed?src=c_86e4982ab98a1b157f078d62c4489999c4833f08ae66003b169896dd26cca926%40group.calendar.google.com&ctz=America%2FLos_Angeles).
The instructor and TA's will have regular office hours every week.
Course producers will have drop-in peer mentoring sessions before each assignment is due.
<div class="center">
<iframe src="https://calendar.google.com/calendar/embed?src=c_86e4982ab98a1b157f078d62c4489999c4833f08ae66003b169896dd26cca926%40group.calendar.google.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
</div>
* **Assignments**: Assignments should be submitted through [Gradescope](https://www.gradescope.com/courses/697428). Feedback will also be provided on Gradescope. All enrolled students should be in Gradescope automatically--let me know if you are not!
You should submit both your PDF writeup and your code on Gradescope; there will be separate assignments for each.
* **Discussions**: We will be using Piazza for general course-related questions and announcements. 
All enrolled students were added at the beginning of the semester; you can also use this [sign-up link](https://piazza.com/usc/spring2024/csci467).
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
|Tue Jan 9|Introduction ([slides](/assets/spring2024/lectures/01_intro.pdf)) |PML 1| Homework 0 released {{ hw0 | strip_newlines }}
|Thu Jan 11|Linear Regression ([lecture](/assets/spring2024/lectures/02_linreg.pdf), [demo](https://colab.research.google.com/drive/11hdXd0C7GGrxpJlC-PV6eImcWJ3Bk_Q2?usp=sharing#scrollTo=COxZk9G7bkW_)) |PML 7.8, 8.2|
|Fri Jan 12|Section (Robin): Review of Probability & Linear Algebra ([notes](https://hackmd.io/@charlotteTYC/prerequisites), [section](/assets/spring2024/sections/section1.pdf)) [](){: .schedule-section} | |
|Tue Jan 16|Featurization, Convexity, Maximum Likelihood Estimation ([lecture](/assets/spring2024/lectures/03_linreg2.pdf)) |PML 2.6.3, 4.2, 8.1 ||
|Thu Jan 18|Logistic Regression, Softmax Regression ([lecture](/assets/spring2024/lectures/04_classification.pdf)) |PML 10.1-10.3| **Homework 0 due** |
|Fri Jan 19|Section (Ameya): Python & numpy tutorial ([demo](https://colab.research.google.com/drive/1DTjbgRrAuphcW5l8aw6h00wLuvJDdBFJ?usp=sharing)) [](){: .schedule-section} | | 
|Tue Jan 23|Overfitting, Regularization ([lecture](/assets/spring2024/lectures/05_overfitting.pdf)) |PML 4.5, 4.7, 11.3-11.4 |
|Thu Jan 25|Bias and Variance, Normal Equations ([lecture](/assets/spring2024/lectures/06_biasvariance.pdf)) | PML 11.2| Homework 1 released {{ hw1 | strip_newlines }} 
|Fri Jan 26|Section (Soumya): Calculus and Gradients ([section](/assets/spring2024/sections/section3.pdf)) [](){: .schedule-section}| |
|Tue Jan 30| Generative Classifiers, Naive Bayes ([slides](/assets/spring2024/lectures/07_naivebayes.pdf)) |PML 9.3-9.4 |
|Thu Feb 1 |Nearest Neighbors, start of Kernels; Project discussion ([lecture](/assets/spring2024/lectures/08_nonparametric.pdf)) |PML 16.1, 16.3 |
|Fri Feb 2 |Section (Ameya): Cross-Validation, Evaluation Metrics ([section](/assets/spring2024/sections/section4.pdf)) [](){: .schedule-section}| | 
|Tue Feb 6 |Kernel methods continued ([lecture](/assets/spring2024/lectures/09_kernels.pdf)) |PML 4.3, 17.1, 17.3| **Homework 1 due** |
|Thu Feb 8 |Introduction to Neural Networks ([lecture](/assets/spring2024/lectures/10_neuralnets.pdf)) |PML 13.1-13.2 | Homework 2 released {{ hw2 | strip_newlines }}
|Fri Feb 9 |Section (Ameya): Review of linear methods ([section](/assets/spring2024/sections/section5.pdf)) [](){: .schedule-section}| | 
|Tue Feb 13|Backpropagation ([lecture](/assets/spring2024/lectures/11_backprop.pdf), demo [part 1](/assets/spring2024/backprop/part1_forward_only.py), [part 2](/assets/spring2024/backprop/part2_trees.py), [part 3](/assets/spring2024/backprop/part3_dags.py)) |PML 13.3 | **Project Proposal due** |
|Thu Feb 15|Neural Network Optimizers, Dropout, Early Stoppin ([slides](/assets/spring2024/lectures/12_nnoptim.pdf)) | PML 8.4, 13.4-13.5|
|Fri Feb 16|Section (Soumya): Pytorch tutorial ([colab](https://colab.research.google.com/drive/1BLD1Eic5yw3myxdDSnL6qgBIjawYCw-Y?usp=sharing)) [](){: .schedule-section}| | 
|Tue Feb 20|Convolutional Neural Networks ([slides](/assets/spring2024/lectures/13_convnets.pdf)) |PML 14.1-14.2 |
|Thu Feb 22|Embedding models, Word Vectors ([slides](/assets/spring2024/lectures/14_wordvec.pdf)) |PML 20.5|
|Fri Feb 23|Section (Soumya): Sci-kit Learn tutorial ([colab](https://colab.research.google.com/drive/1WsH_gfVC7dIFtRtXNak0Lr2HR7ty4DPC?usp=sharing)) [](){: .schedule-section}| | 
|Tue Feb 27|Recurrent Neural Networks ([slides](/assets/spring2024/lectures/15_rnns.pdf)) |PML 15.1-15.2 |
|Thu Feb 29|Sequence-to-sequence, Attention ([slides](/assets/spring2024/lectures/16_attention.pdf)) |PML 15.4 | **Homework 2 due** |
|Fri Mar 1 |Section (Soumya): Midterm preparation ([slides](https://docs.google.com/presentation/d/1C-emdcya92vlaJFV7amxzpW54G6AjEYgugofnkeeSMw/edit?usp=sharing)) [](){: .schedule-section}| | 
|Tue Mar 5 |Decision Trees, ensembles ([slides](/assets/spring2024/lectures/17_trees.pdf)) |PML 18.1-18.5 | 
|Thu Mar 7 |**In-class Midterm Exam** [](){: .schedule-exam} | | 
|Mar 8-15  |No class or section (Spring break) [](){: .schedule-break}| |
|Tue Mar 19|Transformers I ([slides](/assets/spring2024/lectures/18_transformers.pdf)) |PML 15.5-15.6| Homework 3 released {{ hw3 | strip_newlines }} |
|Thu Mar 21|Transformers II, Pretraining ([slides](/assets/spring2024/lectures/19_transformers2.pdf)) |PML 15.7 |
|Fri Mar 22|Section (Soumya): RNNs and backpropagation in pytorch ([tutorial](https://pytorch.org/tutorials/intermediate/char_rnn_generation_tutorial.html)) [](){: .schedule-section}| | 
|Tue Mar 26|k-Means Clustering ([lecture](/assets/spring2024/lectures/20_kmeans.pdf)) | PML 21.3|**Project Midterm Report due** |
|Thu Mar 28|Gaussian Mixture Models, Expectation Maximization ([lecture](/assets/spring2024/lectures/21_gmm.pdf)) | PML 21.4, PML2 8.1-8.2|
|Fri Mar 29|Section: Transformers in code [](){: .schedule-section}| 
|Tue Apr 2 |Expectation Maximization for GMMs; Start Dimensionality Reduction ([lecture](/assets/spring2024/lectures/22_em.pdf)) |PML 20.1, 20.4 |
|Thu Apr 4 |Finish Principal Components Analysis; start Multi-armed Bandits ([lecture](/assets/spring2024/lectures/23_pca.pdf)) |PML2 34.1-34.4 ||
|Fri Apr 5 |Section (Soumya): Practical guide to pretrained language models ([colab](https://colab.research.google.com/drive/1GNmZPzG0qgDG_Kmqg3Uwu08VL-FF1_sW?usp=sharing)) ([slides](https://docs.google.com/presentation/d/1xqOHwtub3aEzouQgTqQtTTc-_Ncd0SGEd6-pqab902o/edit?usp=sharing)) [](){: .schedule-section}| | 
|Tue Apr 9 |Markov Decision Processes, Reinforcement Learning ([lecture](/assets/spring2024/lectures/24_mdp.pdf))  |PML2 34.5-34.6, 35.1, 35.4 |**Homework 3 due**| 
|Thu Apr 11|Q-Learning ([lecture](/assets/spring2024/lectures/25_qlearning.pdf)) |PML2 35.2-35.3 | Homework 4 released {{ hw4 | strip_newlines }}|
|Fri Apr 12|Section (Ameya): Practical guide to computer vision models ([colab](https://colab.research.google.com/drive/1JiIBdWzCv0Jq7jeIaCww904AN82Hq1dL?usp=sharing)) ([slides](https://docs.google.com/presentation/d/19m8DGDO9vAFbArPUiWUITopNdYRtVQRe8TMqT2naNBc/edit?usp=sharing)) [](){: .schedule-section}| |
|Tue Apr 16|Finishing RL ([lecture](/assets/spring2024/lectures/26_policygrad.pdf)) ; Adversarial Examples ([slides](/assets/spring2024/lectures/26_adversarial.pdf)) |PML2 19.1-19.8 |
|Thu Apr 18|Spurious Correlations, Fairness in Machine Learning ([slides](/assets/spring2024/lectures/27_fairness.pdf)) | FAML 1-4 | 
|Fri Apr 19|Section: Review [](){: .schedule-section}| 
|Tue Apr 23|How does ChatGPT work? ([slides](/assets/spring2024/lectures/28_chatgpt.pdf)) | 
|Thu Apr 25|Conclusion ([summary](/assets/spring2024/lectures/29_summary.pdf), [slides](/assets/spring2024/lectures/29_conclusion.pdf)) | | **Homework 4 due** |
|Fri Apr 26|Section: Final Exam preparation [](){: .schedule-section}| | 
|Tue May 7|**Final Exam, 2-4pm** [](){:.schedule-exam} | | **Project Final Report due Friday, May 3**|
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
I have written **[Lecture Notes](/assets/spring2024/notes.pdf)** that accompany all the iPad lectures.
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
