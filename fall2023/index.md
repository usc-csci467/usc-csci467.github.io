---
layout: class
title: "CSCI 467: Introduction to Machine Learning"
semester: Fall 2023
time: Tuesdays and Thursdays at 2:00-3:20pm
location: LVL 17
location_link: "https://maps.usc.edu/?id=1928&reference=LVL"
section_time: Fridays at 2:00-2:50pm
section_location: DMC 100
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

{% capture hw0 %}{% include hw.html num=0 sem="fall2023" %}{% endcapture %}
{% capture hw1 %}{% include hw.html num=1 sem="fall2023" %}{% endcapture %}
{% capture hw2 %}{% include hw.html num=2 sem="fall2023" %}{% endcapture %}
{% capture hw3 %}{% include hw.html num=3 sem="fall2023" %}{% endcapture %}
{% capture hw4 %}{% include hw.html num=4 sem="fall2023" %}{% endcapture %}


**Quick Links:**
* **[Lecture Notes](/assets/fall2023/notes.pdf)** (will be continuously updated throughout the semester)
* **[Final Project information](project)**

**News:**   
* Homework 4 has been released {{hw4 | strip_newlines }}. It is due **Thursday, November 30**.
* I have released a [practice final exam](/assets/fall2023/exams/practice_final.pdf) with [solutions](/assets/fall2023/exams/practice_final_solutions.pdf).
* The final exam will be **Thursday, December 7 from 2-4pm in SLH 200**.

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
![Soumya Sanyal](/assets/fall2023/images/soumya.jpg)  
**Soumya Sanyal**  
Teaching Assistant
</div>
<div class="staff-photo" markdown=1>
![Wang (Bill) Zhu](//billzhu.me/author/admin/avatar_hu42410483742cac5c8006d54d4d8d8fd3_63927_250x250_fill_q90_lanczos_center.jpg)  
**Wang (Bill) Zhu**  
Teaching Assistant
</div>
<div class="staff-photo" markdown=1>
![Vishesh Agrawal](/assets/fall2023/images/vishesh.jpg)  
**Vishesh Agrawal**  
Course Producer
</div>
<div class="staff-photo" markdown=1>
![Ryan Wang](/assets/fall2023/images/ryan.jpg)  
**Ryan Wang**  
Course Producer
</div>
<div class="staff-photo" markdown=1>
![Lorena Yan](/assets/fall2023/images/lorena.jpg)  
**Lorena Yan**  
Course Producer
</div>
<div class="staff-photo" markdown=1>
![Wenyang Zhang](/assets/fall2023/images/wenyang.jpg)  
**Wenyang Zhang**  
Course Producer
</div>

## Logistics
* **Office hours**: See [calendar](https://calendar.google.com/calendar/embed?src=c_86e4982ab98a1b157f078d62c4489999c4833f08ae66003b169896dd26cca926%40group.calendar.google.com&ctz=America%2FLos_Angeles).
* **Assignments**: Assignments should be submitted through [Gradescope](https://www.gradescope.com/courses/577750). Feedback will also be provided on Gradescope. All enrolled students should be in Gradescope automatically--let me know if you are not!
You should submit both your PDF writeup and your code on Gradescope; there will be separate assignments for each.
* **Discussions**: We will be using Piazza for general course-related questions and announcements. 
All enrolled students were added at the beginning of the semester; you can also use this [sign-up link](https://piazza.com/usc/fall2023/csci467).
If you have an individual matter to discuss, email me directly (please put "CSCI 467" in the subject line) or come to my office hours. For grading questions, go to the office hours of the person who graded the problem in question.

## Prerequisites
* Algorithms: CSCI 270 
* Linear Algebra: MATH 225 
* Probability: EE 364 or MATH 407 or BUAD 310

This class will also use some basic multivariate calculus (taking partial derivatives and gradients).
However, knowledge of single-variable calculus is sufficient as we will introduce the required material during class and section. 


## Schedule
All assignments are due by **11:59pm** on the indicated date.

|Date|Topic|Related Readings|Assignments|
|--|--|--|--|
|Tue Aug 22|Introduction ([slides](/assets/fall2023/lectures/01_intro.pdf)) |PML 1| Homework 0 released {{ hw0 | strip_newlines }}
|Thu Aug 24|Linear Regression ([lecture](/assets/fall2023/lectures/02_linreg.pdf), [demo](https://colab.research.google.com/drive/11hdXd0C7GGrxpJlC-PV6eImcWJ3Bk_Q2?usp=sharing)) |PML 7.8, 8.2|
|Fri Aug 25|Section: Probability, Linear Algebra, & Calculus Review [Soumya] ([handout](https://hackmd.io/@charlotteTYC/prerequisites){: .schedule-section}, [notes](/assets/fall2023/sections/section1_notes.pdf)) | |
|Tue Aug 29|Featurization, Convexity, Maximum Likelihood Estimation ([lecture](/assets/fall2023/lectures/03_linreg2.pdf)) |PML 2.6.3, 4.2, 8.1 ||
|Thu Aug 31|Logistic Regression, Softmax Regression ([lecture](/assets/fall2023/lectures/04_logreg.pdf)) |PML 10.1-10.3| **Homework 0 due** |
|Fri Sep 1|Section: Python & numpy tutorial [Bill] ([colab](https://colab.research.google.com/drive/1Qe_HXHHD2KyvOZbbXyl-ly2zSmD_qucp?usp=sharing){: .schedule-section}) | | 
|Tue Sep 5|Overfitting, Regularization ([lecture](/assets/fall2023/lectures/05_overfitting.pdf)) |PML 4.5, 4.7, 11.3-11.4 |
|Thu Sep 7|Bias and Variance, Normal Equations ([lecture](/assets/fall2023/lectures/06_biasvariance.pdf)) | PML 11.2| Homework 1 released {{hw1 | strip_newlines }}
|Fri Sep 8|Section: Probability review continued, taking gradients [Soumya] ([notes](/assets/fall2023/sections/section3_notes.pdf){: .schedule-section})| |
|Tue Sep 12| Generative Classifiers, Naive Bayes ([lecture](/assets/fall2023/lectures/07_naivebayes.pdf)) |PML 9.3-9.4 |
|Thu Sep 14 |Nearest Neighbors, start of Kernels; Project discussion ([lecture](/assets/fall2023/lectures/08_nonparametric.pdf)) |PML 16.1, 16.3 |
|Fri Sep 15|Section: Cross-Validation, Evaluation Metrics  [Bill] ([slides](/assets/fall2023/sections/section4.pdf){: .schedule-section}) | | 
|Tue Sep 19 |Kernel methods continued ([lecture](/assets/fall2023/lectures/09_kernels.pdf)) |PML 4.3, 17.1, 17.3| **Homework 1 due** |
|Thu Sep 21|Introduction to Neural Networks, Dropout, Early Stopping ([lecture](/assets/fall2023/lectures/10_neuralnets.pdf)) |PML 13.1-13.3 | Homework 2 released {{hw2 | strip_newlines}} |
|Fri Sep 22| Section: Scikit-learn tutorial [Vishesh] ([colab](https://colab.research.google.com/drive/1EJ-E1QPGWHWpZU9eMXQuEqMkAhy0yai-?usp=sharing))  [](){: .schedule-section}| | 
|Tue Sep 26|Backpropagation ([slides](/assets/fall2023/lectures/11_backprop.pdf); demo [part 1](/assets/fall2023/backprop/part1_forward_only.py), [part 2](/assets/fall2023/backprop/part2_trees.py), [part 3](/assets/fall2023/backprop/part3_dags.py)) |PML 13.4-13.5 | **Project Proposal due** |
|Thu Sep 28|Convolutional Neural Networks ([slides](/assets/fall2023/lectures/12_convnets.pdf)) |PML 14.1-14.2 |
|Fri Sep 29|Section: Pytorch tutorial [Soumya] ([colab](https://colab.research.google.com/drive/1qJspmUBaQIgXv93L3Bk3Jt5SIN4kEI7O?usp=sharing)) [](){: .schedule-section}| | 
|Tue Oct 3|Recurrent Neural Networks ([slides](/assets/fall2023/lectures/13_rnns.pdf)) |PML 15.1-15.2 |
|Thu Oct 5|Sequence-to-sequence, Attention ([slides](/assets/fall2023/lectures/14_attention.pdf), [review](/assets/fall2023/lectures/14_review.pdf)) |PML 15.4 | **Homework 2 due** |
|Fri Oct 6 |Section: Midterm preparation [](){: .schedule-section}| | 
|Tue Oct 10 |**In-class Midterm Exam** [](){: .schedule-exam} | | 
|Oct 12-13|No class or section (Fall break) [](){: .schedule-break}| |
|Tue Oct 17 |Transformers I ([slides](/assets/fall2023/lectures/15_transformers.pdf)) |PML 15.5-15.6| |
|Thu Oct 19 |Transformers II, Pretraining ([slides](/assets/fall2023/lectures/16_transformers2.pdf)) |PML 15.7 |
|Fri Oct 20|Section: RNNs & backpropagation in pytorch [Soumya] ([tutorial](https://pytorch.org/tutorials/intermediate/char_rnn_generation_tutorial.html)) [](){: .schedule-section}| | 
|Tue Oct 24|Decision Trees, ensembles ([slides](/assets/fall2023/lectures/17_trees.pdf)) |PML 18.1-18.5 | Homework 3 released {{hw3 | strip_newlines}}
|Thu Oct 26|k-Means Clustering ([lecture](/assets/fall2023/lectures/18_kmeans.pdf)) | PML 21.3|
|Fri Oct 27|Section: Optimization strategies for neural networks [Bill] ([tutorial](https://docs.google.com/presentation/d/1eC7QRXejFUoxthSlbN5kM27NHuXoojjn_Xhp9QbMBS0/edit?usp=sharing)) [](){: .schedule-section}| | 
|Tue Oct 31|Gaussian Mixture Models, Expectation Maximization ([lecture](/assets/fall2023/lectures/19_gmm.pdf)) | PML 21.4, PML2 8.1-8.2|**Project Midterm Report due** |
|Thu Nov 2 |Dimensionality Reduction, Principal Component Analysis ([lecture](/assets/fall2023/lectures/20_em.pdf)) |PML 20.1, 20.4 |
|Fri Nov 3 |Section: Practical guide to pretrained language models [](){: .schedule-section}| | 
|Tue Nov 7 |Embedding models, Word Vectors ([pca part 2](/assets/fall2023/lectures/21_pca.pdf), [wordvec slides](/assets/fall2023/lectures/21_wordvec.pdf))  |PML 20.5 |
|Thu Nov 9|Markov Decision Processes, Reinforcement Learning ([lecture](/assets/fall2023/lectures/22_rl1.pdf)) |PML2 34.5-34.6, 35.1, 35.4 | **Homework 3 due**|
|Fri Nov 10|No section (Veteran's Day) [](){: .schedule-break}| | 
|Tue Nov 14|Q-Learning ([lecture](/assets/fall2023/lectures/23_rl2.pdf)) |PML2 35.2-35.3 | Homework 4 released {{hw4 | strip_newlines}} |
|Thu Nov 16|Policy Gradient, Robustness, Adversarial Examples ([policy gradient lecture](/assets/fall2023/lectures/24_policygrad.pdf), [adversarial slides](/assets/fall2023/lectures/24_adversarial.pdf)) |PML2 19.1-19.8 |
|Fri Nov 17|Section: Practical guide to computer vision models [Vishesh] ([tutorial](https://colab.research.google.com/drive/1FUjO0tYUz_n5YKuTLwrxFiZMUAy7M9UX?usp=sharing)) ([slides](https://docs.google.com/presentation/d/1dlvPa_MPIS4OQT1yMpVWOkYHuQ8gWaje_pKo5MQfJ_4/edit#slide=id.p)) [](){: .schedule-section}| | 
|Tue Nov 21|Spurious Correlations, Fairness in Machine Learning ([slides](/assets/fall2023/lectures/25_fairness.pdf)) | FAML 1-4 | 
|Nov 23-24|No class or section (Thanksgiving) [](){: .schedule-break}| |
|Tue Nov 28|How does ChatGPT work? ([slides](/assets/fall2023/lectures/26_chatgpt.pdf)) | 
|Thu Nov 30|Conclusion ([slides](/assets/fall2023/lectures/27_conclusion.pdf)) | | **Homework 4 due** |
|Fri Nov 31|Section: Final Exam preparation [](){: .schedule-section}| | 
|Thu Dec 7|**Final Exam, 2-4pm** [](){:.schedule-exam} | | **Project Final Report due Dec 12**|
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

## Resources
This semester, I am writing **[Lecture Notes](/assets/fall2023/notes.pdf)** that accompany all the iPad lectures.
I recommend using these notes as reference material for studying.
There is no required textbook for this class.
If you do want to learn from a textbook, the following may be useful:
- [*Probabilistic Machine Learning: An Introduction*](https://probml.github.io/pml-book/book1.html) (PML) and [*Probabilistic Machine Learning: Advanced Topics*](https://probml.github.io/pml-book/book2.html) (PML2) by Kevin Murphy. You may also find PML Chapters 2-3 and 7 useful for reviewing prerequisites.
- [*The Elements of Statistical Learning*](https://hastie.su.domains/Papers/ESLII.pdf) by Trevor Hastie, Robert Tibshirani, and Jerome Friedman.
- [*Patterns, Predictions, and Actions: A Story about Machine Learning*](https://mlstory.org/) by Moritz Hardt and Benjamin Recht
- [*Fairness and Machine Learning: Limitations and Opportunities*](https://fairmlbook.org/) (FAML) by Solon Barocas, Moritz Hardt, and Arvind Narayanan.

To review mathematical background material, you may also find the following useful:
- Probability: [*Introduction to Probability*](http://probabilitybook.net/) by Joseph Blitzstein and Jessica Hwang. Most relevant reading: Chapters 1-5, 7, 9-10.
- Linear Algebra: [*Introduction to Applied Linear Algebra*](https://web.stanford.edu/~boyd/vmls/vmls.pdf) by Stephen Boyd and Lieven Vandenberghe. Most relevant reading: Chapters 1-3, 5-8, 10-11. (Chapters 4 and 12-14 overlap with content for this class.) 
- Multivariate Calculus: [Oliver Knill's lecture notes](https://abel.math.harvard.edu/~knill/teaching/math21a2012/21a_fall_2012.pdf).

## Other Notes
**Collaboration policy and academic integrity**: Our goal is to maintain an optimal learning environment. You may discuss the homework problems at a high level with other students, but you should not look at another student's solutions. Trying to find solutions online or from any other sources for any homework or project is prohibited, will result in zero grade and will be reported. Using AI tools to automatically generate solutions to written or programming problems is also prohibited. To prevent any future plagiarism, uploading any material from the course (your solutions, quizzes etc.) on the internet is prohibited, and any violations will also be reported. Please be considerate, and help us help everyone get the best out of this course.

Please remember the expectations set forth in the [USC Student Handbook](https://policy.usc.edu/studenthandbook/). General principles of academic honesty include the concept of respect for the intellectual property of others, the expectation that individual work will be submitted unless otherwise allowed by an instructor, and the obligations both to protect one's own academic work from misuse by others as well as to avoid using another's work as one's own. All students are expected to understand and abide by these principles. Suspicion of academic dishonesty may lead to a referral to the [Office of Academic Integrity](https://academicintegrity.usc.edu/) for further review.

**Students with disabilities**: Any student requesting academic accommodations based on a disability is required to register with Disability Services and Programs (DSP) each semester. A letter of verification for approved accommodations can be obtained from DSP. Please be sure the letter is delivered to the instructor as early in the semester as possible.
